# Basics

## How to ask Git for a hint

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

## How to initialize a new repository

Create a new directory for your code, and then initialize it as a git repo:

```
mkdir my-repo
cd my-repo
git init
```


## How to clone an existing repository

```
git clone git@bitbucket.org/nsidc:git-training.git
```
