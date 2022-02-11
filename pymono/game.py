import frida
import pymem

from typing import Optional, List, Tuple

from pymono.process import Process


class Game:
    """A class to represent a Unity game that uses the Mono Runtime"""
    def __init__(self,
                 name: str = None,
                 path: str = None,
                 *args, **kwargs):

        self.device: frida.core.Device = frida.get_local_device()
        self.name: str = name
        self.path: str = path
        self.args = args
        self.process: Process | None = None

    def attach(self, pid):
        """Attaches to a running instance of the current game using frida"""
        self.process = Process(self.device.attach(pid))

    def spawn(self):
        """Starts a game instance using frida"""
        return self.device.spawn(self.path, self.args)



