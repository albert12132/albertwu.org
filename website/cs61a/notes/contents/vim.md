~ title: Vim

Introduction
------------

Vim is a *mode-based* editor, meaning it has different modes with
different behaviors. To use Vim, you switch between modes depending on
what you want to do.

It often takes time to get used to this feature. You might ask why we
bother having modes in the first place. However, you'll find that,
with practice, switching between and using different modes becomes
effortless and makes coding much faster.

> One **note** before we begin: when first learning Vim, you'll be
> tempted to use your mouse and/or the arrow keys. **Don't do it**. The
> whole point of using Vim is to "throw away the mouse" -- you'll find
> that, after some practice, using Vim's shortcuts will be more
> productive.


Getting Vim
-----------

Vim is already installed on the instructional machines (i.e. your
class account), but it behaves strangely by default. To fix this, type

    echo "set nocompatible" > ~/.vimrc

This creates a file in your home directory called `.vimrc`, which is
Vim's [configuration file](/public/vimrc.html). The `.vimrc`
will contain one line that says `set nocompatible`, which tells Vim
not to be compatible with Vi, Vim's predecessor.

You can also get Vim on your own machines. The download site is
[here](http://www.vim.org/download.php).


### Linux

You can use your package manager to install Vim. For Ubuntu, use the
`apt-get` package manager:

    sudo apt-get install vim

### Macs

OS X comes pre-installed with Vim. If you want the graphical user
interface (GUI) version, you can also install
[MacVim](https://code.google.com/p/macvim/).

### Windows

You can find the files to download
[here](http://www.vim.org/download.php#pc). I personally haven't used
Vim on Windows before -- I suspect it won't be as satisfactory as
using it on a UNIX-based machine.


Basics
------

You can start Vim from the command line just by typing

    vim

You can also open a file with Vim:

    vim myfile.py

If you are using the text-based version, Vim will take up your entire
terminal.

Try typing some words. You'll notice what you type is not rendered on
the screen. Vim uses different *modes* -- the mode Vim starts in is
called **normal mode**.

We'll talk more about normal mode in a bit. Students usually find it
reassuring to know how to type text first. The mode for regular
editing is called **insert mode**. To switch from normal mode to
insert mode, press the letter `i`. Now try typing -- text should be
showing up.

To save the file, we need to return to normal mode. To do so, just
press the `ESC` button. Next, type the following:

    :w

that is, a colon followed by the letter `w` (for `w`rite). After
pressing `Enter`, your file will be saved.

To exit Vim, go to normal mode and type in

    :q

If there are unsaved changes, Vim will prevent you from exiting. You
can either save the changes, or if you want to quit without saving,
add an exclamation mark after the command:

    :q!

And there you have it -- a (very, very, very) basic work cycle in Vim!

> **Note**: you might have noticed that pressing the `ESC` key every
> time you want to switch back to normal mode takes quite a bit of work,
> since the `ESC` key is all the way in the top-left corner of your
> keyboard. Most people who use Vim remap their `ESC` key to something
> else (such as `CAPS` lock).

### Vim Tutor

Vim provides a great built-in tutor to teach you the basics. From the
terminal, type

    vimtutor

`vimtutor` is interactive, and gives you a feel for how to use the
commands.

Modes
-----

You've already seen **insert mode** and **normal mode**. Here is a
full list of modes:

* [Insert mode](#insert-mode)
* [Normal mode](#normal-mode)
* [Visual mode](#visual-mode)
* [Command mode](#command-mode)

There's also an **Ex-mode**, but we won't talk about it here.

Insert mode
-----------

There's not much to say about insert mode. This is where you type like
you would with any other text editor.

Most of the time, you'll be switching between normal mode and insert
mode. To go from insert to normal, just press `ESC`.

There are more options to go the other way, to switch from normal to
insert:

* `i`: start inserting text where the cursor is
* `a`: start inserting text right *after* the cursor
* `I`: insert text at the beginning of the line
* `A`: insert text at the end of the line
* `o`: insert a newline *after* this line and enter insert mode
* `O`: same as lower-case `o`, but inserts a newline *above* this line
* `s`: deletes the character under the cursor and enters insert mode
* `S`: deletes the entire line and enters insert mode

Experiment with each one -- I personally use `i`, `A`, `I`, and `o` the
most.

Normal mode
-----------

Normal mode is used for navigation and manipulating text. There is a
wide variety of commands -- the most frequently used are described
here.

Remember, to enter normal mode, just press `ESC`.

### Navigation

In normal mode, the four basic navigation keys are `h`, `j`, `k`, `l`.

* `j`: down
* `k`: up
* `h`: left
* `l`: right

While you can use the arrow keys, you'll find (with time) that using
`hjkl` is much faster. Trust me, take the time to learn how to use
them -- it'll pay off.

There are lots of other navigation keys:

* words:
    * `w`: moves forward to the beginning of the next word
    * `e`: moves forward to the end of the next word
    * `b`: moves backward to the beginning of the previous word
* sentences (if applicable)
    * `(`: moves backward to the beginning of the previous sentence
    * `)`: moves forward to the beginning of the next sentence
* paragraphs (if applicable)
    * `{`: moves backward to the previous paragraph
    * `}`: moves foward to the next paragraph
* lines
    * `0`: moves to the beginning of the line
    * `$`: moves to the end of the line
* screen:
    * `CTRL-f`: moves an entire "page" down
    * `CTRL-b`: moves an entire "page" up
    * `CTRL-d`: moves half a "page" down
    * `CTRL-u`: moves half a "page" up
* document-level
    * `gg`: moves to the top of the document
    * `G`: moves to the bottom of the document

### Undoing changes

The undo key is `u` -- it undoes any modifications to the text. Vim
remembers several levels of modifications, so you can keep pressing
`u` to undo further and futher back. You can configure Vim to remember
a certain number of levels.

There is also a redo functionality -- to undo an undo, press `CTRL-r`.
Again, Vim will remember multiple levels, so you can redo multiple
times.

### Deleting text

The `x` command deletes a single character:

* `x`: deletes the character right underneath the cursor
* `X`: (i.e. `SHIFT-x`) deletes the character right before the cursor

Using `d` provides more flexibility and range:

* `dd`: deletes the entire line
* `dw`: deletes the rest of the current word, starting from the cursor
* `db`: deletes the beginning of the current word, starting from
  cursor
* `dj`: deletes this line and the next (2 lines)
* `dk`: deletes this line and the previous one (2 lines)
* `D`: deletes from the cursor to the end of the line

I use `x`, `dd`, `dw`, and `D` the most. Of course, play around with
the commands and see which ones you're comfortable with.

> **Note**: Vim's delete functionality acts like *cut* -- Vim remembers
> what you deleted, and you can immediately paste the deleted text.

### Yanking text

*Yanking* is the same as copying text. The primary operator to do so
is `y`:

* `yy`: copy the entire line (`Y` works too)
* `yw`: copy the rest of the current word, starting from the cursor
* `yj`: copy this line and the next

> **Note**: Yanking and deleting use the same buffer to store text, so
> they will overwrite each other.

### Putting text

In Vim, pasting is called *putting* text. The primary key to do so is
`p`:

* `p`: puts copied text right after the cursor
* `P`: (i.e. `SHIFT-p`) puts copied text right before the cursor

> Note that, if you had deleted or yanked an entire line, `p` will place
> the line after the current one, and `P` will place the line before the
> current one.

### Searching

You can initiate a search from normal mode in the following ways:

* `/`: starts a *forward search* -- moving to the "next" match will go
  down the document
* `?`: starts a *backward search* -- moving to the "next" match will go
  up the document

To search for a string, press one of the keys above, and type in the
pattern you want to look for. For example, to search the pattern
"class", type

    /class

and press enter. To move through matches:

* `n`: move to the next match (down if `/`, up if `?`)
* `N`: move to the previous match (up if `/`, down if `?`)

Vim's search uses regular expressions, which can come in handy.

Vim has a [find-and-replace](#find-and-replace) functionality that you can use in Command
mode.

### Replacing text

There are two ways to replace text from normal mode:

* `r`: replaces the character under the cursor. After pressing `r`, type
  the new character, and it will take the place of the old one.
* `R`: enters **replace mode**, which is like pressing the Insert key
  -- it allows you type text, but replaces existing text.

There are lots of other commands in normal mode -- look for them on
the internet.

Visual mode
-----------

Visual mode is used for selecting and highlighting text. There are
several ways to switch from normal mode to visual mode:

* `v`: enters regular visual mode.
* `V`: (i.e. `SHIFT-v`) highlights entire lines at a time.
* `CTRL-v`: "block" visual mode

In each visual mode, you can use normal mode commands for various
things:

* navigation (`hjkl`, `w`, etc.)
* deleting and yanking: `d` will delete all highlighted text; `y` will
  yank the highlighted text. Both then return to normal mode
* replacing (`r`): replaces all highlighted characters with a new
  character (`R` just deletes the lines of the highlighted text)

In this way, visual mode is useful for moving large bodies of text
around. I usually use line-visual mode (`V`) instead of regular visual
mode.

### Block visual mode

You'll notice that in regular visual mode, navigating up and down will
highlight all text on the line. "Block" visual mode highlights a block
of text. The best way to understand it is to try it: from normal mode,
type `CTRL-v`, and then press `k` to go up -- notice that it literally
highlights the character above the cursor, without any of the other
characters on the line!

Command mode
------------

Vim supports a command line similar to your terminal, except the
commands are specific to Vim. To enter command mode from normal mode,
press `:` (the colon). At the bottom of your screen you should see a
`:` appear. Now you can type in a Vim command.

There are tons of Vim commands out there, so we'll only cover a few of
the most frequently used ones.

* `:w` saves the file. You can also save the file with a name by
  typing `:w filename`
* `:q` quits Vim. If you have unsaved work, Vim will warn you. To
  ignore the warning, following the command with a `!`, like `:q!`
* `:x` saves and quits Vim in one command.

There are commands for doing terminal work:

* `:sh` switches to the terminal. This is useful if you need to
  naviagte through your filesystem or execute some UNIX commands.
  (Note: `:sh` opens up a new process)
* `:!unix command` executes a single UNIX command (for example, to
  `ls` your current directory, type `:!ls`)

These two commands come in handy; for example, if you want to run a
doctest, you can type

    :!python3 -m doctest %

and it will run the doctests for the file you are currently working on
(the `%` is a special character in Vim that stands for the name of the
current file).

Finally, there's the help utility:

* `:help feature` brings up Vim's help documentation on the
  specified feature

As you use Vim more, you can look up different features and how they
work.

### Find and replace

As mentioned above, Vim also has a find-and-replace utility. It
behaves like the UNIX program `sed`, so it has regular expression
capabilities. To get the full benefit of Vim's `sed`-like utility, you
should take the time to learn both regular expressions and `sed`.

However, for a simple find-and-replace job, the following command will
suffice:

    :%s/search pattern/replace pattern/g

The `:` indicates that this is a Command mode utility. There are a
couple of characters to be aware of:

* `%`: tells Vim to search the entire document. You can also specify a
  range of lines. You can even highlight text in Visual mode, and
  press `:s` to begin find-and-replace for just the highlighted text
* `s`: stands for "substitute." The `s` should follow the range.
* `/`: the forward slashes are delimiters that separate the different
  fields. Technically, you can replace the `/` with any character you
  want, as long as you are consistent -- for example, you can do
  `:%s_search pattern_replace pattern_g`, but then any unescaped `_`s
  in the search and replace patterns will be interpreted as
  delimeters.
* `g`: an optional argument, `g` stands for "global" and tells Vim to
  find-and-replace all instances on a line. If you omit the `g`, Vim
  will only find-and-replace the first instance of the search pattern
  on each line.

Some example usage:

    # finds all instances of "def" and replaces them with "class"
    :%s/def/class/g

    # finds all instances of "TODO" and deletes them
    :%s/TODO//g

    # finds "foo" between lines 403 and 411 and replaces with "bar"
    :403,411s/foo/bar/g

Multiple Windows
----------------

When working on large projects, it is useful to have multiple files
open at the same time. You can always open multiple terminals, but
that can get annoying. Vim supports multiple windows.

There are two ways to open windows from command mode:

* `:split` opens up a horizontal window. By default, the window
  contains the same file you are editing, so you can view the same
  file from different places at the same time.
* `:vsplit` is the same as `:split`, but opens a vertical window

Both `split` and `vsplit` can also open up a new file by following the
command with the file name

    :split filename
    :vsplit filename

To navigate between windows, type `CTRL-w`, followed by one of the
`hjkl` keys.

To close a window, move to that window and quit (type `:q`).

.vimrc
------

To configure Vim, you can create a file called a `.vimrc` (the `.`
hides the file from a normal `ls` command, but it is still there).
Learn more [here](vimrc.html).
