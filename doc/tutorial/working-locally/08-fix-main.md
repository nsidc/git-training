# "Diverge" by fixing an error on the `main` branch

A colleague has asked you to create a version of this document with more spelling and
grammar corrections applied. You're not ready with your changes on the
`add-safety-warning` branch yet, so you'll have to switch between branches to work on
each of these independent tasks.


## Go back to the main branch and fix the third line

```
$ git switch main
Switched to branch 'main'
```

Now that you're on the main branch, it's expected that the `marbles.txt` file will be
missing the safety warning, but it should have spelling fixes on the first two lines.
Validate this expectation by viewing the first three lines of the file:

```
$ cat marbles.txt | head -n3
The most important reason to never eat marbles is if they're overindulged and the
marbles are out of the water. Just make sure you keep them hydrated and properly lit.

```

The warning is gone (it's not _really_ gone, it's just on the other branch), and the
spelling fixes are present. Let's fix the third line of text (line 4, as line 3 is
empty):

- Change `If your` to `If you're`.
- Change `mabrles` to `marbles`.

Save the file. Commit it:

```
$ git add marbles.txt

$ git commit -m "Fix the third line of text"
[main 00d0a78] Fix the third line of text
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Now that you have changes on `main` and changes on `add-safety-warning` after the
branching point (the commit the branch was created from), your history looks much more
"branchy":

```
* 00d0a78 (HEAD -> main) Fix the third line of text
| * 0dd69ee (add-safety-warning) Clarify safety warning
| * 2ee2574 Add preliminary safety warning
|/  
* 6589abd (tag: first-two-lines-validated) Fix errors on the second line
* 4f88912 Fix errors in first line
* 075bbc6 Add marbles.txt
```

🎉 This tells you that you have two branches originating from `6589abd` (coincidentally,
this is the commit you tagged as `first-two-lines-validated`). In addition to `*` for
each commit, there are now lines connecting the `*`. These lines connect commits to
their parents, and they tell us that `6589abd` is parent to both `00d0a78` and
`2ee2574`. 

```{note}

As you can image, with more branches this text can get harder to read. In normal usage,
`git log` will apply colors to the lines to help you visualize these relationships.
```

In this state, you can say that `main` and `add-safety-warning` have "diverged".
