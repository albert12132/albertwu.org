REVIEW_DST=$(CS61A_DST)/review
REVIEW_TOPICS=$(wildcard cs61a/review/topics/*/*.md)
REVIEW_INDEX=$(basename $(notdir $(wildcard cs61a/review/index/*)))

REVIEW_TEMPLATE=cs61a/review/templates/review.html templates/sidebar-base.html templates/base.html
REVIEW_MAIN_TEMPLATE=cs61a/review/templates/main.html templates/base.html
REVIEW_CONFIG=cs61a/review/config.py config.py

all: review

review: $(REVIEW_TOPICS:cs61a/review/topics/%.md=$(REVIEW_DST)/%.html) $(REVIEW_INDEX:%=$(REVIEW_DST)/%.html)

$(REVIEW_DST)/%.html: cs61a/review/index/%.md $(REVIEW_MAIN_TEMPLATE) $(REVIEW_CONFIG)
	templar -c cs61a/review compile -m -s $< main.html -d $@

$(REVIEW_DST)/%/basic.html: cs61a/review/topics/%/basic.md $(REVIEW_TEMPLATE) $(REVIEW_CONFIG)
	templar -c cs61a/review compile -m -s $< review.html -d $@

$(REVIEW_DST)/%/exam.html: cs61a/review/topics/%/exam.md $(REVIEW_TEMPLATE) $(REVIEW_CONFIG)
	templar -c cs61a/review compile -m -s $< review.html -d $@
