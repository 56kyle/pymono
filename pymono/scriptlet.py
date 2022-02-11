
from typing import TypeVar, Generic


class Scriptlet:
    """A scriptlet is a small piece of code that can be recursively implemented to form a full javascript script"""

    code: str

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        super().__init__(**kwargs)

    def __str__(self):
        return self.code.format(**self.kwargs)

    def __repr__(self):
        """Returns a string representation of how to create this scriptlet"""
        return f'Scriptlet("{self.code}", {self.kwargs})'

