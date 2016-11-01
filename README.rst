dm-cli
=========

*A DM command line program in Python.*

License
-------
Copyright 2016 Codeabovelab

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Purpose
-------

This is a DM CLI application which provids API to DM server

Usage
-----

If you've cloned this project, and want to install the library (*and all
development dependencies*), the command you'll want to run is::

    $ pip install -e .[test]

If you'd like to run all tests for this project (*assuming you've written
some*), you would run the following command::

    $ python setup.py test

This will trigger `py.test <http://pytest.org/latest/>`_, along with its popular
`coverage <https://pypi.python.org/pypi/pytest-cov>`_ plugin.

Lastly, if you'd like to cut a new release of this CLI tool, and publish it to
the Python Package Index (`PyPI <https://pypi.python.org/pypi>`_), you can do so
by running::

    $ python setup.py sdist dmaster_cli
    $ twine upload dist/*

This will build both a source tarball of your CLI tool, as well as a newer wheel
build (*and this will, by default, run on all platforms*).

The ``twine upload`` command (which requires you to install the `twine
<https://pypi.python.org/pypi/twine>`_ tool) will then securely upload your
new package to PyPI so everyone in the world can use it!
