from cement.utils import test
from ipto import Ipto
from mock import Mock, patch

class MyTestCase(test.CementTestCase):
    app_class = Ipto
    default_input = "input_file.txt"
    default_output = "output_file.txt"
    default_argv = ['-i', default_input, '-o', default_output]

    def setUp(self):
        super(MyTestCase, self).setUp()
        self.reset_backend()

        self.app = Ipto(argv=self.default_argv, config_files=[])
        self.app._meta.exit_on_close = False

        self.app.setup()

    def tearDown(self):
        pass

    def test_calls_tor_connect(self):
        with patch("ipto.common.tor.conn") as c:
            self.app.run()
            assert c.called
        self.app.close()

    def test_tor_connect(self):
        assert False

