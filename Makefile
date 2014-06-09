COMPILER=templar compile
TEMPLATE_DIR=templates

# Configure directory for published materials
BASE_PATH=~/git/website

# Add apps to following
APPS=cs61a review notes

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
	cp -rL public $(BASE_PATH)

pub-index: $(TEMPLATE_DIR)/index.html
	python3 $(COMPILER) index.html -d $(BASE_PATH)/index.html

pub-404: $(TEMPLATE_DIR)/404.html
	python3 $(COMPILER) 404.html -d $(BASE_PATH)/404.html

app-%: .example_app
	cp -r .example_app $*

