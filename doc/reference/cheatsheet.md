# Cheat Sheet

A quick reference of Git commands.


## Getting started

### Asking Git for a hint

git status can be used to view the local state of your repo and provide a 
hint for the next possible actions that could be taken.

```
git status
```
Example output:
```
On branch main
Your branch is behind 'origin/main' by 4 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

nothing to commit, working tree clean
```

### Initialize a new repository

Create a new directory for your code, and then initialize it as a git repo:

```
mkdir my-repo
cd my-repo
git init
```


### Clone an existing repository

```
git clone git@bitbucket.org/nsidc:git-training.git
```


## Navigating the git tree

### Checking out a ref (tag/branch/commit)

```
git switch <ref>
```

_git <v2.23 (not recommended):_
```
git checkout <ref>
```


### Comparing branches

TODO


### Getting remote code from a server (e.g. GitHub/Bitbucket)

TODO


## Contributing to a git repository

### Creating a new branch

Create a new branch and switch to it:

```
git switch -c <branchname>
```

_git <v2.23 (not recommended):_
```
git checkout -b <branchname>
```


### Pushing local code to a remote server (e.g. GitHub/Bitbucket)

TODO
