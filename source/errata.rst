======
Errata
======

*Errors in spelling and grammar is not included in this list.*
*Page numbers refer to the print edition.*

Errata for the second edition, Revision 1.0
===========================================

**Section 3.2, Page 21:**

The second example should say::

    >>> 5/2
    2.5

**Appendix I, Page ??:**

In Python 3, division of integers will always return floats.


Errata for the first edition
============================

**Section 3.2, Page 21:**

The second example should say::

    >>> 5/2
    2.5

**Section 3.5.1, Page 27:**

The bug fix for ``total_ordering`` in Python 3.2 only solved some of the 
cases. It's still broken and can still in some cases cause infinite recursion.
There is a `bug report <http://bugs.python.org/issue10042>`_ for this. 

**Section 6.7, Page 65:**

Although the term *"Generator comprehension"* was used in the beginning of the
discussion of the feature, it was deemed confusing and that terminology was 
replaced by the term *"Generator expression"*.

Also, generator expressions have been around since Python 2.4 not 2.6.

**Appendix I, Page ??:**

In Python 3, division of integers will always return floats.

