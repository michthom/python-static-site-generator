import re
from yaml import load, FullLoader
from collections.abc import Mapping


class Content(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        (_, fm, content) = Content.__regex.split(string, maxsplit=2)

        # yaml.load, this isn't recursive!
        load(fm, Loader=FullLoader)

        return cls(content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content

    @property
    def body(self):
        return self.data["content"]

    @property
    def type(self):
        return self.data["type"]

    @type.setter
    def type(self, type):
        self.data["type"] = type
