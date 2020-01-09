Документирование
================

Публикация документации
-----------------------

`Документация`_ размещена на `GitHub Pages`_.

Выполнить::

    (venv) $ make docs
    (venv) $ git worktree add gh-pages gh-pages
    (venv) $ rm -rf gh-pages/*
    (venv) $ cp -r docs/build/html/* gh-pages
    (venv) $ cp -r docs/.nojekyll gh-pages
    (venv) $ cd gh-pages
    (venv) $ git add . && git commit -m "Generate documentation for release 0.1.0"
    (venv) $ git push origin gh-pages
    (venv) $ cd ..
    (venv) $ git worktree remove gh-pages

.. _Документация: https://gurv.github.io/vg-ansible/
.. _GitHub Pages: https://pages.github.com/
