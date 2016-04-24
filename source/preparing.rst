.. _preparing-chapter:

===========================================================================
Preparing for Python 3
===========================================================================

Before you start adding Python 3 support there are several things you should do
to prepare your code to make the transition to Python 3 as smooth as possible,
by changing things that are hard for ``2to3`` to fix. These are things you can
do right now even if you don't plan to move to Python 3 yet and in some cases
they will even speed up your code under Python 2.

You might also want to read the chapter on :ref:`improving-chapter`, which
contains many other improvements you can apply to your code.

---------------------------------------------------------------------------
Run under Python 2.7.
---------------------------------------------------------------------------

The first step in the process is to get your code running in Python 2.6
or 2.7. It isn't very important which version you use here, but obviously the
last Python 2 version makes the most sense, so if you can use Python 2.7,
do so.

Most code will run directly without modifications,
but there are a couple of things that change from Python 2.5 to 2.6. In Python
2.6 ``as`` and ``with`` are keywords, so if you use these as variables you will
need to change them. The easiest is to add an underscore to the end of the
variables.

.. literalinclude:: _tests/test-1.1.txt

You also need to get rid of string exceptions. Using strings for exceptions has
been recommended against for a very long time, mainly because they are very
inflexible, you can't subclass them for example.

.. literalinclude:: _tests/test-1.2.txt

In Python 3 string exceptions are completely gone. In Python 2.6 you can't
raise them, although you can still catch them for backwards compatibility. In
any case you should remove all usage of string exceptions in your code and make
it run under Python 2.6 before doing anything else.

.. literalinclude:: _tests/test-1.3.txt

The next step is to run your code under Python 2.6 or Python 2.7 with the
``-3`` option. This will warn about things that are not supported in Python 3
and which ``2to3`` will not convert. It's mostly ways of doing things that have
long been deprecated and have newer alternative ways to be done, or modules
removed from the standard library. For example the support for Classic Mac OS
has been removed in Python 3, only OS X is supported now and for that reasons
the modules that support specific things about Classic Mac OS have been removed.

You will get warnings for many of the changes listed below (but not all), as well
as for some of the library reorganization. The library reorganization changes
are simple and need no explanation, the warnings will tell you the new name of
the module.

.. _division-section:

---------------------------------------------------------------------------
Use ``//`` instead of ``/`` when dividing integers
---------------------------------------------------------------------------

.. index:: division, __future__

In Python 2 dividing two integers returns an integer. That means five
divided by two will return two.

.. literalinclude:: _tests/test-1.4.txt

However, under Python 3 it returns two and a half.

.. literalinclude:: _tests/test-1.5.txt

Many who use the division operator in Python 2 today rely on the integer
division to always return integers. But the automatic conversion with ``2to3``
will not know what types the operands are and therefore it doesn't know if the
division operator divides integers or not. Therefore it can not do any
conversion here. This means that if you are using the old integer division, your
code may fail under Python 3.

Since this change has been planned already since Python 2.2, it and all later
versions include a new operator, called `floor division`, written with two
slashes. It always returns whole integers, even with floats. Any place in your
code where you really do want to have the floor division that returns whole
numbers, you should change the division operator to the floor division operator.

.. literalinclude:: _tests/test-1.12.txt

Often the Python 2 integer division behavior is unwanted. The most common way
to get around that problem is to convert one of the integers to a float, or
to add a decimal comma to one of the numbers.

.. literalinclude:: _tests/test-1.6.txt

However, there is a neater way to do this and that is to enable the Python 3
behavior. This is done via a ``__future__`` import also available since Python
2.2.

.. literalinclude:: _tests/test-1.7.txt

Although converting one of the operands to a float before division will work
fine it is unnecessary in Python 3 and by using the ``__future__``
import you can avoid it.

Running Python 2.6 with the ``-3`` option will warn you if you use the old
integer division.

.. _newstyleclass:

---------------------------------------------------------------------------
Use new-style classes
---------------------------------------------------------------------------

.. index:: classes, object

In Python 2 there are two types of classes, "old-style" and "new". The
"old-style" classes have been removed in Python 3, so all classes now
subclass from ``object``, even if they don't do so explicitly.

There are many differences between new and old classes, but few of them will
cause you any problems with Python 3. If you use multiple inheritance you
are probably going to encounter problems because of the different method
resolution orders.\ [#mro]_

If you use multiple inheritance you should therefore switch to using new-style
classes before adding Python 3 support. This is done by making sure all objects
subclass from ``object``, and you will probably have to change the order you
list the super-classes in the class definitions.

.. _richcomparisons:

---------------------------------------------------------------------------
Separate binary data and strings
---------------------------------------------------------------------------

In Python 2, you use ``str`` objects to hold binary data and ASCII text, while
text data that needs more characters than what is available in ASCII is held in
``unicode`` objects. In Python 3, instead of ``str`` and ``unicode`` objects,
you use ``bytes`` objects for binary data and ``str`` objects for all kinds of
text data, Unicode or not. The ``str`` type in Python 3 is more or less the
same as the ``unicode`` type in Python 2 and the ``bytes`` type is quite
similar to Python 2's ``str`` type, even though there are significant
differences.

The first step in preparing for this is to make sure you don't use the same
variable name for both binary and text data. In Python 2 this will not cause you
much trouble, but in Python 3 it will, so try to keep binary data and text
separated as much as possible.

In Python 2 the ``'t'`` and ``'b'`` file mode flags changes how newlines are
treated on some platforms, for example Windows. But the flag makes no difference
on Unix, so many programs that are developed for Unix tend to ignore that flag
and open binary files in text mode. However, in Python 3 the flags also
determine if you get ``bytes`` or ``unicode`` objects as results when you read
from the file. So make sure you really use the text and binary flags when you
open a file. Although the text flag is default, add it anyway, as you then show
that the text mode is intentional and not just because you forgot to add the
flag.

Running Python 2.6 with the ``-3`` option will `not` warn about this problem,
as there simply is no way for Python 2 to know if the data is text
or binary data.

.. _keycmp-section:

---------------------------------------------------------------------------
When sorting, use ``key`` instead of ``cmp``
---------------------------------------------------------------------------

.. index:: sorting, TypeError: must use keyword argument for key function

In Python 2 sorting methods take a ``cmp`` parameter that should be a
function that returns -1, 0 or 1 when comparing two values.

.. literalinclude:: _tests/test-4.2.txt

Since Python 2.4 ``.sort()`` as well as the new ``sorted()`` function (see
:ref:`sorting-section`) take a ``key`` parameter which should be a function that
returns a sorting key.

.. literalinclude:: _tests/test-4.3.txt

This is easier to use and faster to run. When using the ``cmp`` parameter, the
sorting compares pairs of values, so the compare-function is called multiple
times for every item. The larger the set of data, the more times the
compare-function is called per item. With the ``key`` function the sorting
instead keeps the key value for each item and compares those, so the key
function is only called once for every item. This results in much faster sorts
for large sets of data.

The ``key`` function is often so simple that you can replace it with a lambda:

.. literalinclude:: _tests/test-4.4.txt

Python 2.4 also introduced a ``reverse`` parameter.

.. literalinclude:: _tests/test-4.5.txt

There is one case where using ``key`` is less obvious than using ``cmp`` and
that's when you need to sort on several values. Let's say we want the result to
be sorted with the longest names first and names of the same length should be
sorted alphabetically. Doing this with a ``key`` function is not immediately
obvious, but the solution is usually to sort twice, with the least important
sorting first.

.. literalinclude:: _tests/test-4.6.txt

This works because since Python 2.3 the timsort sorting algorithm is
used\ [#timsort]_. It's a stable algorithm, meaning that if two items are sorted
as equal it will preserve the order of those items.

You can also make a key function that returns a value that combines the two keys
and sort in one go. This is surprisingly not always faster, you will have to
test which solution is faster in your case, it depends on both the data and
the key function.

.. literalinclude:: _tests/test-4.13.txt

The ``key`` parameter was introduced in Python 2.4, so if you need to support
Python 2.3 you can't use it. If you need to do a lot of sorting using the key
function, the best thing is to implement a simple ``sorted()`` function for
Python 2.3 and use that conditionally instead of the ``sorted()`` builtin in
with Python 2.4 and later.

.. literalinclude:: _tests/test-3.6.txt

Python 2.4 is over five years old now, so it is quite unlikely that you would
need to support Python 2.3.

.. WARNING::

    Running Python with the ``-3`` option will only warn you if you use the
    ``cmp`` parameter explicitly::

        >>> l.sort(cmp=cmpfunction)
        __main__:1: DeprecationWarning: the cmp argument is not
        supported in 3.x

    But it will not warn if you use it like this::

        >>> l.sort(cmpfunction)

    So this syntax may slip through. In these cases you get a ``TypeError: must
    use keyword argument for key function`` when running the code under
    Python 3.

In Python 2.7 and Python 3.2 and later there is a function that will convert
a comparison function to a key function via a wrapper class. It is very
clever, but will make the compare function even slower, so use this only as a
last resort.

.. literalinclude:: _tests/test-4.19.txt


---------------------------------------------------------------------------
Use rich comparison operators
---------------------------------------------------------------------------

.. index:: cmp(), __cmp__(), comparisons

In Python 2 the most common way to support comparison and sorting of your
objects is to implement a ``__cmp__()`` method that in turn uses the builtin
``cmp()`` function, like this class that will sort according to ``lastname``:

.. literalinclude:: _tests/test-3.1.txt

However, you can have objects, for example colors, that are neither "less than"
nor "greater than", but still can be "equal" or "not equal", so since
Python 2.1 there has also been support for rich comparison methods where each
method corresponds to one comparison operator. They are ``__lt__`` for ``<``,
``__le__`` for ``<=``, ``__eq__`` for ``==``, ``__ne__`` for ``!=``, ``__gt__``
for ``>`` and ``__ge__`` for ``>=``.

Having both the rich comparison methods and the ``__cmp__()`` method violates
the principle that there should be only one obvious way to do it, so in
Python 3 the support for ``__cmp__()`` has been removed. For Python 3 you
therefore must implement all of the rich comparison operators if you want your
objects to be comparable. You don't have to do this before supporting Python 3
but doing so makes the experience a bit smoother.

Comparatively tricky
====================

Making comparison methods can be quite tricky, since you also need to handle
comparing different types. The comparison methods should return the
``NotImplemented`` constant if it doesn't know how to compare with the other
object. Returning ``NotImplemented`` works as a flag for Pythons comparisons
that makes Python try the reverse comparison. So if your ``__lt__()`` method
returns ``NotImplemented`` then Python will try to ask the other objects
``__gt__()`` method instead.

.. ATTENTION::

    This means that you should never in your rich comparison methods call the
    other objects comparison operator! You'll find several examples of rich
    comparison helpers that will convert a greater than call like
    ``self.__gt__(other)`` into ``return other < self``. But then you are
    calling ``other.__lt__(self)`` and if it returns ``NotImplemented`` then
    Python will try ``self.__gt__(other)`` again and you get infinite recursion!

Implementing a good set of rich comparison operators that behave properly in
all cases is not difficult once you understand all the cases, but getting to
grips with that is not entirely trivial. You can do it in many different ways,
my preferred way is this mixin, which works equally well in Python 2 and
Python 3.

.. literalinclude:: _tests/mixin.py

The previously mentioned ``functools.total_ordering()`` class
decorator from Python 3.2 is a nice solution as well, and it can be copied and
used in other Python versions as well. But since it uses class decorators it will
not work in versions below Python 2.6.

To use the mixin above you need to implement a ``_cmpkey()`` method that
returns a key of objects that can be compared, similar to the ``key()``
function used when sorting. The implementation could look like this:

.. literalinclude:: _tests/test-3.3.txt

The above mixin will return ``NotImplemented`` if the object compared with
does not implement a ``_cmpkey()`` method, or if that method returns
something that isn't comparable with the value that ``self._cmpkey()``
returns. This means that every object that has a ``_cmpkey()`` that returns
a tuple will be comparable with all other objects that also have a ``_cmpkey()``
that returns a tuple and most importantly, if it isn't comparable, the
operators will fall back to asking the other object if it knows how to
compare the two objects. This way you have an object which has the maximum
chance of meaningful comparisons.

Implementing ``__hash__()``
===========================

In Python 2, if you implement ``__eq__()`` you should also override
``__hash__()``. This is because two objects that compare equal should also
have the same hash-value. If the object is mutable, you should set
``__hash__`` to ``None``, to mark it as mutable. This will mean you can't use
it as a key in dictionaries for example, and that's good, only immutable
objects should be dictionary keys.

In Python 3, ``__hash__`` will be set to ``None`` automatically if you define
``__eq__()``, and the object will become unhashable, so for Python 3 you
don't need to override ``__hash__()`` unless it is an immutable object and
you want to be able to use it as a key value.

The value returned by ``__hash__()`` needs to be an integer, and two objects
that compare equal should have the same hash value. It must stay the same
over the whole lifetime of the object, which is why mutable objects should
set ``__hash__ = None`` to mark them as unhashable.

If you are using the ``_cmpkey()`` method of implementing comparison
operators mentioned above, then implementing ``__hash__()`` is very easy:

.. literalinclude:: _tests/test-3.31.txt

The attributes of this class are marked as internal by the convention of using
a leading underscore, but they are not strictly speaking immutable. If you
want a truly immutable class in Python the easiest way is subclassing
``collections.namedtuple``, but that is out of scope for this book.

.. _iterator-section:

---------------------------------------------------------------------------
Make sure you aren't using any removed modules
---------------------------------------------------------------------------

Many of the modules in the standard library have been dropped from Python 3.
Most of them are specific to old operating systems that aren't supported any more
and others have been supplanted by new modules with a better interface.

Running Python 2.6 with the ``-3`` option will warn you if you use some of the
more commonly used modules. It's quite unlikely that you are using any of the
modules that Python 2.6 will not warn about, but if you are and you are
planning to support both Python 2 and Python 3, you should replace them with
their modern counterparts, if any.

See :ref:`removedmodules-section` for a list of the removed modules.

---------------------------------------------------------------------------
Testing ``coverage`` and ``tox``
---------------------------------------------------------------------------

.. index:: testing, tox

Having a good set of tests is always valuable for any project. When you add
Python 3 support, having tests is going to speed up the process a lot,
because you will need to run the tests over and over and testing an application
by hand takes a lot of time.

It's always a good idea to increase the test coverage with more tests. The
most popular Python tool for getting a report on the test coverage of your
modules is Ned Batchelder's ``coverage`` module.\ [#coverage]_ Many test runner
frameworks like zope.testing, nose and py.test include support for the
``coverage`` module, so you may have it installed already.

If you are developing a module that supports many versions of Python, running the
tests for all these versions quickly becomes a chore. To solve this Holger Krekel
has created a tool called ``tox``\ [#tox]_ that will install a virtualenv for
each version you want to support, and will run your tests with all these versions
with one simple command. It seems like a small thing, and it is, but it makes
the experience just a little bit more pleasant. If you plan to support both Python 2
and Python 3 you should try it out.

---------------------------------------------------------------------------
Optional: Use the iterator-methods on dictionaries
---------------------------------------------------------------------------

.. index:: dictionaries

Since Python 2.2 the built-in Python dictionary type has had the methods
``iterkeys()``, ``itervalues()`` and ``iteritems()``. They yield the same data
as ``keys()``, ``values()`` and ``items()`` do, but instead of returning lists
they return iterators, which saves memory and time when using large
dictionaries.

.. literalinclude:: _tests/test-1.8.txt

In Python 3 the standard ``keys()``, ``values()`` and ``items()`` return
dictionary views, which are very similar to the iterators of Python 2. As there
is no longer any need for the iterator variations of these methods
they have been removed.

``2to3`` will convert the usage of the
iterator methods to the standard methods.
By explicitly using the iterator methods
you make it clear that you don't need a list, which is helpful for the ``2to3``
conversion, which otherwise will replace your ``dict.values()`` call with a
``list(dict.values())`` just to be safe.

Python 2.7 also has the new view iterators available on dictionaries as
``.viewitems()``, ``.viewkeys()`` and ``.viewvalues()``, but since they don't
exist in earlier Python versions they are only useful once you can drop support
for Python 2.6 and earlier.

Also note that if your code is relying on lists being returned, then you
are probably misusing the dictionary somehow. For example, in the code below,
you can't actually rely on the order of the keys being the same every time,
with the result that you can't predict exactly how the code will behave. This
can lead to some troublesome debugging.

.. literalinclude:: _tests/test-1.9.txt

Remember, if all you want to do is loop over the dictionary, use ``for x in
dict`` and you will use iterators automatically in both Python 2 and Python 3.

.. literalinclude:: _tests/test-1.10.txt

.. rubric:: Footnotes

.. [#timsort] `http://en.wikipedia.org/wiki/Timsort <http://en.wikipedia.org/wiki/Timsort>`_
.. [#coverage] `https://pypi.python.org/pypi/coverage <https://pypi.python.org/pypi/coverage>`_
.. [#tox] `http://testrun.org/tox/latest/ <http://testrun.org/tox/latest/>`_
.. [#mro] See `http://www.python.org/download/releases/2.2.3/descrintro/#mro
              <http://www.python.org/download/releases/2.2.3/descrintro/#mro>`_
