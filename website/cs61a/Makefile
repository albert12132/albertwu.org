CS61A_DST=$(DST)/cs61a
CS61A_TEMPLATE = templates/cs61a.html templates/base.html
CS61A_CONFIG = config.py

all: cs61a

cs61a: cs61a-index

cs61a-index: $(CS61A_DST)/index.html

$(CS61A_DST)/index.html: cs61a/index.md $(CS61A_INDEX) $(CS61A_CONFIG)
	$(COMPILE) -m -s $< -d $@ cs61a.html

SUBDIRS=review notes
-include $(SUBDIRS:%=cs61a/%/Makefile)
