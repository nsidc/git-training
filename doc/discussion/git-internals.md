# About internal Git objects

For the purposes of this training, you don't need to know anything about the
internals of Git!


## The hidden `.git/` directory

The `.git/` directory exists at the root of every repository. In fact, the
`.git/` directory is all `git` needs to work. A Git repository with only a
`.git/` directory and no working tree is called a "bare repository".

This directory contains data (objects) and metadata such as pointers, refs,
commit messages, and hooks (advanced automated behaviors, like "run tests
before each commit").

All of the examples in this document use real objects in this repository and
can be reproduced on your computer!


## Git objects

Inside the `.git/` directory, the actual data is stored in the `objects/`
directory, indexed by object hash. The first two characters of each hash make
the name of the directory, and the rest of the hash makes a filename inside the
directory. 

Git objects are used to represent the changing state of a repository:

* `commit` objects represent a unit of change. Each `commit` contains a `tree`, and
  a `parent`, which is a reference to another commit object. The full history
  of a Git repository is built of these parent relationships.
* `tree` objects are snapshots of directory structure. Each `tree` contains at
  least one other `tree` or `blob`.
* `blob` objects are snapshots of file contents. Each `blob` contains the
  contents of that file at a given point in time.


### Exploring some objects

In this repository the `dff557a5cdaa8b7a826d74ce82fd65c878d2b9bd` commit is
represented by the file below. The first 7 digits `dff557a` can be used with
`git` as a short representation of the full commit hash.

```
$ file .git/objects/df/f557a5cdaa8b7a826d74ce82fd65c878d2b9bd 
.git/objects/df/f557a5cdaa8b7a826d74ce82fd65c878d2b9bd: zlib compressed data
```

As shown by the `file` utility above, this data is compressed, so we won't be
able to read it normally:

```
$ cat !:1
cat .git/objects/df/f557a5cdaa8b7a826d74ce82fd65c878d2b9bd
xAn @Ѭ9\`E+q
!*]Ԇ)o(#z=hOr6G!Qܶ?I~m[pC֊ޓ"
                           ,$uk;k[Oo
```

We can decompress it with generic tools:

```
$ zlib-flate -uncompress < .git/objects/df/f557a5cdaa8b7a826d74ce82fd65c878d2b9bd 
commit 248tree be8302d77917a381cd91bb04901eace1d542ae47
parent cb775ec187cc757e55f4c9255a12ebb2b97b8846
author Matt Fisher <matt.fisher@nsidc.org> 1647034766 -0700
committer Matt Fisher <matt.fisher@nsidc.org> 1647034766 -0700

Add SSH key instructions link
```

But `git` also provides a utility we can use to display the object
corresponding with a hash: `git cat-file`. We will use this utility going
forward, just know that under the hood, `git cat-file` is only doing the above:
Finding the object corresponding to a hash, and decompressing it for us to
read.


#### A `commit` object

```{figure} https://git-scm.com/book/en/v2/images/commit-and-tree.png
---
alt: Commit diagram
---
Credit: Pro Git 2nd Edition
```

A `commit` object has two pieces of data (keep in mind, "objects" are data and
are referenced by hash. Everything else is metadata): a `tree`, which is its
own type of object that we'll explore later, and a `parent`. Finally the commit
contains metadata like the `author` (a name, email, and a UNIX timestamp),
`committer`, and commit message.

The `commit` object `dff557a` can be inspected using `-p` to "pretty-print" the
contents of the object, and `-t` to show the type of the object. Additionally,
`-s` can show the size in bytes. Further, we can use the `date` utility to
convert the UNIX timestamp to a human-readable one:

```
$ git cat-file -t dff557a
commit

$ git cat-file -s dff557a
248

$ git cat-file -p dff557a
tree be8302d77917a381cd91bb04901eace1d542ae47
parent cb775ec187cc757e55f4c9255a12ebb2b97b8846
author Matt Fisher <matt.fisher@nsidc.org> 1647034766 -0700
committer Matt Fisher <matt.fisher@nsidc.org> 1647034766 -0700

Add SSH key instructions link

$ date -d @1647034766
Fri 11 Mar 2022 02:39:26 PM MST
```

```{figure} https://git-scm.com/book/en/v2/images/commits-and-parents.png
---
alt: Parent relationship diagram
---
Credit: Pro Git 2nd Edition
```

The `parent` is just another `commit` object. The `parent` relationship is what
establishes the structure of the git history. Just like with humans, parents
are ancestors, or past versions. Children are descendents, or future versions.
Each commit can have one to many parents (except a root commit which can have
zero parents), and zero to many children.

> zero parents for the initial commit, one parent for a normal commit, and
> multiple parents for a commit that results from a merge of two or more
> branches.

[Pro Git 2nd Ed. Chapter 3.1](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell#ch03-git-branching)

By looking at the `parent` object, we can see that `Matt Fisher` first
performed a change called `Extract planning to its own doc`, then another
operation called `Add SSH key instructions link`. We can continue to follow
this parent relationship all the way to the beginning of the repository if we
want!

```
$ git cat-file -t cb775ec187cc757e55f4c9255a12ebb2b97b8846
commit

$ git cat-file -p cb775ec187cc757e55f4c9255a12ebb2b97b8846
tree 81e6377718f49156f99e60fcac725fd45bc64519
parent d913a4784fd68d13e6bc04d61f374f336ab090ea
author Matt Fisher <matt.fisher@nsidc.org> 1647034564 -0700
committer Matt Fisher <matt.fisher@nsidc.org> 1647034564 -0700

Extract planning to its own doc
```


#### A `tree` object

The `tree` object from the previous section can be abbreviated as `81e6377`. A
`tree` object represents the structure of the files in the repo at a given
point in time. The "root" tree we're looking at contains a `tree` for each
directory in the repository, as well as a `blob` for each file.

```
$ git cat-file -t 81e6377
tree

$ git cat-file -p 81e6377
100644 blob 29791eda0b90a331e41d4d3992d089ae6d764748  README.md
100644 blob 32303047543dfb4f77a804070f82a699aa442581  _planning.md
040000 tree 9aa2a1611c62dd36db2ec6329021e75a5e586f2d  doc
```

This tells us that at the time of commit `cb775ec` (which we learned above was
March 11th), the repository contained files (`blob`s) named `README.md` and
`_planning.md`, and a directory (`tree`) called `doc`. We can see what was
inside the `doc` `tree` and thusly explore the entire contents of the
repository at this point in time:

```
$ git cat-file -p 9aa2a16
100644 blob bda1a223d98790c8710ebbd89b2571f70e8b28f5  .gitconfig-example
100644 blob 5b549963deab12a43c42d33e416b19a19557f684  git-cheatsheet.md
100644 blob e9753d38cdbfdceff24d97da93748ae8171cae32  glossary.md
100644 blob 67fa85e89ced7979424e2cf94755a7c92c93032a  learn-more.md
```


#### A `blob` object

Finally, a `blob` is just a _snapshot_ of a file. The full contents of the file
at a given time are contained in the blob.

```
$ git cat-file -p 29791ed
# Git Training

![git logo](https://git-scm.com/images/logos/2color-lightbg@2x.png)

Learn to use `git`!
<...output truncated...>
```


## Hashes

Git's hashes are (usually) `sha1` hashes calculated on the type, size, and
contents of an object. The hashes are deterministic, meaning the hash will
always be the same for the same content. They are not random as they appear!

We can manually re-generate the hash of commit `dff557a` like so:

```
$ content=$(git cat-file -p dff557a)
$ size=$(git cat-file -s dff557a)
$ type=$(git cat-file -t dff557a)

$ echo $content
tree be8302d77917a381cd91bb04901eace1d542ae47 parent cb775ec187cc757e55f4c9255a12ebb2b97b8846 author Matt Fisher <matt.fisher@nsidc.org> 1647034766 -0700 committer Matt Fisher <matt.fisher@nsidc.org> 1647034766 -0700 Add SSH key instructions link

$ echo $size
248

$ echo $type
commit

$ echo -e "$type $size\x00$content" | sha1sum
dff557a5cdaa8b7a826d74ce82fd65c878d2b9bd  -
```

In the end, we have an exact match!


## Learn more

* [Git SCM - Git Internals](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)
* [Computerphile - Inside the Hidden Git Folder](https://www.youtube.com/watch?v=bSA91XTzeuA)
