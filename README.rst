BLOG
======
**We have developed a blog project.**

Install
-------

**Be sure to use the same version of the code as the version of the docs
you're reading.** You probably want the latest tagged version, but the
default Git version is the master branch. ::

    # clone the repository
    $ git clone https://github.com/...
    $ cd flask
    # checkout the correct version
    $ git tag  # shows the tagged versions
    $ git checkout latest-tag-found-above
    $ cd examples/tutorial

Create a virtualenv and activate it::

    $ python3 -m venv venv
    $ . venv/bin/activate

Or on Windows cmd::

    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat

Install ::

    $ pip install -e .

Or if you are using the master branch, install blog from source before
installing Blog_project::

    $ pip install -e ../..
    $ pip install -e .


Run
---

::

    $ export FLASK_APP=blog
    $ export FLASK_ENV=development
    $ flask run

Or on Windows cmd::

    > set FLASK_APP=blog
    > set FLASK_ENV=development
    > flask run

Open http://127.0.0.1:5000 in a browser.

**In MongoDB documents should be created in the "Category" collection as shown below:**
::
    {
    "id": "ورزشی",
    "parent": "#",
    "text": "ورزشی"
    }

    {
    "id": "والیبال",
    "parent": "ورزشی",
    "text": "والیبال"
    }

    {
    "id": "فوتبال",
    "parent": "ورزشی",
    "text": "فوتبال"
    }

    {
    "id": "لیگ برتر",
    "parent": "فوتبال",
    "text": "لیگ برتر"
    }




