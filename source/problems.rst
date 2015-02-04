.. _problems-chapter:

===========================================================================
Common migration problems
===========================================================================

If you have followed the recommendation to make sure your code runs without
warnings with ``python2.7 -3`` many of the simpler errors you can get now will
be avoided, such as having variable names that are Python 3 keywords and other
easy fixes. You will also have avoided one of the more subtle errors, that
integer division now can return a float. There is still a range of common errors
you may run into. Some are easy to fix, other less so.

If you need to support both Python 2 and Python 3 it's quite likely that you
will need to make conditional code depending on the Python version. In this book
I consistently use my favourite way of testing, I compare the ``sys.version``
string with ``'3'``. But there are many other
ways of doing the same test, like ``sys.version[0] != '3'`` or using the
version_info tuple with ``sys.version_info < ('3',)`` etc. Which one you use is
a matter of personal preference. If you end up doing a lot of tests, setting a
constant is a good idea:

.. code-block:: none

    >>> import sys
    >>> PY3 = sys.version > '3'

Then you can just use the PY3 constant in the rest of the software.

Now, onto the most common problems.

---------------------------------------------------------------------------
Incorrect imports
---------------------------------------------------------------------------

.. index:: imports, urllib/urllib2

Sometimes you'll encounter a situation where ``2to3`` seems to have missed
changing an import. This
is usually because you can import a function or class from another module than where
it's defined.

For example, in Python 2 ``url2pathname`` is defined in ``urllib``, but it is
used by and imported into ``urllib2``. It's common to see code that imports ``url2pathname``
from ``urllib2`` to avoid needing to import ``urllib`` separately. However, when
you do this, the import will not be correctly changed to the new library locations, as ``2to3`` doesn't
know about this trick, so you need to change your code to import from the
correct place before running ``2to3``.

---------------------------------------------------------------------------
Relative import problems
---------------------------------------------------------------------------

.. index:: imports, urllib/urllib2

Python 3 changes the syntax for imports from within a package, requiring you
to use the relative import syntax, saying ``from . import mymodule`` instead
of the just ``import mymodule``. For the most part ``2to3`` will handle this
for you, but there are a couple of cases where ``2to3`` will do the wrong
thing.

The ``import`` fixer will look at your imports and look at your local modules
and packages, and if the import is local, it will change it to the new
syntax. However, when the local module is an extension module, that module
will typically not have been built when you run ``2to3``. That means the
fixer will not find the local module, and not change the import.

Contrariwise, if you import a module from the standard library and you also
have a folder with the same name as that library, the ``import`` fixer will
assume that it is a local package, and change the import to a local import.
It will do this even if the folder is not a package. This is a bug in the
``import`` fixer, but all current versions of Python has this bug, so you
need to be aware of it.


The solution to these problems for Python 2.5 and later is to convert the
imports to relative imports and add the ``__future__`` import to enable
Python 3's absolute/relative import syntax.

.. code-block:: python

    from __future__ import absolute_import
    from . import mymodule

Since the module already uses the new import behavior the ``import`` fixer
will not make any changes to the relative imports, avoiding these problems.

If you need to support Python 2.4 or earlier you can avoid these issue by not
having any relative imports at all, and excluding the ``import`` fixer when
running ``2to3``.


.. _comparisons:

---------------------------------------------------------------------------
Unorderable types, ``__cmp__`` and ``cmp``
---------------------------------------------------------------------------

.. index:: cmp(), __cmp__(), comparisons, TypeError: unorderable types

Under Python 2 the most common way of making types sortable is to implement a
``__cmp__()`` method that in turn uses the builtin ``cmp()`` function, like this
class that will sort according to ``lastname``:

.. literalinclude:: _tests/test-3.1.txt

Since having both ``__cmp__()`` and rich comparison methods violates the
principle of there being only one obvious way of doing something, Python 3
ignores the ``__cmp__()`` method. In addition to this, the ``cmp()`` function is
gone! This typically results in your converted code raising a ``TypeError:
unorderable types`` error. So you need to replace the ``__cmp__()`` method with
rich comparison methods instead. To support sorting you only need to implement
``__lt__()``, the method used for the "less then" operator, ``<``.

.. literalinclude:: _tests/test-3.2.txt

To support other comparison operators you need to implement them separately.
See :ref:`richcomparisons` for an example of how to do that.


---------------------------------------------------------------------------
Sorting
---------------------------------------------------------------------------

.. index:: sorting, TypeError: 'cmp' is an invalid keyword argument,
           TypeError: must use keyword argument for key function

In parallel to the removal of the ``cmp()`` function and ``__cmp__()`` method
the ``cmp`` parameter to ``list.sort()`` and ``sorted()`` is gone in Python 3.
This results in one of these following errors::

    TypeError: 'cmp' is an invalid keyword argument for this function
    TypeError: must use keyword argument for key function

Instead of the ``cmp`` parameter you need to use the ``key`` parameter that was
introduced in Python 2.4. See :ref:`keycmp-section` for more information.

---------------------------------------------------------------------------
Sorting Unicode
---------------------------------------------------------------------------

.. index:: sorting, Unicode

Because the ``cmp=`` parameter is removed in Python 3 sorting Unicode with
``locale.strcoll`` no longer works. In Python 3 you can use
``locale.strxfrm`` instead.

.. literalinclude:: _tests/unicodesort30.txt

This will not work under Python 2, where ``locale.strxfrm`` will expect a
non-unicode string encoded with the locale encoding. If you only support
Python 2.7 and Python 3.2 and later, you can still use ``locale.strcoll``
thanks to a convenience function in ``functools``.

.. literalinclude:: _tests/unicodesort26.txt

This is however much slower, and doesn't work in Python 2.6 or Python 3.1.

.. _binary-section:

---------------------------------------------------------------------------
Bytes, strings and Unicode
---------------------------------------------------------------------------

.. index:: binary data, bytes, strings, Unicode

The biggest problem you may encounter relates to one of the most important
changes in Python 3; strings are now always Unicode. This will simplify any
application that needs to use Unicode, which is almost any application that
is to be used outside of English-speaking countries.

Of course, since strings are now always Unicode, we need another type for
binary data. Python 3 has two new binary types, ``bytes`` and ``bytearrays``.
The ``bytes`` type is similar to the the string type, but instead of being a
string of characters, it's a string of integers. ``Bytearrays`` are more like a
list, but a list that can only hold integers between 0 and 255. A ``bytearray``
is mutable and used if you need to manipulate binary data. Because it's a new
type, although it also exists in Python 2.6, I'm mostly going to ignore it in
this book and concentrate on other ways  of handling binary data.

Byte literals
=============

The first problem we encounter is how to put binary data into the Python code.
In Python 2 we used standard strings and therefore standard string literals. To
check if a file really is a GIF file, we can look at the first six bytes, which
should start with ``GIF89a`` (or ``GIF87a``, but let's ignore that for now):

.. literalinclude:: _tests/test-3.7.txt

In Python 3 the test would always fail, as you need to compare with a bytes
object instead. If you don't need Python 2 support you can simply change any
string literals that hold binary data to be bytes literals by adding a leading
``b`` to them.

.. literalinclude:: _tests/test-3.8.txt

There are also a couple of other cases that need changing. The string type in
Python 2 is a list of 8-bit characters, but the bytes type in Python 3 is a
list of 8-bit integers. So taking one character of a string will return a
one-character long string, but taking one byte of a bytes object will return an
integer! You will therefore have to change any byte-level manipulation to use
integers instead. Often this is a question of removing a lot of ``ord()`` and
``chr()`` calls, as manipulation on byte levels tend to be about integers and
not characters in the first place.

.. literalinclude:: _tests/test-3.9.txt

Binary data in Python 2 and Python 3
====================================

These changes create a problem if you want to still support Python 2. ``2to3``
will generally assume that when you use a string in Python 2, that's what you
want in Python 3 as well and in most cases this is true. So when it is not
true, you need to mark the data as binary so it keeps working in Python 3.

In Python 2.6 and the upcoming 2.7 there is both a bytes literal you can use to
specify that the data is binary, as well as a bytes type. Under Python 2 the
bytes literal and bytes type are just aliases for ``str`` so the objects will
not behave exactly the same as the bytes object in Python 3. Most importantly,
it will be a string of characters, not a string of bytes, so in Python 2,
``b'GIF89a'[2]`` will not return the integer ``70``, but the string ``'F'``.

Luckily this is not a very common problem, as most cases of handling binary data
handle the data as one block and you don't need to look at or modify separate
bytes. If you need to do it there is a trick that works under both Python 2 and
Python 3 and that is to make a one character long slice.

.. literalinclude:: _tests/test-3.10.txt

This will work equally well under Python 2.6 as Python 3, although you get a
one character ``str``-string in Python 2.6 and a one character ``bytes``-string in Python 3.

However, under Python 2.5 or earlier, the ``b'GIF89a'`` syntax doesn't work at
all, so it's only a solution if you don't need to support versions of Python
before 2.6. To ensure that the data is binary you can make a Unicode string and
encode it to get binary data. This code will work well in all versions of
Python 2 and Python 3.

.. literalinclude:: _tests/test-3.11.txt

Of course, the ``u'GIF89a'`` isn't valid syntax in Python 3, because the
separate Unicode literal is gone, but ``2to3`` will handle it and remove the
``u`` prefix.

Nicer solutions
===============

If you think this is all a bunch of ugly hacks, you are correct. Let's improve
things by making a special function which under Python 3 will take a string and
make binary data from it and in Python 2 will simply return the string as is.
This is both less ugly and gets rid of the encoding step under Python 2. You
can call this function anything you want, including "``ArthurBelling``", but
several early adopters of Python 3 has made their own variants of this function
and they all called it "``b``" which is nice, short and looks similar to the
bytes literal. We'll define it like this:

.. literalinclude:: _tests/makebytes.py

Under Python 2 this will return a the string you pass in, ready for use as
binary data:

.. literalinclude:: _tests/test-3.12.txt

While under Python 3 it will take a string and encode it to return a bytes
object.

.. literalinclude:: _tests/test-3.13.txt

This method uses the ISO-8859-1 encoding, also known as Latin-1, as it is the
only encoding whose 256 characters are identical to the 256 first characters of
Unicode. The example here would work fine with the ASCII encoding, but if you
have a character value over 127 then you need to use the ISO-8859-1 and its
one-to-one mapping to Unicode.

This implementation of the ``b()`` function picks up the encoding function
directly from the ``codecs`` module as this is marginally faster, but it will
not be noticeable in practice. You'll need to call ``b()`` millions of times for
it to make a difference, and since you use it as a replacement for bytes
literals this will not happen. Feel free to use ``x.encode('ISO-8859-1')``
instead if you like it better.

Manipulating binary data
========================

The ``b()`` function makes it possible to create binary data from literals, so
it solves one major problem with binary data when supporting both Python 2 and
Python 3. It doesn't solve the unusual case where you need to inspect or modify
the bytes one by one, as indexing or iterating over the binary data will return
one-character strings under Python 2 but integers under Python 3.

If you only need to support Python 2.6 and Python 2.7 you can use the new
``bytearray`` type for this. It is a mutable type that has an interface that
supports a useful mix of the most common list and string operations, it has for
example both ``.append()`` and ``.find()`` as well as some methods of its own,
like the handy ``.fromhex()``.

.. index:: bytearray

.. literalinclude:: _tests/test-3.30.txt

If you need to support Python 2.5 or earlier you can solve this issue by
introducing helper functions to iterate or get a specific index out of either a
``str`` or a ``bytes`` and return integers in both cases:

.. literalinclude:: _tests/test-3.29.txt

The above ``iterbytes`` example uses a generator expression, which requires
Python 2.4. To support earlier Pythons you can make it a list comprehension
instead, which just uses more memory.

If you don't like these helper functions you might want to introduce a special
binary type that works the same under both Python 2 and Python 3. However, the
standard library will assume you pass in strings under Python 2 and under
Python 3 it will assume you pass in bytes, so you have to subclass it from
``str`` in Python 2 and ``bytes`` in Python 3. This solution introduces a new
type that has extra functions that behave the same under all versions of Python,
but leave the standard functions alone:

.. literalinclude:: _tests/bites.py

This new binary class, which I called ``Bites`` but equally well could be called
anything else, including just ``b``, in analogy with the method above, will
accept both strings and lists of integers in the construction. As you see it
subclasses ``str`` in Python 2 and ``bytes`` in Python 3 and is therefore an
extension of the binary types in both versions, so it can be passed straight
into standard library functions that need binary data.

You would use it like this:

.. literalinclude:: _tests/test-3.14.txt

You could easily add support for taking a slice out of the class and always get
a list of integers as well, or any other method you need to work the same in
Python 2 and Python 3.

If you think a whole class like this seems overly complicated, then you are
right. It is quite likely that you won't ever need it, even when handling binary
data. Most of the time you need to handle binary data you do it by reading or
writing binary data from a stream or calling functions, and in these cases you
handle the data as one block and do not look at individual bytes. So for almost
all handling of binary data the ``Bites`` class is overkill.

Reading from files
==================

.. index:: files

Another source of problems in handling binary and Unicode data is when you read
and write to files or other streams. One common problem is that the file is
opened in the wrong mode. Make sure you open text files with the ``'t'`` flag
and binary files with the ``'b'`` flag and you have solved many problems.

Opening a file with the ``'t'`` flag will return a ``unicode`` object under
Python 3 and it will be decoded from the system default encoding, which is
different on different platforms. If it has any other encoding you need to pass
that encoding into the ``open()`` function as a parameter. In Python 2 the
``open()`` function doesn't take an encoding parameter and will return a ``str``
object. As long as your file contains only ASCII characters this isn't a
problem, but when it does you will have to make some changes.

Opening the file as binary and decoding the data afterward is an option, for
example with ``codecs.open()``. However, the translation of line endings that
happens on Windows isn't going to work in that case:

.. literalinclude:: _tests/test-3.28.txt

Python 3's handling and open method is contained in the new ``io`` module.
This module has been backported to Python 2.6 and 2.7, so if you don't need
to support Python 2.5 or earlier, you can replace all ``open()`` calls with
``io.open()`` for Python 3 compatibility. It doesn't suffer from the line
ending problem under Windows that ``codecs.open()`` has and will in fact
convert
line endings in text mode under all platforms, unless
explicitly told not to with the ``newline=''`` parameter.

.. literalinclude:: _tests/test-3.27.txt

But beware that the ``io`` module under Python 2.6 and Python 3.0 is quite slow,
so if you are handling loads of data and need to support Python 2.6 this may not
be the right solution for you.

Another case where you need to open the file in binary mode is if you
don't know if the file is text or binary until you have read part of it, or if
the file contains both binary and text. Then you need to open it in binary mode
and decode it conditionally, where in Python 2 you could often have opened
it in binary mode, and skipped the decoding.

Also, if you do a lot of seeking in a file it will be very slow if you open the
file in text mode, as the seeking will need to decode the data. In that case you
need to open the file in binary mode, and decode the data after reading it.

.. _userdict-section:

---------------------------------------------------------------------------
Replacing UserDict
---------------------------------------------------------------------------

.. index:: UserDict, collections

When you want to make classes that behave like dictionaries but aren't, the
``UserDict`` module is a popular solution because you don't have to implement
all the dictionary methods yourself. However, the ``UserDict`` module is gone in
Python 3, merged into the ``collections`` module. Because of the change in how
dictionaries work in Python 3, where ``items()``, ``keys()`` and ``values()``
now return views instead of lists as well as the changes in how sorting and
comparing is done, the replacements are not completely compatible. Because of
this there are no fixers that make these changes, you will have to do them
manually.

In most cases it is just a question of replacing the base class.
``UserDict.IterableUserDict`` is replaced by ``collections.UserDict`` and
``UserDict.DictMixin`` is now ``collections.MutableMapping``,
``UserDict.UserDict`` is gone, but ``collections.UserDict`` will work as a
solution in most cases.

One of the common problems is that ``collections.MutableMapping`` requires
your dictionary to implement ``__len__`` and ``__iter__`` where ``DictMixin``
doesn't. However, implementing them so that they work under Python 3 won't
break anything under Python 2.

If you need to support both Python 3 and versions below Python 2.6 you also
have to make conditional imports:

.. literalinclude:: _tests/test-3.24.txt


---------------------------------------------------------------------------
CSV API changes
---------------------------------------------------------------------------

.. index:: csv

In Python 2, the ``csv`` module requires you to open files in binary mode.
This is because the module needs to be able to control line-endings, as
typical CSV files use DOS line-endings, and the text-mode under Python 2
can change line-endings on some platforms. The ``csv`` module will also
return and expect data in byte-strings.

The Python 3 ``csv``-module instead requires you to open the file in
text-mode with ``newline=''``, and it returns and expects Unicode strings.

If you need to support both Python 2 and Python 3, and you need to support
Unicode, the best solution I have found is to use "wrapper" classes. The
following classes work for Python 2.6 and later.

.. literalinclude:: _tests/csvutil.py

The ``DictReader`` and ``DictWriter`` can easily be extended in the same
way, by encoding and decoding both keys and values.

---------------------------------------------------------------------------
Running doctests
---------------------------------------------------------------------------

.. index:: doctests, testing

One of the more persistently annoying problems you may encounter are doctests.
Personally I think doctests are brilliant for testing documentation, but there
has been a recommendation in some circuits to make as many tests
as possible doctests.
This becomes a problem with Python 3 because doctests
rely on comparing the output of the code. That means they are sensitive to
changes in formatting and Python 3 has several of these. This means that if you
have doctests you will get many, many failures. Don't despair! Most of them are
not actual failures, but changes in the output formatting. ``2to3`` handles that
change in the code of the doctests, but not in the output.

If you are only porting to Python 3, the solution is simple and boring. Run the
doctests and look at each failure to see if it is a real failure or a change in
formatting. This can sometimes be frustrating, as you can sit and stare at a
failure trying to figure out what actually is different between the expected and
the actual output. On the other hand, that's normal with doctests, even when you
aren't porting to Python 3, which of course is one of the reasons that they
aren't suitable as the main form of testing for a project.

It gets more tricky if you need to continue to support Python 2, since you need
to write output that works in both versions and that can be difficult and in
some cases impossible for example when testing for exceptions, see below.

``write()`` has a return value
==============================

One common reason a doctest fails under Python 3 is when writing to a file. The
``write()`` method now returns the number of bytes written. Doctests for
Python 2 will not expect anything to be returned, so they will break. The
workaround for that is easy and will work under Python 2 as well. Just assign a
dummy variable to the result:

.. literalinclude:: _tests/test-3.16.txt


Types are now classes
=====================

Also, the ``__repr__()`` output of many types have changed. In Python 2 built-in
classes represented themselves as types.

.. literalinclude:: _tests/test-3.17.txt

In Python 3, they are classes, like everything else.

.. literalinclude:: _tests/test-3.18.txt

Here you have two options if you want to support both Python 2 and Python 3.
The first it to use ``isinstance`` instead:

.. literalinclude:: _tests/test-3.19.txt

The alternative is to enable the ``ELLIPSIS`` flag for the doctests and
replace the part of the output that changes with three dots.

.. literalinclude:: _tests/test-3.20.txt

Handling expected exceptions
============================

Using the ``ELLIPSIS`` flag is something you can use for most differences you find when
you need to support both Python 2 and Python 3, but with one exception, namely
exceptions. The output of tracebacks now includes the module names of the
exception. In Python 2 checking for an exception would look like this:

.. literalinclude:: _tests/test-3.21.txt

However, in Python 3 that traceback will include the module name, so you have
to make it look like this:

.. literalinclude:: _tests/test-3.22.txt

In addition to this, some Exceptions have moved as a part of the general
reorganization of the standard library. You can't use the ``ELLIPSIS`` flag and
put an ellipsis in the beginning of the exception definition, because if you add
that doctests no longer recognize the output as an exception and it will
stop working in all versions of Python! The solution to this is to trap the
exception:

.. literalinclude:: _tests/test-3.23.txt

It's not a pretty solution, but the only one available at the moment. Luckily
the most common exceptions, the ones in the builtin module, do not change their
rendering, so they will continue to work. You only need to do this change with
exceptions from the modules in the standard library or any third-party modules.
In Python 2.7 the ``IGNORE_EXCEPTION_DETAIL`` flag has been extended so that it
will handle the differences in exception formatting. However, it will still not
work under Python 2.6, so if you need to support Python 2.6 or earlier you
need to rewrite the test to trap the exception.

If I have doctests with a lot of exception testing I usually end up using a
helper function, similar to the ``assertRaises`` of standard unit tests:

.. literalinclude:: _tests/shouldraise.py

The usage would be like this:

.. literalinclude:: _tests/test-3.25.txt

String representation
=====================

Output from functions that return binary data, like reading from a website,
will return ``str`` under Python 2, while in Python 3 they will
return ``bytes``, which has a different representation.

To solve this I have used
a helper function that makes sure the output is a string before printing it:

.. literalinclude:: _tests/test-3.26.txt

It also removes leading and trailing whitespace for good measure, so that
you don't have to have as many ``<BLANKLINE>`` statements in the code.

``dict`` and ``set`` order
==========================

In Python 3.3 a random seed value is added to the hash function, for security
reasons. This means that any doctest you have that tests the output of a
dictionary or set will fail when you try to run it in Python 3.3, as the
order will change with every run.

.. code-block:: None

    Failed example:
        {x for x in department}
    Expected:
        {'a', ' ', 'i', 'k', 'l', 'S', 'W', 'y'}
    Got:
        {'y', 'S', 'W', 'i', 'k', 'l', 'a', ' '}

This must be changed to equality testing, which unfortunately will make the
failures much less informative.

.. code-block:: None

    Failed example:
        {x for x in department} == \
            {'a', ' ', 'i', 'e', 'l', 'S', 'W', 'y'}
    Expected:
        True
    Got:
        False
