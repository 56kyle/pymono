
import frida

import pymem
from frida.core import Session, Script
from typing import Optional


class Process:
    """A class that represents a running process"""
    session: Session

    def __init__(self, session: Session):
        self.session: Session = session
        self.pid =


