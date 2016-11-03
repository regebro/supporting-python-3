CHANGES
=======

1.1 (Unreleased)
----------------

* Clarified that long() typically is not needed.


1.0 (2016-10-23)
----------------

Changes from "Porting to Python 3":

* Renamed the book to "Supporting Python 3"

* Removed any mentions of "porting" as it makes the process sound difficult.

* Use sys.version_info instead of sys.version

* De-emphasized 2to3 and other strategies in favour of supporting both
  languages directly in one source code.

* The old % style string formatting is no longer deprecated.

* Typo fixes and grammar improvements.

* The UnicodeReader example didn't use it's own encoding.

* A Py23DocChecker class to format unicode output in DocTests was added.

* Switched from the commercial Flux font to the open source Linux Biolinum O
