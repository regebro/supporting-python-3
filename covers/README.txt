How to make covers
==================

The cover is in the Covers.xcf file. That's a GIMP file, so you need to use
GIMP to open it for editing and PDF generation. And you need to create a lot
of PDF's. You will also need GhostScript installed.

The Covers.xcf is designed for use with Createspace self publishing.
For more information on the PDF requirements, check with createspace.

The Spine of the book is the number of interior pages * 0.002252 inches.
If a significant amount of pages is added to the book, you may need to
adjust the design.

The two top layers are:

* BookCover6X9_BW_140. This is an import of the Createspace cover template.
  It's for 140 pages, and the book is currently 151, but that's not enough
  to create a problem.

* Preview Mask. This is a gray mask that will allow you to see approximately
  the area that the printed cover will be.

Both these layers must be invisible when printing the cover.


Custom paper sizes
------------------

The PDF's come in three formats: Print, Phone, Tablet and Screen. OK, fine,
phones and tablets are also screens, but they are also computers, and "PC"
kinda implies it's not a Mac, so I choose "screen" as a name.

To create the cover PDFs them you need to create several custom paper sizes.
There should be creates with 0 page margins, and the following sizes
(width x height):

* Print size: 17" x 11"
* Phone size: 4.8" x 7.2"
* Tablet size: 6" x 9"
* Screen size: 7.32" x 11"
  (This fits both in A4 and Letter and hence you can also print it.)


The print cover PDF
-------------------

To create the cover for printing, select the custom paper size that is 17" wide
by 11" high. Go to the Image Settings tab in the print dialog, select "Ignore
page margins" and then scale the image to as big as possible.

Print to a file in portrait mode. Yes, that portrait mode will be wider than
high, but that's not a problem. The default output for printing is typically a
file called ``output.pdf`` in your home directory.

The resulting PDF will be sent to the printing company to make the cover, and
the PDF created by Sphinx is the inside pages. The printing companies I have
used for the big conference print runs have both accepted this PDF, and it's
designed for use with Createspace. Other online self-publishing companies may
have other requirements.


The PDF covers
--------------

The PDF issues should also have covers, but unlike the print cover they
should contain only the printed area. Therefore you must crop the image
before printing. Turn on the preview mask, make sure that Snap to guides
is enabled and crop away the gray area and the spine. The resulting image
should be approximately 6" x 9".

This image you then print to the Phone, Tablet and Screen papers, again
while ignoring page margins and scaling the image to be as big as possible.
The resulting images will be too heavy, with front covers being around 6MB.

Therefore you need to optimize each PDF with Ghostscript. The command to
optimize the front PDF for the Phone size would be this::

  gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4  -sOutputFile=PhoneFront.pdf ~/output.pdf

Repeat for each of the sizes, and then do the same for the back cover.

Done!
