import pytest
from pyrender import cli


@pytest.fixture()
def parser():
    return cli.CreateParser()


def test_basic_cli(parser):
    """
    Test if the object was created successifully
    """
    assert parser.parse_args([
        "test/jinja-files/test.html.j2",
        "--set",
        "foo=batata"
    ])


def test_verbose_option(parser):
    """
    Test if the object was created successifully
    """
    assert parser.parse_args([
        "test/jinja-files/test.html.j2",
        "--set",
        "foo=batata",
        "-v"
    ])


def test_destination_option_as_dir(parser):
    """
    Test if the object was created successifully
    """
    assert parser.parse_args([
        "test/jinja-files/test.html.j2",
        "--set",
        "foo=batata",
        "-o",
        "/tmp"
    ])


def test_destination_option_as_file(parser):
    """
    Test if the object was created successifully
    """
    assert parser.parse_args([
        "test/jinja-files/test.html.j2",
        "--set",
        "foo=batata",
        "-o",
        "/tmp/test.html"
    ])


def test_destination_option_as_output(parser):
    """
    Test if the object was created successifully
    """
    assert parser.parse_args([
        "test/jinja-files/test.html.j2",
        "--set",
        "foo=batata",
        "--output",
        "/tmp/test.html"
    ])


def test_list_parameter(parser):
    """
    Test if passing a list as a parameter will
    not break the code
    """
    assert parser.parse_args([
        "test/jinja-files/test-list.html.j2",
        "--set",
        "foo=[10.1.0.10,10.1.0.11,10.1.0.12]",
        "--output",
        "/tmp/test.html"
    ])


def test_overwrite_file_parameter(parser):
    """
    Test if overwrite parameter will not break the code
    not break the code
    """
    assert parser.parse_args([
        "test/jinja-files/test-list.html.j2",
        "--set",
        "foo=[10.1.0.10,10.1.0.11,10.1.0.12]",
        "--output",
        "/tmp/test.html",
        "-f"
    ])


def test_overwrite_file_parameter_force(parser):
    """
    Test if overwrite parameter will not break the code
    not break the code
    """
    assert parser.parse_args([
        "test/jinja-files/test-list.html.j2",
        "--set",
        "foo=[10.1.0.10,10.1.0.11,10.1.0.12]",
        "--output",
        "/tmp/test.html",
        "--force"
    ])


def test_set_receaving_empty_value(parser):
    """
    Test if the funcion now how to deal with empty value
    """
    assert parser.parse_args([
        "test/jinja-files/test.html.j2",
        "--set",
        "foo="
    ])
