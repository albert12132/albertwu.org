COMPILE=templar compile
PORT=8000
BASE_TEMPLATE=templates/base.html

# Configure directory for published materials
DST=~/git/website

SUBDIRS=cs61a projects

-include $(SUBDIRS:%=%/Makefile)

all: 404 index assets

##############
# Main pages #
##############

index: $(DST)/index.html
404: $(DST)/404.html

$(DST)/index.html: templates/index.html $(BASE_TEMPLATE)
	$(COMPILE) $(notdir $<) -d $@

$(DST)/404.html: templates/404.html $(BASE_TEMPLATE)
	$(COMPILE) $(notdir $<) -d $@

##########
# Assets #
##########

ASSETS := $(shell python3 -c 'import os;print(*(os.path.join(dir,file) for dir,_,files in os.walk("public") for file in files))')
PUB_ASSETS := $(ASSETS:%=$(DST)/%)

assets: $(PUB_ASSETS)

.SECONDEXPANSION:
$(DST)/public/%: public/% | $$(dir $$@)
	cp -r $< $(dir $@)

$(sort $(dir $(PUB_ASSETS))):
	mkdir -p $@

-include articles/Makefile

################
# View changes #
################

view:
	cd $(DST); python3 -m http.server $(PORT)
