import re
from yaml import load
from yaml import FullLoader

from collections.abc import Mapping

class Content(Mapping):
    __delimeter = "^(?:-|\+){3}\s*$"

    __regex = re.compile(__delimeter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _ = cls.__regex.split(string, 2)
        fm = cls.__regex.split(string, 2)
        content = cls.__regex.split(string, 2)

        load(fm, Loder = FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        content = {self.data:"content"}

    @property
    def body(self):
        self.data["content"]

    @property
    def type(self):
        if self.data[:1] is type:
            self.data["type"]
        else:
            return None
        self.data = self.data["type"]

    def __getitem__(self, item):
        self.type()

    def __iter__(self):
        iter(self.data)

    def __len__(self):
        len(self.data)

    def __repr__(self):
        data = {}
        return str(data)

        for key in self.data.items():
            if key is not "conent":data[key]
            return "Error"

