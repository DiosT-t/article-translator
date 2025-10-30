import pymupdf4llm
from app.utils.markdown_utils import process_markodwn


def read_pdf_text(file) -> str:
    markdown = pymupdf4llm.to_markdown(
        file,
        ignore_images=True,
        ignore_graphics=True,
        # page_separators=True
        )
    with open("output.md", "w", encoding="utf-8") as f:
        f.write(process_markodwn(markdown))
    print(process_markodwn(markdown))
    return process_markodwn(markdown)
