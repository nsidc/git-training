# Make the structure/order of the materials more clear

* How should people use these training materials? In what order?

* How should NSIDC deliver these trainings to users? (e.g. tiny bites? 1 tutorial + 1
discussion in a session?)

* Should there be a way of indicating materials that you can get by without? e.g. you
don't _need_ to understand the history as a DAG but it may help some learners.


## Guided learning

The most attention-drawing thing a user sees when they first load the page should be an
outline of the materials suggesting where to start and how to progress. The sidebar can
provide similar quick-navigation once the user has left the front page.


### Discussion: What is Git / what is Git for?

* Who is Git for? What can Git do for me?
* Why should I use Git and not Google Docs / MS Office?
* When should I not use Git?


### Tutorial 1a: Intro to Git through GitHub GUI

* Creating repositories with the GUI
* Contributing to repositories with the GUI
* Reviewing changes in GitHub GUI

NOTE: Using GitHub GUI features first, or CLI first?


### Tutorial 1b: Intro to Git at the CLI / `git` commands

* Cloning a repository from GitHub / `init` on local computer
* Adding changes, committing
* Log, diffing
* Authenticating to push
* Pushing

NOTE: How  to make "pushing" part easiest? All methods seem non-trivial and require
install of something (e.g. `openssh` not necessarily installed). [GH
docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github#authenticating-with-the-command-line)
describe using GitHub CLI, using the `git` program with a Personal Access Token, using
Git Credential Manager, or using SSH keys.


### Discussion: Understanding Git's history with graph theory

* Git's history is a Directed Acyclic Graph

NOTE: Should this be before the branching/merging tutorial or after?


### Tutorial 2: Branching and merging at the CLI

* What do branches do for me?
* What are conflicts? How do I resolve conflicts?


### Discussion: Merge strategies

* Fast-forward
* Squash

NOTE: Integrate this information into branching/merging tutorial?


### Tutorial 3: Pull requests

* How do I open a PR?
* What do I do after I open a pull request?
* What do I do after I'm asked to review a PR?


### Tutorial 4: Forks / upstreams

* What does it mean to fork?
* How to fork?
* Remotes and having multiple (e.g. `origin` and `upstream`)


## Reference

* Dedicated section for workflow-focused cheat sheets? The "How-to" section currently
  contains that material.
* Cheat sheets paired with tutorial contents?
* A "style guide" or "symbology" page? Would be useful to document re-usable elements
  like BitBucket/GitLab compatibility notes, authors' notes, warnings, format standards
  for images/captions, etc.
