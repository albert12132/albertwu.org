BASE_PATH=~/public_html
REVIEW_PATH=$(BASE_PATH)/review

MT1=$(BASE_PATH)/mt1_review
MT2=$(BASE_PATH)/mt2_review
FINAL=$(BASE_PATH)/final_review

COMPILER=../compile.py

INDEX_TEMP=main.html
Q_TEMP=question.html
S_TEMP=solution.html
Q_PY=templates/question.py

PACKAGE=templates/__init__.py

MT1_TOPICS=hof lambdas environments control
MT2_TOPICS=tuples lists rlists functions dictionaries identity nonlocal oop below
FINAL_TOPICS=trees oog scheme interpreter iterators streams dynamic

TOPICS=$(MT1_TOPICS) $(MT2_TOPICS) $(FINAL_TOPICS)

assets:
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(REVIEW_PATH) ]; then mkdir $(REVIEW_PATH); fi
	cp -r public $(REVIEW_PATH)

mt1:
	make index-mt1
	for topic in $(MT1_TOPICS); do \
		if [ -d $$topic ]; then \
			make publish-$$topic; \
		fi; \
	done

mt2:
	make index-mt2
	for topic in $(MT2_TOPICS); do \
		if [ -d $$topic ]; then \
			make publish-$$topic; \
		fi; \
	done

final:
	make index-final
	for topic in $(FINAL_TOPICS); do \
		if [ -d $$topic ]; then \
			make publish-$$topic; \
		fi; \
	done

index-%: %.py
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(REVIEW_PATH) ]; then mkdir $(REVIEW_PATH); fi
	python3 $(COMPILER) $(INDEX_TEMP) $< $(REVIEW_PATH)/$*.html

publish-%: %
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(REVIEW_PATH) ]; then mkdir $(REVIEW_PATH); fi
	if [ -d $(REVIEW_PATH)/$< ]; then rm -rf $(REVIEW_PATH)/$<; fi
	mkdir $(REVIEW_PATH)/$< $(REVIEW_PATH)/$</basic $(REVIEW_PATH)/$</exam
	python3 $(COMPILER) $(Q_TEMP) $</basic/question.py $(REVIEW_PATH)/$</basic/$(Q_TEMP)
	python3 $(COMPILER) $(S_TEMP) $</basic/question.py $(REVIEW_PATH)/$</basic/$(S_TEMP)
	python3 $(COMPILER) $(Q_TEMP) $</exam/question.py $(REVIEW_PATH)/$</exam/$(Q_TEMP)
	python3 $(COMPILER) $(S_TEMP) $</exam/question.py $(REVIEW_PATH)/$</exam/$(S_TEMP)

$(TOPICS):
	if [ -d $@ ]; then rm -rf $@; fi
	mkdir $@ $@/basic $@/exam
	cp $(PACKAGE) $@
	cp $(Q_PY) $(PACKAGE) $@/basic
	cp $(Q_PY) $(PACKAGE) $@/exam

clean-mt1:
	rm -rf $(MT1)/*

clean-mt2:
	rm -rf $(MT2)/*

clean-final:
	rm -rf $(FINAL)/*

