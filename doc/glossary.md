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
from a co-worker's repository if you want.


## Patch

A set of line-level additions and deletions representing a change to a file.
e.g. the following patch changes "foo" to "bar" by removing the "foo" line and
adding the "bar" line:

```
-foo
+bar
```


## Changeset

A collection of at least one _patch_ to at least one file.


## Commit

A git object (with associated metadata, e.g. author, date, hash, message)
representing a single _changeset_.


### Commit hash

A unique identifier generated randomly for every commit.


## Tree / History

A collection of commits, each linked by reference(s) to parent commit(s).

It's called a "tree" because each commit is linked to at least one parent,
forming a tree shape. A "leaf" commit has no children, and the "root" commit
has no parents.

It's also called a "history" because the full history of all changesets is
present in the git tree.


### Ref

A string representing a commit on the tree. A ref can be a `tag`, a `branch`,
or a `commit` hash.


### Tag

TODO


### Branch

TODO


## Working tree

On your local machine, the files on disk are called the "working tree".

When you edit a file in your working tree, the working tree is considered
"dirty". It's considered clean when there are no changes in the working tree
compared to the currently checked-out ref.


## Checkout

When you "checkout" a ref, you are updating your working tree to reflect that
ref. Once you've checked out a ref, you can now open a file in an editor and
see its contents at that point of the history.



## Remote

A remote is just another git repository living on another computer that is
accessible over the network using the git protocol. In other words, it's
another repository online that you can talk to using the `git` CLI.

When you clone a repository, a remote is created called `origin` that points at
the original repository you cloned (e.g. from GitHub or BitBucket).

GitHub and BitBucket are just _hosting_ a copy of your repository that you can
treat as your "source-of-truth".
