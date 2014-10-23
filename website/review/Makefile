BASE_PATH=~/git/website/cs61a
REVIEW_PATH=$(BASE_PATH)/review

COMPILER=templar compile -m

INDEX_TEMP=main.html
Q_TEMP=question.html
Q_PY=templates/question.py

MT1_TOPICS=hof lambdas environments control newtons recursion tuples
MT2_TOPICS=abstraction linked-lists lists dictionaries functions identity nonlocal oop below special generic oop-linked-lists trees oog scheme
FINAL_TOPICS=interpreter tail iterators streams dynamic logic final_review

TOPICS=$(MT1_TOPICS) $(MT2_TOPICS) $(FINAL_TOPICS)

.PHONY: pub-assets all all-mt1 all-mt2 all-final destroy

all:
	make index-index
	make all-mt1
	make all-mt2
	make all-final
	make pub-assets

pub-assets:
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(REVIEW_PATH) ]; then mkdir $(REVIEW_PATH); fi
	cp -r public $(REVIEW_PATH)

all-mt1:
	make index-mt1
	for topic in $(MT1_TOPICS); do \
		if [ -d contents/$$topic ]; then \
			make pub-$$topic; \
		fi; \
	done

all-mt2:
	make index-mt2
	for topic in $(MT2_TOPICS); do \
		if [ -d contents/$$topic ]; then \
			make pub-$$topic; \
		fi; \
	done

all-final:
	make index-final
	for topic in $(FINAL_TOPICS); do \
		if [ -d contents/$$topic ]; then \
			make pub-$$topic; \
		fi; \
	done

index-%: indices/%.md
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(REVIEW_PATH) ]; then mkdir $(REVIEW_PATH); fi
	$(COMPILER) -s $< $(INDEX_TEMP) -d $(REVIEW_PATH)/$*.html

pub-%: contents/%
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(REVIEW_PATH) ]; then mkdir $(REVIEW_PATH); fi
	if [ -d $(REVIEW_PATH)/$* ]; then rm -rf $(REVIEW_PATH)/$*; fi
	mkdir $(REVIEW_PATH)/$*
	if [ -f $</basic.md ]; then \
		$(COMPILER) -s $</basic.md $(Q_TEMP) -d $(REVIEW_PATH)/$*/basic.html; fi
	if [ -f $</exam.md ]; then \
		$(COMPILER) -s $</exam.md $(Q_TEMP) -d $(REVIEW_PATH)/$*/exam.html; fi
	if [ -d $</assets/ ] ; then \
		cp $</assets/* $(REVIEW_PATH)/$*/ ; fi

$(TOPICS):
	if [ -d contents/$@ ]; then rm -rf contents/$@; fi
	mkdir contents/$@ contents/$@/basic contents/$@/exam contents/$@/basic/assets contents/$@/exam/assets
	cp $(Q_PY) contents/$@/basic.md
	cp $(Q_PY) contents/$@/exam.md
