collection := $(notdir $(realpath $(CURDIR)      ))
namespace  := $(notdir $(realpath $(CURDIR)/..   ))
toplevel   := $(notdir $(realpath $(CURDIR)/../..))

err_msg := Place collection at <WHATEVER>/ansible_collections/gurv/vg
ifneq (vg,$(collection))
  $(error $(err_msg))
else ifneq (gurv,$(namespace))
  $(error $(err_msg))
else ifneq (ansible_collections,$(toplevel))
  $(error $(err_msg))
endif

export ANSIBLE_COLLECTIONS_PATHS ?= $(realpath $(CURDIR)/../../..)

python_version := $(shell \
  python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))' \
)


.PHONY: help
help:
	@echo Available targets:
	@fgrep "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sort

.PHONY: requirements
requirements:
	pip install \
	  -r sanity.requirements \
	  -r units.requirements \
	  -r integration.requirements \
	  -r docs.requirements

.PHONY: sanity
sanity:
	flake8
	ansible-lint -p roles/*
	ansible-test sanity --python $(python_version)

.PHONY: units
units:
	-ansible-test coverage erase # On first run, there is nothing to erase.
	ansible-test units --python $(python_version) --coverage
	# FIXME ERROR: 'CoverageData' object has no attribute 'read_file'
	#     https://github.com/ansible/ansible/issues/65907
	#     https://github.com/ansible/ansible/pull/65999
	# ansible-test coverage html

.PHONY: integration
integration:
	$(MAKE) -C tests/integration $(CI)

.PHONY: docs
docs:
	$(MAKE) -C docs -f Makefile.custom docs

.PHONY: clean
clean:
	$(MAKE) -C docs -f Makefile.custom clean
