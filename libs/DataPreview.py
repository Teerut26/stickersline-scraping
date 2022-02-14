# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = data_preview_from_dict(json.loads(json_string))

from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class DataPreview:
    type: str
    id: int
    static_url: str
    fallback_static_url: str
    animation_url: str
    popup_url: str
    sound_url: str

    def __init__(self, type: str, id: int, static_url: str, fallback_static_url: str, animation_url: str, popup_url: str, sound_url: str) -> None:
        self.type = type
        self.id = id
        self.static_url = static_url
        self.fallback_static_url = fallback_static_url
        self.animation_url = animation_url
        self.popup_url = popup_url
        self.sound_url = sound_url

    @staticmethod
    def from_dict(obj: Any) -> 'DataPreview':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        id = int(from_str(obj.get("id")))
        static_url = from_str(obj.get("staticUrl"))
        fallback_static_url = from_str(obj.get("fallbackStaticUrl"))
        animation_url = from_str(obj.get("animationUrl"))
        popup_url = from_str(obj.get("popupUrl"))
        sound_url = from_str(obj.get("soundUrl"))
        return DataPreview(type, id, static_url, fallback_static_url, animation_url, popup_url, sound_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["id"] = from_str(str(self.id))
        result["staticUrl"] = from_str(self.static_url)
        result["fallbackStaticUrl"] = from_str(self.fallback_static_url)
        result["animationUrl"] = from_str(self.animation_url)
        result["popupUrl"] = from_str(self.popup_url)
        result["soundUrl"] = from_str(self.sound_url)
        return result


def data_preview_from_dict(s: Any) -> DataPreview:
    return DataPreview.from_dict(s)


def data_preview_to_dict(x: DataPreview) -> Any:
    return to_class(DataPreview, x)
