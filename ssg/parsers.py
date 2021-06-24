from pathlib import Path
from typing import List
import shutil

class Parser:

    extensions: List[str] = []

    def valid_extension(self, extension):
        extension is self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path):
        with open(path) as file:
            file.read()

    def write(self,path, dest, content, ext = ".html"):
        full_path = self.dest / path.with_suffix(ext).name
        with open(full_path) as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest / source.path)

class ResourceParser(Parser):

    extensions = [".jpg",".png",".gif",".css",".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        super.copy(path, source,dest)