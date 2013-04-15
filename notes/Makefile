TEMPLATE_DIR=template
BASIC_Q=$(TEMPLATE_DIR)/basic_q.html
BASIC_S=$(TEMPLATE_DIR)/basic_s.html
EXAM_Q=$(TEMPLATE_DIR)/exam_q.html
EXAM_S=$(TEMPLATE_DIR)/exam_s.html
STARTER=$(TEMPLATE_DIR)/starter.py

BASE_PATH=~/public_html
NOTES_PATH=$(BASE_PATH)/notes

COMPILER=../compile.py
NOTES=debugging style_guide tuples

all:
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(NOTES_PATH) ]; then mkdir $(NOTES_PATH); fi
	cp pdfs/* $(NOTES_PATH)
	for note in $(NOTES) ; do make $$note ; done

%: templates/%.html
	python3 $(COMPILER) $*.html notes.py $(BASE_PATH)/notes/$*.html

clean:
	rm $(NOTES_PATH)/*
