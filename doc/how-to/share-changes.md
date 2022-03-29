# Share changes (remote, fetch, pull, push)

## How to manage remotes (e.g. GitHub/Bitbucket repositories)

You shouldn't need much beyond these commands, but if you do, check `git help remote`.


### Add a remote

```
git remote add <name> <URL>
```

Typically, you'll only add one remote, a GitHub or Bitbucket repo, and its name will be
`origin`. If you cloned your repository from GitHub or Bitbucket, this is done for you.


### Remove a remote

```
git remote rm <name>
```


### Rename a remote

```
git remote rename <old> <new>
```


## Getting commits from a remote

```
git fetch
```

This will fetch commits from a remote server but will not checkout / switch to them. In
other words, your {term}`Working tree` will not be affected.

Once this is complete, you should see a message indicating which remote tracking
branches have been updated by this command (if any updates were fetched). Local branches
will not be affected.


## Updating a local branch with a remote tracking branch

```
git pull
```

If your currently-checked-out branch is already configured to track a remote branch,
this will update that local branch to the most recent commit on the remote branch (that
we know of). If tracking is _not_ configured, follow Git's instructions. I recommend
always doing a `git fetch` then viewing the History before a `git pull`.

Once this is complete, you should see your local branch move to the same commit as the
remote tracking branch.


## Pushing local code to a remote server (e.g. GitHub/Bitbucket)

```
git push -u <remote> <branch>
```

Push your local `<branch>` to `<remote>`. Once this is complete, you will see that the
`<remote>/<branch>` tracking branch has moved.

`-u` is short for `--set-upstream` sets up tracking relationships between your local
branch and the remote branch. You only need to specify this on your first push, and it
can be ommitted afterwards.
