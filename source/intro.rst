===========================================================================
Welcome to Python 3
===========================================================================

On Christmas Day 1999 I sat down to write my first piece of software in Python.
My experience seems to be typical for Python users. I was initially surprised
that indentation was significant, it felt scary to not define variables and I
was hesitant to use a dynamic language to make serious software. However, in no
time at all these worries were gone and I noticed I wrote code faster than ever.
18 months later a friend hired me to his start-up to help him write a content
management system and I ended up in the enviable position of being a full time
Python developer. I don't even mention other languages on my CV anymore, because
I don't want to use them. I've become a full fledged, fanatic, Pythonista.

I got interested in Python 3 at EuroPython 2007 in lovely Vilnius. Guido van
Rossum's keynote was about the upcoming changes in Python 3 and although he
emphatically said that you could not run the same code under Python 2 and
Python 3, I couldn't see many reasons why it couldn't be done, considering the
forward compatibility that was planned for Python 2.6. So I started looking at
the differences between Python 2 and Python 3 and tried to find out how to
write code that would run under both versions and learned a whole lot about
Python on the way.

Most surprising was how little the fundamentals have changed. Writing code with
Python 3 still feels just like the old comfortable shoes, but newly shined and
with new laces. The hardest change to get used to is to remember that ``print``
is a function. The relatively small differences don't necessarily mean that
supporting Python 3 is easy, but it can be and hopefully this book will make it
even easier.

---------------------------------------------------------------------------
The time is nigh
---------------------------------------------------------------------------

Python 2 is still more widely used than Python 3. A major reason for not
switching yet is that Python 2 is so good that most developers feel little
incentive to switch. Although it has been officially declared that
Python 2.7 will be the last version of Python 2, it will receive bug-fixes
until 2020, so there are still a few years left.

Despite this you should move to Python 3 as soon as as possible. Python 3 is
a nicer cleaner language, and all the new cool features end up there. Those
features are out of scope for this book, but I can just mention features like
keyword-only arguments, chained exceptions, ``yield from``, and enums.

If you are writing a package that other `developers` use, every day it doesn't
support Python 3 is a day when you are blocking your users from using Python 3,
and a day when Python 3 users have to look for another package than yours. In
this case you should really try to add Python 3 support immediately, and if you
have dependencies that does not support Python 3, then help with those first.

---------------------------------------------------------------------------
What if I can't switch right now?
---------------------------------------------------------------------------

.. index:: trove classifier

In any case all the packages `you` depend on need support Python 3 before you
can switch. Most packages that support Python 3 are listed on the CheeseShop
under the "Python 3 packages" heading\ [#pypi3]_. That list is a list of all
packages that includes ``"Programming Language :: Python :: 3"`` as a trove
classifier in the package meta data. If your dependencies do not support Python
3 it is a good idea to contact the maintainers of your dependencies to see what
plans they have for Python 3 support. Perhaps they do already support Python 3,
but didn't update their meta data? Maybe they just didn't know anyone was
waiting for Python 3 support? Maybe you can help?

It's always a good idea to publish information on your plans for Python 3 on your
software's homepage or in the description of the package on the CheeseShop.
Include a list of your dependencies that are blocking you. That way your users can
see if there is something they can help with. Open source is all about
programmers helping each other; both using and contributing to each other's
software. Supporting Python 3 is no different.

And even if you aren't switching right now, there are things you can do already.
Chapter 3, :ref:`preparing-chapter` lists things you should change before adding
Python 3 support, and Chapter 6 :ref:`improving-chapter` lists modern idioms in
Python that you already can use, depending on what Python versions you need to
support. To ease the transition to Python 3, many of the new functions and
modules in Python 3 have been backported to Python 2.6 or Python 2.7, and the
only thing that stops you from using this already is if you need to support
Python 2.5 or earlier.

---------------------------------------------------------------------------
Python and its versions
---------------------------------------------------------------------------

Since I started writing this book, Python 2.7 and Python 3.2 have been
released. For the purposes of this book, Python 2.6 and Python 2.7 can be seen
as equal. So most of the times the book says Python 2.6, you can read that as
Python 2.6 or Python 2.7.

Python 3.1 was released quite quickly after Python 3.0 and before any
significant adoption of Python 3. Therefore it was decided to drop support for
Python 3.0. As most platforms that support Python 3 already use Python 3.1
for that support it is unlikely that you ever need to care about Python 3.0.
When running your tests under Python 3 you only have to run it with Python 3.1
and Python 3.2, and you can safely ignore Python 3.0. So when this book says
Python 3, you can read that as Python 3.1 and later.

---------------------------------------------------------------------------
Further resources
---------------------------------------------------------------------------

There is still very little documentation on how to support Python 3. There is a
short how-to in the Python 3.2 documentation at
http://docs.python.org/dev/howto/pyporting.html. There is also a page on the
official Python wiki at http://wiki.python.org/moin/PortingPythonToPy3k which
contain a good list of other resources.

If you need help, or if you want to help out, there is the
``python-porting@python.org`` mailing list. You can subscribe to it from
http://mail.python.org/mailman/listinfo/python-porting.


.. rubric:: Footnotes

.. [#pypi3] `http://pypi.python.org/pypi?:action=browse&c=533&show=all <http://pypi.python.org/pypi?:action=browse&c=533&show=all>`_
