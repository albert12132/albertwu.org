BASE_PATH=~/git/website/cs61a
NOTES_PATH=$(BASE_PATH)/notes

COMPILER=../compile.py
NOTES=debugging style_guide indexing git vim vimrc autograder submission environments


.PHONY: destroy pdfs

all:
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(NOTES_PATH) ]; then mkdir $(NOTES_PATH); fi
	make pdfs
	make pub-assets
	for note in $(NOTES) ; do make $$note ; done

pub-assets:
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(NOTES_PATH) ]; then mkdir $(NOTES_PATH); fi
	cp -r public $(NOTES_PATH)

%: contents/%.md
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(NOTES_PATH) ]; then mkdir $(NOTES_PATH); fi
	python3 to_template.py $< $*.py
	python3 $(COMPILER) -c $*.py notes.html $(BASE_PATH)/notes/$*.html
	rm $*.py

pdfs:
	cp -r pdfs/* $(NOTES_PATH)
