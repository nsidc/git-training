# Share changes (fetch, pull, push)

## Managing remotes (e.g. GitHub/Bitbucket)

TODO


## Getting commits from a remote

```
git fetch
```

This will only fetch commits from a remote server but will not check them out or switch
to them.

Once this is complete, you should see a message indicating which remote tracking
branches have been updated by this command (if any updates were fetched).


## Updating a local branch with a remote tracking branch

```
git pull
```

If your currently-checked-out branch is already configured to track a remote branch,
this will update that local branch to the most recent commit on the remote branch. If
tracking is _not_ configured, follow Git's instructions. I recommend always doing a `git
fetch` then viewing the History before a `git pull`.

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
