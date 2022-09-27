# Compare/review the two branches

Now that you have two diverging branches, you can visualize how they diverge with `git
diff`.


## How is `main` different from `add-safety-warning`?

The `git diff` command can tell you the difference between one commit (or label pointing
to a commit) and another. The comparison is done as `git diff <before> <after>` to
visualize the change between `<before>` and `<after>`.

```
$ git diff main add-safety-warning
diff --git a/marbles.txt b/marbles.txt
index 8b18a6a..12e2b75 100644
--- a/marbles.txt
+++ b/marbles.txt
@@ -1,7 +1,9 @@
+WARNING: This information is harmful. Never eat marbles for any reason.
+
 The most important reason to never eat marbles is if they're overindulged and the
 marbles are out of the water. Just make sure you keep them hydrated and properly lit.

-If you're going to eat marbles next time around, make sure you make your marbles for the
+If your going to eat marbles next time around, make sure you make your mabrles for the
 day in advance. Make sure you're preppared to eat them right at teh beginning of the day
 and immediately teh next day, especially on weekends and busyy days. (And please be
 mindful of teh amount of time they require!
```

This diff shows (based on the lines starting with `+` and `-`) that the safety warning
being added, and the spelling fixes being removed. The opposite would be shown if you
passed the branches to `git diff` in the opposite order, like `git diff
add-safety-warning main`.

🎉 This shows that each branch has changes that are not present in the other branch.
