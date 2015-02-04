.. _improving-chapter:

===========================================================================
Improving your code with modern idioms
===========================================================================

Once you have added Python 3 support you have a chance to use the newer features of
Python to improve your code. Many of the things mentioned in this chapter are in
fact possible to do even before adding Python 3 support, as they are supported
even by quite old versions of Python. But I mention them here anyway, because
they aren't always used when the code could benefit from them. This includes
generators, available since Python 2.2; the ``sorted()`` method, available
since Python 2.4 and context managers, available since Python 2.5.

The rest of the new features mentioned here have in fact been backported to
either Python 2.6 or Python 2.7. So if you are able to drop support for
Python 2.5 and earlier, you can use almost all of these new features even if you
are not adding Python 3 support.

.. _sorting-section:

---------------------------------------------------------------------------
Use ``sorted()`` instead of ``.sort()``
---------------------------------------------------------------------------

.. index:: sorting

Lists in Python has a ``.sort()`` method that will sort the list in place. Quite
often when ``.sort()`` is used is it used on a temporary variable discarded
after the loop. Code like this is used because up to Python 2.3 this was the
only built-in way of sorting.

.. literalinclude:: _tests/test-4.1.txt

Python 2.4 has a new built-in, ``sorted()``, that will return a sorted list and
takes the same parameters as ``.sort()``. With ``sorted()`` you often can avoid
the temporary variable. It also will accept any iterable as input, not just
lists, which can make your code more flexible and readable.

.. literalinclude:: _tests/test-4.12.txt

There is however no benefit in replacing a ``mylist.sort()`` with
``mylist = sorted(mylist)``, in fact it will use more memory.

The ``2to3`` fixer ``"idioms"`` will change some usage of ``.sort()`` into
``sorted()``.

---------------------------------------------------------------------------
Coding ``with`` context managers
---------------------------------------------------------------------------

.. index:: context managers, with

Since Python 2.5 you can create context managers, which allows you to create
and manage a runtime context. If you think that sounds rather abstract, you are
completely right. Context managers are abstract and flexible beasts that can be
used and misused in various ways, but this chapter is about how to improve
your existing code so I'll take up some examples of typical usage where they
simplify life.

Context managers are used as a part of the ``with`` statement. The context
manager is created and entered in the ``with`` statement and available during
the ``with`` statements code block. At the end of the code block the context
manager is exited. This may not sound very exiting until you realize that you
can use it for resource allocation. The resource manager then allocates the
resource when you enter the context and deallocates it when you exit.

The most common example of this type of resource allocation are open files. In
most low level languages you have to remember to close files that you open,
while in Python the file is closed once the file object gets garbage collected.
However, that can take a long time and sometimes you may have to make sure you
close the file explicitly, for example when you open many files in a loop as you
may otherwise run out of file handles. You also have to make sure you close the
file even if an exception happens. The result is code like this:

.. literalinclude:: _tests/test-4.7.txt

Since files are context managers, they can be used in a ``with``-statement,
simplifying the code significantly:

.. literalinclude:: _tests/test-4.8.txt

When used as a context manager, the file will close when the code block is
finished, even if an exception occurs. As you see the amount of code is much
smaller, but more importantly it's much clearer and easier to read and
understand.

Another example is if you want to redirect standard out. Again you would
normally make a ``try/except`` block as above. That's OK if you only do it once
in your program, but if you do this repeatedly you will make it much cleaner by
making a context manager that handles the redirection and also resets it.

.. literalinclude:: _tests/test-4.9.txt

The ``__enter__()`` method is called when the indented block after the ``with``
statement is reached and the ``__exit___()`` method is called when the block
is exited, including after an error was raised.

Context managers can be used in many other ways and they are generic enough
to be abused in various ways as well. Any code you have that uses exception
handling to make sure an allocated resource or a global setting
is unallocated or unset will be a good candidate for a context manager.

There are various functions to help you out in making context managers in the
``contextlib`` module. For example, if you have objects that have a ``.close()``
method but aren't context managers you can use the ``closing()`` function to
automatically close them at the end of the ``with``-block.

.. literalinclude:: _tests/test-4.18.txt

---------------------------------------------------------------------------
Advanced string formatting
---------------------------------------------------------------------------

.. index:: string formatting

In Python 3 and also Python 2.6 a new string formatting support was introduced. It is more
flexible and has a clearer syntax than the old string formatting.

.. literalinclude:: _tests/test-7.8.txt

It is in fact a mini-language, and you can do some crazy stuff, but when you
go overboard you lose the benefit of the more readable syntax:

.. literalinclude:: _tests/test-7.9.txt

For a full specification of the advanced string formatting syntax see
the ``Common String Operations`` section of the Python documentation\ [#asf]_.

The old string formatting based on % is planned to be eventually removed, but
there is no decided timeline for this.

---------------------------------------------------------------------------
Class decorators
---------------------------------------------------------------------------

.. index:: class decorators

Decorators have been around since Python 2.4 and have become commonplace thanks
to the builtin decorators like ``@property`` and ``@classmethod``. Python 2.6
introduces class decorators, that work similarly.

Class decorators can both be used to wrap classes and modify the class that
should be decorated. An example of the later is ``functools.total_ordering``,
that will let you implements a minimum of rich comparison operators, and then
add the missing ones to your class. They can often do the job of metaclasses,
and examples of class decorators are decorators that make the class into a
singleton class, or the ``zope.interface`` class decorators that register a
class as implementing a particular interface.

If you have code that modify classes, take a look at class decorators, they may
help you to make your code more readable.

.. _set-literal-section:

---------------------------------------------------------------------------
Set literals
---------------------------------------------------------------------------

.. index:: sets

There is a new literal syntax for sets available in Python 3.
Instead of ``set([1, 2, 3])`` you can now write the cleaner ``{1, 2, 3}``.
Both syntaxes work in Python 3, but the new one is the recommended and the
representation of sets in Python 3 has changed accordingly:

.. literalinclude:: _tests/test-7.1.txt

The set literal has been back-ported to Python 2.7, but the representation
has not.

---------------------------------------------------------------------------
``yield`` to the generators
---------------------------------------------------------------------------

.. index:: yield, generators

Like the floor division operators and the ``key``-parameter to ``.sort()``,
generators have been around for long time, but you still don't see them that
much. But they are immensely practical and save you from creating temporary
lists and thereby both save memory and simplify the code. As an example we take
a simple function with two loops:

.. literalinclude:: _tests/test-4.14.txt

This becomes more elegant by using ``yield`` and thereby a generator:

.. literalinclude:: _tests/test-4.15.txt

Although this is a rather trivial case, making complicated loops into
generators can sometimes make them much simpler, resulting in cleaner and
more readable code. They can be a bit tricky to debug though, since they
reverse the normal program flow. If you have a chain of generators, you can't
step "up" in the call stack to see what the function that created the
generator did. "Up" in the call stack is instead the function that will *use
the result* of the generator. This feels backwards or upside down until you
get used to it, and can be a bit of a brain teaser. If you are used to
functional programming you will feel right at home though.

---------------------------------------------------------------------------
More comprehensions
---------------------------------------------------------------------------

.. index:: list comprehensions, comprehension, dictionary comprehensions,
           set comprehensions, sets

Generators have been around since Python 2.2, but a new way to make
generators appeared in Python 2.4, namely generator expressions. These
are like list comprehesions, but instead of returning a list, they return
a generator. They can be used in many places where list comprehensions are
normally used:

.. literalinclude:: _tests/test-4.16.txt

Becomes:

.. literalinclude:: _tests/test-4.17.txt

Thereby saving you from creating a list with 2 million items and then
immediately throwing it away. You can use a generator expression anywhere
you can have any expression, but quite often you need to put parentheses
around it:

.. literalinclude:: _tests/test-7.3.txt

In Python 3 the generator expression is not just a new nice feature, but a
fundamental change as the generator expression is now the base around which
all the comprehensions are built. In Python 3 a list comprehension is
only syntactic sugar for giving a generator expression to the ``list`` types
constructor:

.. literalinclude:: _tests/test-7.4.txt

This also means that the loop variable no longer leaks into the surrounding
namespace.

The new generator expressions can be given to the ``dict()`` and
``set()`` constructors in Python 2.6 and later, but in Python 3 and also in
Python 2.7 you have new syntax for dictionary and set comprehensions:

.. literalinclude:: _tests/test-7.5.txt


---------------------------------------------------------------------------
The next ``next()``
---------------------------------------------------------------------------

.. index:: next()

In Python 2 iterators have a ``.next()`` method you use to get the next value
from the iterator.

.. literalinclude:: _tests/test-7.10.txt

This special method has in Python 3 been renamed to ``.__next__()`` to be
consistent with the naming of special attributes elswhere in Python. However,
you should generally not call it directly, but instead use the builtin
``next()`` function. This function is also available from Python 2.6, so
unless you are supporting Python 2.5 or earlier you can switch.

.. literalinclude:: _tests/test-7.11.txt


---------------------------------------------------------------------------
New modules
---------------------------------------------------------------------------

.. modules::

There is several new modules that you should also take a look at to see if they
can be of use for you. I won't take them up in detail here, since most of them
are hard to benefit from without refactoring your software completely, but
you should know they exist. For more information on them, you can look at the
Python documentation.

Abstract base classes
=====================

.. index:: abstract base classes

The ``abc`` module contains support for making abstract base classes, where you
can mark a method or property on a base class as "abstract", which means you
must implement it in a subclass. Classes that do not implement all abstract
methods or properties can not be instantiated.

The abstract base classes can also be used to define interfaces by creating
classes that have no concrete methods. The class would then work only as
an interface, and subclassing from it guarantees that it implements the
interface. The new hierarchy of mathematical classes introduced
in Python 2.6 and Python 3.0 is a good example of this.

The ``abc`` module is included in Python 2.6 and later.


``multiprocessing`` and ``futures``
===================================

.. index:: multiprocessing, futures

``multiprocessing`` is a new module that helps you if you are using Python
do to concurrent processing, letting you have process queues and use locks
and semaphores for synchronizing the processes.

``multiprocessing`` is included in Python 2.6 and later.
It is also available for Python 2.4 and Python 2.5 on the
CheeseShop\ [#multiprocessing]_.

If you do concurrency you may also want to take a look at the ``futures``
module which will be included in Python 3.2, and exists on the CheeseShop in
a version that supports Python 2.5 and later\ [#futures]_.


``numbers`` and ``fractions``
=============================

.. index:: numbers, fractions

Python 3 has a new class hierarchy of mathematical classes. For the most
part you will not notice this, but one of the interesting results of this
is the ``fractions`` module, available in Python 2.6 and later.

.. literalinclude:: _tests/test-7.7.txt

There is also a ``numbers`` module that contains the abstract base classes
for all the number types which is useful if you are implementing your own
numeric types.


.. rubric:: Footnotes

.. [#asf] `http://docs.python.org/library/string.html#format-string-syntax
           <http://docs.python.org/library/string.html#format-string-syntax>`_

.. [#multiprocessing] `http://pypi.python.org/pypi/multiprocessing
                      <http://pypi.python.org/pypi/multiprocessing>`_

.. [#futures] `http://pypi.python.org/pypi/futures/
              <http://pypi.python.org/pypi/futures/>`_
