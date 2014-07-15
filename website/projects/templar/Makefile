BASE_PATH=~/git/website/projects
PUB_PATH=$(BASE_PATH)/templar

CONTENTS= \
  configuration \
  getting-started \
  markdown \
  misc \
  substitutions \
  index \
  templates \
  # source-files

all: $(CONTENTS)

%: %.md $(PUB_PATH)
	templar compile templar.html -m -s $*.md -d $(PUB_PATH)/$*.html

$(PUB_PATH):
	mkdir -p $(PUB_PATH)
