.PHONY: doc

all: build

build:
	python setup.py build

install:
	python setup.py install

test:
	pytest

clean:
	find . -name \*.pyc -print0 | xargs -0 rm -f
	find . -name \*~ -print0 | xargs -0 rm -f
	find . -name __pycache__ -type d -print0 | xargs -0 rm -rf
	-python setup.py clean
	rm -rf suricatactl.egg*
	rm -rf build dist MANIFEST

sdist:
	python setup.py sdist

sdist-upload:
	python setup.py sdist upload
