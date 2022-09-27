..
    The "main" or "root" table of contents tree.
.. toctree::
    :maxdepth: 1
    :hidden:

    acknowledgements.md


..
    The four categories of documentation according to Diataxis: Tutorials, How-tos,
    Reference, and Discussion:

.. toctree::
    :name: Tutorials
    :caption: Tutorials
    :maxdepth: 1
    :numbered:
    :hidden:

    tutorial/1b-intro-to-git-cli/index.rst
    tutorial/working-with-others/index.rst


.. toctree::
    :name: How-to
    :caption: How-to
    :maxdepth: 1
    :hidden:

    how-to/help.md
    how-to/create-or-copy.md
    how-to/make-changes.md
    how-to/comparison.md
    how-to/branch-and-merge.md
    how-to/checkout.md
    how-to/share-changes.md


.. toctree::
    :name: Reference
    :caption: Reference
    :maxdepth: 1
    :hidden:
    :glob:

    reference/*


.. toctree::
    :name: Discussion
    :caption: Discussion
    :maxdepth: 1
    :hidden:
    :glob:

    discussion/*


..
    Add the contents of `home.rst` to this page.
.. include:: home.rst
