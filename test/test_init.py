import mock
import pytest
import os
from pyrender import __main__


def test_init():
    with mock.patch.object(__main__, "main", return_value=42):
        with mock.patch.object(__main__, "__name__", "__main__"):
            with mock.patch.object(__main__.sys, 'exit') as mock_exit:
                __main__.init()
                assert mock_exit.call_args[0][0] == 42


def test_exit_error():
    with mock.patch.object(__main__, "__name__", "__main__"):
        with mock.patch.object(__main__.sys, 'exit') as mock_exit:
            __main__.init([
                "test/jinja-files/test.html.j2",
                "--set",
                "foo=batata",
                "--output",
                "test/rendered-files/overwrite.html"
            ])
            assert mock_exit.call_args[0][0] == 1


def test_exit_success():
    with mock.patch.object(__main__, "__name__", "__main__"):
        with mock.patch.object(__main__.sys, 'exit') as mock_exit:
            __main__.init([
                "test/jinja-files/test.html.j2",
                "--set",
                "foo=batata",
                "--output",
                "/tmp/test-error.html",
                "--force"
            ])
            assert mock_exit.call_args[0][0] == 0
            os.remove("/tmp/test-error.html")
