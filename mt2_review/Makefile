TEMPLATE_DIR=template
BASIC_Q=$(TEMPLATE_DIR)/basic_q.html
BASIC_S=$(TEMPLATE_DIR)/basic_s.html
EXAM_Q=$(TEMPLATE_DIR)/exam_q.html
EXAM_S=$(TEMPLATE_DIR)/exam_s.html
STARTER=$(TEMPLATE_DIR)/starter.py

TOPICS=lists nonlocal identity dictionaries functions rlists oop below recursion oog trees

$(TOPICS):
	mkdir $@ $@/basic $@/exam
	cp $(BASIC_Q) $(BASIC_S) $(STARTER) $@/basic
	cp $(EXAM_Q) $(EXAM_S) $(STARTER) $@/exam

clean-%: %
	if [ -d $< ] ; then rm -rf $< ; fi

clean-all:
	rm -rf $(TOPICS)

		

