import os
from pathlib import Path
import shutil

from jinja2 import Environment, FileSystemLoader, select_autoescape
import sass


BASE_PATH = Path(__file__).parent.parent
SRC_PATH = BASE_PATH / "src"
DEST_PATH = BASE_PATH / "dest"


def generate_html():
    """
    Compiles Jinja2 templates in `{SRC_PATH}/html/pages` to produce rendered
    HTML pages in `{DEST_PATH}/`.

    Other files in `{SRC_PATH}/html` will be visible to the Jinja2 compiler,
    e.g. for includes, inheritance, etc.
    """

    html_src_path = SRC_PATH / "html"
    pages_path = html_src_path / "pages"

    env = Environment(
        loader=FileSystemLoader(str(html_src_path)),
        autoescape=select_autoescape(),
    )

    context = {
        "CONTACT_EMAIL": "...",
        "GOOGLE_ANALYTICS_ID": "...",
    }

    for path in pages_path.glob("**/*.html"):
        template_path = path.relative_to(html_src_path)
        template = env.get_template(str(template_path))
        html = template.render(**context)

        dest_path = DEST_PATH / path.relative_to(pages_path)
        dest_path.parent.mkdir(parents=True, exist_ok=True)

        with dest_path.open("w") as dest_file:
            dest_file.write(html + "\n")


def generate_css():
    """
    Compiles Sass file at `{SRC_PATH}/scss/_manifest.scss` to produce a CSS
    file at `{DEST_PATH}/hobbit.css`.

    Other files in `{SRC_PATH}/scss` will be visible to the Sass compile,
    e.g. for imports.
    """

    scss_src_path = SRC_PATH / "scss"
    manifest_path = scss_src_path / "_manifest.scss"

    css = sass.compile(
        filename=str(manifest_path),
        include_paths=(str(scss_src_path),),
        output_style="compact",
    )
    with (DEST_PATH / "hobbit.css").open("w") as dest_file:
        dest_file.write(css)


def copy_static():
    """
    Copies static files from `{SRC_PATH}/static` to DEST_PATH.
    """

    static_src_path = SRC_PATH / "static"

    shutil.copytree(
        src=static_src_path,
        dst=DEST_PATH,
        dirs_exist_ok=True,
    )


if __name__ == "__main__":
    generate_html()
    generate_css()
    copy_static()
