import json
import uuid

from wagtail.wagtailforms.models import AbstractForm, AbstractFormField
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from django.db.models.fields import TextField, URLField
from django.db import models
from django.db.models import Q
from django.db.models.expressions import RawSQL
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from urllib.parse import parse_qs
from itertools import chain

from resources.models.tags import TopicTag, IssueTag, ReasonTag, ContentTag, ExcludeTag
from resources.models.resources import ResourcePage, ResourceIndexPage
from resources.models.helpers import combine_tags, count_likes, get_liked_value, filter_tags, get_tags, generate_custom_form, valid_request, handle_request, get_resource

uid = uuid.uuid4()

class FormField(AbstractFormField):
    page = ParentalKey('Home', related_name='form_fields')

class Home(AbstractForm):
    banner = RichTextField(blank=True, help_text="Banner at the top of every page")
    header = RichTextField(blank=True, help_text="Hero title")
    body = RichTextField(blank=True, help_text="Description of page")
    filter_label_1 = TextField(blank=True, help_text="Label/Question for first set of filters")
    filter_label_2 = TextField(blank=True, help_text="Label/Question for second set of filters")
    filter_label_3 = TextField(blank=True, help_text="Label/Question for third set of filters")
    assessment_text = RichTextField(blank=True, help_text="Label for sleep assessment link")
    crisis_text = RichTextField(blank=True, help_text="Label for sleep crisis page link")
    lookingfor = RichTextField(blank=True, help_text="Information on how to leave suggestions and what the suggestions are for")
    alpha = RichTextField(blank=True, help_text="What is Alpha")
    alphatext = RichTextField(blank=True, help_text="Why to take part in the alpha")
    footer = RichTextField(blank=True, help_text="Footer text")
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Max file size: 10MB. Choose from: GIF, JPEG, PNG (but pick PNG if you have the choice)"
    )
    video_url = URLField(blank=True, help_text="URL of an introductiary youtube video")
    exclude_tags = ClusterTaggableManager(
        through=ExcludeTag, blank=True, verbose_name="Exclude Tags",
        help_text='Tags you do not want to show in the filters for this home page'
    )

    def get_context(self, request):
        context = super(Home, self).get_context(request)

        query = request.GET.get('q')

        tag_filter = request.GET.getlist('tag')
        issue_filter = request.GET.getlist('issue')
        content_filter = request.GET.getlist('content')
        reason_filter = request.GET.getlist('reason')
        topic_filter = request.GET.getlist('topic')

        if self.slug != 'home':
            topic_filter = self.slug

        issue_tags = get_tags(IssueTag)
        content_tags = get_tags(ContentTag)
        reason_tags = get_tags(ReasonTag)
        topic_tags = get_tags(TopicTag)

        resources = ResourcePage.objects.all().annotate(
            number_of_likes=count_likes(1),
            number_of_dislikes=count_likes(-1)
        ).order_by('priority')

        if 'ldmw_session' in request.COOKIES:
            cookie = request.COOKIES['ldmw_session']
            resources = resources.extra(
                select={ 'liked_value': 'select like_value from likes_likes where resource_id = resources_resourcepage.page_ptr_id and user_hash = %s'},
                select_params=([cookie])
            )
        else:
            cookie = ''

        if topic_filter:
            filtered_issue_tags, filtered_reason_tags, filtered_content_tags = filter_tags(resources, topic_filter)

            if filtered_issue_tags:
                context['issue_tags'] = get_tags(IssueTag, filtered_tags=filtered_issue_tags).values()

            if filtered_content_tags:
                context['content_tags'] = get_tags(ContentTag, filtered_tags=filtered_content_tags).values()

            if filtered_reason_tags:
                context['reason_tags'] = get_tags(ReasonTag, filtered_tags=filtered_reason_tags).values()
        else:
            context['issue_tags'] = issue_tags.values()
            context['content_tags'] = content_tags.values()
            context['reason_tags'] = reason_tags.values()

        if (tag_filter):
            resources = resources.filter(
                Q(content_tags__name__in=tag_filter) |
                Q(reason_tags__name__in=tag_filter) |
                Q(issue_tags__name__in=tag_filter) |
                Q(topic_tags__name__in=tag_filter)
            ).distinct()

        if (issue_filter):
            resources = resources.filter(issue_tags__name__in=issue_filter).distinct()

        if (content_filter):
            resources = resources.filter(content_tags__name__in=content_filter).distinct()

        if (reason_filter):
            resources = resources.filter(reason_tags__name__in=reason_filter).distinct()

        if (topic_filter):
            resources = resources.filter(topic_tags__name=topic_filter).distinct()

        if (query):
            resources = resources.search(query)

        filtered_resources = map(combine_tags, resources)

        context['landing_pages'] = Home.objects.filter(~Q(slug="home"))
        context['resources'] = filtered_resources
        context['resource_count'] = resources.count()
        context['topic_tags'] = topic_tags.values()
        context['selected_topic'] = topic_filter
        context['selected_tags'] = list(chain(
            tag_filter,
            issue_filter,
            content_filter,
            reason_filter,
        ))
        return context

    content_panels = AbstractForm.content_panels + [
        FieldPanel('banner', classname="full"),
        ImageChooserPanel('hero_image'),
        FieldPanel('header', classname="full"),
        FieldPanel('body', classname="full"),
        FieldPanel('video_url', classname="full"),
        MultiFieldPanel([
            FieldPanel('filter_label_1', classname="full"),
            FieldPanel('filter_label_2', classname="full"),
            FieldPanel('filter_label_3', classname="full"),
            FieldPanel('exclude_tags', classname="full")
        ]),
        FieldPanel('assessment_text', classname="full"),
        FieldPanel('crisis_text', classname="full"),
        FieldPanel('lookingfor', classname="full"),
        FieldPanel('alpha', classname="full"),
        FieldPanel('alphatext', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('footer', classname="full"),
    ]

    def process_form_submission(self, request_dict):
        if 'email' in request_dict or 'suggestion' in request_dict:
            page = Home.objects.get(slug='home')
            try:
                email = request_dict['email'][0]
            except:
                email = ''
            try:
                suggestion = request_dict['suggestion'][0]
            except:
                suggestion = ''

            form_data = {'email': email, 'suggestion': suggestion}
        else:
            page = ResourceIndexPage.objects.get(slug="resource-index")
            form_data = {
                'resource_title': request_dict['resource_title'],
                'resource_name': request_dict['resource_name'],
                'feedback': request_dict['feedback'],
                'liked': request_dict['liked'],
            }
        return self.get_submission_class().objects.create(
            form_data=json.dumps(form_data, cls=DjangoJSONEncoder),
            page=page,
        )

    def serve(self, request, *args, **kwargs):
        try:
            request_dict = parse_qs(request.body.decode('utf-8'))
        except:
            request_dict = request.POST.dict()

            id = request_dict['id']

            self.process_form_submission(request_dict)

            try:
                cookie = request.COOKIES['ldmw_session']
            except:
                cookie = uid.hex

            resource = get_resource(id, cookie)

            result = render_to_string(
                'resources/resource.html',
                {'page': resource, 'like_feedback_submitted': True}
            )
            return JsonResponse({'result': result, 'id': id})

        if request.method == 'POST':
            form = self.get_form(request.POST, page=self, user=request.user)
            if form.is_valid():
                self.process_form_submission(request_dict)

                if valid_request(request_dict):
                    return handle_request(
                      request,
                      request_dict,
                      HttpResponseRedirect,
                      messages
                    )

        else:
            form = self.get_form(page=self, user=request.user)

        form_fields = FormField.objects.all().filter(page_id=form.page.id)

        context = self.get_context(request)
        context['form'] = form

        like_feedback_submitted = False
        for m in messages.get_messages(request):
            if m.__str__()[:14] == 'like_feedback_':
                like_feedback_submitted = True

        context['like_feedback_submitted'] = like_feedback_submitted
        context['custom_form'] = generate_custom_form(
            form_fields,
            request_dict,
            messages.get_messages(request)
        ) # custom

        return render(
            request,
            self.get_template(request),
            context
        )