from markdown import Markdown
from io import StringIO
import re

def process_markdown(md_text: str) -> str:
    md_text = re.sub(r'\n(?!\n)', ' ', md_text)

    return re.sub(r'\n(?!\n)', ' ', md_text)


def unmark_element(element, stream=None):
    if stream is None:
        stream = StringIO()
    if element.text:
        stream.write(element.text)
    for sub in element:
        unmark_element(sub, stream)
    if element.tail:
        stream.write(element.tail)
    return stream.getvalue()


# patching Markdown
Markdown.output_formats["plain"] = unmark_element
__md = Markdown(output_format="plain")
__md.stripTopLevelTags = False


def unmark(text):
    return __md.convert(text)