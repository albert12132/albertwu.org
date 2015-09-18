REVIEW_DST=$(CS61A_DST)/review
REVIEW_TOPICS=$(wildcard cs61a/review/topics/*/*.md)
REVIEW_INDEX=$(basename $(notdir $(wildcard cs61a/review/index/*)))

INDEX_TEMP=main.html
Q_TEMP=question.html

all: review

review: $(REVIEW_TOPICS:cs61a/review/topics/%.md=$(REVIEW_DST)/%.html) $(REVIEW_INDEX:%=$(REVIEW_DST)/%.html)

$(REVIEW_DST)/%.html: cs61a/review/index/%.md cs61a/review/templates/main.html
	templar -c cs61a/review compile -m -s $< main.html -d $@

$(REVIEW_DST)/%/basic.html: cs61a/review/topics/%/basic.md cs61a/review/templates/basic.html
	templar -c cs61a/review compile -m -s $< basic.html -d $@

$(REVIEW_DST)/%/exam.html: cs61a/review/topics/%/exam.md cs61a/review/templates/exam.html
	templar -c cs61a/review compile -m -s $< exam.html -d $@

