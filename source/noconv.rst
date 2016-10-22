.. _noconv-chapter:

===========================================================================
Supporting Python 2 and 3 without 2to3 conversion
===========================================================================

Although the official documentation for Python 3 discourages writing code for
both Python 2 and Python 3, in some cases it is desirable. Especially if you
can drop support for Python 2.5 and earlier, since Python 2.6 introduces quite
a lot of forwards compatibility.

It's possible to make the same code run under earlier versions of Python as
well, but then you start getting into the "contorted" writing style the
Python 3 documentation mentions. I'll take up tricks to do this and the ``six``
module I mention at the end of this chapter will help a lot. It has been done
even for some quite big projects, but I would in general not recommend it for a
large project. For small projects or parts of bigger projects, for example
bootstrapping scripts, supporting old versions of Python without using ``2to3``
is often the best solution.

Python 2.7 has some small improvements on Python 3 compatibility, but it's
likely that if you want to run the same code under both Python 2 and Python 3
you will have to support Python 2.6 for some time to come.

Many of the changes you need will be done by ``2to3``, so to start converting
your code you actually want to first run ``2to3`` on your code and make your
code run under Python 3. It is generally easier, or at least less monotonous,
to introduce Python 2 compatibility in Python 3 code, than to introduce
Python 3 compatibility in Python 2 code.

Once you have the project running under Python 3, try to run it under Python
2.6. At this stage you may run into syntax errors. They should come from only
changes in the ``print`` statement. Once you have fixed them you can fix the
remaining errors and then lastly you do the same for earlier versions of Python,
if you need to support them as well.

.. _print-section:

---------------------------------------------------------------------------
Supporting the ``print()`` function
---------------------------------------------------------------------------

.. index:: print

One of the major causes of syntax errors is the change of ``print`` from a
statement to a function. The simple cases are not problematic, you can simply
put parentheses around the text that should be printed. The following will
print exactly the same in all versions of Python:

.. literalinclude:: _tests/test-5.5.txt

However, if you use any more advanced feature of ``print`` you either end up
with a syntax error or not printing what you intended. Python 2's trailing
comma has in Python 3 become a parameter, so if you use trailing commas to
avoid the newline after a print, this will in Python 3 look like ``print('Text
to print', end=' ')`` which is a syntax error under Python 2.

Under Python 2.6 there is a ``__future__`` import to make ``print`` into a
function. So to avoid any syntax errors and other differences you should start
any file where you use ``print()`` with ``from __future__ import
print_function``. The ``__future__`` import only works under Python 2.6 and
later, so for Python 2.5 and earlier you have two options. You can either
convert the more complex ``print`` to something simpler, or you can use a
separate print function that works under both Python 2 and Python 3.

Writing your own print function sounds more complicated than it is. The trick is
to use ``sys.stdout.write()`` and formatting according to the parameters passed
in to the function. However, it is even easier to use the ``print_()`` function
from the ``six`` module that I will present at the end of this chapter.

---------------------------------------------------------------------------
Handling exceptions
---------------------------------------------------------------------------

.. index:: exceptions

If you in your exception handling need access to the exception itself you need
to use an exception variable. In Python 2 the syntax for this is:

.. literalinclude:: _tests/test-5.1.txt

However, this syntax is confusing when you need to catch more than one
exception. You need to have parentheses around the list of exceptions:

.. literalinclude:: _tests/test-5.2.txt

If you forget the parentheses only ``ZeroDivisionError`` is caught and the
raised exception will be stored in a variable named ``TypeError``. That's not
what you expect. Therefore, in Python 3, the syntax has changed to use ``as``
instead of a comma, which avoids this mistake. It will also give you a syntax
error if you do not have parentheses when catching more than one exception:

.. literalinclude:: _tests/test-5.3.txt

The above syntax also works in Python 2.6 where both the old syntax with a
comma and the new syntax using ``as`` works. If you need to support Python
versions lower than Python 2.6 and you need access to the exception that was
raised, you can get that in all versions through the ``exc_info()`` function:

.. literalinclude:: _tests/test-5.4.txt

Another difference is that Exceptions are no longer iterable. In Python 2 the
arguments to the exception was available by iterating over the exception or
subscripting the exception.

.. literalinclude:: _tests/test-5.16.txt

In Python 3 you need to use the exception attribute ``args`` instead:

.. literalinclude:: _tests/test-5.17.txt

A ``message`` attribute was added to the built-in exceptions in Python 2.5. It
was however deprecated already in Python 2.6 and removed in Python 3.
Python 2.6 and Python 2.7 will warn you about this when using the ``-3`` flag.

---------------------------------------------------------------------------
Import errors
---------------------------------------------------------------------------

.. index:: imports

One of the big changes is the reorganization of the standard library and as a
result the typical errors you will get at this stage are mostly import errors.
Getting around it is very easy. You simply try to import from the Python 3
locations and if that fails you import from the Python 2 locations. For modules
that have been renamed, you can just import them as the new name.

.. literalinclude:: _tests/test-5.6.txt

Some of the new modules are mergers of several old modules and in that case the
above will not work if you need things from several of the old modules. You can
also not do this with modules that have sub-modules. ``import httplib as
http.client`` is a syntax error. The ``urllib`` and ``urllib2`` modules have not
only been merged, but reorganized into several sub-modules. So there you need to
import each name you use separately. This often means you need to make changes
to your code as well. In Python 2 retrieving a web page looks like this:

.. literalinclude:: _tests/test-5.7.txt

After conversion with ``2to3`` it will look like this:

.. literalinclude:: _tests/test-5.8.txt

Yes, urllib.parse will be imported twice and urllib.error imported even though
it isn't used. That's how this fixer does it and solving that would be a lot of
extra effort, so it imports more than is needed. We need to fix up the code to
import the names we use directly instead of the modules they are located in, so
the version that runs under both Python 2 and Python 3 ends up like this:

.. literalinclude:: _tests/test-5.9.txt

---------------------------------------------------------------------------
Integer incompatibilities
---------------------------------------------------------------------------

.. index:: integers, long, octal

There are two big changes in integer handling in Python 3. The first one is
that the ``int`` and the ``long`` types have been merged. That means that you
can't specify that an integer should be long by adding the ``L`` suffix any
more. ``1L`` is a syntax error in Python 3.

If you have to have an integer being a ``long`` in Python 2 and still be
compatible with Python 3, the following code will solve it. It defines up a
``long`` variable to be the same as the ``int`` class under Python 3, and it
can then be used explicitly to make sure the integer is a ``long``.

.. literalinclude:: _tests/test-5.10.txt

Another change is that the syntax for octal literals has changed. In Python 2
any number starting with a ``0`` is an octal, which can be confusing if you
decide to format your numbers by starting them with zeros. In Python 3 the
syntax has instead changed to the less confusing ``0o``, similar to ``0x`` used
for hex numbers. Starting numbers with ``0`` is a syntax error to prevent you
from trying the old octal syntax by mistake.

Octal is used almost exclusively when setting permissions under Unix, but that
in turn is quite a common task. There is an easy way that works under both
Python 2 and Python 3: Use the decimal or hex value and put the octal value in
a comment::

    >>> f = 420 # 644 in octal, 'rw-r--r--'

.. _unicode-section:

---------------------------------------------------------------------------
More bytes, strings and Unicode
---------------------------------------------------------------------------

.. index:: binary data, bytes, strings, Unicode

It's no surprise that the trickiest issue we have in supporting Python 2 and
Python 3 without ``2to3`` is handling binary data, just as it is when using
``2to3``. When we choose not to use ``2to3`` the problem is made more tricky by
making Unicode an issue as well. When using ``2to3`` to support Python 2 and
Python 3, ``2to3`` will convert any Unicode literals to straight string
literals. Without ``2to3`` we have no such luxury and since the Unicode literal
``u''`` is gone in Python 3 we need to find a way to say that we want
a Unicode string that works in all versions of Python.

Here, only supporting Python 3.3 will make things much easier for you, because
in Python 3.3, the ``u''`` literal is back! In that case you can mostly
ignore this section.

But if you need to support Python 3.1 or 3.2,
the best way to do this is to make a Unicode string maker function just like the
``b()`` function in :ref:`problems-chapter` but for Unicode strings
instead of binary ``bytes``. The natural name for this function is of course
``u()``. We would then use ``b()`` instead of the ``b''`` literal, and ``u()``
instead of the ``u''`` literal.

.. literalinclude:: _tests/makeunicode.py

This will return a unicode object in Python 2:

.. literalinclude:: _tests/test-5.14.txt

While it will return a string object in Python 3:

.. literalinclude:: _tests/test-5.15.txt

Here I use the ``unicode_escape`` encoding, because other encodings could fail
if you save the file with a different encoding than the one specified in the
function. Using ``unicode_escape`` is a bit more work that just typing in the
characters and saving the file but it will be work on different
versions of Python as well as different operating system platforms.

The ``unicode_escape`` encoding will convert all the various ways of entering
unicode characters. The ``'\x00'`` syntax, the ``'\u0000'`` and even the
``'\N{name}'`` syntax:

.. literalinclude:: _tests/test-5.18.txt

If you only need to support Python 2.6 or later there is also ``from __future__
import unicode_literals``. This will turn all string literals in the file into
Unicode literals:

.. literalinclude:: _tests/test-5.11.txt

Both with the ``__future__`` import and the ``u()`` function the the binary data
type is still called ``str`` and the text type is still called ``unicode`` under
Python 2, while under Python 3 they are called ``bytes`` and ``str``.

The best way around this is to define two variables; ``text_type`` and
``binary_type``, depending on Python version and then we test against that
variable.

.. literalinclude:: _tests/test-5.13.txt

For the handling of binary data you can use the same techniques as discussed in
:ref:`problems-chapter`.

---------------------------------------------------------------------------
Two times three is "six"
---------------------------------------------------------------------------

.. index:: six

There are many many more unusual and sometimes subtle differences between
Python 2 and Python 3. Although the techniques mentioned here works for most
of them, I definitely recommend you to look at Benjamin Petersons module
"six"\ [#six]_ It contains a ``PY3`` constant to use when checking for the version of
Python, and it contains the above mentioned ``b()`` and ``u()`` functions,
although the ``u()`` function doesn't specify an encoding, so you are restricted
to using ASCII characters. It also has many helpful constants like ``text_type``
and ``binary_type`` and a ``print_()`` function that works both under Python 2
and Python 3.

It also contains imports of much of the reorganized standard library, so instead
of the ``try/except`` construct from the beginning of this chapter you can
import the module from the six module instead. However it notably doesn't
support the reorganization of the urllib and urllib2 modules, so there you still
need to use the ``try/except`` import technique.

The six module even contains helpers for unusual problems, like using
metaclasses and the attributes of functions, which also have been renamed.
Although it requires Python 2.4 or later you can use many of the techniques in
it even under earlier versions of Python, if you need to support them.

If you are attempting to support Python 2 and Python 3 without conversion you
will definitely find it very helpful.


.. rubric:: Footnotes

.. [#six] `http://pypi.python.org/pypi/six <http://pypi.python.org/pypi/six>`_
