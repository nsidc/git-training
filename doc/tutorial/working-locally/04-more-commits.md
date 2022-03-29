# Make changes and take more snapshots!

For your next snapshots, you will fix errors in this content one line at a time and make
commits (previously referred to as taking snapshots, but we're going to use the official
terminology from here on) with each change.


## Fix some errors on the first line

Correct the following two errors on the first line of `marbles.txt`:

- Remove the comma between `to` and `never`.
- Change `their` to `they're`.

Save the file!


## Commit the fixes

Run `git status` to show the current state of the working tree.

```
$ git status
On branch main
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
    modified:   marbles.txt

    no changes added to commit (use "git add" and/or "git commit -a")
```

Once again, Git is suggesting using `git add` to prepare your changes for commit. You
already know how to commit the changes once you've added them. However, it's never a bad
idea to check your change first.

```
$ git diff
diff --git a/marbles.txt b/marbles.txt
index c7108ef..99e3a6e 100644
--- a/marbles.txt
+++ b/marbles.txt
@@ -1,4 +1,4 @@
-The most important reason to, never eat marbles is if their overindulged and the
+The most important reason to never eat marbles is if they're overindulged and the
 marbles are out of the water. just make sure you keep them hydrated and porperly lit.
  
 If your going to eat marbles next time around, make sure you make your mabrles for the
```

This output is confusing at first, but focus on the lines which start with `-` and `+`.
These are your change. The `-` line is the "before" text, and the `+` line is the
"after" text for the first line of the `marbles.txt` file. This looks like an accurate
representation of your change!

Now you're ready to commit your changes.
```
$ git add marbles.txt
$ git commit -m "Fix errors in first line"
[main 4f88912] Fix errors in first line
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Again, one file was changed. And we altered one line in that file, which `git`
represents as one insertion and one deletion of a line.

```{note}

If you like, run `git status` between the `add` and `commit` commands to get more
context at each step. Similarly, you can run `git diff --staged` between these two
commands to see the changes that are staged for commit.
```


## Fix some errors on the second line

Fixing the errors on the second line and taking another snapshot is a piece of cake
given what we now know! I see two errors:

- Change `just` to `Just`.
- Change `porperly` to `properly`.

Save `marbles.txt`.


## Commit the second batch of fixes

Since you already know how to commit the changes in two steps, here's a shortcut to do it
in one command -- the "add" occurs automatically:

```
$ git commit -m "Fix errors on the second line" -- marbles.txt 
[main 6589abd] Fix errors on the second line
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Again, one line in one file was changed.

```{note}

The `--` tells `git` (and many other commands) that the values after the symbol are a
list of files. This is just another option, not "better" than doing `git add` first.
```


## Check your progress

Now you should have three commits. One which added the `marbles.txt`, and two for fixing
errors in it.

We can use this compressed version of `git log` to validate at a glance:

```
$ git log --graph --decorate --oneline
* 6589abd (HEAD -> main) Fix errors on the second line
* 4f88912 Fix errors in first line
* 075bbc6 Add marbles.txt
```

Each asterisk here is a commit. The oldest commit is at the bottom, and the newest at
the top. Notice that the labels `HEAD` and `main` have both moved with you as you added
more commits.

```{note}

You may have noticed that the commit messages have a common style. See
{doc}`/reference/best-practices-and-good-habits` for more information on writing commit
messages.
```
