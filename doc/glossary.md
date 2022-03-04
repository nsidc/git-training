# Glossary

Some of these terms are git-specific, and some of them are more generic
version-control terms.


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

TODO
