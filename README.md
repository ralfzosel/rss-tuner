
# rss-tuner

You can email your latest blog post using Mailchimp. The RSS feed provided by WordPress may contain HTML elements that cause layout issues in the email:

- Images appear full width
- Code formatted as "pre" appears as a single line

Both can cause a horizontal scrollbar in the email.

This Python script solves these problems by fine-tuning such HTML elements.


## Installation

First, you need Python, of course. On a Mac, it works best with Homebrew. I prefer pyenv because it can handle different versions of Python on the same machine.

Download the files above from GitHub (or use git clone https://github.com/ralfzosel/rss-tuner.git).

Usually, for Python, a virtual environment is recommended. This can be done with venv or via pyenv (see above).


## ToDo

- Upload RSS feed to the webserver via SFTP