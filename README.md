# Git Training

![git logo](https://git-scm.com/images/logos/downloads/Git-Logo-1788C.png)

Learn to use `git`!


## Prerequisites

* **Git!**
    * Linux: `apt install git`
    * OSX: `brew install git` TODO: ? Add Homebrew install instructions?
    * Windows: Install *Git Bash*. TODO: Link, etc.
    * _NOTE: What version do you have? Try to install a version `>= v2.23`._

* **Basic Git setup:**
  * Set up your `~/.gitconfig` file. [Example](./doc/.gitconfig-example)
  * Create a directory for all your git repositories to live in, e.g.
    `~/Projects`.

* **Bitbucket configured:**
  * Account created.
  * Bitbucket access to [NSIDC organization](bitbucket.org/nsidc/). Ask any
    developer to add you.
  * Member of the [Tech training](https://bitbucket.org/nsidc/workspace/settings/groups/tech-training)
    group in NSIDC Bitbucket organization. Ask any developer to add you.
  * SSH keys configured for your Bitbucket account. TODO: Link

* **Prepared to learn something broadly accessible, but hard.** Like learning
  to ride a bike, to swim, to ski, solder, perform long division, drive a car,
  or to write a TPS report, learning to use `git` is not trivial, but it's also
  within your reach. It may take a few sessions, and you may feel challenged,
  frustration, even despair! But like any of the skills above, it's normal to
  feel those things; and it won't take long at all to reach the moment where
  you feel massive satisfaction and pride in a new skill which will benefit you
  for the rest of your career. If/when you feel stuck, please don't hesitate to
  ask for help.


## The plan

### Prep-work

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


### What to do in the training session(s)?

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


### To think about

* What skills are important and not important for our audience?

* What skills should be known up-front?

* What will live in this repo? ReadTheDocs-style tutorial? A collection of jokes?

* What content would serve as a good example for a contribution exercise? E.g.
  a git glossary could be updated with a new term, and we could see that
  reflect in a ReadTheDocs site.

* Should it be something that can be optionally "run" using docker?


## Resources

* TODO: Link to some git tools, e.g. for visualizing git tree, integrating git
  with IDEs, whatever.
