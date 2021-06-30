import pytest
import os
import shutil
import filecmp
import pathlib
from pyrender import render



def test_render_object_creation():
    """
    Test if the apiserver template where rendered successifully
    """
    jinja_name = "test/jinja-files/test.html.j2"
    parameters = {'foo': 'batata'}
    assert render.JinjaRender(jinja_name, parameters)


def test_template_rendering():
    """
    Test template Rendering
    """
    jinja_name = "test/jinja-files/test.html.j2"
    parameters = {'foo': 'batata'}
    oo = render.JinjaRender(jinja_name, parameters)
    assert oo.RenderTemplate()


def test_if_rendered_correctly():
    """
    Test if the function to used to render the template is doing
    it correctly
    """
    jinja_name = "test/jinja-files/test.html.j2"
    parameters = {'foo': 'batata'}
    oo = render.JinjaRender(jinja_name, parameters)
    assert oo.RenderTemplate() == "<h1>batata</h1>"


def test_where_file_was_created():
    """
    Test if the file was created on the corret folder
    """
    jinja_name = "test/jinja-files/test.html.j2"
    parameters = {'foo': 'batata'}
    oo = render.JinjaRender(jinja_name, parameters)
    oo.RenderJinjaFile()
    rendered_file_name = ".".join(jinja_name.split("/")[-1].split(".")[:-1])
    assert os.path.isfile(rendered_file_name)
    os.remove(rendered_file_name)


def test_if_file_is_generated():
    """
    Test if the file is returning the expected success message
    """
    jinja_name = "test/jinja-files/test.html.j2"
    parameters = {'foo': 'batata'}
    oo = render.JinjaRender(jinja_name, parameters)
    rendered_file_name = ".".join(jinja_name.split("/")[-1].split(".")[:-1])
    assert oo.RenderJinjaFile() == "Succeded in rendering the file"
    os.remove(rendered_file_name)


def test_if_file_the_content_is_correct():
    """
    Test the content inside the file if being rendered correctly
    """
    jinja_name = "test/jinja-files/test.html.j2"
    parameters = {'foo': 'batata'}
    oo = render.JinjaRender(jinja_name, parameters)
    oo.RenderJinjaFile()
    rendered_file_name = ".".join(jinja_name.split("/")[-1].split(".")[:-1])
    with open(rendered_file_name) as f:
        assert ''.join(f.readlines()) == "<h1>batata</h1>"
    os.remove(rendered_file_name)


def test_where_file_was_created_if_on_pwd_folder():
    """
    Test if the file was created on the corret folder as
    as the template is on the . folder path
    """
    src = r'test/jinja-files/test.html.j2'
    dst = r'./test.html.j2'
    shutil.copyfile(src, dst)
    jinja_name = 'test.html.j2'
    parameters = {'foo': 'batata'}
    oo = render.JinjaRender(jinja_name, parameters)
    oo.RenderJinjaFile()
    rendered_file_name = ".".join(jinja_name.split(".")[:-1])
    assert os.path.isfile(rendered_file_name)
    os.remove(rendered_file_name)
    os.remove('./test.html.j2')


def test_if_file_was_created_on_the_choosen_folder():
    """
    Test if the file was created on the folder passed as paramter
    """
    jinja_name = "test/jinja-files/test.html.j2"
    parameters = {'foo': 'batata'}
    output = "/tmp/"
    oo = render.JinjaRender(jinja_name, parameters, output)
    oo.RenderJinjaFile()
    rendered_file_name = ".".join(jinja_name.split("/")[-1].split(".")[:-1])
    assert os.path.isfile(output + rendered_file_name)
    os.remove(output + rendered_file_name)


def test_if_file_was_created_choosing_the_name():
    """
    Test if the file was created on the folder passed as paramter
    """
    jinja_name = "test/jinja-files/test.html.j2"
    parameters = {'foo': 'batata'}
    output = "/tmp/index.html"
    oo = render.JinjaRender(jinja_name, parameters, output)
    oo.RenderJinjaFile()
    assert os.path.isfile(output)
    os.remove(output)


def test_rendering_complex_jinja():
    """
    Test if the file redered correctly
    """
    jinja_name = "test/jinja-files/kube-apiserver.sh.j2"
    rendered_file = "test/rendered-files/kube-apiserver.sh"
    parameters = {
        'etcd_ip': [
            '10.1.0.11',
            '10.1.0.12',
            '10.1.0.13'
        ],
        'cntlr_ip': [
            '10.1.0.21',
            '10.1.0.22',
            '10.1.0.23'
        ],
        'k8s_services_version': '1.20.2',
        'k8s_internal_network': '10.200.0.0',
        'k8s_cert_dir': '/var/lib/kubernetes/pki/',
        'k8s_ca_cert': 'cat.pem',
        'k8s_apiserver_cert': 'kubernetes.pem',
        'k8s_apiserver_key': 'kubernetes-key.pem',
        'k8s_account_cert': 'service-account.pem',
        'k8s_account_key': 'service-account-key.pem',
        'k8s_config_dir': '/var/lib/kubernetes/',
        'etcd_cert': 'etcd.pem',
        'etcd_key': 'etcd-key.pem',
        'etcd_client_port': '2379'
    }
    output = "kube-apiserver.sh"
    oo = render.JinjaRender(jinja_name, parameters, output)
    oo.RenderJinjaFile()
    assert filecmp.cmp(output, rendered_file)
    os.remove(output)


def test_if_fail_to_overwrite_without_parameter():
    """
    Test if the code will fail to overwrite the file
    whithout the parameter
    """
    jinja_name = "test/jinja-files/test.html.j2"
    parameters = {'foo': 'batata'}
    output = "test/rendered-files/overwrite.html"
    oo = render.JinjaRender(jinja_name, parameters, output)
    err_msg = "Failed to render the file, it already exists"
    assert oo.RenderJinjaFile() == err_msg


def test_varibles_with_equal_sign():
    """
    Test if the file is returning the expected success message
    """
    jinja_name = "test/jinja-files/test-list.html.j2"
    parameters = {'foo': ["zone=A", "environment=admin"]}
    oo = render.JinjaRender(jinja_name, parameters)
    rendered_file_name = ".".join(jinja_name.split("/")[-1].split(".")[:-1])
    assert oo.RenderJinjaFile() == "Succeded in rendering the file"
    os.remove(rendered_file_name)


def test_using_absolute_path():
    """
    Test if the file was created on the folder passed as paramter
    """
    current_directory = str(pathlib.Path().resolve())
    jinja_name = current_directory + "/test/jinja-files/test.html.j2"
    parameters = {'foo': 'batata'}
    output = "/tmp/index.html"
    oo = render.JinjaRender(jinja_name, parameters, output)
    oo.RenderJinjaFile()
    assert os.path.isfile(output)
    os.remove(output)
