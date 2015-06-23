from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose
from cement.core import handler
import common.tor as tor
from stem import CircStatus, Signal
import requesocks as requests

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
        controller = tor.conn()

        proxies = {
          "http": "socks5://localhost:9050/",
          "https": "socks5://localhost:9050/",
        }


        resp = requests.get("https://api.ipify.org", proxies=proxies)
        print(resp.text)

        controller.signal(Signal.NEWNYM)
        import time
        print("u--qw-dq-wd-qw-dq-wd-q-wd-")
        time.sleep(5)

        resp = requests.get("https://api.ipify.org", proxies=proxies)
        print(resp.text)

class Ipto(CementApp):
    class Meta:
        label = 'myapp'
        base_controller = 'base'
        handlers = [MainController]
