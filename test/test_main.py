import mock
import pytest
import os
import filecmp
from pyrender import __main__


def test_pyrender_min_main():
    """
    Test if the main function is working as intended
    """
    jinja_name = "test/jinja-files/test.html.j2"
    rendered_file_name = ".".join(jinja_name.split("/")[-1].split(".")[:-1])
    assert __main__.main([
        jinja_name,
        "--set",
        "foo=batata"
    ]) == 0
    os.remove(rendered_file_name)


def test_pyrender_main_adding_verbose():
    """
    Test if the verbose option is working
    """
    jinja_name = "test/jinja-files/test.html.j2"
    rendered_file_name = ".".join(jinja_name.split("/")[-1].split(".")[:-1])
    assert __main__.main([
        jinja_name,
        "--set",
        "foo=batata",
        "-v"
    ]) == 0
    os.remove(rendered_file_name)


def test_pyrender_main_adding_verbose_and_output():
    """
    Test if the verbose is working with the output option
    """
    jinja_name = "test/jinja-files/test.html.j2"
    rendered_file_name = ".".join(jinja_name.split("/")[-1].split(".")[:-1])
    output = "/tmp/"
    assert __main__.main([
        jinja_name,
        "--set",
        "foo=batata",
        "-v",
        "--output",
        output
    ]) == 0
    os.remove(output + rendered_file_name)


def test_pyrender_main_output_choosing_file_name():
    """
    Test if the template create a file /tmp/index.html
    """
    jinja_name = "test/jinja-files/test.html.j2"
    output = "/tmp/index.html"
    __main__.main([
        jinja_name,
        "--set",
        "foo=batata",
        "-v",
        "--output",
        output
    ])
    assert os.path.isfile(output)
    os.remove(output)


def test_pyrender_main_output_using_contracted_option():
    """
    Test if the apiserver template where rendered successifully
    """
    jinja_name = "test/jinja-files/test.html.j2"
    output = "/tmp/index.html"
    assert __main__.main([
        jinja_name,
        "--set",
        "foo=batata",
        "-o",
        output
    ]) == 0
    assert os.path.isfile(output)
    os.remove(output)


def test_pyrender_list_parameter():
    """
    Test if passing a list as a parameter will
    not break the code
    """
    jinja_name = "test/jinja-files/test-list.html.j2"
    output = "/tmp/test-list.html"
    rendered_file = "test/rendered-files/test-list.html"
    assert __main__.main([
        jinja_name,
        "--set",
        "foo=10.1.0.10,10.1.0.11,10.1.0.12",
        "--output",
        output
    ]) == 0
    assert filecmp.cmp(output, rendered_file)
    os.remove(output)


def test_pass_empty_variable():
    """
    Test if the behavior is what is expected
    """
    jinja_name = "test/jinja-files/test.html.j2"
    output = "/tmp/empty.html"
    assert __main__.main([
        jinja_name,
        "--set",
        "foo=",
        "-o",
        output
    ]) == 0
    os.remove(output)


def test_multiple_variables_with_equal_sign():
    """
    Test if the behavior is what is expected
    """
    jinja_name = "test/jinja-files/test-list.html.j2"
    output = "/tmp/empty.html"
    assert __main__.main([
        jinja_name,
        "--set",
        "foo=zone=A,environment=admin",
        "-o",
        output
    ]) == 0
    os.remove(output)


def test_test_if_the_overwrite_is_working():
    """
    Test if the behavior is what is expected
    """
    jinja_name = "test/jinja-files/test.html.j2"
    output = "test/rendered-files/overwrite.html"
    assert __main__.main([
        jinja_name,
        "--set",
        "foo=batata",
        "-o",
        output,
        "-f"
    ]) == 0
