# Create a new Git repository

```{Important}

The code blocks in this tutorial begin with a `$`, indicating a non-root or user prompt.
Copy the command after the `$`, not the `$` itself. If the command has important output,
it will be shown on additional lines, for example, to execute the code block below, you
would copy `ls -a1`:

    $ ls -a1
    ./
    ../
    .git/
```


## Move to a directory on your computer where you have write access

The repository we're creating doesn't need to be saved long-term, so we can make it in
the temp directory. Feel free to substitute another directory if you prefer.

```
$ cd /tmp
```

```{note}
`cd` is short for "change directory". Learn more about the command with `cd --help`.
Some other commands have "manual pages" ("man pages" for short) that are available with
`man <command>`, e.g.  `man git`.
```


## Initialize a repository

```
$ git init nsidc-tutorial-1
```

This will initialize a new repository in the directory `/tmp/nsidc-tutorial-1`!

```{note}
You can get help for `git init` (and any other `git` command) with either `git help
init` or `man git-init`.
```


## Move into the repository

```
$ cd nsidc-tutorial-1
```

Once you're in the directory, take a look at the contents:

```
$ ls -a1
./
../
.git/
```

🎉 The presence of the `.git/` directory tells us that we have successfully initialized a
repository and that we're now in the correct directory!
