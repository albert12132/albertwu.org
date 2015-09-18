COMPILE=templar compile
TEMPLATE_DIR=templates
PORT=8000

# Configure directory for published materials
DST=~/git/website

SUBDIRS=cs61a review notes

all: index assets
-include $(SUBDIRS:%=%/Makefile)

##############
# Main pages #
##############

index: $(DST)/index.html
404: $(DST)/404.html

$(DST)/index.html: templates/index.html templates/base.html
	$(COMPILE) $(notdir $<) -d $@

$(DST)/404.html: templates/404.html templates/base.html
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
