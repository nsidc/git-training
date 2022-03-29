# Label (AKA `tag`) a version so we can come back to it later

A {term}`tag<Tag>` is another type of {term}`ref<Ref>` or label, like a
{term}`branch<Branch>`. The difference is that tags are immobile, while branches follow
your progress. Tags are great for labeling a specific point in time, for example a
released version.


## Add a tag

Tags can be named anything and can be applied arbitrarily. You normally wouldn't use
tags for something this trivial, but as an example, create a tag recording that the
first two lines of this file have passed validation at this point.

```
$ git tag first-two-lines-validated
```

View the log again to see what's changed:

```
$ git log --graph --decorate --oneline --all
* 6589abd (HEAD -> main, tag: first-two-lines-validated) Fix errors on the second line
* 4f88912 Fix errors in first line
* 075bbc6 Add marbles.txt
```

🎉 Looks like your new tag is present!

Notice the new label in parentheses: `tag: first-two-lines-validated`. Git has prefixed
this label with `tag:` since it's a special type of label: the kind that never moves
(unless forced).
