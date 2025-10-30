from app.text_translation.deepl_translate import translate_text

def markdown_translate(md_text: str, target_lang: str, backend: str = "deepl") -> str:

    lines = md_text.split("\n")

    translated_md = ""
    for line in lines:
        translated_text = translate_text(line, target_lang)
        translated_md += translated_text + "\n"
    
    return translated_md