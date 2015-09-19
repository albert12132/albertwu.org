~ title: Git

Introduction
------------

When working on projects for this class, you'll need some way to share
code with your partner. Some people simply email code, others use
Dropbox. Then there's the problem of combining changes. If you've
tried this, you'll know that it is a hassle.

That's where Git comes in. Git is a version control system that has 2
features that are useful for this class:

1. **Code merging**: automatically merge changes between multiple
   collaborators
2. **Revision tracking**: keep track of previous changes and revert
   back to them in case of an accident

When using Git, your code is stored in a **repository** (repo for
short). As you edit code, you will be pushing changes so that
collaborators will receive your changes.

This document uses Git's [book](http://git-scm.com/book/en) as
reference.

### Installing Git

You can download the latest version of Git
[here](http://git-scm.com/downloads).

The Windows version comes with a Git Bash terminal emulator that is
similar to Cygwin. It's basically another command line that you'll be
using to interact with Git.

### Online Hosting

In addition to Git (used from the command line), many people also use
an online hosting service. These services provide a centralized
overview of your project. Here are two such services:

* [GitHub](https://github.com/): a very popular choice -- many, if not
  most, people use GitHub.
* [Bitbucket](https://bitbucket.org/): allows users to create an
  unlimited number of private repositories.

GitHub also gives you a small number of private repos, but the number
is limited. For this reason, we encourage you to use Bitbucket *for
this class*. Remember, **you may only share code with your partner.
Sharing, or even showing code to anyone besides your partner and the
61A staff is considered cheating.** In the past, we've had incidents
of students copying code from the public repos of other students --
make sure this doesn't happen to you.

That's not to say you shouldn't use GitHub at all. You can (and
should) use GitHub for your own (not class related) projects.

For the remainder of this tutorial, we'll be using Bitbucket as our
hosting service. The process is pretty much the same if you use
GitHub.

Getting Started
---------------

First, [create an account](https://bitbucket.org/account/signup/) on
Bitbucket.

You'll be taken to your homepage. There should be a button labeled
"Create repository." Every project starts with a **repository** --
this is where you'll be storing your code.

Fill in the information about your project. You can call it whatever
you want, and play around with the extra options. Just make sure
*Access level* is set to *private*, and the *Repository type* is
set to *Git*. Then, click "Create repository."

Next, you'll see a page that tells you to "Add some code." Since we're
starting a new repository, click on "I'm starting from scratch."

At this point, if you've already downloaded the project you're working
on from the 61A website (e.g. Hog), you can immediately make the
directory containing those files into a repository:

    cd /path/to/your/project
    git init
    git remote add origin <the url displayed on Bitbucket>

If, instead, you created a separate directory for your repository, go
ahead and follow the steps described on the website. Then move all
your project files into the repo.

The next page tells you to create a `README`. For the purposes of 61A,
you don't really need one, but you can go ahead and create one if you
want. Usually, `README`s provide a summary of your project.

Assuming you have your project files in the repo, type the following
in your terminal:

    git add -A
    git commit -m "First commit"
    git push origin master

We'll explain what these three lines do later. For now, refresh the
Bitbucket page -- you'll see the code you committed. To see the actual
source code, click on "Source." You've just created your first repo!

### Joining a repo

If you started the repo, you can invite your partner to join. Since
we're using private repos, you'll need to send your partner an
invitation.

1. From your repo's dashboard (homepage), click on the small cog
   symbol on the right. This takes you to your repo's settings.
2. On the left, click on "Access management." You'll see which users
   have access to the repo
3. Fill in your partner's information: their Bitbucket username or
   their email, what permissions they have (either "write" or "admin",
   unless you only want your partner to "read" what you've done...)
4. Click "Add". Your partner should receive an email inviting them to
   join.

Once your partner has joined the repo, they can immediately copy the
source code onto their own computer. From the "Overview" page, find a
line labeled "HTTPS" on the right side of the page. There should be a
URL to the right of the "HTTPS" -- copy it, and type this into your
terminal

    git clone <repo url>

This will create a new directory (so no need to create your own) and
populate it with the contents of the repo.


Basic Work Cycle
----------------

A usualy work cycle in Git has the following steps:

1. `git pull` to get updates
2. Edit your code
3. `git add` your changes
4. `git commit` your changes
5. `git push` your changes

All of these are done from your command line.

When you edit code in a repository, the changes are not automatically
available to your collaborators. All edits will be local to your
machine. So how do you publish your changes?

### Pull

Usually, you will be working with other people (e.g. your project
partner). To receive updates that they have made, you need to `pull`:

    git pull origin master

`origin` is the nickname of your repository (so that you don't have to
type in the full name every time). `master` is the main **branch** of
your repository. These names were configured when you first created
the repository -- if you want, you can change them.

We'll explain in more detail what [branching](#branching) means later.
For now, this will be enough to get your partner's updates. All their
changes will have merged with your code, so you're ready to start
making some edits of your own!

### Add

*Adding* a file tells `git` that you want to include that file in the
next commit. After modifying a file, you can add it by typing this:

    git add filename

You can add more than one file at a time. Git also supports wildcard
expansion, so the following are valid

    git add file1.py file2.py
    git add file*.py          # adds all files that start with 'file'
                              # and end in '.py'

If you want to add all modified files at once, you can use the `-A`
flag:

    git add -A

Git also supports some UNIX-like commands:

    git mv filename dest      # records the movement of a file
    git rm filename           # records the removal of a file


You can check which files are waiting to be added and which files have
been added with this command:

    git status

After adding modified files, you are ready to commit those changes.


### Commit

*Committing* changes tells `git` to create a new stage in the revision
history. Think of it as a checkpoint -- if you need to revert to a
previous stage, you'll reset it to one of the previous commits.

To commit changes (you'll need to have [added](#add) changes
first), type

    git commit -m "Your message here"

Git requires commits to contain a brief message. The message should
describe the changes you've made. Make sure the message is concise.

After committing, your changes are still local to your machine. To
make the changes available to collaborators, you need to `push` your
changes.

### Push

To make your changes available to collaborators, you should `push`
your changes:

    git push origin master

Git will prompt you for your Bitbucket credentials. After it's done,
you can go to the website and view your changes!

> **Note**: The `origin` and `master` represent the same things as in
> `git push`.

.gitignore
----------

There might be some files that you don't want to push to the remote
repo. For example, we wouldn't want to clutter our project repo with
the HTML and CSS files. We can create a file in the repo called
`.gitignore` the contains the following lines

    *.html
    *.css
    *.pyc

These three lines tell git to ignore all HTML, CSS, and `.pyc` files
(`.pyc` files are generated in the `__pycache__` directory).

You can commit and push `.gitignore` so that your collaborators also
won't push those files.

Merge Conflicts
---------------

You will occasionally face a **merge conflict** when doing `git pull`.
This occurs if you and your partner modify the same line(s) in a file;
Git won't know which modification should be the final one.

When this happens, Git will notify you of the problem:

    Auto-merging hog.py
    CONFLICT (content): Merge conflict in hog.py
    Automatic merge failed; fix conflicts and then commit the result.

In the example above, there is a merge conflict in the file `hog.py`.
We'll work with this scenario for this example.

> **Note**: non-conflicting changes will have been successfully pulled,
> so you don't need to `git pull` again.

Open up `hog.py` (the conflicted file). After scrolling through the
file, you should see one or more blocks of code delimited in this
fashion:

    <<<<<<< HEAD
    Changes you made
    =======
    Changes your partner made
    >>>>>>> ...

The `...` will either be a long hexidecimal number that represents a
commit ID, or the name of a [branch](#branching).

Next, edit the conflicted code, using your own judgement (obviouslly
you'll want to get rid of the `<<<<<<<` and other delimiters).

Finally, `git add` the conflicted file and `commit` it. That's it! If
you want to push the merge resolution, go ahead.

Revision Selection
------------------

Sometimes, you might want to revert to a previous stage in your
project (e.g. if you made a fatal error that broke your project, or
perhaps you just want to take a quick look at a certain stage of the
projct). Git provides a way to revert back to a certain **commit**.

### Commit logs

First, the following command shows you your local commit history:

    git log

It will display a summary of each commit in the following format:

    commit <ID>
    Merge: 26bdca5 d4670c0
    Author: ...
    Date:   ...

        <commit message>

Remember those commit messages? Those will be how you identify which
backup is the one you want, so make sure you write good messages!

The output of `git log` is displayed in a **pager** like `less` or
`more`, depending on your computer. This allows you to scroll through
the log.

You can also generate a condensed version of the log by using the
following flag:

    git log --pretty=format:'%h %s'

In this case, the string `%h %s` specifies the format to be the commit
ID, then a space, followed by the commit message. You can [customize
the
format](http://git-scm.com/book/en/Git-Basics-Viewing-the-Commit-History).

Once you've found the commit you are looking for, remember its ID
(technically, it's called a *hash*) -- this is the long hexidecimal
number found in the line

    commit ...

It's okay to remember only the first few digits of the ID, as long as
you remember at least 4 digits (7 digits is a good rule of thumb) and
those digits are unambigious (can't refer to more than one commit).
For example, the following ID

    d615a5e7612794621f0ab192271ad13b2aaac43d

can be shortened to just `d615a5e`.

You can run the following command to double-check that the ID refers
to the correct commit:

    git show d615a5e    # replace the ID with your own

Remember what the commit ID is, because we will be using it soon.

### Revert

The following command will undo committed changes:

    git revert <commit ID>

Changes that were made during `<commit ID>` will be "discarded." There
are two important aspects of `revert`:

* `revert` does **not** reset your project to its state at `<commit
  ID>`. Instead, it simply undoes changes introduced by `<commit ID>`.
  It will appear as if you never made that commit, but all commits you
  made after it will still be reflected in your project.
* `revert` creates a *new commit* -- it does not delete an old commit.
  Git finds out what changes have to be made in order to undo the
  specified commit, and makes a new commit reflecting these changes.

If you want to undo changes made by a range of commits, you can do

    git revert <ID 1>..<ID 2>

For example, if you want to undo all commits after a certain point,
you can do

    git revert d615a5e..HEAD

An explanation can be found
[here](http://www.atlassian.com/git/tutorial/undoing-changes#!revert).

> **Note**: the two properties above make `revert` a safe and useful way
> to selectively undo a change:

* If you just want to get rid of a small bug that was introduced at a
  certain point (but still leave all following changes intact), you
  can do so with `revert`
* Because `revert` doesn't delete old commits, you can always go back
  (undo the undo).

### Checkout

If you just want to revert a single file, you can use the `checkout`
command:

    git checkout <commit ID> <file>

For example, if we want to restore `hog.py` to what it was during the
commit `d615a5e`, we would do

    git checkout d615a5e hog.py

This will overwrite our current `hog.py` file with its former state,
and we can go ahead and edit it like normal.

If it turns out we didn't want to revert `hog.py` after all, we can
get back our most recent version (assuming we haven't committed yet):

    git checkout HEAD hog.py

`HEAD` represents the most recent commit.

Branching
---------

Branching offers a way to work on different parts of your project
without interfering with the changes of other people. For example, if
you are revising your solution to Q5 of the Hog project, you might not
want to change the original solution just yet (in case your new one
breaks!). This is where branching comes in.

The Git website has a good
[tutorial](http://git-scm.com/book/en/Git-Branching-Basic-Branching-and-Merging)
for branching.

Branching usually follows a couple of steps:

1. Create the branch
2. Edit code on that branch
3. Merge branches

Before we go into details, let's introduce the `branch` command:

    git branch

Without any additional arguments, `git branch` displays all the
branches in your repo, as well as which one you're currently in. The
output will look something like this:

    * master

This tells you there is only one branch so far, and the `*` means you
are in the `master` branch.

### Creating a branch

Continuing with the Hog Q5 scenario, let's create a branch:

    git checkout -b q5

This creates a *local* branch called `q5` and immediately switches to
it. This is a shortcut for

    git branch q5
    git checkout q5

As a sanity check, type in `git branch`. You should see that you now
have two branches, and that you are in the `q5` branch:

      master
    * q5

You can now edit your code, and the changes will not affect the main
`master` branch. You can still do `add` and `commit`. The commit will
only affect the current branch.

> **Note**: you have not created a *remote* branch yet -- i.e. no one
> else can see the new branch you created. It is only local to your own
> machine.

### Switching between branches

You might need to switch back to the `master` branch to work on
something else. To do this, type

    git checkout <name of branch>

This will switch you to the specified branch. For example, if you want
to switch back to the `master` branch, type

    git checkout master

Make sure that, when you are `git pull`ing from a [remote
server](#pushing-and-pulling-branches) (such as Bitbucket), you should
be in the correct *local* branch.

### Merging branches

After implementing and testing our new solution for Q5, we can
incorporate it into our main project. To do this, we merge (make sure
you've committed all changes on the q5 branch):

    git checkout master
    git merge q5

Now, the `master` branch and the `q5` branch point to the same commit
stage -- in other words, the `master` branch contains all the changes
you made on the `q5` branch!

You can check which branches have been matched to your current branch:

    git branch --merged     # lists merged branches
    git branch --no-merged  # lists unmerged branches

You may want to continue working on the `q5` branch (maybe you want to
try out another solution), so you might want to keep it around. If you
want to delete the branch, however, you can type

    git checkout master
    git branch -d q5

### Pushing and Pulling branches

Up until now, all the branches we've created are local to our own
computer. To share a branch with your collaborators, you need to push
it:

    git checkout q5       # make sure you're in the right local branch
    git push origin q5

To retrieve a branch that you don't have yet (let's call it `q10`),
you can do

    git checkout -b q10   # create a local q10 branch
    git pull origin q10

In general, make sure you are in the correct local branch before you
pull from the server.

To delete a remote branch, type

    git push origin :q10  # deletes the Bitbucket q10 branch

For more information, see [this
link](http://git-scm.com/book/en/Git-Branching-Remote-Branches).
