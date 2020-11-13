from typing import List
from pathlib import Path
import shutil


class Parser:
    def __init__(self):
        self.extensions: List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path: Path):
        with path.open() as file:
            return file.read()

    def write(self, path: Path, dest: Path, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name

        with full_path.open(mode="w") as file:
            file.write(content)

    def copy(self, path: Path, source: Path, dest: Path):
        shutil.copy2(path, dest / path.relative_to(source))

class ResourceParser(Parser):
    def __init__(self):
        self.extensions = [ ".jpg", ".png", ".gif", ".css", ".html", ]

    def parse(self, path: Path, source: Path, dest: Path):
        self.copy(path, source, dest)