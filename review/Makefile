BASE_PATH=~/public_html/
TEMPLATE_DIR=template
MT1=$(BASE_PATH)mt1_review
MT2=$(BASE_PATH)mt2_review
FINAL=$(BASE_PATH)final_review

COMPILER=compile.py

INDEX=index.html
STYLE=$(TEMPLATE_DIR)/style.css

QUESTION=question
SOLUTION=solution

Q_TEMP=$(TEMPLATE_DIR)/$(QUESTION).html
S_TEMP=$(TEMPLATE_DIR)/$(SOLUTION).html
Q_PY=$(TEMPLATE_DIR)/$(QUESTION).py

PACKAGE=$(TEMPLATE_DIR)/__init__.py

MT1_TOPICS=hof lambdas environments control
MT2_TOPICS=tuples lists rlists functions dictionaries identity nonlocal oop below
FINAL_TOPICS=trees oog scheme interpreter iterators streams dynamic

TOPICS=$(MT1_TOPICS) $(MT2_TOPICS) $(FINAL_TOPICS)

mt1: mt1.html
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(MT1) ]; then mkdir $(MT1); fi
	cp mt1.html $(MT1)/index.html
	cp $(STYLE) $(MT1)/style.css
	for topic in $(MT1_TOPICS); do \
		if [ -d $$topic ]; then \
			make mt1-$$topic; \
		fi; \
	done

mt2: mt2.html
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(MT2) ]; then mkdir $(MT2); fi
	cp mt2.html $(MT2)/index.html
	cp $(STYLE) $(MT2)/style.css
	for topic in $(MT2_TOPICS); do \
		if [ -d $$topic ]; then \
			make mt2-$$topic; \
		fi; \
	done

final: final.html
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(FINAL) ]; then mkdir $(FINAL); fi
	cp final.html $(FINAL)/index.html
	cp $(STYLE) $(FINAL)/style.css
	for topic in $(FINAL_TOPICS); do \
		if [ -d $$topic ]; then \
			make final-$$topic; \
		fi; \
	done

mt1-%: %
	if [ ! -d $< ]; then echo "No such directory"; exit 1; fi
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(MT1) ]; then mkdir $(MT1); fi
	if [ -d $(MT1)/$< ]; then rm -rf $(MT1)/$<; fi
	mkdir $(MT1)/$< $(MT1)/$</basic $(MT1)/$</exam
	python3 $(COMPILER) $(Q_TEMP) $</basic/$(QUESTION).py $(MT1)
	python3 $(COMPILER) $(S_TEMP) $</basic/$(QUESTION).py $(MT1)
	python3 $(COMPILER) $(Q_TEMP) $</exam/$(QUESTION).py $(MT1)
	python3 $(COMPILER) $(S_TEMP) $</exam/$(QUESTION).py $(MT1)

mt2-%: %
	if [ ! -d $< ]; then echo "No such directory"; exit 1; fi
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(MT2) ]; then mkdir $(MT2); fi
	if [ -d $(MT2)/$< ]; then rm -rf $(MT2)/$<; fi
	mkdir $(MT2)/$< $(MT2)/$</basic $(MT2)/$</exam
	python3 $(COMPILER) $(Q_TEMP) $</basic/$(QUESTION).py $(MT2)
	python3 $(COMPILER) $(S_TEMP) $</basic/$(QUESTION).py $(MT2)
	python3 $(COMPILER) $(Q_TEMP) $</exam/$(QUESTION).py $(MT2)
	python3 $(COMPILER) $(S_TEMP) $</exam/$(QUESTION).py $(MT2)

final-%: %
	if [ ! -d $< ]; then echo "No such directory"; exit 1; fi
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	if [ ! -d $(FINAL) ]; then mkdir $(FINAL); fi
	if [ -d $(FINAL)/$< ]; then rm -rf $(FINAL)/$<; fi
	mkdir $(FINAL)/$< $(FINAL)/$</basic $(FINAL)/$</exam
	python3 $(COMPILER) $(Q_TEMP) $</basic/$(QUESTION).py $(FINAL)
	python3 $(COMPILER) $(S_TEMP) $</basic/$(QUESTION).py $(FINAL)
	python3 $(COMPILER) $(Q_TEMP) $</exam/$(QUESTION).py $(FINAL)
	python3 $(COMPILER) $(S_TEMP) $</exam/$(QUESTION).py $(FINAL)

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

