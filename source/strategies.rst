===========================================================================
Migration strategies
===========================================================================

Making a new release of software that is backwards incompatible is a high risk
strategy. When people need to rewrite their software, or maintain separate
versions of their source code to support both versions of a language or a
framework, the risk is that they never make the transition and stay on the old
version forever, or worse, that they switch to another framework.

For that reason Python versions 2.6 and 2.7 include both several forward
compatibility features to enable you to write code for both Python 2 and
Python 3, as well as support for migrating in the form of ``2to3``, a program
and package that can convert code
from Python 2 to Python 3. There are other techniques and strategies you can
use and there are also different ways to use ``2to3``. Which strategy to use
depends very much on what type of software you are converting.

---------------------------------------------------------------------------
Only supporting Python 3
---------------------------------------------------------------------------

The easiest case is when you only need to support one version of Python at a
time. In these cases you can just convert your code to Python 3 and forget
about Python 2. With this strategy you will first use the ``2to3`` tool to make
an automatic conversion of most of the changes and then fix every problem that
remains manually in the Python 3 code. You will probably also want to go
through all of the converted code and clean it up, as the ``2to3`` conversions
may not always be the most elegant solution for your case.

---------------------------------------------------------------------------
Separate branches for Python 2 and Python 3
---------------------------------------------------------------------------

.. index:: CheeseShop, PyPI, setup.py, Distutils

If you need to continue to support Python 2, the simplest case is having a
branch in your source tree with the code for Python 2 and another branch for
Python 3. You will then have to make every change on the two different
branches, which is a bit more work, but feasible if the code doesn't change that
often.

One problem with this strategy is that your distribution becomes complex,
because you now have two distributions and you need to make sure that Python 3
users get the Python 3 version and Python 2 users get the Python 2 version of
your package. Solutions for this are documented in :ref:`distribution-section`.

---------------------------------------------------------------------------
Converting to Python 3 with 2to3
---------------------------------------------------------------------------

.. index:: 2to3

In complex cases you can support both Python 2 and Python 3 by
maintaining the source code in a Python 2 version and converting it with ``2to3`` for
Python 3 support. That means you will have to run ``2to3`` each time you have
made a code change so you can test it under Python 3, but on the other hand
``2to3`` deals with many of the differences.

To do this you need a script that performs the ``2to3`` conversion, because
doing all the steps manually quickly becomes really boring. Since you need to do
the conversion every time you have changed something so you can run the tests
under Python 3, you want to run the conversion only on the files that have been
modified as the conversion can be rather slow. That means that the conversion
script should compare time stamps on the files to see which ones have been
modified and convert only them, which means the script can not be a trivial
shell script.

You can of course write these conversion scripts yourself, but you might not
need to. If you are using Distutils it has support for running ``2to3`` as a
part of the build process. This also solves the distribution problems, as this
way you can distribute only Python 2 code and ``2to3`` will be run on that code
during install when installed on Python 3. That way you don't have to have
separate packages or even two copies of the code in your package.
:ref:`distribution-section` also has information on this.

However, the lazy coders approach here would be to use Distribute, as it
includes some extensions to the ``2to3``-story.


Using Distribute to support the 2to3 conversion
===========================================================================

.. index:: Distribute, Setuptools, Distutils

Distribute\ [#distribute]_ is a fork of Phillip J. Eby's popular Setuptools
package and provides Python 3 compatibility, as well as extensions simplifying
the support of Python 2 and Python 3 from the same source. Basically what
Distribute has done is to extend the principles of the Distutils ``build_py_2to3``
command and integrated ``2to3`` into all parts of the packaging story.

These changes will be merged back into Setuptools during 2013, but at the time
of writing Setuptools doesn't support Python 3.

With Distribute you can add a few extra parameters in the ``setup.py`` file to
have ``2to3`` run the conversion at build time. This means you only need to have
one version of the source in your version control system and you therefore only
need to fix bugs once. You also need only one source release, so you only have
to release the software once and there is only one package to download and
install for both Python 2 and Python 3.

You still need to run your tests under all versions of Python that you want to
support, but Distribute includes a test command that will convert your code with
``2to3`` before running the tests. You can easily set up your package to use
that. Then testing becomes just running ``python setup.py test`` once for every
python version you want to support.

The main drawback with this solution is that you can't use the earliest versions
of ``2to3``, because they are too buggy. In practice it means you need to have
Python 3.1 or later installed on the target machine. This is generally not a
problem, as most platforms that support Python 3 already use Python 3.1 for
that support.

You can find examples of how to set up your module or package to use Distribute
for your Python 3 support under :ref:`usingdistribute` as well as in the
standard Distribute documentation\ [#distributedoc]_.

---------------------------------------------------------------------------
Python 2 and Python 3 without conversion
---------------------------------------------------------------------------

In many cases it's often perfectly feasible to modify the code so that it runs
under both Python 2 and Python 3 without needing any conversion, although you
have to apply several tricks to avoid the incompatibilities between Python 2
and Python 3.

Python 2.6 and 2.7 have a lot of forward compatibility, making supporting
Python 2.6 and Python 3 much easier than supporting Python 2.5 and Python 3.
Supporting 2.5 or even older versions means you have to employ more tricks.
Python 3.3 also re-introduces the ``u''`` literal for strings, which helps with
one of the major difficulties in supoprting Python 3.

.. index:: six

Benjamin Petersons excellent ``six`` module\ [#six]_ also helps by wrapping
much of the incompatibilities, and since the need to support older Python
versions is shrinking, supporting both Python 2 and Python 3 without conversion
is becoming the preferred method.

There are also cases where you can't use Distribute, or don't want to. You may
need to distribute your code in a format that is not installable with Distutils
and therefore not Distribute. In those cases you can't use Distribute's ``2to3``
support and then using ``2to3`` is more work and not using ``2to3`` becomes a
more attractive prospect.

Even if you do use ``2to3`` for your project as a whole, you still may
end up with having to write some code so it runs on both Python 2 and Python 3
without conversion. This is useful for bootstrapping scripts and setup scripts
or if your code generates code from strings, for example to create command line
scripts. You can of course have two separate strings depending on the Python
version, or even run ``2to3`` on the string using ``lib2to3``. However, in these
cases it's generally easier to make the generated code snippets run on all
Python versions without ``2to3``.

My recommendation for the development workflow if you want to support Python
3 without using ``2to3`` is to run ``2to3`` on the code once and then fix it up
until it works on Python 3. Only then introduce Python 2 support into the
Python 3 code, using ``six`` where needed. Add support for Python 2.7 first,
and then Python 2.6. Doing it this way can sometimes result in a very quick
and painless process.

There is also a tool called ``python-modernize`` which will do a
``2to3``-type conversion of your code, but it will keep Python 2
compatibility together with the ``six`` library. This can be a good start.

More information on the techniques necessary to do this is in the chapter
:ref:`noconv-chapter`.

---------------------------------------------------------------------------
Using 3to2
---------------------------------------------------------------------------

.. index:: 3to2

The ``2to3`` tool is flexible enough for you to define what changes should be
done by writing "fixers". Almost any kind of Python code conversion is
imaginable here and ``3to2``\ [#3to2]_ is a set of fixers written by Joe Amenta
that does the conversion from Python 3 to Python 2. This enables you to write
your code for Python 3 and then convert it to Python 2 before release.

However, there is no Distribute support for ``3to2`` and also Python 2.5 or
earlier do not include the required ``lib2to3`` package. Therefore ``3to2``
currently remains only an interesting experiment, although this may change in
the future.

---------------------------------------------------------------------------
Which strategy is for you?
---------------------------------------------------------------------------

Applications
===========================================================================

Unless your code is a reusable package or framework you probably do not need to
support older versions of Python, unless some of your customers are stuck on
Python 2 while others demand that you support Python 3. In most cases you
can just drop Python 2 support completely.


Python modules and packages
===========================================================================

If you are developing some sort of module or package that other Python
developers use you would probably like to support both Python 2 and Python 3
at the same time. The majority of your users will run Python 2 for some time to
come, so you want to give them access to new functionality, but if you don't
support Python 3, the users of Python 3 must find another package to fulfill
their need.

Today you typically only need to support Python 2.7, Python 3.4 and Python
3.5. These versions have enough backwards and forwards compatibility to make
it easy to make code that runs on both Python 2 and Python 3. So this is the
recommended strategy for reusable packages.

---------------------------------------------------------------------------
Summary
---------------------------------------------------------------------------

In general, if you write end-user software, you can just switch to Python 3,
starting with a one-time run of ``2to3`` on your code. If you write a Python
package you want to support both Python 2 and Python 3 at the same time, and
you can drop Python 2.5 support, try first to support Python 2 and 3 without
``2to3`` conversion.

If you need to support Python 2.5 or older, using ``2to3`` is often the best
option.

.. rubric:: Footnotes

.. [#distribute] `http://pypi.python.org/pypi/distribute <http://pypi.python.org/pypi/distribute>`_
.. [#distributedoc] `http://packages.python.org/distribute/python3.html <http://packages.python.org/distribute/python3.html>`_
.. [#six] `http://pypi.python.org/pypi/six <http://pypi.python.org/pypi/six>`_
.. [#3to2] `http://pypi.python.org/pypi/3to2 <http://pypi.python.org/pypi/3to2>`_
