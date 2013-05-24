~ Vimrc ~

The `.vimrc` is [Vim]({{ NOTES_DIR }}/vim.html)'s configuration file.
After you get used to using Vim, you can start customizing it by
adding lines to `.vimrc`.

Location
--------

The `.vimrc` file goes in your home directory. The `.` at the
beginning will hide the file from a normal `ls` UNIX command (so as
not to clutter), but it is still there. You can edit the file from vim
itself:

    vim .vimrc

Sample vimrc
------------

You can find my `.vimrc` file [here]({{ NOTES_DIR }}/public/vimrc).

Syntax
------

To turn on syntax highlighting, add

    syntax on

You can change the colorscheme (replace `desert` with any other
colorscheme):

    colorscheme desert

Indentation rules for different filetypes can be set:

    filetype plugin indent on

Settings
--------

The first thing you'll want to do is

    set nocompatible

This turns of Vi compatibility. This is especially important if you
are using Vim on your class account.

**Note**: the `"` (double-quote) character begins a comment in
VimScript.

### Miscellaneous

    set noerrorbells    " Gets rid of beeping sound

### Dimensions

    set lines=50        " Vim starts with this many lines
    set columns=80      " You can change these numbers
    set textwidth=80    " This sets the 'virtual' line number

The `textwidth` setting is useful when writing paragraphs (such as in
LaTeX), as it automatically forces overflowing text onto a newline. It
can be distracting when writing code, however, so you can always omit
it.

### Information

    set showcmd         " Show (partial) command in status line
    set showmode        " Show the current mode
    set laststatus=2    " Always show status line

The status line can contain useful information. For a full list of
things you can put there, type the Vim command `:help statusline`.
Here is the one I use:

    set statusline=%.40F%=%m\ %Y\ Line:\ %3l/%L[%3p%%]

The full filepath is displayed on the left, and various things are
displayed on the right -- whether or not the file has been modified,
the filetype, the line number, and the percentage through the file.

### Navigation

    set nu              " Set line numbering
    set scrolloff=5     " Keep at least 5 lines above/below cursor
    set mouse=a         " Enable mouse usage in all modes
    set mousehide       " Hide the mouse when typing

I personally like `scrolloff` because it allows me to see ahead, but
it can be distracting for some people.

### Searching

    set ignorecase      " Do case insensitive matching
    set smartcase       " Unless you explicitly search for upper case
    set incsearch       " Incremental search
    set hlsearch        " Highlight searches
    set showmatch       " Show matching parentheses

### Tabs

    set expandtab       " Uses spaces instead of tabs
    set tabstop=4       " Each tab is 4 spaces
    set shiftwidth=4    " Sets the >> and << width
    set autoindent

### Backups

    set nobackup        " remove backup files
    set noswapfile      " remove swap files

Only set these if you don't want backup files. Some people find them
useful.

Key bindings
------------

There are a couple of key-binding commands:

* `map`: a simple map
* `remap`: a "recursive map", which means that mappings are influenced
  by previous mappings
* `noremap`: a "non-recursive map", which means mappings are *not*
  influenced by previous mappings

For mode-specific bindings, add a letter before each command. For
example, normal mode mappings are done with `nmap`, `nremap`, and
`nnoremap`.

Normal Mode Key Bindings
------------------------

    nnoremap ; :              " Enter command mode faster

### Windows

    nnoremap <C-k>  <C-w>k    " Move along windows faster
    nnoremap <C-j>  <C-w>j
    nnoremap <C-h>  <C-w>h
    nnoremap <C-l>  <C-w>l

### Line movement

    nnoremap j      gj        " Move along rows, not lines
    nnoremap k      gk        " Useful for long lines
    nnoremap 0      g0
    nnoremap $      g$

### Screen centering

    nnoremap <space>  zz      " Centers screen around cursor
    nnoremap n        nzz
    nnoremap N        Nzz

Command Mode Key Bindings
-------------------------

The following alias accidental shifts:

    cnoremap W<CR> w<CR>
    cnoremap Q<CR> q<CR>
    cnoremap X<CR> x<CR>
    cnoremap Sh<CR> sh<CR>
    cnoremap sH<CR> sh<CR>
    cnoremap SH<CR> sh<CR>

