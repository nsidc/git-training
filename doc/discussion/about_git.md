# About Git for non-users

It may not be immediately obvious that Git isn't just a tool for developers to
manage and share code. On this page, we hope to describe the usefulness of Git
to someone who has never used it.


## "Save early, save often" with time travel

We all learned at some point to "save early, save often". Maybe we learned the
hard way by starting with a very naive approach to writing a document:

* *Saving when you're done editing a file*: If your computer crashes before
  you're done, you could lose all your work!

* *Saving frequently*: If your computer crashes, you'll be able to recover
  where you last saved. But what if you save and then later realize that part
  of your document had been deleted before saving?

* *Saving copies frequently*: This enables you to view old versions of your
  document, as long as you manually saved a copy with a unique name. But what
  if you start having trouble figuring out whether the version you want is
  `document_new_final_really_final.csv` or `document_final_v2_latest.csv`?

* *Saving copies with a naming convention*: This enables you to find the right
  version at a glance. Maybe you use dates or a version number that always goes
  up. This requires you to put in a nontrivial amount of effort managing your
  versions.

* *Using a version management program*: Instead of manually naming your files,
  a program could do it for you. You don't even need to _look_ at all those
  copies because that program could store them somewhere out of sight, and put
  only the version you want in `document.csv`. This program could also talk to
  other version management programs to share all the different versions with
  someone else, and also get their versions and help merge your work with
  theirs. This is what Git does.
