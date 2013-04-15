TEMPLATE_DIR=template
BASIC_Q=$(TEMPLATE_DIR)/basic_q.html
BASIC_S=$(TEMPLATE_DIR)/basic_s.html
EXAM_Q=$(TEMPLATE_DIR)/exam_q.html
EXAM_S=$(TEMPLATE_DIR)/exam_s.html
STARTER=$(TEMPLATE_DIR)/starter.py

BASE_PATH=~/public_html
COMPILER=compile.py

assets:
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	cp -r public $(BASE_PATH)

index: index.py
	python3 $(COMPILER) index.html $< $(BASE_PATH)/index.html

main:
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -f index.html ]; then echo 'index.html is missing'; \
		else cp index.html $(BASE_PATH); fi
	if [ ! -f style.css ]; then echo 'style.css is missing'; \
		else cp style.css $(BASE_PATH); fi
	if [ ! -d prettify ]; then echo 'prettify is missing'; \
		else cp -r prettify $(BASE_PATH); fi
cp-notes:
	if [ ! -d notes ]; then echo "No notes"; exit 1; fi
	cp -r notes $(BASE_PATH)

clean-%: %
	if [ -d $(BASE_PATH)/$< ] ; then rm -rf $< ; fi

clean-all:
	rm -rf $(BASE_PATH)

