TEMPLATE_DIR=templates

BASE_PATH=~/public_html
COMPILER=compile.py

APPS=review notes

.PHONY: pub-assets pub-index destroy

all:
	make pub-assets
	make pub-index
	for app in $(APPS) ; do \
		cd $$app; \
		make all; \
		cd ..; \
	done \

local_config.py: .local_config.py.example
	cp .local_config.py.example local_config.py

pub-assets: public
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	cp -r public $(BASE_PATH)

pub-index: index.py $(TEMPLATE_DIR)/index.html
	python3 $(COMPILER) index.html $< $(BASE_PATH)/index.html

app-%: .example_app
	cp -r .example_app $*

destroy:
	rm -rf $(BASE_PATH)

