COMPILER=compile.py
TEMPLATE_DIR=templates

# Configure directory for publsihed materials
BASE_PATH=~/public_html

# Add apps to following
APPS=review notes

.PHONY: pub-all pub-assets pub-index pub-clean

pub-all:
	make pub-assets
	make pub-index
	for app in $(APPS) ; do \
		cd $$app; \
		make all; \
		cd ..; \
	done \

pub-assets: public
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	cp -r public $(BASE_PATH)

pub-clean:
	rm -rf $(BASE_PATH)

pub-index: index.py $(TEMPLATE_DIR)/index.html
	python3 $(COMPILER) -c $< index.html $(BASE_PATH)/index.html

app-%: .example_app
	cp -r .example_app $*

local_config.py: .local_config.py.example
	cp .local_config.py.example local_config.py
