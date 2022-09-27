# Travel back and forth in time

Now that you have three snapshots, you can view any of those states easily.


## Go back to the original version

To checkout the original commit, you can use its {term}`hash<Hash>`. Note that your hash
will be different, because it's calculated based on your name, your email, and the time
of the commit.

```
$ git log --graph --decorate --oneline --all
* 6589abd (HEAD -> main) Fix errors on the second line
* 4f88912 Fix errors in first line
* 075bbc6 Add marbles.txt
```

We see that `075bbc6` is the oldest commit.

```
$ git checkout 075bbc6
Note: switching to '075bbc6'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 075bbc6 Add marbles.txt
```

```{note}

This output is kind of big and scary, but it's not a big deal. You've simply checked out
a commit that is not associated with a branch. Git calls this "detached".

Careful reading of this text will inform you of your available options, but for the
purposes of this tutorial, we're going to move on and ignore the message.

An alternative way to run this operation which tells Git "I know I'm going in to a
detached state and what that means, don't spam me" is `git switch --detach 075bbc6`. We
will use `git switch` instead of `git checkout` going forward. Note that Git versions <
2.23 will only have `checkout` available.
```

Now you can view the original contents of the file, without the spelling and grammar
fixes added in the most recent commits:

```
$ cat marbles.txt | head -n2
The most important reason to, never eat marbles is if their overindulged and the
marbles are out of the water. just make sure you keep them hydrated and porperly lit.
```

```{note}

The `|` in this command is called a "pipe", which redirects the ouput of the command on
the left hand side of the pipe to the command on the right side of the pipe. Since `cat`
prints the contents of a file, and `head -n2` grabs the first 2 lines of its input, this
command prints the first two lines of `marbles.txt`.
```

As you can see, all of the original errors are back in the file.


## Viewing the History state

```
$ git log --graph --decorate --oneline --all
* 6589abd (main) Fix errors on the second line
* 4f88912 Fix errors in first line
* 075bbc6 (HEAD) Add marbles.txt
```

Notice the difference between the last time you ran `git log`. The commits are the same,
but the {term}`refs<Ref>` in parentheses (think of them as "labels") are different.

`HEAD` is what you have {term}`checked out<Checkout>`. This label is now on the oldest
commit. `main` is currently the only branch in this repository (it was created by
default when you ran `git init`), and it is still attached to the newest commit. It
didn't move when you ran `git checkout`.


## Returning to the latest change

Since the `main` label hasn't moved, you can use it to switch back to where you were:

```
$ git switch main
Previous HEAD position was 075bbc6 Add marbles.txt
Switched to branch 'main'
```

Now you can view the first two lines of your file again to see that the fixes are back!

```
$ cat marbles.txt | head -n2
The most important reason to never eat marbles is if they're overindulged and the
marbles are out of the water. Just make sure you keep them hydrated and properly lit.
```

And `git log` shows that the `HEAD` label has once again moved to reflect your current
position in the history.


## Make a big mistake

At this point, your status should look like:

```
$ git status
On branch main
nothing to commit, working tree clean
```

Everything is up to date, and your working tree doesn't contain any changes. What if you
accidentally delete the only file in your repository?

```
$ rm marbles.txt

$ git status
On branch main
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    marbles.txt

        no changes added to commit (use "git add" and/or "git commit -a")

```

`git status` is showing us what we did: We deleted `marbles.txt` with the `rm` (remove)
command. Getting it back is easy, since we have committed three versions of it.

```
$ git restore marbles.txt
```

That's it, the file is back! Check out `git status` or `cat` the file if you like.

```{note}

If you have an older version of `git`, <2.23, use `git checkout` instead of `git
restore`.
```
