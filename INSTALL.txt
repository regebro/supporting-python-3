Installation
============

You need a Python with Sphinx installed. It's tested with Python 3.4, but
any Python with Sphinx is likely to work.

To run make spell you need aspell and american english dictionaries.

* Debian-based: ``apt-get install aspell-en``
* Red Hats: ``yum install aspell-en``

To make pdf's you need Texlive 2013:

* Debian-based: ``apt-get install texlive-full``
* Red Hats: ``yum install texlive*``
* Other systems: http://www.tug.org/texlive/quickinstall.html

You also need the following fonts:

* Flux Bold (FLUXB___.ttf)
  This is a commercial font, so you need to buy it if you want to generate PDF's.
* DejaVu Sans Mono
  It's included in many Linux distro's by default.
* TeX Gyre Schola
  http://www.gust.org.pl/projects/e-foundry/tex-gyre/schola
  Installable as ``texlive-tex-gyre`` on RPM based linuces and
  ``fonts-texgyre`` on DEB based linuces.


Testing setup
=============

(This is all stupid and needs to change. We should probably use Spiny.
We can't use Tox, because it doesn't support old Python versions.)

This script tests locales, for testing purposes the locale sv_SE.UTF-8
must be available.

The script tries to find system wide python installations.

On Ubuntu, you can get all these linux installations from the ppa:fkrull/deadsnakes

If this fails, it looks for Python 2.3, 2.4, 2,5 in ``/opt/python23`` etc.

Python 2.5, 2.7, 3.1, 3.2, 3.3, 3.4 must be installed in ``./python26``,
...

In Python 2.6 and above also do this::

    pip install zope.interface setuptools==11.2

Run the tests with ``make test``. Some tests may fail on the first time, with
warnings like ``warning: no previously-included files matching '*.pyc' found
anywhere in distribution``. Re-running them solves that.

