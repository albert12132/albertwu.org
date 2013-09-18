BASE_PATH=~/public_html
REVIEW_PATH=$(BASE_PATH)/review

COMPILER=../compile.py

INDEX_TEMP=main.html
Q_TEMP=question.html
S_TEMP=solution.html
Q_PY=templates/question.py

PACKAGE=templates/__init__.py

MT1_TOPICS=hof lambdas environments control newtons recursion
MT2_TOPICS=abstraction rlists tuples lists dictionaries functions identity nonlocal oop below special generic mut_rlists trees oog scheme
FINAL_TOPICS=interpreter tail iterators streams dynamic logic

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

index-%: indices/%.py
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(REVIEW_PATH) ]; then mkdir $(REVIEW_PATH); fi
	python3 $(COMPILER) -c $< $(INDEX_TEMP) $(REVIEW_PATH)/$*.html

pub-%: contents/%
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(REVIEW_PATH) ]; then mkdir $(REVIEW_PATH); fi
	if [ -d $(REVIEW_PATH)/$* ]; then rm -rf $(REVIEW_PATH)/$*; fi
	mkdir $(REVIEW_PATH)/$* $(REVIEW_PATH)/$*/basic $(REVIEW_PATH)/$*/exam
	python3 $(COMPILER) -c $</basic/question.py $(Q_TEMP) $(REVIEW_PATH)/$*/basic/index.html
	python3 $(COMPILER) -c $</exam/question.py $(Q_TEMP) $(REVIEW_PATH)/$*/exam/index.html
	if [ -d $</basic/assets/ ] ; then \
		cp $</basic/assets/* $(REVIEW_PATH)/$*/basic/ ; fi
	if [ -d $</exam/assets/ ] ; then \
		cp $</exam/assets/* $(REVIEW_PATH)/$*/exam/ ; fi

$(TOPICS):
	if [ -d contents/$@ ]; then rm -rf contents/$@; fi
	mkdir contents/$@ contents/$@/basic contents/$@/exam contents/$@/basic/assets contents/$@/exam/assets
	cp $(PACKAGE) contents/$@
	cp $(Q_PY) $(PACKAGE) contents/$@/basic
	cp $(Q_PY) $(PACKAGE) contents/$@/exam

destroy:
	rm -rf $(REVIEW_PATH)
