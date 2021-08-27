BLOG
======
**We have developed a blog project using the MongoDB database.**

Install
-------

**Be sure to use the same version of the code as the version of the docs
you're reading.** You probably want the latest tagged version, but the
default Git version is the master branch. ::

    # clone the repository
    $ git clone https://github.com/mahdisj/Blog_Project.git
    $ cd Blog_Project

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

**In this project, "category" data should be created like the file uploaded in the link below:**
::

    Open https://github.com/mahdisj/Blog_Project/blob/main/category.json in your browser.

