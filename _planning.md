## Prep-work

* (started) Prepare this repo for use as a reference for Git knowledge and to
  be used for experimenting with git (e.g. by forking, commiting, opening PRs).

* Should we use Sphinx to generate a sweet doc site, or is BitBucket Markdown
  rendering enough?

* (started) Curate a Git cheat sheet that is appropriate for our audience to
  use as quick reference.

* (started) Curate a simple Git glossary appropriate to the scope of this
  training.

* Curate external resources for continued learning.

* Plan out the training sessions. Think about timing; do we need more than one
  session?


## What to do in the training session(s)?

* Explain basic `git` concepts:
    * What is the git tree / history?
    * What is a commit?
    * What is the working tree?
    * What is the relationship between the above? Convey the indepdendence of
      Git history's state and the "working tree" state. i.e.: You can have a
      bare repository without a working tree! That would be only the `.git`
      directory, nothing else; no files. Since the Git history is constructed
      of patches, `git` can re-construct all of the files at any point in time
      by simply starting at the root and constructing the files from the
      patches up to the desired ref/commit to produce a working tree. How can
      we visualize this?
 
* Demonstrate moving around the Git tree.

* Explain "refs"; demonstrate using branches and tags to access different
  versions of code.

* Demonstrate example of working with others.


## To think about

* What skills are important and not important for our audience?

* What skills should be known up-front?

* What will live in this repo? ReadTheDocs-style tutorial? A collection of jokes?

* What content would serve as a good example for a contribution exercise? E.g.
  a git glossary could be updated with a new term, and we could see that
  reflect in a ReadTheDocs site.

* Should it be something that can be optionally "run" using docker?

* Should we create a VM with a "training" generic user that anyone can log in
  to?
