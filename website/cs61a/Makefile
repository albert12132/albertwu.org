BASE_PATH=~/git/website/cs61a
# Set publish path here

COMPILER=templar compile -m
TEMPLATE_DIR=templates

# define targets below

all:
	make pub-index
	make pub-assets

pub-index: index.md $(TEMPLATE_DIR)/index.html
	$(COMPILER) -s index.md cs61a:index.html -d $(BASE_PATH)/index.html

pub-assets: public
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	cp -r public $(BASE_PATH)

