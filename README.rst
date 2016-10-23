Supporting Python 3
===================

.. image:: https://api.travis-ci.org/regebro/supporting-python-3.png

This is a free book about how to make your code support Python 3.

It costs nothing, and you can both publish it and contribute to it!


Reading this book
-----------------

Supporting Python 3 is available for free on http://python3porting.com/ . You
can also download a PDF version from https://gumroad.com/l/python3 for any
price you like, and you can buy a paper version from
https://www.createspace.com/4312357 for $4.45, which is the printing cost of
the book, and hence as close to free as you can possibly come.

As of today, the name of the book in all these places are "Porting to Python
3", which is the old name of the book before I made it into a community
effort. This will change sometime during 2015, and the above links will also
change as a result.


Contributing to this book
-------------------------

To contribute to this book, fork it on
`GitHub <https://github.com/regebro/supporting-python-3>`_.

If you are making any changes or additions that fall under copyright law, you
must first `sign the Contributor License Agreement
<https://www.clahub.com/agreements/regebro/supporting-python-3>`_.

Follow the instructions in `INSTALL.rst <INSTALL.rst>`_ on how to install it, and
make the changes you like, and create a pull request.

It's probably a good idea to talk to Lennart Regebro before making major
changes or additions.


License
-------

This book is (c) Lennart Regebro 2011-2015, and is licensed under a Creative
Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.

See http://creativecommons.org/licenses/by-nc-sa/3.0/

This means you can publish this book or parts of it, but not in such a way
that you make money from it. Should you want to use this book in a commercial
setting, please contact Lennart Regebro, regebro@gmail.com.

The book in it's current form uses Flux Bold, which is a commercial font.
If you want to publish this book in any form, you need either to replace
this font, or buy a license for the usage that you intend.

Generating the PDFs
-------------------

Making a PDF is not just a matter of doing ``make pdf``. Doing so will indeed
create a PDF, but you need to create four PDF's when releasing the book.

You need::

* A print PDF, 6" x 9", black only.
* A screen PDF, 8.27" x 11", with syntax highlighting.
* A tablet PDF, 7" x 9", with syntax highlighting.
* A phone PDF, 4.8" x 7.2", with syntax highlighting.

You do this by changing the conf.py. For the print PDF, the ``pygments_style``
should be ``"none"`` otherwise it should be ``"sphinx"``.

To select the paper size, change the used variable in ``print_latex_elements``
between ``print_form``, ``screen_form``, ``tablets_form`` or ``phone_form``.

You don't need to do anything more for the Print PDF, it's done, but the
other PDF's should have the front and back covers merged. This can be done
with tools like pdfunite::

    $ pdfunite covers/PhoneFront.pdf build/latex/SupportingPython3.pdf \
        covers/PhoneBack.pdf SupportingPython3-phone-1.0-dev.pdf

An additional hitch is that each release of Sphinx or texlive will have changes
that break the PDF generation, so it's highly unlikely that this book will
generate cleanly on your computer.
