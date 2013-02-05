BASE_PATH=~/public_html/mt1_review
TEMPLATE_DIR=template

INDEX=index.html
STYLE=$(TEMPLATE_DIR)/style.css

QUESTION=question
SOLUTION=solution

Q_TEMP=$(TEMPLATE_DIR)/$(QUESTION).html
S_TEMP=$(TEMPLATE_DIR)/$(SOLUTION).html
Q_PY=$(TEMPLATE_DIR)/$(QUESTION).py
S_PY=$(TEMPLATE_DIR)/$(SOLUTION).py

PACKAGE=$(TEMPLATE_DIR)/__init__.py

TOPICS=environments control hof lambda newton

all:
	make main
	for topic in $(TOPICS) ; do make recompile-$$topic; done

main:
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	cp $(INDEX) $(STYLE) $(BASE_PATH)


$(TOPICS):
	mkdir $@ $@/basic $@/exam
	cp $(PACKAGE) $@
	cp $(Q_PY) $(S_PY) $(PACKAGE) $@/basic
	cp $(Q_PY) $(S_PY) $(PACKAGE) $@/exam

reload-%: %
	rm -rf $<
	make $<

compile-%: %
	if [ ! -d $< ]; then echo "No such directory"; exit 1; fi
	if [ ! -d $(BASE_PATH) ]; then mkdir $(BASE_PATH); fi
	mkdir $(BASE_PATH)/$< $(BASE_PATH)/$</basic $(BASE_PATH)/$</exam
	python3 compile.py $(Q_TEMP) $</basic/$(QUESTION).py $(BASE_PATH)
	python3 compile.py $(S_TEMP) $</basic/$(SOLUTION).py $(BASE_PATH)
	python3 compile.py $(Q_TEMP) $</exam/$(QUESTION).py $(BASE_PATH)
	python3 compile.py $(S_TEMP) $</exam/$(SOLUTION).py $(BASE_PATH)

recompile-%: %
	make clean-$<
	make compile-$<

clean-%: %
	if [ -d $(BASE_PATH)/$< ] ; then rm -rf $(BASE_PATH)/$< ; fi

clean-all:
	rm -rf $(BASE_PATH)


