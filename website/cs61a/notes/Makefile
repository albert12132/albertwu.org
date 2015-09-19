NOTES_DST=$(CS61A_DST)/notes
NOTES=$(wildcard cs61a/notes/contents/*.md)
NOTES_CONFIG=cs61a/notes/config.py config.py
NOTES_TEMPLATE=templates/article.html templates/sidebar-base.html templates/base.html

all: notes

notes: $(NOTES:cs61a/notes/contents/%.md=$(NOTES_DST)/%.html)

$(NOTES_DST)/%.html: cs61a/notes/contents/%.md $(NOTES_TEMPLATE) $(NOTES_CONFIG)
	templar -c cs61a/notes compile -m -s $< article.html -d $@

