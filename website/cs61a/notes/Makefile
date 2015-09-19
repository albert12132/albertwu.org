NOTES_DST=$(CS61A_DST)/notes
NOTES=$(wildcard cs61a/notes/contents/*.md)

all: notes

notes: $(NOTES:cs61a/notes/contents/%.md=$(NOTES_DST)/%.html)

$(NOTES_DST)/%.html: cs61a/notes/contents/%.md templates/article.html
	templar -c cs61a/notes compile -m -s $< article.html -d $@

