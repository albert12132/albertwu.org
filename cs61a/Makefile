BASE_PATH=~/git/website/cs61a
# Set publish path here

COMPILER=../compile.py
TEMPLATE_DIR=templates

# define targets below

all:
	make pub-index

pub-index: index.py $(TEMPLATE_DIR)/index.html
	python3 $(COMPILER) -c $< cs61a:index.html $(BASE_PATH)/index.html

pub-assets: public
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	cp -r public $(BASE_PATH)

