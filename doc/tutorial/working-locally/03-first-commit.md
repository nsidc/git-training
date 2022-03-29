# Take a snapshot of our content with Git

## Add your new file to the {term}`Staging area`

You can think of the {term}`Staging area` as where files live before they are
snapshotted.

To view the current status of the repo, run:

```
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
      marbles.txt

      nothing added to commit but untracked files present (use "git add" to track)
```

In the output above, `git` has recommended that we use `git add` to "track" this new
file.

```
$ git add marbles.txt
```


## View what is ready for commit

```
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
    new file:   marbles.txt
```

Notice that the file `marbles.txt` is now displayed in green (if you have a
color-enabled terminal), and is in a section labeled "Changes to be committed".

🎉 This means we're ready for the next step!


## Take a snapshot

```
$ git commit -m "Add marbles.txt"
[main (root-commit) 075bbc6] Add marbles.txt
 1 file changed, 7 insertions(+)
  create mode 100644 marbles.txt
```

This will created a snapshot (called a {term}`commit<Commit>` in Git parlance) of our
new file in the staging area, `marbles.txt`. The argument `-m "Add marbles.txt"` set a
commit message, which describes our change.

In the output above, we can see that a new commit was created, and it was given the
unique {term}`hash<Hash>` `075bbc6`. One file was changed (`marbles.txt`), and seven
lines were added (`7 insertions(+)` in Git language).

```{note}

You can omit the `-m` argument to use the interactive commit workflow, but I recommend
replacing it with `--verbose` in that case to provide useful context when writing a
commit message. For the purpose of this tutorial, we will not use the interactive commit
interface and will always use `-m`.
```


## Check the repository status again

```
$ git status
On branch main
nothing to commit, working tree clean
```

🎉 This tells us that our changes are saved as a snapshot in time, also known as a
{term}`commit<Commit>`. The text `working tree clean` tells us that there are no changes
in progress in the "{term}`working tree<Working tree>`", Git's name for the directory of
files we're working on.


### Viewing the History

Now that we've added our first {term}`commit<Commit>` to the {term}`history<History>`,
we can take a look. `git log` displays a log of commits. Use `git help log` to learn
more. 

```
$ git log
commit 075bbc6f990324818619e3e081fe49298cf74888 (HEAD -> main)
Author: Matt Fisher <matt.fisher@nsidc.org>
Date:   Tue Mar 29 12:17:52 2022 -0600

    Add marbles.txt
```

There's a lot of information here.

The first line `commit 075bbc6f990324818619e3e081fe49298cf74888 (HEAD -> main)` is the
most important. It includes the commit {term}`hash<Hash>`, which is a long,
intimidating, and seemingly random string. The string isn't actually random, and you can
learn more in the glossary entry for {term}`Hash` if you'd like. You don't need to use
the full hash in any case, you can abbreviate these long hashes to 5+ characters. After
the hash, in parentheses, are the {term}`refs<Ref>`, or labels, attached to this commit
(`HEAD` and `main`). You can use these labels instead of the hash to refer to this
commit. Note that some kinds of labels may move over time, so after you've made more
commits, the `HEAD` and `main` labels will point at different commits.

```{note}

`HEAD` refers to your current location in the {term}`History`.

`main` refers to the "main" or "default" branch which is created by default with every
Git repository. You may also see the "main" branch called `master` in some repositories!
```

The next two lines, author and date, are self-explanatory, and the final line is the
commit message we entered with the `-m` argument to `git commit`.

We can get a more compressed view of the history like so:

```
$ git log --graph --decorate --oneline
* 075bbc6 (HEAD -> main) Add marbles.txt
```

This type of display will be more useful when we have more commits.
