# Create an independent {term}`branch<Branch>` for making an isolated change

At this point, let's say you realize that you need to work on a change without
disrupting the `main` branch, which other people (or you) might be relying on.

## Create a new branch

Run `git branch` to see which branches currently exist:

```
$ git branch
* main
```

The only branch present is the `main` branch, and the `*` indicates that `main` is the
active branch. Similarly, in `git log` output, `HEAD -> main` indicates that `main` is
the currently active branch:

```
$ git log --graph --decorate --oneline --all
* 6589abd (HEAD -> main, tag: first-two-lines-validated) Fix errors on the second line
* 4f88912 Fix errors in first line
* 075bbc6 Add marbles.txt
```

`git status` also tells you which branch is currently active, as you've seen in previous
steps.

You can create a new branch with `git branch <newbranchname>` but then you'd also need
to `git switch` to activate that branch. You can do it in one step instead:

```
$ git switch --create add-safety-warning
Switched to a new branch 'add-safety-warning'
```

```{note}

`--create` can be abbreviated as `-c`
```

`git log` shows the new branch label, and that it is active with `HEAD ->
add-safety-warning`:

```
$ git log --graph --decorate --oneline --all
* 6589abd (HEAD -> add-safety-warning, tag: first-two-lines-validated, main) Fix errors on the second line
* 4f88912 Fix errors in first line
* 075bbc6 Add marbles.txt
```

With four labels on one commit (`HEAD`, one tag, and two branches), things are looking a
bit crowded.


## Apply a safety warning on this branch

Add a safety warning to the document's first line, followed by a blank line.

```
WARNING: This information looks dubious. It may not be safe.

The most important reason to never eat marbles is if they're overindulged and the
<...snip...>
```

Save the file.

Add and commit this change:

```
$ git add marbles.txt
$ git commit -m "Add preliminary safety warning"
[add-safety-warning 2ee2574] Add preliminary safety warning
 1 file changed, 2 insertions(+)
```

This time you inserted two lines: The warning, and the blank line.

```{note}

Run `git status` and `git log` commands at each stage for more context if you're not yet
feeling comfortable with adding and committing.
```


## Improve the safety warning

That safety warning could be better. Change it to:

```
WARNING: This information is harmful. Never eat marbles for any reason.
```

Save `marbles.txt`, stage it, and commit it.

```
$ git add marbles.txt
$ git commit -m "Clarify safety warning"
[add-safety-warning 0dd69ee] Clarify safety warning
 1 file changed, 1 insertion(+), 1 deletion(-)
```


## Check the history

With two new commits, you can now see that our branch is "ahead" of the `main` branch
with `git log`:

```
$ git log --graph --decorate --oneline --all
* 0dd69ee (HEAD -> add-safety-warning) Clarify safety warning
* 2ee2574 Add preliminary safety warning
* 6589abd (tag: first-two-lines-validated, main) Fix errors on the second line
* 4f88912 Fix errors in first line
* 075bbc6 Add marbles.txt
```

🎉 The new branch is looking great.

Notice that the `main` branch label didn't move, because it wasn't active. The active
branch, `add-safety-warning`, has moved with our progress. The tag,
`first-two-lines-validated`, did not move because tags are immobile {term}`refs<Ref>`
(or labels).
