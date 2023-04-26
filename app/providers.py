from googletrans import Translator

_default_providers = {
    "en->fa": "googletrans",

    "fa->en": "googletrans",

    "ar->fa": "googletrans",

    "fa->ar": "googletrans",

    "ar->en": "googletrans",

    "en->ar": "googletrans"
}


def googletrans(source, target, text):
    translator = Translator()
    result = translator.translate(text, src=source, dest=target)
    return result['text']


def findProvider(source, target):
    p = _default_providers[source + "->" + target]
    match p:
        case "googletrans":
            return googletrans
