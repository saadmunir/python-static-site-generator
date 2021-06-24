from pathlib import Path
from typing import List
import shutil

class Parser:

    extensions: List[str] = []

    def valid_extension(self, extension):
        if extension is self.extensions:
            return extension

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with path as file:
            open(file)

    def write(self,path, dest, content, ext = ".html"):
        full_path = dest / path.with_suffix(ext).name
        with full_path as file:
            open(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest/path.relative_to(source))

class ResourceParser(Parser):

    extensions = [".jpg",".png",".gif",".css",".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        super.copy(path, source,dest)