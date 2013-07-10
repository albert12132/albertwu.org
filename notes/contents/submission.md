~ title: Submitting Assignments ~

This is a guide on the homework/project submission process we use in
61A.

Class Accounts
--------------

In 61A (as with many courses at Berkeley), you will need a **class
account** in order to submit assignments. At the beginning of the
semester, you will be given a sheet of paper with the following
information:

* **Username**: will be of the form `cs61a-xx`, where `xx` is unique
  to every student
* **Password**: needed to login

Upon receiving the class account, you should login and change the
password. You can do this by running

    ssh update

from the terminal; then follow the instructions on the screen.

Starting an Assignment
----------------------

In 61A, all assignments will be posted on the course website. There
will always be a page specifically for the assignment that you can
view from your browser -- this page will have all the instructions for
that assignment.

We will also provide you a template Python file for each assignment
(e.g. `hw1.py`). You should download this template, and write all your
code here (think of this as a worksheet that you will turn in).

Writing the Assignment
----------------------

You can write your code on your own computer, or you can write it on
your class account -- it's up to you. Most students find it more
convenient to write homework and projects on their own computer. There
are various text editors with which you can do this:

* [Emacs](http://www.gnu.org/software/emacs/): the editor we showed
  you on the first day of lab
* [Vim](http://www.vim.org/download.php): you can learn more about
  Vim [here]({{ NOTES_DIR }}/vim.html)
* [Sublime Text](http://www.sublimetext.com/2): a very, very popular
  choice among students
* [Notepad++](http://notepad-plus-plus.org/): a solid choice for a
  text editor
* [Eclipse](http://www.eclipse.org/downloads/): a heavyweight IDE.
  You'll need to download a plugin for Python. Eclipse has many
  features that are not necessary for this class
* IDLE: an editor provided with Python. **The staff does not recommend
  using IDLE, since it has some bugs.**

### Testing your code ###

Whenever you are writing homework or a project, you **test your code
frequently**. This ensures that you are at least on the right track.
You can run doctests with the following command from your terminal:

    python3 -m doctest hw1.py

where you can replace `hw1.py` with the name of the file. The projects
usually have some additional testing mechanisms. I can't stress this
enough: **always test your code before you submit your assignment.**

Copying the assignment to your class account
--------------------------------------------

Once you are done writing your assignment and finished testing, the
next step is to copy your assignment to your class account. Exactly
how you do this depends on your operating system (OS):

* **Macs and Linux**: from your terminal, use the `scp` command:

    scp hw1.py cs61a-xx@star.cs.berkeley.edu:~

  where `xx` is your login. You can use any other Berkeley server to
  login, and you can transfer your file to any directory on your class
  account. A more general format for the command is the following:

    scp path/to/assignment.py cs61a-xx@servername.cs.berkeley.edu:path/on/class/account

  where `servername` is a [Berkeley
  server](http://inst.eecs.berkeley.edu/cgi-bin/clients.cgi?choice=servers).

  After executing the command, you will be prompted for your password.

* **Windows**: you will have to install
  [WinSCP](http://winscp.net/eng/download.php). There are more
  instructions on how to use WinSCP in the resources section of the
  course website.

**Note**: copying your file over to your class account does NOT mean
you have finished submitting. See the next step to complete the
process.

Submitting the assignment
-------------------------

First, login to your class account. Again, depending on your OS, how
you login will be different:

* **Macs and Linux**: from your terminal, use the `ssh` command:

    ssh cs61a-xx@star.cs.berkeley.edu

  Again, you can replace `star` with the name of any Berkeley server.

* **Windows**: use
  [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)
  to login; there instructions on how to use PuTTY in the resources
  section of the course website.

Once you've logged on, follow this procedure:

1. Create a directory for the assignment and move your `.py` file into
   the new directory:

    mkdir hw1
    mv hw1.py hw1

2. Go into the new directory

    cd hw1

3. Run the `submit` script:

    submit hw1

  where `hw1` is replaced with the name of the assignment. For
  projects, the assignment name will be `proj1` for Project 1,
  `proj2` for Project 2, and so on.

  During submission, we will usually perform a **sanity check** on
  your file -- this sanity check **only checks for syntax errors**. It
  does NOT check the correctness of your code. You should have checked
  that yourself by running doctests.

4. After submitting, you should run the following command:

    glookup -t

  This will show you timestamps of all your submissions. If your
  latest submission shows up, then you'll know we've received your
  submission. If it doesn't show up, run `submit` again.

**Note**: to make the grading process easier for us, only **one
partner** should submit projects.

Checking your grade
-------------------

You can check your grades with the following command (from your class
account):

    glookup

This will list your scores for all assignments. If you have a `---`
for an assignment, it means you haven't received a score for that
assignment yet.

You can also see how the entire class did by running

    glookup -s hw1

where you can replace `hw1` with the name of the assignment.
