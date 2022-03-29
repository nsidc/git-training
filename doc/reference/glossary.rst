Glossary
========

..
  This document should be written to supplement the official Git glossary. This document
  should focus on helping people understand or remember concepts, e.g. metaphors,
  mnemonics.

Some of these terms are Git-specific, and some of them are more generic
version-control terms.

.. note:: Check out the official glossary, too!

  The official Git glossary can be viewed by running the command :code:`man gitglossary`
  or viewing https://git-scm.com/docs/gitglossary


.. glossary::

  Version Control System
    A Version Control System (VCS) enables you to track different versions of data (e.g.
    code, notes, documentation) as they change.

    Git is only one example of a program for version-controlling data. Others include
    CVS, Subversion, Mercurial, Bazaar. Git has become the most popular thanks to its
    extreme flexibility and efficiency.


  Distributed Version Control System
    In a "centralized" VCS, everyone must push to and pull from one central repository.
    One downside of this approach is the single point-of-failure that central repository
    or server represents.

    Git is a "Distributed" Version Control System (DVCS). This means that all copies of
    a repository are considered equal in Git's eyes. There is no such thing as a
    "client" repository or "server" repository. You can push to and pull from a
    co-worker's repository if you want. Or you can create many clones of a repo on your
    laptop and push and pull between them arbitrarily.


  Object
    A unique "thing" in Git' internal storage. Each object has a unique identifier
    called a :term:`hash<Hash>`.

    See :doc:`/discussion/git-internals` for more.


  Hash
    A long string generated deterministically from the contents of an
    :term:`object<Object>`.

    Hashes can be abbreviated with the first 5+ characters.


  Commit
    An :term:`object<Object>` representing a snapshot of your repository. Includes
    metadata such as the author of the changes leading to the snapshot, the date the
    commit was performed, and a message describing the changes.

    See :doc:`/discussion/git-internals` for more.


  Ref
    A name representing a pointer to an oject or to another ref.


  Branch
    A type of :term:`ref<Ref>` that, once created, automatically advances with each child
    commit added.

    You can think of a branch as creating an independent or alternate timeline, like
    when a Star Trek episode needs to violate previously-established rules. When the
    branch is created, you can start making changes that only affect that branch. When
    you merge a branch, you can bring those changes back to the home "timeline".

    These are great for keeping changes independent, for example:

    - Preserving a branch, e.g. the :code:`main` branch, as a known-good codebase
    - Avoiding conflict with or disruption from your colleagues' work


  Tag
    A type of :term:`ref<Ref>` that does not move after being created (unless explicitly
    forced).

    These are great for marking a point in time that you care about, for example:

    - Each versioned release: :code:`v1.2.3`
    - A temporary marker for a known-good version: :code:`i-know-this-works`


  File state
    A file can be in one of four states:

    - Untracked: Git doesn't know or care about this file at all. It's not in the
      :term:`History`. It shows up in the "Untracked" section in red in :code:`git
      status` (or not at all if the file matches an ignore rule).
    - Unmodified: A file that is committed to the repository (i.e. in the
      :term:`History`), but doesn't have any local modifications. It will not appear in
      :code:`git status`.
    - Modified: A file that is committed to the repository (i.e. in the
      :term:`History`), and has been locally modified. It will appear in the "Changes
      not staged for commit" section in red in :code:`git status`.
    - Staged: A file that is committed to the repository, has been locally modified, and
      has been added to the :term:`Staging area` (using :code:`git add`). It will show
      up in the "Changes to be committed" section in green in :code:`git status`.
      :code:`git commit` will create a new :term:`commit<Commit>` from all staged files.
    
    See :doc:`/discussion/file-state` for more.


  History
    A collection of :term:`commits<Commit>`, each linked by reference(s) to parent
    commit(s).

    Git's history is sometimes called a "tree" because each commit is linked to at least
    one parent, forming a tree shape. A "leaf" commit has no children, and the "root"
    commit has no parents. However, the term "tree" also refers to a specific type of
    Git object, so it is not a good term to use to refer to the history. A "tree" is
    also not a good metaphor because the branches of a tree do not normally merge.

    The History is actually in the form of a `Directed Acyclic Graph
    (DAG) <https://en.wikipedia.org/wiki/Directed_acyclic_graph>`_.

    The History exists entirely in the :code:`.git/` directory of your repository and is
    managed by `git` commands.

    See :doc:`/discussion/git-internals` and :doc:`/discussion/file-state` for more.


  Working tree
    In a git repository, the files on that you edit are called the "working tree". In
    other words, everything _except_ the :code:`.git/` directory is the working tree.

    When you edit a file in your working tree, the working tree is considered "dirty".
    It's considered clean when there are no changes in the working tree compared to the
    currently checked-out ref.

    Working trees are entirely independent of the actual repository's state, so it's
    possible to have any number of working trees associated with a Git repository,
    including zero (this is called a "bare" repository)!

    See :doc:`/discussion/file-state` for more.


  Staging area
    The "staging area" is where your changes are prepared for a commit. They are added
    to the staging area with :code:`git add`. Once the staging area is ready, you turn
    it into a :term:`commit<Commit>` with :code:`git commit`.

    Also sometimes refered to as the "Index" or "Cache" in Git's documentation and
    commands.

    See :doc:`/discussion/file-state` for more.


  Checkout
    When you "checkout" a :term:`commit<Commit>` or :term:`ref<Ref>`, Git is updating
    your :term:`Working Tree` to reflect point in the :term:`History`. Once you've
    checked out, you can now open a file in an editor and see its contents at that point
    of the history and work on it.

    You can perform a checkout with the :code:`git switch` (recommended) or :code:`git
    checkout` (legacy) commands.


  Remote
    A "remote" is just a copy of a git repository living on another computer (for
    the purposes of this course) that is accessible using the Git protocol. In
    other words, it's another repository that you can talk to using the `git`
    Command Line Interface (CLI). That other repository can be somewhere on
    your computer, or it could be online (e.g. on GitHub or Bitbucket).

    When you clone a repository, a remote is created called `origin` that
    points at the original repository you cloned.

    GitHub and BitBucket are just hosting a copy of your repository that you
    can treat as your "source-of-truth".
