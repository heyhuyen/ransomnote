# Ransom Note

A simple web app for generating ransom messages using [Python](http://www.python.org) and [web.py](http://webpy.org). An exercise in my quest to learn web programming.

Written during [Hacker School](https://www.hackerschool.com/), Batch[4], Fall 2012.

## Can I play with it?
Sorry, I don't have it hosted anywhere, so to play with it you will have to run it on your local machine.

### You will need:
- [Python](http://www.python.org) and [web.py](http://webpy.org/install)
- a clone of this repo: `git clone https://github.com/heyhuyen/ransomnote.git`
- a sqlite3 database named `scrapfont.db` with the following table:
        CREATE TABLE letters(id integer primary key autoincrement, letter text not null, ext text not null);

## Usage
From top directory, run `python bin/app.py`and open up your browser to `http://localhost:8080/`

#### Upload letters
1. Type a letter into the textfield.
2. Select a file to upload.

#### Make a ransom note
Type your message in the textfield! Letters not found will display a rather ugly default image.

## Todo/Extensions
- uploading letters: auto-resize images
- uploading letters: in-browser image editing to select multiple characters
- uploading letters: auto-character detection would be really cool
- uploading letters: allow only single characters or provide a dropdown list
- making ransom note: allow punctuation and symbols: `!`, `?`, `.`, etc.
- making ransom note: handle `\n` and allow text alignment
- save message to image format
- make it pretty 

## Troubleshooting
from [Learn Python The Hard Way, Ex 52](http://learnpythonthehardway.org/book/ex52.html): "Before you run `bin/app.py` you need to change your `PYTHONPATH` environment variable."

`export PYTHONPATH=$PYTHONPATH:.`

For Windows PowerShell: `$env:PYTHONPATH = "$env:PYTHONPATH;."`
