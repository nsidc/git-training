# Make changes (add, commit)

## How to edit some content

Just use your favorite editor, open a file, and save it.

You can run `git status` to see that your changed file is "not staged for commit", and
is displayed in red.


## How to stage your change for commit

```
git add <file(s)>
```


## How to commit staged changes

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


## How to restore a file to its committed state

If you've made a mistake and want to restore a file to its known good state:

```
git restore -- myfile.txt
```

If you want to restore a specific version of a file from a ref:

```
git restore --source=<ref> -- myfile.txt
