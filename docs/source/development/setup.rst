Подготовка окружения
====================

Предварительные требования
--------------------------

Уже должно быть:

  * python (версия не менее 3.3),
  * ``git``.

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
