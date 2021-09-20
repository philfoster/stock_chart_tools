PYTHON=python3
PIP=pip3

MODULE_NAME=stock_chart_tools
DIST_DIR=dist
BUILD_DIR=build

CLEAN_TARGETS=${DIST_DIR} ${BUILD_DIR} *.egg-info
.PHONY: dist

all:
	@echo "Targets:"
	@echo "    init      - install the requirements"
	@echo "    install   - install this module"
	@echo "    dist      - create the distribution file"
	@echo "    clean     - clean up"
	@echo "    uninstall - uninstall this module"

init:
	${PIP} install -r requirements.txt

install:
	${PIP} install --upgrade .

dist:
	${PYTHON} setup.py sdist bdist_wheel

clean:
	rm -rf ${CLEAN_TARGETS}

uninstall: 
	pip3 uninstall -y ${MODULE_NAME}
