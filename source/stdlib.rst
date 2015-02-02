.. _stdlib-chapter:

===========================================================================
Reorganizations and renamings
===========================================================================

.. index:: modules

---------------------------------------------------------------------------
The standard library
---------------------------------------------------------------------------

.. index:: six

The Python standard library has been reorganized in Python 3 to be more
consistent and easier to use. All the module names now conform to the
style guide for Python code, PEP 8\ [#pep8]_,
and several modules have been merged.

``2to3`` contains fixers for all of this, so this sectin is mostly of interest
if you need to support both Python 2 and Python 3 without ``2to3`` conversion.

The ``six`` module\ [#six]_ has support for most of the standard library
reorganization. You can import the reorganized modules from ``six.moves``::

    >>> from six.moves import cStringIO

In Python 2 this will be equivalent to::

    >>> from cStringIO import StringIO

While in Python 3 this will be equivalent to::

    >>> from io import StringIO

If you want to support Python 2 and Python 3 without conversion and you don't
want to use the ``six`` module, this is also very easy. You just try to import
from one location, catch the error and then import from the other location.
It doesn't matter of you put the Python 3 location first or last, both works
equally well::

    >>> try:
    ...     from io import StringIO
    ... except ImportError:
    ...     from cStringIO import StringIO

This table contains the renamings and reorganizations of the standard library,
except for the ``urllib``, ``urllib2`` and ``urlparse`` reorganization, which
has a separate table:

..
    The following raw LaTeX syntax is necessary to make the typeface smaller
    in the tables. This is because this first table will otherwise not fit on
    a 6" wide page. The other tables do fit, but I've made them smaller as
    well, for consistency.

.. raw:: latex

    \begin{footnotesize}

+--------------------------+--------------------------+----------------------------+
| Python 2 name            |  Python 3 name           | ``six`` name               |
+==========================+==========================+============================+
| ``anydbm``               | ``dbm``                  |                            |
+--------------------------+--------------------------+----------------------------+
| ``BaseHTTPServer``       | ``http.server``          | ``BaseHTTPServer``         |
+--------------------------+--------------------------+----------------------------+
| ``__builtin__``          | ``builtins``             | ``builtins``               |
+--------------------------+--------------------------+----------------------------+
| ``CGIHTTPServer``        | ``http.server``          | ``CGIHTTPServer``          |
+--------------------------+--------------------------+----------------------------+
| ``ConfigParser``         | ``configparser``         | ``configparser``           |
+--------------------------+--------------------------+----------------------------+
| ``copy_reg``             | ``copyreg``              | ``copyreg``                |
+--------------------------+--------------------------+----------------------------+
| ``cPickle``              | ``pickle``               | ``cPickle``                |
+--------------------------+--------------------------+----------------------------+
| ``cProfile``             | ``profile``              |                            |
+--------------------------+--------------------------+----------------------------+
| ``cStringIO.StringIO``   | ``io.StringIO``          | ``cStringIO``              |
+--------------------------+--------------------------+----------------------------+
| ``Cookie``               | ``http.cookies``         | ``http_cookies``           |
+--------------------------+--------------------------+----------------------------+
| ``cookielib``            | ``http.cookiejar``       | ``http_cookiejar``         |
+--------------------------+--------------------------+----------------------------+
| ``dbhash``               | ``dbm.bsd``              |                            |
+--------------------------+--------------------------+----------------------------+
| ``dbm``                  | ``dbm.ndbm``             |                            |
+--------------------------+--------------------------+----------------------------+
| ``dumbdb``               | ``dbm.dumb``             |                            |
+--------------------------+--------------------------+----------------------------+
| ``Dialog``               | ``tkinter.dialog``       | ``tkinter_dialog``         |
+--------------------------+--------------------------+----------------------------+
| ``DocXMLRPCServer``      | ``xmlrpc.server``        |                            |
+--------------------------+--------------------------+----------------------------+
| ``FileDialog``           | ``tkinter.FileDialog``   | ``tkinter_filedialog``     |
+--------------------------+--------------------------+----------------------------+
| ``FixTk``                | ``tkinter._fix``         |                            |
+--------------------------+--------------------------+----------------------------+
| ``gdbm``                 | ``dbm.gnu``              |                            |
+--------------------------+--------------------------+----------------------------+
| ``htmlentitydefs``       | ``html.entities``        | ``html_entities``          |
+--------------------------+--------------------------+----------------------------+
| ``HTMLParser``           | ``html.parser``          | ``html_parser``            |
+--------------------------+--------------------------+----------------------------+
| ``httplib``              | ``http.client``          | ``http_client``            |
+--------------------------+--------------------------+----------------------------+
| ``markupbase``           | ``_markupbase``          |                            |
+--------------------------+--------------------------+----------------------------+
| ``Queue``                | ``queue``                | ``queue``                  |
+--------------------------+--------------------------+----------------------------+
| ``repr``                 | ``reprlib``              | ``reprlib``                |
+--------------------------+--------------------------+----------------------------+
| ``robotparser``          | ``urllib.robotparser``   | ``urllib_robotparser``     |
+--------------------------+--------------------------+----------------------------+
| ``ScrolledText``         | ``tkinter.scolledtext``  | ``tkinter_scrolledtext``   |
+--------------------------+--------------------------+----------------------------+
| ``SimpleDialog``         | ``tkinter.simpledialog`` | ``tkinter_simpledialog``   |
+--------------------------+--------------------------+----------------------------+
| ``SimpleHTTPServer``     | ``http.server``          | ``SimpleHTTPServer``       |
+--------------------------+--------------------------+----------------------------+
| ``SimpleXMLRPCServer``   | ``xmlrpc.server``        |                            |
+--------------------------+--------------------------+----------------------------+
| ``StringIO.StringIO``    | ``io.StringIO``          |                            |
+--------------------------+--------------------------+----------------------------+
| ``SocketServer``         | ``socketserver``         | ``socketserver``           |
+--------------------------+--------------------------+----------------------------+
| ``test.test_support``    | ``test.support``         | ``tkinter``                |
+--------------------------+--------------------------+----------------------------+
| ``Tkinter``              | ``tkinter``              | ``tkinter``                |
+--------------------------+--------------------------+----------------------------+
| ``Tix``                  | ``tkinter.tix``          | ``tkinter_tix``            |
+--------------------------+--------------------------+----------------------------+
| ``Tkconstants``          | ``tkinter.constants``    | ``tkinter_constants``      |
+--------------------------+--------------------------+----------------------------+
| ``tkColorChooser``       | ``tkinter.colorchooser`` | ``tkinter_colorchooser``   |
+--------------------------+--------------------------+----------------------------+
| ``tkCommonDialog``       | ``tkinter.commondialog`` | ``tkinter_commondialog``   |
+--------------------------+--------------------------+----------------------------+
| ``Tkdnd``                | ``tkinter.dnd``          | ``tkinter_dnd``            |
+--------------------------+--------------------------+----------------------------+
| ``tkFileDialog``         | ``tkinter.filedialog``   | ``tkinter_tkfiledialog``   |
+--------------------------+--------------------------+----------------------------+
| ``tkFont``               | ``tkinter.font``         | ``tkinter_font``           |
+--------------------------+--------------------------+----------------------------+
| ``tkMessageBox``         | ``tkinter.messagebox``   | ``tkinter_messagebox``     |
+--------------------------+--------------------------+----------------------------+
| ``tkSimpleDialog``       | ``tkinter.simpledialog`` | ``tkinter_tksimpledialog`` |
+--------------------------+--------------------------+----------------------------+
| ``turtle``               | ``tkinter.turtle``       |                            |
+--------------------------+--------------------------+----------------------------+
| ``UserList``             | ``collections``          |                            |
+--------------------------+--------------------------+----------------------------+
| ``UserString``           | ``collections``          |                            |
+--------------------------+--------------------------+----------------------------+
| ``whichdb``              | ``dbm``                  |                            |
+--------------------------+--------------------------+----------------------------+
| ``_winreg``              | ``winreg``               | ``winreg``                 |
+--------------------------+--------------------------+----------------------------+
| ``xmlrpclib``            | ``xmlrpc.client``        |                            |
+--------------------------+--------------------------+----------------------------+

.. raw:: latex

    \end{footnotesize}


``urllib``, ``urllib2`` and ``urlparse``
========================================

The three modules ``urllib``, ``urllib2`` and ``urlparse`` has been reorganized
into three new modules, ``urllib.request``, ``urllib.parse`` and
``urllib.error``. Since there is no ``six`` support for these renames you have
to use the ``try/except`` technique above.

.. raw:: latex

    \begin{footnotesize}

+---------------------------------------------+--------------------+
| Python 2 name                               |  Moved to          |
+=============================================+====================+
| ``urllib._urlopener``                       | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib.ContentTooShortError``             | ``urllib.error``   |
+---------------------------------------------+--------------------+
| ``urllib.FancyURLOpener``                   | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib.pathname2url``                     | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib.quote``                            | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urllib.quote_plus``                       | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urllib.splitattr``                        | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urllib.splithost``                        | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urllib.splitnport``                       | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urllib.splitpasswd``                      | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urllib.splitport``                        | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urllib.splitquery``                       | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urllib.splittag``                         | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urllib.splittype``                        | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urllib.splituser``                        | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urllib.splitvalue``                       | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urllib.unquote``                          | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urllib.unquote_plus``                     | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urllib.urlcleanup``                       | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib.urlencode``                        | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urllib.urlopen``                          | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib.URLOpener``                        | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib.urlretrieve``                      | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.AbstractBasicAuthHandler``        | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.AbstractDigestAuthHandler``       | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.BaseHandler``                     | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.build_opener``                    | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.CacheFTPHandler``                 | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.FileHandler``                     | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.FTPHandler``                      | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.HTTPBasicAuthHandler``            | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.HTTPCookieProcessor``             | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.HTTPDefaultErrorHandler``         | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.HTTPDigestAuthHandler``           | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.HTTPError``                       | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.HTTPHandler``                     | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.HTTPPasswordMgr``                 | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.HTTPPasswordMgrWithDefaultRealm`` | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.HTTPRedirectHandler``             | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.HTTPSHandler``                    | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.install_opener``                  | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.OpenerDirector``                  | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.ProxyBasicAuthHandler``           | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.ProxyDigestAuthHandler``          | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.ProxyHandler``                    | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.Request``                         | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.UnknownHandler``                  | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.URLError``                        | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urllib2.urlopen``                         | ``urllib.request`` |
+---------------------------------------------+--------------------+
| ``urlparse.parse_qs``                       | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urlparse.parse_qsl``                      | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urlparse.urldefrag``                      | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urlparse.urljoin``                        | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urlparse.urlparse``                       | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urlparse.urlsplit``                       | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urlparse.urlunparse``                     | ``urllib.parse``   |
+---------------------------------------------+--------------------+
| ``urlparse.urlunsplit``                     | ``urllib.parse``   |
+---------------------------------------------+--------------------+

.. raw:: latex

    \end{footnotesize}

.. _removedmodules-section:


---------------------------------------------------------------------------
Removed modules
---------------------------------------------------------------------------

Some of the standard library modules have been dropped. One is ``UserDict``, but
some of the classes have replacements that are almost, but not quite completely
compatible. See :ref:`userdict-section` for more information on that.

Most of the other modules that have been dropped are modules that have long
been supplanted by other, improved modules, or modules that are specific to
platforms that is no longer supported. Fittingly, and exception to this rule is
the ``exception`` module. It contains a hierarchy of exceptions, but all of them
are also built-ins, so you never need to import anything from the ``exception``
module. It has therefore been removed from Python 3 completely.

Except for the modules specific for Solaris, IRIX and Mac OS 9, this is the
list of modules that has been removed in Python 3:

.. raw:: latex

    \begin{footnotesize}

+-------------------+----------------------------------------------------------+
| Module name       | Comment                                                  |
+===================+==========================================================+
| ``audiodev``      |                                                          |
+-------------------+----------------------------------------------------------+
| ``Bastion``       |                                                          |
+-------------------+----------------------------------------------------------+
| ``bsddb185``      | Supplanted by ``bsddb3``                                 |
+-------------------+----------------------------------------------------------+
| ``bsddb3``        | Available on the CheeseShop                              |
+-------------------+----------------------------------------------------------+
| ``Canvas``        |                                                          |
+-------------------+----------------------------------------------------------+
| ``cfmfile``       |                                                          |
+-------------------+----------------------------------------------------------+
| ``cl``            |                                                          |
+-------------------+----------------------------------------------------------+
| ``commands``      |                                                          |
+-------------------+----------------------------------------------------------+
| ``compiler``      |                                                          |
+-------------------+----------------------------------------------------------+
| ``dircache``      |                                                          |
+-------------------+----------------------------------------------------------+
| ``dl``            | Supplanted by ``ctypes``                                 |
+-------------------+----------------------------------------------------------+
| ``exception``     | See above                                                |
+-------------------+----------------------------------------------------------+
| ``fpformat``      |                                                          |
+-------------------+----------------------------------------------------------+
| ``htmllib``       | Supplanted ``html.parser``                               |
+-------------------+----------------------------------------------------------+
| ``ihooks``        |                                                          |
+-------------------+----------------------------------------------------------+
| ``imageop``       |                                                          |
+-------------------+----------------------------------------------------------+
| ``imputil``       |                                                          |
+-------------------+----------------------------------------------------------+
| ``linuxaudiodev`` | Supplanted by ``ossaudiodev``                            |
+-------------------+----------------------------------------------------------+
| ``md5``           | Supplanted by ``hashlib``                                |
+-------------------+----------------------------------------------------------+
| ``mhlib``         |                                                          |
+-------------------+----------------------------------------------------------+
| ``mimetools``     | Supplanted by ``email``                                  |
+-------------------+----------------------------------------------------------+
| ``MimeWriter``    | Supplanted by ``email``                                  |
+-------------------+----------------------------------------------------------+
| ``mimify``        | Supplanted by ``email``                                  |
+-------------------+----------------------------------------------------------+
| ``multifile``     | Supplanted by ``email``                                  |
+-------------------+----------------------------------------------------------+
| ``mutex``         |                                                          |
+-------------------+----------------------------------------------------------+
| ``new``           |                                                          |
+-------------------+----------------------------------------------------------+
| ``popen2``        | Supplanted by ``subprocess``                             |
+-------------------+----------------------------------------------------------+
| ``posixfile``     |                                                          |
+-------------------+----------------------------------------------------------+
| ``pure``          |                                                          |
+-------------------+----------------------------------------------------------+
| ``rexec``         |                                                          |
+-------------------+----------------------------------------------------------+
| ``rfc822``        | Supplanted by ``email``                                  |
+-------------------+----------------------------------------------------------+
| ``sha``           | Supplanted by ``hashlib``                                |
+-------------------+----------------------------------------------------------+
| ``sgmllib``       |                                                          |
+-------------------+----------------------------------------------------------+
| ``sre``           | Supplanted by ``re``                                     |
+-------------------+----------------------------------------------------------+
| ``stat``          | Supplanted by ``os.stat()``                              |
+-------------------+----------------------------------------------------------+
| ``stringold``     |                                                          |
+-------------------+----------------------------------------------------------+
| ``sunaudio``      |                                                          |
+-------------------+----------------------------------------------------------+
| ``sv``            |                                                          |
+-------------------+----------------------------------------------------------+
| ``test.testall``  |                                                          |
+-------------------+----------------------------------------------------------+
| ``thread``        | Supplanted by ``threading``                              |
+-------------------+----------------------------------------------------------+
| ``timing``        |                                                          |
+-------------------+----------------------------------------------------------+
| ``toaiff``        |                                                          |
+-------------------+----------------------------------------------------------+
| ``user``          |                                                          |
+-------------------+----------------------------------------------------------+

.. raw:: latex

    \end{footnotesize}


---------------------------------------------------------------------------
Moved builtins
---------------------------------------------------------------------------

.. index:: intern(), reduce(), reload()

There are also a couple of builtin functions that have been moved to
standard library modules. You handle them in a similar way, by trying to import them
from the Python 3 location and if this fails you just do nothing::

    >>> try:
    ...     from imp import reload
    ... except ImportError:
    ...     pass

The moved builtins are:

..
   This and the next table also has a \par in the LaTex, otherwise they will
   be incorrectly positioned to the right of the text instead of below it.

.. raw:: latex

    \par
    \begin{footnotesize}

+--------------------------+--------------------------+----------------------------+
| Python 2 name            | Python 3 name            | ``six`` name               |
+==========================+==========================+============================+
| ``intern()``             | ``sys.intern()``         |                            |
+--------------------------+--------------------------+----------------------------+
| ``reduce()``             | ``functools.reduce()``   | ``reduce``                 |
+--------------------------+--------------------------+----------------------------+
| ``reload()``             | ``imp.reload()``         | ``reload_module``          |
+--------------------------+--------------------------+----------------------------+


.. raw:: latex

    \end{footnotesize}


---------------------------------------------------------------------------
``string`` module removals
---------------------------------------------------------------------------

.. index:: string, str, capitalize(), center(), count(), expandtabs(),
           find(), index(), join(), ljust(), lower(), lstrip(), zfill(),
           maketrans(), replace(), rfind(), rindex(), rjust(), rsplit(),
           rstrip(), split(), strip(), swapcase(), translate(), upper()

Several functions have existed both in the ``string`` module and as methods
on the ``str`` type and instances. These have now been removed from the
``string`` module. You can use them either on string instances or from the
``str`` type itself. So what in Python 2 could be written:

.. literalinclude:: _tests/upper24.txt

Should now be written in one of the following ways:

.. literalinclude:: _tests/upper26.txt

The first way of doing it is the most common one, but moving to the
second way can be done with a simple search and replace.

The removed functions are ``capitalize()``, ``center()``, ``count()``,
``expandtabs()``, ``find()``, ``index()``, ``join()``, ``ljust()``,
``lower()``, ``lstrip()``, ``maketrans()``, ``replace()``, ``rfind()``,
``rindex()``, ``rjust()``, ``rsplit()``, ``rstrip()``, ``split()``,
``strip()``, ``swapcase()``, ``translate()``, ``upper()`` and ``zfill()``.

In addition the functions ``atof()``, ``atoi()`` and ``atol()`` has been
removed, and have been replaced with passing the string value into the
``float`` and ``int`` constructors. Since these functions have been
deprecated since Python 2.0 it's highly unlikely that you actually use them.

---------------------------------------------------------------------------
Function and method attribute renamings
---------------------------------------------------------------------------

.. index:: im_func, im_self, im_class, func_closure, func_doc, func_globals,
           func_name, func_defaults, func_code, func_dict

Many of the special attribute names on functions and methods were named before
it was decided that Python should use the "double underscore" method for
special names used by Python. They   have been renamed in Python 3.

The easiest way of handling this if you are not using ``2to3`` is to define a
variable with the attribute name depending on the Python version and using
``getattr`` to access the attribute. This doesn't work in the case of the
renaming of ``im_class``, though, so there you need a function to fetch the
result:

.. literalinclude:: _tests/renames26.txt

Six has  defined functions to retrieve the most common attribute names:

.. raw:: latex

    \par
    \begin{footnotesize}

+-------------------+------------------------+-----------------------------+
| Python 2 name     |  Python 3 name         | ``six`` function            |
+===================+========================+=============================+
| ``func_closure``  | ``__closure__``        |                             |
+-------------------+------------------------+-----------------------------+
| ``func_doc``      | ``__doc__``            |                             |
+-------------------+------------------------+-----------------------------+
| ``func_globals``  | ``__globals__``        |                             |
+-------------------+------------------------+-----------------------------+
| ``func_name``     | ``__name__``           |                             |
+-------------------+------------------------+-----------------------------+
| ``func_defaults`` | ``__defaults__``       | ``get_function_defaults()`` |
+-------------------+------------------------+-----------------------------+
| ``func_code``     | ``__code__``           | ``get_function_code()``     |
+-------------------+------------------------+-----------------------------+
| ``func_dict``     | ``__dict__``           |                             |
+-------------------+------------------------+-----------------------------+
| ``im_func``       | ``__func__``           | ``get_method_function()``   |
+-------------------+------------------------+-----------------------------+
| ``im_self``       | ``__self__``           | ``get_method_self()``       |
+-------------------+------------------------+-----------------------------+
| ``im_class``      | ``__self__.__class__`` |                             |
+-------------------+------------------------+-----------------------------+

.. raw:: latex

    \end{footnotesize}


.. rubric:: Footnotes

.. [#pep8] `http://www.python.org/dev/peps/pep-0008/
           <http://www.python.org/dev/peps/pep-0008/>`_

.. [#six] `http://pypi.python.org/pypi/six <http://pypi.python.org/pypi/six>`_
