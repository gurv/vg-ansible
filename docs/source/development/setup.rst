Подготовка окружения
====================

Предварительные требования
--------------------------

Linux
^^^^^

Должны быть установлены:

  * python (версия не менее 3.3),
  * ``git``.

Windows
^^^^^^^

Установить ``MSYS2`` (например, http://repo.msys2.org/distrib/x86_64/msys2-x86_64-20190524.exe).

Запустить msys2.exe и выполнить 
:download:`скрипт <../../examples/installation/install-ansible-on-msys2.sh>`
установки Ansible:

.. literalinclude:: ../../examples/installation/install-ansible-on-msys2.sh
   :language: bash

Загрузка исходного кода
-----------------------

Выполнить::

   $ mkdir -p ansible_collections/gurv
   $ cd ansible_collections/gurv
   $ git clone git@github.com:gurv/vg-ansible.git vg
   $ cd vg

Установка инструментов разработки
---------------------------------

Создать виртуальное окружение и активировать его::

   $ python3 -m venv ../../../venv
   $ . ../../../venv/bin/activate


Установить Ansible::

   (venv) $ pip install ansible

Установить зависимости::

   (venv) $ make requirements


Проверка
--------

Для проверки можно выполнить тесты и собрать документацию::

   (venv) $ make sanity
   (venv) $ make units
   (venv) $ make docs
   (venv) $ make -j4 integration

.. note::

   При работе под Windows выявлены следующие проблемы:
   
     * make sanity
     
     ::

       ERROR: plugins/modules/aur.py:0:0: module should not be executable

     * make units

     ::

       /tmp/python-aiyj2d6k-ansible/python: Error while finding module specification for 'coverage.__main__' (ModuleNotFoundError: No module named 'coverage')
       ERROR: Command "pytest --boxed -r a -n auto --color yes -p no:cacheprovider -c /c/prj/venv/lib/python3.7/site-packages/ansible_test/_data/pytest.ini --junit-xml
       /c/prj/ansible_collections/gurv/vg/tests/output/junit/python3.7-units.xml --strict-markers tests/unit/module_utils/test_utils.py" returned exit status 1.
       make: *** [Makefile:43: units] Ошибка 1
