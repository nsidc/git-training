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

A collection of at least one patch to at least one file.


## Commit

A git object (with associated metadata, e.g. author, date, hash, message)
representing a single changeset or patch.


### Commit hash

A unique identifier generated randomly for every commit.


## Tree

A collection of commits, each linked by reference(s) to parent commit(s).


### Ref

A string representing a commit on the tree. A ref can be a `tag`, a `branch`,
or a `commit` hash.


### Tag

TODO


### Branch

TODO


## Remote

A remote is just another git repository living on another computer that is
accessible over the network using the git protocol. In other words, it's
another repository online that you can talk to using the `git` CLI.

When you clone a repository, a remote is created called `origin` that points at
the original repository you cloned (e.g. from GitHub or BitBucket).

GitHub and BitBucket are just _hosting_ a copy of your repository that you can
treat as your "source-of-truth".
