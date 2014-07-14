BASE_PATH=~/git/website
BLOG_PATH=$(BASE_PATH)/blog
INDEX_TEMP=blog-index.html

COMPILER=../compile.py

all:
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(BLOG_PATH) ]; then mkdir $(BLOG_PATH); fi
	make index
	make pub-assets
	for note in $$(ls contents | sed 's/\.md//') ; do make $$note ; done

index:
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(BLOG_PATH) ]; then mkdir $(BLOG_PATH); fi
	python3 $(COMPILER) -c index.py $(INDEX_TEMP) $(BLOG_PATH)/index.html

pub-assets:
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(BLOG_PATH) ]; then mkdir $(BLOG_PATH); fi
	cp -r public $(BLOG_PATH)

%: contents/%.md
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(BLOG_PATH) ]; then mkdir $(BLOG_PATH); fi
	python3 to_template.py $< $*.py
	python3 $(COMPILER) -c $*.py blog-article.html $(BLOG_PATH)/$*.html
	rm $*.py
