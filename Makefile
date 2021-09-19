PYTHON=python3
PIP=pip3

MODULE_NAME=stock_chart_tools
DIST_DIR=dist
CLEAN_TARGETS=${DIST_DIR} *.egg-info

all:
	@echo "Targets:"
	@echo "    init    - install the requirements"
	@echo "    install - install this module"
	@echo "    dist    - create the distribution file"
	@echo "    clean   - clean up"

init:
	${PIP} install -r requirements.txt

install:
	${PIP} install --upgrade .

dist:
	${PYTHON} setup.py sdist

clean:
	rm -rf ${CLEAN_TARGETS}

uninstall: 
	pip3 uninstall -y ${MODULE_NAME}
