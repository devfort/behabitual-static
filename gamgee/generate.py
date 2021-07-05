import os
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape


BASE_PATH = Path(__file__).parent.parent
SRC_PATH = BASE_PATH / "src"
PAGES_PATH = SRC_PATH / "pages"
DEST_PATH = BASE_PATH / "dest"


env = Environment(
    loader=FileSystemLoader(str(SRC_PATH)),
    autoescape=select_autoescape(),
)

context = {"name": "world"}

for path in PAGES_PATH.glob("**/*.html"):
    template_path = path.relative_to(SRC_PATH)
    template = env.get_template(str(template_path))
    html = template.render(**context)

    dest_path = DEST_PATH / path.relative_to(PAGES_PATH)
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    with dest_path.open("w") as dest_file:
        dest_file.write(html + "\n")
