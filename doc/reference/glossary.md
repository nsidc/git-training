# Glossary

Some of these terms are git-specific, and some of them are more generic
version-control terms.


## Version Control System (VCS)

Many applications exist for version controlling data files, and Git is only one
of them. It has become the most popular thanks to its extreme flexibility and
featureset.


## Distributed Version Control System (DVCS)

In a "centralized" VCS, everyone must push to and pull from one central
repository.

Git is a "Distributed" Version Control System. This only means that all copies
of a repository are considered equal in Git's eyes. You can push to and pull
from a co-worker's repository if you want. Or you can create many clones of a
repo on your laptop and push and pull between them arbitrarily.


## Commit

A git object (with associated metadata, e.g. author, date, hash, message)
representing a group of changes to files.

See {doc}`/discussion/git-internals` for more.


### Commit hash

A unique identifier generated deterministically for every commit based on the
commit's data and metadata.

See {doc}`/discussion/git-internals` for more.


## History

A collection of commits, each linked by reference(s) to parent commit(s).

Git's history is sometimes called a "tree" because each commit is linked to at
least one parent, forming a tree shape. A "leaf" commit has no children, and
the "root" commit has no parents. However, the term "tree" also refers to a
specific type of Git object, so it is not a good term to use to refer to the
history.


### Ref

A string representing a commit on the tree. A ref can be a `commit` hash, a
pointer (e.g. a tag, branch, or `HEAD`), or an expression (e.g., `HEAD~1`).


### Tag

TODO


### Branch

TODO


## Working tree

In a git repository, the files on disk that you edit are called the "working
tree".

When you edit a file in your working tree, the working tree is considered
"dirty". It's considered clean when there are no changes in the working tree
compared to the currently checked-out ref.

It's possible to have any number of working trees associated with a Git
repository, including zero (this is called a "bare" repository)!


## Checkout

When you "checkout" a ref, you are updating your working tree to reflect that
ref. Once you've checked out a ref, you can now open a file in an editor and
see its contents at that point of the history.


## Remote

A remote is just a copy of a git repository living on another computer (for the
purposes of this course) that is accessible using the Git protocol. In other
words, it's another repository that you can talk to using the `git` Command
Line Interface (CLI). That other repository can be somewhere on your computer,
or it could be online (e.g. on GitHub or Bitbucket).

When you clone a repository, a remote is created called `origin` that points at
the original repository you cloned.

GitHub and BitBucket are just hosting a copy of your repository that you can
treat as your "source-of-truth".
