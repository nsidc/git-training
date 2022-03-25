# Best practices and good habits

## Look at Git's status and history often

Use `git status` and `git log` (or other tools) to frequently check Git's
state. The `git status` command even gives useful hints for actions you could
take.


## Read Git's output and check if it succeeded

After doing a `git` command, read the output. It's possible the command failed.
Often when Git fails to do something, it will give you helpful hints to fix
your command.


## When to branch

You might create a new branch for various reasons, e.g.:

- **Working independently on the same repository as a colleague**: Branches
  enable you to work without conflicting with each other.
- **Trying multiple approaches to solving a problem**: Branches enable you
  to quickly switch between approaches without them conflicting.
- **Isolating changes in progress from known-good state**: If you only
  merge branches into the `main` branch once they are fully working, you can
  trust that `main` will always work.


## When to commit

Commit when you've "done one good thing". Try to make your commits small and
self-contained changes that can be easily described in a short commit message.


## Commit message

Commit messages should be written in "imperative voice", as though you are
commanding someone to take an action. Commits messages should not end in
punctuation. Commit messages should be less than 80 characters. Details can be
added after a blank line.

Correct:

- "Add type signature"
- "Create type annotations"

Incorrect:

- "Add type signature." (ends in period)
- "Added a type signature" (incorrect voice)
- "Made a type signature that says the arguments are both strings and the
  return value is an integer" (too long, incorrect voice)
