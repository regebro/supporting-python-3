===========================================================================
Language differences and workarounds
===========================================================================

This appendix contains a listing of the differences between Python 2 and Python
3 and example code that will run both in Python 2 and Python 3 without ``2to3``
conversion.

This listing is incomplete. What is listed here is only the intentional changes
that are not bug fixes and even so there may be accidental ommissions.

---------------------------------------------------------------------------
``apply()``
---------------------------------------------------------------------------

.. index:: apply()

.. rubric:: 2to3 fixer ☑ six support ☐

The Python 2 builtin ``apply()`` has been removed in Python 3. It's used to
call a function, but since you can call the function directly it serves no
purpose and has been deprecated since Python 2.3. There is no replacement.

---------------------------------------------------------------------------
``buffer()``
---------------------------------------------------------------------------

.. index:: buffer()

.. rubric:: 2to3 fixer ☑ six support ☐

The Python 2 ``buffer()`` builtin is replaced by the ``memoryview`` class in
Python 3. They are not fully compatible, so ``2to3`` does not change this unless
you explicitly specify the ``buffer`` fixer.

This code will run in both Python 2 and Python 3 without ``2to3`` conversion:

.. literalinclude:: _tests/buffer26.txt

---------------------------------------------------------------------------
``callable()``
---------------------------------------------------------------------------

.. index:: callable()

.. rubric:: 2to3 fixer ☑ six support ☑

The Python 2 builtin ``callable()`` was removed in Python 3.0, but reintroduced
in Python 3.2. If you need to support Python 3.1 you
can try to call the object under scrutiny and catch the ``TypeError`` if it
is not callable.

If you need to know if something is callable without calling it, there are
several solutions for Python 3:

.. literalinclude:: _tests/callable30.txt

If you need code that runs in both Python 2 and Python 3 without ``2to3``
conversion, you can use this:

.. literalinclude:: _tests/callable26.txt

The ``six`` module also defines a ``callable`` function for use under
Python 3.

---------------------------------------------------------------------------
Classes
---------------------------------------------------------------------------

.. index:: old-style classes, method-resolution order

.. rubric:: 2to3 fixer ☐ six support ☐

In Python 2 there is two types of classes, "old-style" and "new". The
"old-style" classes have been removed in Python 3.

See also :ref:`newstyleclass`

---------------------------------------------------------------------------
Comparisons
---------------------------------------------------------------------------

.. index:: cmp(), __cmp__()

.. rubric:: 2to3 fixer ☐ six support ☐

The Python 2 builtin ``cmp()`` has been removed in Python 3.0.1, although
it remained in Python 3.0 by mistake. It is mostly used when defining the
``__cmp__`` comparison method or functions to pass as ``cmp`` parameters
to ``.sort()`` and the support for this has been removed in Python 3 as well.

Should you need ``cmp()`` you can define it like this::

    def cmp(a, b):
        return (a > b) - (a < b)

See :ref:`comparisons` for more information.

---------------------------------------------------------------------------
``coerce()`` and ``__coerce__``
---------------------------------------------------------------------------

.. index:: coercing

.. rubric:: 2to3 fixer ☐ six support ☐

The ``coerce()`` builtin function and the support for the ``__coerce__`` method
has been removed in Python 3. ``coerce()`` would convert the numeric arguments
to have the same type according to the coercion rules for Pythons arithmetic
operators and was only useful in early versions of Python when implementing new
numeric types. There is no replacement in Python 3; coercion should instead
be done by the numeric operator methods.

---------------------------------------------------------------------------
Dictionary methods
---------------------------------------------------------------------------

.. index:: iterators, has_key()

.. rubric:: 2to3 fixer ☑ six support ☐

In Python 2 dictionaries have the methods ``iterkeys()``, ``itervalues()`` and
``iteritems()`` that return iterators instead of lists. In Python 3 the standard
``keys()``, ``values()`` and ``items()`` return dictionary views, which are
iterators, so the iterator variants become pointless and are removed.

If you need to support both Python 2 and Python 3 without ``2to3``
conversion and you must use the iterator methods, you can access it via a
``try/except``:

.. literalinclude:: _tests/dict26.txt

Also, the ``has_key()`` method on dictionaries is gone. Use the ``in`` operator
instead.

See also :ref:`iterator-section`

---------------------------------------------------------------------------
``except``
---------------------------------------------------------------------------

.. index:: exceptions

.. rubric:: 2to3 fixer ☑ six support ☐

In Python 2 the syntax to catch exceptions have changed from::

    except (Exception1, Exception2), target:

to the clearer Python 3 syntax::

    except (Exception1, Exception2) as target:

Other differences is that the target no longer can be a tuple and that string
exceptions are gone. ``2to3`` will convert all this, except string exceptions.

Both syntaxes work in Python 2.6 and Python 2.7, but if you need code that is
to run in earlier versions as well as Python 3 without ``2to3`` conversion you
can get the exception object through ``sys.exc_info()``:

.. literalinclude:: _tests/exception_syntax26.txt

---------------------------------------------------------------------------
Exception objects
---------------------------------------------------------------------------

.. index:: exceptions

.. rubric:: 2to3 fixer ☑ six support ☐

In Python 2 the exception object is iterable and indexable:

.. literalinclude:: _tests/exceptions25.txt

In Python 3 you must use the ``args`` attribute, which will work under
Python 2 as well.

.. literalinclude:: _tests/exceptions26.txt

There was also a ``message`` attribute on exceptions introduced in Python 2.5,
but it was deprecated already in Python 2.6, so it's unlikely that you will
use it.

---------------------------------------------------------------------------
``exec``
---------------------------------------------------------------------------

.. index:: exec

.. rubric:: 2to3 fixer ☑ six support ☑

In Python 2 ``exec`` is a statement:

.. literalinclude:: _tests/exec25.txt

In Python 3 ``exec`` is a function:

.. literalinclude:: _tests/exec30.txt

The Python 3 syntax without the global and local dictionaries will work in
Python 2 as well:

.. literalinclude:: _tests/exec26.txt

If you need to pass in the global or local dictionaries you will need to
define a custom function with two different implementations, one for Python 2
and one for Python 3. As usual ``six`` includes an excellent implementation
of this called ``exec_()``.

---------------------------------------------------------------------------
``execfile``
---------------------------------------------------------------------------

.. index:: execfile

.. rubric:: 2to3 fixer ☑ six support ☐

The Python 2 ``execfile`` statement is gone on Python 3. As a replacement
you can open the file and read the contents::

    exec(open(thefile).read())

This works in all versions of Python.

---------------------------------------------------------------------------
``file``
---------------------------------------------------------------------------

.. index:: file


.. rubric:: 2to3 fixer ☐ six support ☐

In Python 2 there is a ``file`` type builtin. This is replaced with various
file types in Python 3. You commonly see code in Python 2 that uses
``file(pathname)`` which will fail in Python 3. Replace this usage with
``open(pathname)``.

If you need to test for types you can in Python 3 check for ``io.IOBase``
instead of ``file``.

---------------------------------------------------------------------------
``filter()``
---------------------------------------------------------------------------

.. index:: filter()

.. rubric:: 2to3 fixer ☑ six support ☐

In Python 2 ``filter()`` returns a list while in Python 3 it returns an iterator.
``2to3`` will in some cases place a ``list()`` call around the call to ``filter()``
to ensure that the result is still a list. If you need code that runs
in both Python 2 and Python 3 without ``2to3`` conversion and you need the result to
be a list, you can do the same.

---------------------------------------------------------------------------
Imports
---------------------------------------------------------------------------

.. index:: imports

.. rubric:: 2to3 fixer ☑ six support ☐

In Python 2, if you have a package called ``mypackage`` and that contains
a module called ``csv.py``, it would hide the ``csv`` module from the
standard library. The code ``import csv`` would within ``mypackage`` import
the local file, and importing from the standard library would become tricky.

In Python 3, this has changed so that ``import csv`` would import from the
standard library, and to import the local ``csv.py`` file you need to write
``from . import csv`` and ``from csv import my_csv`` needs to be changed to
``from .csv import my_csv``. These are called "relative imports", and there is
also a syntax to import from one level up module above; ``from .. import csv``.

If you to support both Python 2 and Python 3 without ``2to3`` the ``from .``
and ``from ..`` syntax has been available since Python 2.5, together with a
``from __future__ import absolute_import`` statement that changes the behavior
to the Python 3 behavior.

If you need to support Python 2.4 or earlier you have to spell out the whole
package name so ``import csv`` becomes ``from mypkg import csv`` and ``from csv
import my_csv`` becomes ``from mypckg.csv import my_csv``. For clarity and
readability I would avoid relative imports if you can and always spell out
the whole path.

``2to3`` will check if your imports are local and change them.

---------------------------------------------------------------------------
Indentation
---------------------------------------------------------------------------

.. index:: indentation, TabError: inconsistent use of tabs and spaces in indentation

.. rubric:: 2to3 fixer ☐ six support ☐

In Python 2 a tab will be equal to eight spaces as indentation, so you can
indent one line with a tab, and the next line with eight spaces. This is
confusing if you are using an editor that expands tabs to another number than
eight spaces.

In Python 3 a tab is only equal to another tab. This means that each
indentation level has to be consistent in its use of tabs and spaces. If you
have a file where an indented block sometimes uses spaces and sometimes tabs,
you will get the error ``TabError: inconsistent use of tabs and spaces in
indentation``.

The solution is of course to remove the inconsistency.

---------------------------------------------------------------------------
``input()`` and ``raw_input()``
---------------------------------------------------------------------------

.. index:: input(), raw_input()

.. rubric:: 2to3 fixer ☑ six support ☐

In Python 2 there is ``raw_input()`` that takes a string from ``stdin`` and
``input()`` that takes a string from ``stdin`` and evaluates it. That last
function is not very useful and has been removed in Python 3, while
``raw_input()`` has been renamed to ``input()``.

If you need to evaluate the input string you can use ``eval()``::

    >>> eval(input('Type in an expression: '))
    'Type in an expression: ' 1+2
    3

If you need code that runs in both Python 2 and Python 3 without ``2to3``
conversion you can conditionally set ``input()`` to be ``raw_input()``:

.. literalinclude:: _tests/input26.txt

---------------------------------------------------------------------------
Integer division
---------------------------------------------------------------------------

.. index:: integers, division

.. rubric:: 2to3 fixer ☐ six support ☐

In Python 2, the result of dividing two integers will itself be an integer; in
other words ``3/2`` returns ``1``. In Python 3 integer division will always
return a float. So ``3/2`` will return ``1.5`` and ``4/2`` will return ``2.0``.

If you want the old behavior you should instead use the floor division operator
``//``, available since Python 2.2. If you need to support both Python 2
and Python 3 without ``2to3`` conversion the following ``__future__`` import
works since Python 2.2 and enables the new behavior:

.. literalinclude:: _tests/division26.txt

See also: :ref:`division-section`

---------------------------------------------------------------------------
``long``
---------------------------------------------------------------------------

.. index:: long

.. rubric:: 2to3 fixer ☐ six support ☑ (partial)

Python 2 has two integer types ``int`` and ``long``. These have been
unified in Python 3, so there is now only one type, ``int``. This means
that the following code fails in Python 3:

.. literalinclude:: _tests/long25.txt

It's quite unusual that you would need to specify that an integer should be a
long in Python 2, as Python's integer functions all will return ``long`` when
needed. If you do require it the following code works on both Python 2 and
Python 3 without ``2to3`` conversion:

.. literalinclude:: _tests/long26.txt

However, the representation is still different, so doctests will fail.

If you need to check if something is a number you need to check against
both ``int`` and ``long`` under Python 2, but only ``int`` in Python 3. The
best way to do that is to set up a ``integer_types`` tuple depending on
Python version and test against that. ``six`` includes this:

.. literalinclude:: _tests/inttypes26.txt

---------------------------------------------------------------------------
``map()``
---------------------------------------------------------------------------

.. index:: map()

.. rubric:: 2to3 fixer ☐ six support ☐

In Python 2 ``map()`` returns a list while in Python 3 it returns an iterator.
``2to3`` will in some cases place a ``list()`` call around the call to
``map()`` to ensure that the result is still a list. If you need code that
runs in both Python 2 and Python 3 without ``2to3`` conversion and you need
the result to be a list, you can do the same.

In Python 2 ``map()`` will continue until the longest of the argument
iterables are exhausted, extending the other arguments with ``None``.

.. literalinclude:: _tests/map25.txt

In Python 3 ``map()`` will instead stop at the shortest of the arguments. If
you want the Python 2 behaviour in Python 3 you can use a combination of
``starmap()`` and ``zip_longest()``.

.. literalinclude:: _tests/map30.txt

The Python 2 ``map()`` will accept ``None`` as it's function argument, where
it will just return the object(s) passed in. As this transforms ``map()``
into ``zip()`` it's not particularily useful, and in Python 3 this no longer
works. However, some code dependes on this behavior, and you can use the
following function as a full replacement for the Python 2 map.

.. literalinclude:: _tests/map2.py

---------------------------------------------------------------------------
Metaclasses
---------------------------------------------------------------------------

.. index:: __metaclass__, metaclasses

.. rubric:: 2to3 fixer ☑ six support ☑

In Python 2 you specified the metaclass with the ``__metaclass__`` attribute.
In Python 3 you instead pass in a ``metaclass`` parameter in the class
definition. Supporting metaclasses in Python 2 and Python 3 without using ``2to3``
requires you to create classes on the fly. If you want this, I highly recommend
to use the ``six`` module, which has a very clever ``with_metaclass()`` function.

---------------------------------------------------------------------------
``.next()``
---------------------------------------------------------------------------

.. index:: next(), iterators

.. rubric:: 2to3 fixer ☑ six support ☑

In Python 2 you get the next result from an iterator by calling the iterators
``.next()`` method. In Python 3 there is instead a ``next()`` builtin.

If you need code that runs in both Python 2 and Python 3 without ``2to3``
conversion you can make a function that under Python 2 calls
``iterator.next()`` and under Python 3 calls ``next(iterator)``. The ``six``
module contains such a function, called ``advance_iterator()``.

---------------------------------------------------------------------------
Parameter unpacking
---------------------------------------------------------------------------

.. index:: parameter unpacking

.. rubric:: 2to3 fixer ☐ six support ☐

In Python 2 you have parameter unpacking:

.. literalinclude:: _tests/unpacking25.txt

Python 3 does not support this, so you need to do your own unpacking:

.. literalinclude:: _tests/unpacking26.txt

---------------------------------------------------------------------------
``print``
---------------------------------------------------------------------------

.. index:: print

.. rubric:: 2to3 fixer ☑ six support ☑

The Python 2 ``print`` statement is in Python 3 a function. If you need to run
the same code in both Python 2 and Python 3 without ``2to3`` conversion there
are various techniques for this. This is discussed in detail in
:ref:`print-section`.

---------------------------------------------------------------------------
``raise``
---------------------------------------------------------------------------

.. index:: raise, exceptions

.. rubric:: 2to3 fixer ☑ six support ☑

In Python 2 the syntax for the ``raise`` statement is::

    raise E, V, T

Where ``E`` is a string, an exception class or an exception instance, ``V`` the
an optional exception value in the case that ``E`` is a class or a string and
``T`` is a ``traceback`` object if you want to supply a traceback from a
different place than the current code. In Python 3 this has changed to::

    raise E(V).with_traceback(T)

As with the Python 2 syntax, ``value`` and ``traceback`` are optional.
The syntax without the traceback variable is::

    raise E(V)

This works in all versions of Python. It's very unusual that you need the
traceback parameter, but if you do and you also need to write code that runs
under Python 2 and Python 3 without using ``2to3`` you need to create different
a function that takes ``E``, ``V`` and ``T`` as parameters and have different
implementations under Python 2 and Python 3 for that function. The ``six``
module has a nice implementation of that, called ``reraise()``.

---------------------------------------------------------------------------
``range()`` and ``xrange()``
---------------------------------------------------------------------------

.. index:: range(), xrange()

.. rubric:: 2to3 fixer ☑ six support ☑

In Python 2 ``range()`` returns a list, and ``xrange()`` returns an object
that will only generate the items in the range when needed, saving memory.

In Python 3, the ``range()`` function is gone, and ``xrange()`` has been
renamed ``range()``. In addition the ``range()`` object support slicing in
Python 3.2 and later .

``2to3`` will in some cases place a ``list()`` call around the call to
``range()``, to ensure that the result is still a list. If you need code that
runs in both Python 2 and Python 3 without ``2to3`` conversion and you need
the result to be a list, you can do the same.

You can import ``xrange()`` from the ``six`` module to be sure you get the
iterator variation under both Python 2 and Python 3.

---------------------------------------------------------------------------
``repr()`` as backticks.
---------------------------------------------------------------------------

.. index:: repr()

.. rubric:: 2to3 fixer ☑ six support ☐

In Python 2 you can generate a string representation of an expression by
enclosing it with backticks:

.. literalinclude:: _tests/repr25.txt

The only purpose with this syntax is to confuse newbies and make obfuscated
Python. It has been removed in Python 3, since the ``repr()`` builtin does
exactly the same.

.. literalinclude:: _tests/repr26.txt

---------------------------------------------------------------------------
Rounding behavior
---------------------------------------------------------------------------

.. index:: round()

.. rubric:: 2to3 fixer ☐ six support ☐

The behavior of ``round`` has changed in Python 3. In Python 2, rounding of
halfway cases was away from zero, and ``round()`` would always return a
float.

.. literalinclude:: _tests/round24.txt

In Python 3 rounding of halfway cases are now always towards the nearest
even. This is standard practice, as it will make a set of evenly distributed
roundings average out.

When called without the second parameter, which determines the number of
decimals, ``round()`` will in Python 3 return an integer. If you pass in a
parameter to set the number of decimals to round to, the returned value will
be of the same type as the unrounded value. This is true even if you pass in
zero.

.. literalinclude:: _tests/round30.txt

If you need the Python 2 behavior, you can use the following method:

.. literalinclude:: _tests/round26.txt


---------------------------------------------------------------------------
Slice operator methods
---------------------------------------------------------------------------

.. index:: __getslice__, __setslice__, __delslice__

.. rubric:: 2to3 fixer ☐ six support ☐

In Python 1 you used ``__getslice__`` and ``__setslice__`` to support slice
methods like ``foo[3:7]`` on your object. These were deprecated in Python 2.0
but still supported. Python 3 removes the support for the slice methods, so you
need to instead extend ``__getitem__``, ``__setitem__`` and ``__delitem__`` with
slice object support.

.. literalinclude:: _tests/getitem26.txt

---------------------------------------------------------------------------
Sorting
---------------------------------------------------------------------------

.. index:: sorting

.. rubric:: 2to3 fixer ☐ six support ☐


In Python 2 the ``.sort()`` method on lists as well as the ``sorted()`` builtin
takes two parameters, ``cmp`` and ``key``. In Python 3 only the ``key``
parameter is supported. There are no fixers for this, so you need to change
that in the Python 2 code.

See :ref:`keycmp-section` for more information.

---------------------------------------------------------------------------
``StandardError``
---------------------------------------------------------------------------

.. index:: StandardError

.. rubric:: 2to3 fixer ☑ six support ☐

Python 2 has an exception class called ``StandardError`` that has been removed
in Python 3. Use ``Exception`` instead.

---------------------------------------------------------------------------
String types
---------------------------------------------------------------------------

.. index:: Unicode, strings, bytes

.. rubric:: 2to3 fixer ☑ six support ☑

Python 2 had two string types; ``str`` and ``unicode``. Python 3 has only one;
``str``, but instead it also has a ``bytes`` type made to handle binary
data. For more information on this, see :ref:`binary-section` and
:ref:`unicode-section`.

.. rubric:: Footnotes
