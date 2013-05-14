BASE_PATH=~/public_html
NOTES_PATH=$(BASE_PATH)/notes

COMPILER=../compile.py
NOTES=debugging style_guide tuples

.PHONY: destroy

all:
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(NOTES_PATH) ]; then mkdir $(NOTES_PATH); fi
	cp pdfs/* $(NOTES_PATH)
	for note in $(NOTES) ; do make $$note ; done

%: templates/%.html
	python3 $(COMPILER) $*.html notes.py $(BASE_PATH)/notes/$*.html

destroy:
	rm -rf $(NOTES_PATH)
