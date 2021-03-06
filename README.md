jinjarenderer
=============

CLI to verify to render jinja files from the command line.

Preparing the Development
-------------------------

1. Ensure ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``git clone ``
3. ``cd`` into the repository.
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``

Usage
-----

Pass the files or a directory to be searched by the tool.

Example using mesos verification passing a file:

::

    $ scanjson somefile.app.json
    
Example using 

Running Tests
-------------

Run tests locally ``make`` if virtualenv is active:

::

    $ make

If virtual env isn't active then use:

::

    $ pipenv run make
