
from pymono.scriptlet import Scriptlet


class InterceptorAttach(Scriptlet):
    """This scriptlet calls Interceptor.attach() on the target process."""
    code = """Interceptor.attach(Module.findExportByName("{module}", "{function}"), {callback})"""

class InterceptorDetach(Scriptlet):
    """This scriptlet calls Interceptor.detach() on the target process."""
    code = """Interceptor.detach({callback})"""


