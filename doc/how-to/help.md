# Help and introspection (man, help, status, log)

Git offers built-in documentation that's accessible through `man` or `git` commands, as
well as the ability to make context-aware suggestions to help the user.


## How to get help with a command

For help with `git push`, for example, you can do either:

```
man git-push
```

or

```
git help push
```


## How to access built-in documentation

* Glossary: `man gitglossary`
* Tutorials: `man gittutorial`, `man gittutorial-2`
* Workflows: `man gitworkflows`
* Everyday Git: `man giteveryday`


## How to ask Git for a hint about your current situation

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


## How to visualize the Git History

```
git log
```

The default display is long-form information about commits, but if you have lots of
commits or want to view the branching structure of your history, you may want to try:

```
git log --graph --decorate --oneline  --all
```
