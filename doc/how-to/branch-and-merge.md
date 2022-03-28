# Branch and merge


## How to create a new branch

Create a new branch (from the current `HEAD` commit) and switch to it:

```
git switch -c <branchname>
```

This is equivalent to:

```
git branch <branchname>
git switch <branchname>
```

```{note}
In git <v2.23 (not recommended):

    git checkout -b <branchname>
```


## Merge a branch

To merge branch `<branchname>` into the currently checked-out branch:

```
git merge <branchname>
```

Alternately, you can merge branch `<branchname>` into `<into-branchname>`:

```
git merge <branchname> <into-branchname>
```

```{note}
If your branch can be merged without creating a merge commit, a fast-forward merge will
be performed. If you don't want a fast-forward merge, you can specify the `--no-ff`
argument to `git merge`.
```
