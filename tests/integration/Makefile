modules   := $(wildcard molecule/module_*)
roles     := $(wildcard molecule/role_*)
actions   := $(wildcard molecule/action_*)
scenarios := $(modules) $(roles) $(actions)

export ANSIBLE_COLLECTIONS_PATHS ?= $(realpath $(CURDIR)/../../../../..)

.PHONY: all
all: $(scenarios)

.PHONY: modules
modules: $(modules)

.PHONY: roles
roles: $(roles)

.PHONY: actions
actions: $(actions)

.PHONY: $(modules) $(roles) $(actions)
$(modules) $(roles) $(actions):
	molecule -c base.yml test --parallel -s $(notdir $@)
