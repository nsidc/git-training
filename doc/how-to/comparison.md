# Perform comparisons (diff)

Comparison commands follow this pattern:

```
git diff <before-ref> <after-ref>
```

...to enable you to visualize the difference between `<before-ref>` and `<after-ref>`.
These are some common comparisons you might want to do.


## How to see the changes on your branch

Compare your branch to its parent:

```
git diff <branched-from> <my-branch>
```

e.g.

```
git diff main TKT-23-fix-rendering-issue
```

...to compare a bugfix branch to the `main` branch.


## How to compare two releases

If you have two release tags `v1.2.3` and `v1.2.4`, you can compare them:

```
git diff v1.2.3 v1.2.4
```


## How to compare your local edits to checked-in files

If you have edited `foo.txt` but haven't `add`ed or `commit`ed your changes, you can:

```
git diff -- foo.txt
```

If you have added/staged some changes to `foo.txt` you can see them with:

```
git diff --cached -- foo.txt
```

Simply omit the filename(s) from these commands to see all changed files, e.g.:

```
git diff --cached
```
