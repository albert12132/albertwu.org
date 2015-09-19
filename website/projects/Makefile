PROJECT_DST=$(DST)/projects
PROJECT_TEMPLATE = projects/templates/project.html templates/base.html
PROJECT_CONFIG = projects/config.py config.py

all: projects

projects: $(PROJECT_DST)/index.html

$(PROJECT_DST)/index.html: projects/templates/project.html $(PROJECT_CONFIG)
	templar compile -m project.html -d $@
