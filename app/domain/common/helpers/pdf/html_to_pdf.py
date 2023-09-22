import os
import tempfile
from dataclasses import dataclass
from pathlib import Path

from weasyprint import HTML


@dataclass
class HtmlToPdf:
    template: str
    filename: str
    assigns: dict
    path: str = ""
    content: str = ""

    def render(self):
        tempdir = tempfile.mkdtemp()
        self.path = f"{tempdir}/{self.filename}"

        self.__render_template()
        HTML(string=self.content).write_pdf(self.path)

        return self

    def __render_template(self) -> str | None:
        content = self.__resolve_template()

        for key, value in self.assigns.items():
            content = content.replace("{{" + str(key) + "}}", value)
        self.content = content

    def __resolve_template(self):
        root_path = os.path.abspath(os.curdir)
        template_path = f"{root_path}/{self.template}"

        return Path(template_path).read_text()
