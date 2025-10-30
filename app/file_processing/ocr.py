from typing import List
from paddleocr import PaddleOCRVL
from pathlib import Path

engine = PaddleOCRVL(
            use_layout_detection=False,
            enable_mkldnn=True
    )


def ocr_file(file , lang: str) -> List[str]:
    output = engine.predict(input=file)

    markdown_list = []
    markdown_images = []

    for res in output:
        md_info = res.markdown
        markdown_list.append(md_info)
        markdown_images.append(md_info.get("markdown_images", {}))

    markdown_texts = engine.concatenate_markdown_pages(markdown_list)

    mkd_file_path = Path("") / f"{Path(file).stem}.md"
    mkd_file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(mkd_file_path, "w", encoding="utf-8") as f:
        f.write(markdown_texts)

    for item in markdown_images:
        if item:
            for path, image in item.items():
                file_path = Path("") / path
                file_path.parent.mkdir(parents=True, exist_ok=True)
                image.save(file_path)

    return markdown_texts