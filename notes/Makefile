BASE_PATH=~/public_html
NOTES_PATH=$(BASE_PATH)/notes

COMPILER=../compile.py
NOTES=debugging style_guide tuples

MARKDOWN=markdown2.py --extras=header-ids
TEMP_CREATE=to_template.py


.PHONY: destroy pdfs

all:
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(NOTES_PATH) ]; then mkdir $(NOTES_PATH); fi
	cp pdfs/* $(NOTES_PATH)
	for note in $(NOTES) ; do make $$note ; done

pub-assets:
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(NOTES_PATH) ]; then mkdir $(NOTES_PATH); fi
	cp -r public $(NOTES_PATH)



%: contents/%.md
	cd ..; notes/$(MARKDOWN) notes/$< | python3 notes/$(TEMP_CREATE) > notes/templates/tmp.html
	python3 $(COMPILER) tmp.html notes.py $(BASE_PATH)/notes/$*.html
	rm templates/tmp.html

pdfs: pdfs
	cp -r pdfs $(NOTES_PATH)

destroy:
	rm -rf $(NOTES_PATH)
