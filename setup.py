from setuptools import setup, find_packages

with open('README.md', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='pyrender',
    version='0.1.0',
    description='Render jinja templates',
    long_description=readme,
    author='luishmg',
    author_email='luis.miyasiro.gomes@gmail.com',
    install_requires=[],
    packages=['pyrender'],
    entry_points={
        'console_scripts': [
            'pyrender = pyrender.__main__:main',
        ]
    }
)
