TEMPLATE_DIR=templates

BASE_PATH=~/public_html
COMPILER=compile.py

pub-assets: public
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	cp -r public $(BASE_PATH)

pub-index: index.py $(TEMPLATE_DIR)/index.html
	python3 $(COMPILER) index.html $< $(BASE_PATH)/index.html

destroy:
	rm -rf $(BASE_PATH)

