from app.core.settings import get_settings
from deep_translator import DeeplTranslator

Settings = get_settings()

def translate_text(text: str, target_lang: str) -> str:
    translator = DeeplTranslator(api_key=Settings.deepl_api_key, 
                                 source="en",
                                 target=target_lang,
                                 use_free_api=True)
    translated_text = translator.translate(text)

    return translated_text