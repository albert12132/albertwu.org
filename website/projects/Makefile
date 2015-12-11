PROJECT_DST=$(DST)/projects
PROJECT_TEMPLATE = projects/templates/project.html templates/base.html
PROJECT_CONFIG = projects/config.py base_config.py

all: projects

projects: $(PROJECT_DST)/index.html

$(PROJECT_DST)/index.html: projects/index.md $(PROJECT_TEMPLATE) $(PROJECT_CONFIG)
	templar -c projects/config.py -t project.html -s $< -d $@
