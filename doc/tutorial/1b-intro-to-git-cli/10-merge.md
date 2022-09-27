# Merge the two branches

Now that you know each branch has unique changes not present in the other branch, you
want the best of both worlds. How do you now combine the good things from both branches
in to one new version?


## Merge!

It's a good idea to validate that our merged product looks good without impacting the
`main` branch. To accomplish this, merge the `main` branch into the `add-safety-warning`
branch to bring the changes from the former into the latter:

```
$ git switch add-safety-warning
Switched to branch 'add-safety-warning'

$ git merge main
```

```{note}

We didn't _have_ to switch before merging. Learn more about `git merge` with `git help
merge`.
```

This will merge `main` into the currently active branch, `add-safety-warning`. You will
be prompted to edit a commit message, but you can save and close the editor to use the
default commit message for the merge.

After the merge, you should see output like:

```
Auto-merging marbles.txt
Merge made by the 'ort' strategy.
 marbles.txt | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Similar to the output of a commit, we see a summary of changes.


## What just happened?

A merge does exactly what it sounds like. We can see with `git log`:


```
$ git log --graph --decorate --oneline --all
*   6dc2dfa (HEAD -> add-safety-warning) Merge branch 'main' into add-safety-warning
|\
| * 00d0a78 (main) Fix the third line of text
* | 0dd69ee Clarify safety warning
* | 2ee2574 Add preliminary safety warning
|/
* 6589abd (tag: first-two-lines-validated) Fix errors on the second line
* 4f88912 Fix errors in first line
* 075bbc6 Add marbles.txt
```

A new commit (called a "merge commit") was added. This is a special type of commit with
more than one parent (`6dc2dfa` has parents `00d0a78` and `0dd69ee` -- follow the
asterisks to the right to find their commit IDs).

```{note}

A merge commit is not always necessary. See the entry for "fast-forward" in `man
gitglossary` to learn more about this. If you want to avoid fast-forward, you can use
the `--no-ff` option to `git merge`.
```

Now that we've merged, we can compare the branches again and see that
`add-safety-warning` now contains the spelling fixes.

🎉 The only difference is the warning!

```
$ git diff main add-safety-warning
diff --git a/marbles.txt b/marbles.txt
index 8b18a6a..8fa37a6 100644
--- a/marbles.txt
+++ b/marbles.txt
@@ -1,3 +1,5 @@
+WARNING: This information is harmful. Never eat marbles for any reason.

The most important reason to never eat marbles is if they're overindulged and the
marbles are out of the water. Just make sure you keep them hydrated and properly lit.
```


## But I want the merged changes on `main`, not `add-safety-warning`!

Good point, that's where the changes should be when they're ready! Now that the
`add-safety-warning` branch includes the fixes on `main`, though, it's easier for us to
see how it's different from `main`, and how `main` will be impacted by a merge. The diff
above describes that impact fairly clearly, so you can confidently merge into `main`
now.

```
$ git switch main
Switched to branch 'main'

$ git merge --no-ff add-safety-warning
```

```{note}

We used `--no-ff` here to force Git to create a merge commit. This makes it easier to
see what was done by the merge operation, but was not _necessary_ in this case.
```

Once again, save and quit the editor to use the default commit message.

```
Merge made by the 'ort' strategy.
 marbles.txt | 2 ++
 1 file changed, 2 insertions(+)
```

As expected, two lines were added: The warning, and a blank line.

`git log` shows us the new merge commit:

```
$ git log --graph --decorate --oneline --all
*   c05127e (HEAD -> main) Merge branch 'add-safety-warning'
|\
| *   6dc2dfa (add-safety-warning) Merge branch 'main' into add-safety-warning
| |\
| |/
|/|
* | 00d0a78 Fix the third line of text
| * 0dd69ee Clarify safety warning
| * 2ee2574 Add preliminary safety warning
|/
* 6589abd (tag: first-two-lines-validated) Fix errors on the second line
* 4f88912 Fix errors in first line
* 075bbc6 Add marbles.txt
```

This output is fairly confusing without color, so please reference the output on your
computer at this step. Note that `6dc2dfa` still has the same two parents. We also have
a new merge commit for merging `add-safety-warning` into `main`: `c05127e`, which has
parents `6dc2dfa` (the `add-safety-warning` branch) and `00d0a78` (the previous commit
to the `main` branch).

🎉 Now if we examine `marbles.txt` from the `main` branch, we can see that it has all of
the changes we've done so far!

```
$ cat marbles.txt | head -n4
WARNING: This information is harmful. Never eat marbles for any reason.

The most important reason to never eat marbles is if they're overindulged and the
marbles are out of the water. Just make sure you keep them hydrated and properly lit.
```
