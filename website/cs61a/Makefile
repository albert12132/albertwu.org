CS61A_DST=$(DST)/cs61a
CS61A_TEMPLATE = templates/cs61a.html templates/base.html
CS61A_CONFIG = base_config.py

all: cs61a

cs61a: cs61a-index

cs61a-index: $(CS61A_DST)/index.html

$(CS61A_DST)/index.html: cs61a/index.md $(CS61A_INDEX) $(CS61A_CONFIG)
	templar -c base_config.py -t cs61a.html -s $< -d $@

SUBDIRS=review notes
-include $(SUBDIRS:%=cs61a/%/Makefile)
