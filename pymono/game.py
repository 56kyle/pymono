import frida
import pymem

from typing import Optional, List, Tuple


class Game:
    """A class to represent a Unity game that uses the Mono Runtime"""
    def __init__(self,
                 name: Optional[str] = None,
                 path: Optional[str] = None,
                 *args):
        self.name = name
        self.path = path
        self.args = args
        self.process: Process = None

    def attach(self, pid):
        """Attaches to a running instance of the current game using frida"""
        pass

    def start(self):
        """Starts a game instance using frida"""
        pass


