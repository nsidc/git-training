# Make changes

## Edit some content

Just use your favorite editor, open a file, and save it.

You can run `git status` to see that your changed file is "not staged for commit", and
is displayed in red.


## Stage your change for commit

```
git add <file(s)>
```


## Commit staged changes

```
git commit --verbose
```

`--verbose` is recommended because Git will display your changes, making it easier to
write a commit message describing them.

Your selected editor (configured in `~/.gitconfig`) will open a file containing a place
to write a message followed by commented instructions (lines beginning with `#`). After
you've written a commit message, save the file and close it to finalize the commit.

See {doc}`/reference/best-practices-and-good-habits` for more on writing good
commit messages.
