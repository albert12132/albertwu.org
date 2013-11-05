BASE_PATH=~/public_html
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
	python3 to_template.py $< tmp.py
	python3 $(COMPILER) -c tmp.py notes.html $(BASE_PATH)/notes/$*.html
	rm tmp.py

pdfs:
	cp -r pdfs/* $(NOTES_PATH)

destroy:
	rm -rf $(NOTES_PATH)
