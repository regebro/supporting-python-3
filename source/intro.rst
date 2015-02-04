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
Rossums keynote was about the upcoming changes in Python 3 and although he
emphatically said that you could not run the same code under Python 2 and
Python 3, I couldn't see many reasons why it couldn't be done, considering the
forward compatibility that was planned for Python 2.6. So I started looking at
the differences between Python 2 and Python 3 and tried to find out how to
write code that would run under both versions and learned a whole lot about
Python on the way.

Most surprising was how little the fundamentals have changed. Writing code with
Python 3 still feels just like the old comfortable shoes, but newly shined and
with new laces. The hardest change to get used to is to remember that ``print``
is a function. The relatively small differences doesn't necessarily mean that
porting to Python 3 is easy, but it can be and hopefully this book will make it
even easier.

---------------------------------------------------------------------------
Is it time yet?
---------------------------------------------------------------------------

Yes, Python 3 is a nicer language to work with. But Python 2 is also very good
and the major reason for not porting yet is that Python 2 is so good that most
developers feel little incentive to switch. Although it has been officially
declared that Python 2.7 will be the last version of Python 2, it will receive
bug-fixes for many years to come, so there is no hurry to change to Python 3 for
that reason.

So when should you port? In general, I would recommend everyone to move to
Python 3 as soon as you can. If the applications and modules you write are for
your or your company's use only, then look into porting when it feels like you
have the time. If your project is in a state of panic, moving to Python 3 is
probably not the right thing to do.

If you are writing software that you sell or share as open source, then you want
to move more quickly to enable your customers to move over to Python 3.

If you are writing a package that other `developers` use, every day it doesn't
support Python 3 is a day when you are blocking your users from porting, and a
day when Python 3 users have to look for another package than yours. In this
case you should really try to port immediately, and if you have dependencies
that are not ported, then help port them first.

---------------------------------------------------------------------------
What if I can't port right now?
---------------------------------------------------------------------------

.. index:: trove classifier

In any case all the packages `you` depend on need to be ported before you can
port. Most packages that have been ported to Python 3 are listed on the
CheeseShop under the "Python 3 packages" heading\ [#pypi3]_. That list is a list
of all packages that includes ``"Programming Language :: Python :: 3"`` as a
trove classifier in the package meta data. If your dependencies have not been
ported it is a good idea to contact the maintainers of your dependencies to see
what plans they have for porting. Perhaps they do already support Python 3, but
didn't update their meta data? Maybe they just didn't know anyone was waiting
for a Python 3 port? Maybe you can help porting?

It's always a good idea to publish information on your plans for porting on your
software's homepage or in the description of the package on the CheeseShop.
Include a list of your dependencies that aren't ported. That way your users can
see if there is something they can help with. Open source all is about
programmers helping each other; both using and contributing to each other's
software. A porting effort is no different.

And even if you aren't porting right now, there are things you can do already.
Chapter 3, :ref:`preparing-chapter` lists things you should change before
porting, and Chapter 6 :ref:`improving-chapter` lists modern idioms in Python
that you already can use, depending on what Python versions you need to support.
To ease porting, many of the new functions and modules in Python 3 has been
backported to Python 2.6 or Python 2.7, and the only thing that stops you from
using this already is if you need to support older versions.

---------------------------------------------------------------------------
Python and its versions
---------------------------------------------------------------------------

Since I started writing this book, Python 2.7 and Python 3.2 has been
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

There is still very little documentation on how to port to Python 3. There is a
short how-to in the Python 3.2 documentation at
http://docs.python.org/dev/howto/pyporting.html. There is also page on the
official Python wiki for porting notes at
http://wiki.python.org/moin/PortingPythonToPy3k but it is still fairly
empty.

If you need help, or if you want to help out, there is the
``python-porting@python.org`` mailing list. You can subscribe to it from
http://mail.python.org/mailman/listinfo/python-porting.


.. rubric:: Footnotes

.. [#pypi3] `http://pypi.python.org/pypi?:action=browse&c=533&show=all <http://pypi.python.org/pypi?:action=browse&c=533&show=all>`_
