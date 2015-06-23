from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose
from cement.core import handler
import common.tor as tor

class MainController(CementBaseController):
    class Meta:
        label = 'base'
        description = """Convert list of IP addresses into lists of domain names
        using robtex and Tor."""
        arguments = [
            ( ['-i', '--input'],
              dict(action='store', help='Input file to read IP addresses from.', required=True)),
            ( ['-o', '--output'],
              dict(action='store', help='File to output the domains to.', required=True)),
            ]

    @expose(hide=True)
    def default(self):
        controller = tor.connect()


class Ipto(CementApp):
    class Meta:
        label = 'myapp'
        base_controller = 'base'
        handlers = [MainController]
