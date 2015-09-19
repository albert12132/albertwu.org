PROJECT_DST=$(DST)/projects

all: projects

projects: $(PROJECT_DST)/index.html

$(PROJECT_DST)/index.html: projects/templates/project.html
	templar compile -m project.html -d $@
