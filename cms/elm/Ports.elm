port module Ports exposing (..)

import Types exposing (Tag)


port listeners : () -> Cmd msg


port selectTag : List Tag -> Cmd msg


port updateTags : (List Tag -> msg) -> Sub msg
