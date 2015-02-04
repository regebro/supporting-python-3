# Makefile for Sphinx documentation
#

export PYTHONPATH = $(shell echo "$$PYTHONPATH"):.

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = build

# Internal variables.
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(SPHINXOPTS) source

LATEXPATH = $${PATH}
LATEXEXE = xelatex
LATEXOPTS =

OUTPUTNAME=SupportingPython3

SPELL = aspell -l en_US

.PHONY: help clean html dirhtml pickle json htmlhelp qthelp latex changes linkcheck doctest

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html      to make standalone HTML files"
	@echo "  dirhtml   to make HTML files named index.html in directories"
	@echo "  latex     to make LaTeX files, you can set PAPER=a4 or PAPER=letter"
	@echo "  pdf       to make a PDF"
	@echo "  epub      to make an ePUB book"
	@echo "  changes   to make an overview of all changed/added/deprecated items"
	@echo "  linkcheck to check all external links for integrity"

clean:
	-rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

epub:
	$(SPHINXBUILD) -b epub $(ALLSPHINXOPTS) $(BUILDDIR)/epub
	@echo
	@echo "Build finished. The epub pages are in $(BUILDDIR)/epub."

dirhtml:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
	@echo "Run \`make all-pdf' or \`make all-ps' in that directory to" \
	      "run these through (pdf)latex."

changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

pdf: latex
	# Copy in some custom files
	cp source/_templates/sphinxcustom.cls $(BUILDDIR)/latex/sphinxcustom.cls
	cp source/_templates/sphinx.sty $(BUILDDIR)/latex/sphinx.sty
	cp source/_static/by-nc-sa.pdf $(BUILDDIR)/latex/by-nc-sa.pdf
	# Run LaTeX three times, the first time generates the text:
	cd $(BUILDDIR)/latex; PATH=$(LATEXPATH) $(LATEXEXE) $(LATEXOPTS) $(OUTPUTNAME).tex
	# Create the indexes
	-cd $(BUILDDIR)/latex; PATH=$(LATEXPATH) makeindex -s python.ist $(OUTPUTNAME).idx
	# Re run LaTex with indexes. Now we get a content listing and an index.
	cd $(BUILDDIR)/latex; PATH=$(LATEXPATH) $(LATEXEXE) $(LATEXOPTS) $(OUTPUTNAME).tex
	# Recreate the index since all the page numbers changed when the content listing appeared.
	-cd $(BUILDDIR)/latex; PATH=$(LATEXPATH) makeindex -s python.ist $(OUTPUTNAME).idx
	# And run LaTex again, this time with correct page numbers
	cd $(BUILDDIR)/latex; PATH=$(LATEXPATH) $(LATEXEXE) $(LATEXOPTS) $(OUTPUTNAME).tex

spell:
	for f in source/*.rst; do $(SPELL) -c $$f; done

stats:
	wc source/*.rst

test:
	./runtests.sh

check: spell test stats
