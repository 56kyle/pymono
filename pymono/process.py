
import frida

import pymem
from frida.core import Session, Script
from typing import Optional


class Process:
    """A class that represents a running process"""
    session: Session

    def __init__(self, ):
        self.session: Session = session
        pymem.Pymem.

    @classmethod
    def attach(cls, pid):
        """Attach to a process"""
        return cls(frida.attach(pid), pid)

    @classmethod
    def spawn(cls, path, **kwargs):
        """Spawn a process"""
        return cls(frida.spawn(path, **kwargs))

