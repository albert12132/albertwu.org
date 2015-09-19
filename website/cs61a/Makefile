CS61A_DST=$(DST)/cs61a
CS61A_INDEX = templates/cs61a.html

all: cs61a

cs61a: cs61a-index

cs61a-index: $(CS61A_DST)/index.html

$(CS61A_DST)/index.html: cs61a/index.md $(CS61A_INDEX) $(BASE_TEMPLATE)
	$(COMPILE) -m -s $< -d $@ $(notdir $(CS61A_INDEX))

SUBDIRS=review notes
-include $(SUBDIRS:%=cs61a/%/Makefile)
