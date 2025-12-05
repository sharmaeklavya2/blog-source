title: A Comprehensive Guide to Customizing your MacBook
slug: customize-macos
date: 2019-07-12
modified: 2024-08-08
summary: This post contains a list of all the things I did to customize my MacBook. Most instructions here are useful only for programmers and power users.


I recently got a new laptop - a MacBook Air!
I customized it so that it's easy for me to use.
Major changes include:

* Moving data from my old laptop to my new laptop.
* Installing and configuring software for basic necessities, programming and writing content.
* Setting up a nice environment on my [terminal](https://en.wikipedia.org/wiki/Terminal_emulator).

As I made all these changes to my new laptop, I noted down the steps that I took for future reference.
I think they could be useful to others, so here they are, as a blog post.

This post is written for macOS Mojave.
You may have to modify some instructions if you're using a newer macOS.
If you're not using macOS, you can still get a similar working environment on Linux,
but you'll have to make major modifications to the instructions below.

You can also refer to this [dependency graph]({static}/img/macos-customize-graph.dot.svg)
([source code]({static}/img/macos-customize-graph.dot)).

[TOC]


## Basic setup

* **Connect to a WiFi network**, since we'll be downloading a lot of stuff.
* **Update your OS**.
* macOS will offer a **tour of the OS**. Take that if you're new to macOS.
* **Remove useless apps from dock**: right-click on the app in the dock, go to Options and uncheck 'Keep in Dock'.

### System Preferences

Click the Apple logo in the top-left corner of your screen and choose 'System Preferences'.
Here you can customize most aspects of your operating system.
If you have the time, go through each of the items and choose the options which make sense to you.
These are the changes which I made:

* General: Use dark theme (Appearance: Dark).
* Dock:
    * Position on screen: Left.
    * Uncheck 'Show recent applications in Dock'.
* Language and Region: Select 'English (US)' as the primary language.
  I live in India, so the default was 'English (India)',
  but I changed it because I generally follow US spelling.
  I don't want my spell-checker to highlight 'color' and 'center' as misspelled words.
* Keyboard: Input Sources: Hide input menu in menu bar.
* Display: Choose Resolution as Scaled and choose the large size.
* Bluetooth: Show Bluetooth in menu bar.
* Sharing:
    * Change hostname. The hostname shows up in the terminal prompt, so I want it to be short.
    * Allow remote login via SSH.
* Siri: Disable Siri. I rarely use it.
* Date and Time: In the 'Clock' tab, check 'Display time with seconds' and 'show date'.
* Accessibility: Siri: 'Enable type to Siri' if you don't want to disable Siri
  but want to talk to it by typing instead of speaking.

### Finder preferences

Finder is the file manager in macOS.

* Finder preferences (`Cmd + ,`):
    * General: Show hard disk and connected servers on desktop.
    * Sidebar: Select useful locations.
    * Advanced:
        * Show all filename extensions.
        * Keep folders on top in windows.
        * Search current folder when performing a search.
* Go to 'View' in Finder's menu bar:
    * Show view options (`Cmd + J`): 'Sort by Name' and 'Use as Defaults'.
    * Show path bar.
* Press `Cmd + Shift + .` to enable viewing hidden files.

### Install Google Chrome and sync profile

I prefer Google Chrome over Safari.
I made Chrome the default browser.
I also synced my account to get all my bookmarks and extensions.

### TextEdit preferences

TextEdit is the default plain-text and rich-text editor bundled with macOS.

I usually use <a href="https://en.wikipedia.org/wiki/Vim_(text_editor)">Vim</a> for text editing.
Vim is far superior to TextEdit in terms of advanced functionality,
like customizability, syntax highlighting, find-and-replace, etc.
But having a lightweight GUI text editor can be handy.

TextEdit preferences (`Cmd + ,`):

* Format: plain text. This is needed to prevent new instances of TextEdit from opening a rich-text editor.
* Font: Menlo, size 16.
* Disable 'Correct spelling automatically'.
* Display HTML files as HTML code.
* Disable 'add .txt extension to plain text files'. This is needed if you have to edit extensionless files.


## <span style="background-color: rgba(255, 204, 0, 0.3)"/>Terminal and Shell</span>

If you're an aspiring programmer or power user, you should get to know the command-line.
For this blog post, I'm going to assume that you know how to run commands from the shell and
you know the meaning of the following words:
terminal emulator, shell, prompt, home directory, current working directory.
In case you don't, here's a nice short tutorial by TreeHouse:
[Introduction to the Mac OS X Command Line](https://blog.teamtreehouse.com/introduction-to-the-mac-os-x-command-line).

### Terminal preferences

Terminal.app is the default terminal emulator on macOS.
But I recommend a better alternative, like [iTerm2](https://www.iterm2.com/features.html).
I use iTerm2 with the _Solarized_ color scheme.

In iTerm2, you may want to configure <kbd>Option</kbd> + arrow keys to move over words,
just like in Terminal.app. To do this, go to Settings > Profiles > Keys > Key Mappings,
and select 'Terminal.app Compatibility' as the preset.

If you decide to stick to Terminal.app, that's also not a bad option.
If you want to use the Solarized color scheme on Terminal.app,
you'll need to download and install it:

1.  Download the [Solarized dark theme for Terminal.app](https://raw.githubusercontent.com/tomislav/osx-terminal.app-colors-solarized/master/Solarized%20Dark.terminal). Open it in finder and double-click on it.
2.  macOS will say that the file cannot be opened because it is not from an identified developer.
Go to 'System Preferences > Security > General' and press 'Open Anyway' (don't worry; it's not an executable).
3.  Open terminal, 'Preferences > Profiles', select 'Solarized Dark' and press the 'Default' button.
Now restart Terminal.app and you'll see the dark blue background of the Solarized color scheme.

Additionally, you may want to deselect 'restore text when reopening windows'
in the 'Preferences > Profile > Window' tab in Terminal.app.

### Installing [Xcode command-line tools](http://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/)

The 'Xcode command-line tools' consist of command-line applications that are
very common in Unix-like environments, like git, gcc, make, perl.

Run `xcode-select --install` from a terminal.
A dialog box will pop up. Select install.
You should probably connect to a power source before doing this
because macOS is going to suggest you do so.

### Dotfiles

Dotfiles colloquially refers to configuration files placed in the home directory.
These files' names start with a dot (`.`).
Common examples are `.bash_profile`, `.vimrc` and `.gitconfig`.

I have put all my dotfiles in a Github repository at
[`sharmaeklavya2/dotfiles`](https://github.com/sharmaeklavya2/dotfiles).
You can find detailed instructions for setting them up in the repository's readme.
Here is a brief version:

    git clone https://github.com/sharmaeklavya2/dotfiles.git
    cd dotfiles
    ./scripts/make_links.py
    shopt -s dotglob nullglob
    mv _links/.bashrc _links/.bash_profile
    mv _links/* ~

Now either restart your terminal or run `source ~/.bash_profile`.
If you executed the above instructions correctly,
the first thing you'll notice is the improved, colorful prompt.

My dotfiles are written with the Solarized terminal color scheme in mind.
If you're not using Solarized, you should modify `.vimrc` accordingly:
either remove `colorscheme solarized` or pick a different colorscheme,
like [one](https://github.com/rakr/vim-one).

I also recommend using the `git-prompt.sh` utility script, which will display useful information
about git repositories (like branch, dirty status, etc) in your prompt.
To do this, download [git-prompt.sh](https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh)
to `~/ext_bin/git-prompt.sh`. The `~/.bash_profile` will use it to modify the prompt.

I also recommend adding the lines `export HISTSIZE=100000` and `export HISTCONTROL=ignoredups`
to either `~/.env` or `~/.bash_profile` to increase your shell input history size
and remove consecutive duplicates.

### Install [Homebrew](https://brew.sh/)

Homebrew (a.k.a. brew) is a package manager, which means it's like a terminal version of the App Store.
You can install programs (called packages by brew) by simply writing commands on the terminal:

    brew install name-of-package

According to [brew's website](https://brew.sh/), brew can be installed by typing this into the terminal:

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

Installation may require superuser permissions.

### Install [tmux](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/)

I usually need multiple shells to be open.
I can use Terminal.app's 'tabs' (`Cmd + T`) to achieve this.
But I use tmux instead since it has more features.
Also, if you SSH to a server that has tmux installed,
you can open multiple shells on the server on a single SSH session.

To install, run `brew install tmux`.

Brew will check for updates every time you run it.
To prevent that from happening, add `export HOMEBREW_NO_AUTO_UPDATE=1`
to `~/.bash_profile` or `~/.env`.


## <span style="background-color: rgba(0, 255, 102, 0.3)">Install command-line programs</span>

### MacTex

MacTex is a suite of programs for typesetting documents using TeX and LaTeX.
LaTeX is a great system for writing professional-looking mathematical documents.

You can install MacTex using a GUI installer, but I did it using `brew install --cask mactex`.

### Python and packages

macOS has Python 2 pre-installed, but we should use Python 3, since
[Python 2 will reach EOL](https://www.anaconda.com/end-of-life-eol-for-python-2-7-is-coming-are-you-ready/)
on Jan 1, 2020.

Run `brew install python3`. That will install `python3` and [`pip3`](https://pip.pypa.io/en/stable/).

I use [python virtual environments](https://docs.python.org/3/tutorial/venv.html).
I use one big virtualenv where I install all commonly used packages,
and I create application-specific virtualenvs for large applications that I'm developing.

Run `python3 -m venv /path/to/venv/` to create a python3 virtualenv.

Activate the virtualenv using `source /path/to/venv/bin/activate`.
Now all python commands and applications you run will use this virtualenv.

I usually install python packages only when required,
but some are useful enough that I installed them in the beginning:

    pip install ipython requests jinja2 pipdeptree flake8 grip

These packages are useful for math and computation:

    pip install numpy scipy pandas matplotlib seaborn sympy

### Other useful programs

* Although git is provided by the Xcode command line tools,
a more recent version can be obtained using `brew install git`.
* To be able to write and run Java programs, install openjdk: `brew install openjdk`.
* Node.js and npm: `brew install node`.
* Other useful programs that can be `brew install`ed:
[`diffr`](https://github.com/mookid/diffr/),
[`dos2unix`](https://linux.die.net/man/1/dos2unix),
[`htop`](https://en.wikipedia.org/wiki/Htop),
[`rlwrap`](https://github.com/hanslub42/rlwrap/),
[`graphviz`](https://graphviz.org),
[`ffmpeg`](https://ffmpeg.org),
[`pandoc`](https://pandoc.org),
[`youtube-dl`](https://github.com/ytdl-org/youtube-dl/).


## <span style="background-color: rgba(0, 136, 255, 0.3)">Transfer backed-up data</span>

### Reorganizing data and backup

There are many places where I store my files:

* My laptop's SSD (which is small enough for all my files to not fit on it).
* My external hard drive.
* My [Dropbox](https://www.dropbox.com/) account.
* [My Github repositories](https://github.com/sharmaeklavya2).
* My Android phone.

Some of my files are stored on more than one of the above locations.
Sometimes the files on one storage medium get updated but not others.
This made it very difficult for me to manage them without the risk of accidentally losing some files.

To mitigate this problem, I did a massive reorganization of my files before moving them to my new laptop.
I organized them into folders based on the kind of content and access patterns
and demarcated which folders will be on which storage mediums.

I moved my frequently-changing content to Dropbox.
I use the Dropbox desktop app which syncs my files online in real-time.
On my external hard drive, I have an up-to-date backup of content that rarely changes.

If you use git for your code, make sure to push all unpushed code on your old computer
to an online remote to avoid losing data.

### NTFS drivers for macOS

My external hard drive is NTFS-formatted, but macOS cannot write to NTFS drives; it can only read from them.
This was problematic when I was transferring my files from my old laptop (which was also a MacBook)
to my external hard drive. There are 3 options available:

* Somehow reformat the external drive to FAT32 without losing data.
* Install an open-source NTFS driver.
It's hard to make them work and you have to mount/unmount via command-line.
* Install a paid NTFS driver, like [Paragon](https://www.paragon-software.com/home/ntfs-mac/).
These work seamlessly, but are either expensive or offer a limited-time trial version.

Fortunately, my external hard drive was a Seagate product.
Seagate offers a [free-of-charge version of Paragon's NTFS driver](https://www.seagate.com/in/en/support/downloads/item/ntfs-driver-for-mac-os-master-dl/)
which only works on Seagate drives.

### Install Dropbox and use symlinks

I installed [Dropbox's desktop app](https://www.dropbox.com/install) on my new laptop.
This app creates a directory at `~/Dropbox` and downloads all your online content into it.
Anything you put in this directory will get synced to your online account.

Dropbox has the limitation that it will only sync files inside `~/Dropbox`.
If I ever change my mind about what to sync, I'll have to move things in and out of `~/Dropbox`.
If you're a command-line user, you'll know how annoying it can be to change frequently-used paths.

To solve this problem, I placed all my files outside `~/Dropbox`
and created [symlinks](https://kb.iu.edu/d/abbe) to them which I placed in `~/Dropbox`.

**Edit**: This no longer works, since
[Dropbox removed support for using external symlinks](http://www.paulingraham.com/dropbox-and-symlinks.html).
Now I place my files inside Dropbox and created symlinks to access them from outside `~/Dropbox`.

### Wallpapers and profile picture

After transferring files from my external hard drive to my new laptop,
I configured macOS to use my custom wallpapers instead of the system-default ones
and use my profile picture on the lock screen.


## <span style="background-color: rgba(255, 0, 0, 0.3)">Customize Vim</span>

### Install newer Vim

Although macOS comes with `vim` pre-installed, that version of Vim was compiled without some important features.
You can see which features are installed by running `vim --version`.

Run `brew install vim` to install a newer, better Vim.
Alternatively, you can install MacVim (`brew install macvim`).
This will not replace the old vim; the old vim can still be accessed at `/usr/bin/vim`.

### Get Vim plugins

Go to `~/.vim/pack/default/start` (create this directory if it doesn't exist)
and clone the git repositories of the plugins you need.
You can see the list of plugins that I use at
[`vimpackages.txt`](https://github.com/sharmaeklavya2/dotfiles/blob/master/vimpackages.txt) in my dotfiles.

<!--If you're using my dotfiles, you can run `./scripts/get_vim_packages.py`.
This will download the vim plugins from `vimpackages.txt` and place them in a directory named `vim_bundle`.
[Symlink](https://kb.iu.edu/d/abbe) `vim_bundle` to `~/.vim/bundle`.-->

### Install [YouCompleteMe](https://github.com/ycm-core/YouCompleteMe)

YouCompleteMe is a vim plugin for code auto-completion.
To install this plugin:

* `brew install cmake`
* `cd ~/.vim/pack/default/start`
* `git clone --recursive --depth=1 https://github.com/ycm-core/YouCompleteMe.git`
* `cd YouCompleteMe`
* If you use a python virtualenv, activate it.
* `./install.py`

If you don't switch to the virtualenv before running `./install.py`,
python auto-complete may not work for external libraries installed in that virtualenv.

You should read [the documentation](https://github.com/ycm-core/YouCompleteMe)
for more detailed installation instructions. This is important if you
want good completion for C, C++, Java, Rust, Go or JavaScript
(Python auto-complete works out-of-the-box and I'm okay with rudimentary auto-complete for other languages).

The documentation says that MacVim is required,
but I'm able to use YouCompleteMe with Vim installed via `brew install vim`.

### Fix Vim locale error

You may get error messages like this when you start Vim:

    Warning: Failed to set locale category LC_NUMERIC to en_IN.
    Warning: Failed to set locale category LC_TIME to en_IN.
    Warning: Failed to set locale category LC_COLLATE to en_IN.
    Warning: Failed to set locale category LC_MONETARY to en_IN.
    Warning: Failed to set locale category LC_MESSAGES to en_IN.


Fix this by adding `export LC_ALL=en_US.UTF-8` to `~/.bash_profile` or `~/.env`
([brew forum post](https://discourse.brew.sh/t/failed-to-set-locale-category-lc-numeric-to-en-ru/5092)).


## <span style="background-color: rgba(170, 0, 255, 0.3)">Install Nginx and serve website mirrors</span>

I use [Nginx](https://nginx.org/en/) to serve static content.
It's useful to access local websites that I downloaded or created.

### Install and run Nginx

    brew install nginx
    nginx

Now go to http://localhost:8080. You should see a welcome page from Nginx.

### Enable nginx autoindex

Go to `/usr/local/etc/nginx/nginx.conf` and
add `autoindex on;` to '`http` > `server` > `location /`'.
You may also wish to change the port from 8080 to something else by changing the `listen` value.

Then rename `/usr/local/var/www/index.html` to `/usr/local/var/www/index.html~`.

After making these changes, run `nginx -s reload` for the changes to take effect.

Visit http://localhost:8080 again. Now instead of seeing the welcome page,
you should see the list of files in `/usr/local/var/www`.

Optionally, if you want the index page to look pretty, you can
use the [ngx-fancyindex](https://github.com/aperezdc/ngx-fancyindex) module.
But it seemed a bit too difficult to configure.
So I use the following string-replacement hack to inject my own CSS:

1.  Put `style.css` at `/usr/local/var/www/`. You can put whatever CSS you want in `style.css`.
    You can see my style file in [this gist](https://gist.github.com/sharmaeklavya2/e8808872c4acd462d6cccff4ffa994c9).

2.  Add this to '`http` > `server` > `location /`' in `/usr/local/etc/nginx/nginx.conf`:

            sub_filter '<head><title>Index of' '<head>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta name="color-scheme" content="light dark" />
        <link rel="stylesheet" href="/style.css" />
        <title>Index of';
            sub_filter_once on;

### Serve my websites with Nginx

I had backed up compressed archives of my websites to my external hard disk.
I copied the websites from there, uncompressed them, and placed them in `/usr/local/var/www`.

You can put symlinks in `/usr/local/var/www`, but `/usr/local/var/www` itself cannot be a symlink.

### Security

Anyone on your network can see your files in `/usr/local/var/www`,
so you should be careful about what you put there to preserve your privacy.

You can [set password authentication for Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-password-authentication-with-nginx-on-ubuntu-14-04),
but if someone is eavesdropping, they can
[easily recover your password](https://en.wikipedia.org/wiki/Basic_access_authentication#Security).

If you want to prevent others on your network from accessing the http server,
you can restrict Nginx to work on `localhost` only.
To do this, go to `/usr/local/etc/nginx/nginx.conf` and
change `listen 8080;` to `listen localhost:8080;`.
This is somewhat secure, but not secure against a talented attacker
(see <https://security.stackexchange.com/q/86773>).
