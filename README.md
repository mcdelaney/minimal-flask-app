# minimal-flask-app

## What is this?
An extremely minimal app for the purposes of teaching Flask to person unfamiliar with both python and web frameworks, as well as command line operations generally.
It assumes you are using macOS, and have access to the internet.
It will also require you to use something called the Terminal, which seems scary but actually is not.  
Do not fear the dark of night.

### Before we begin.... a few notes on terminology:
In the programming world, we have at least 3 words for most things.  
The reasons for this are both banal and beyond the scope of both this tutorial.

Separately: if you are a Computer Science person and wish to quibble over the precise meaning of these terms, or feel compelled to note that in certain obscure circumstances these terms are actually not fully synonymous:
 - I already know.
 - Go away.

With that out of the way, the following are a few terms used in this tutorial which should be considered identical.
 - `directory`, `folder`. These are the same thing.
 - `library`, `package`.  These are the same thing.
 - `command line`, `terminal`.  These are (more roughly) the same thing.

## If you are a person unfamiliar with both python and Flask, but wish to be neither, do the following:

# Setup
Note: There may be terms in the steps below that are confusing or unfamiliar.  
Don't worry about it.
The things that are important for the purposes of working through this example will be explained later in the code.

If you have not already done so, download this project by clicking the green `Clone or Download` button, then selecting `Download Zip`.
Unzip the files, and then drag the resulting folder, `minimal-flask-app`, to your Desktop.

#### Things to install:
- A code editor.  I recommend Atom, which is free and can be downloaded from here: https://atom.io/.
Install it like you'd install any other program.

- Homebrew.  This is a command line program that makes it easy to install things.  
To install it
  - Open the Terminal program on your mac.  This can be found in the Applications/Utilities folder.
  The terminal app is a big white or black box.  You can type commands into it.
  - Copy this entire line:
    ```
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    ```
  - Go back to the terminal app, right click, and select Paste (or command+v if you are fancy with keyboard shortcuts).  
  You should see the command from the previous step in the terminal.
  - Press enter. This will begin the process of downloading and installing Homebrew, and may take a few minutes.
  Don't close the terminal until it is finished.

- pip. This is a python program that we use to install other python programs.  
To install it:
  - Go back to the terminal, and type (or copy), the following:
  ```
  brew install pip
  ```
  Press enter.
  `brew` == Homebrew, the thing we just installed in the previous step.
  So, this command is telling Homebrew to install `pip` for us.

- Flask.  Flask is the python package that we will use to make our website.  
To install it, go back to the terminal an run:
```
pip install flask
```
You may see a prompt asking you if you want to create a local site-packages directory.  
If you see this, type `y` and then press enter.
If this worked, great.
If not, quit the terminal app, re-open it, and run the `pip install flask` command again.
(Pro tip, when using the Terminal, pressing the up arrow key will show you the last command you entered.
You can just hit enter to re-run it.)
If it still didn't work, or you got an error message about directories not being writeable/not having permissions, run:
```
sudo pip install flask
```
This will prompt you for your password, and won't work unless you have a admin rights on your machine.
If you _still_ have not successfully installed Flask, you have probably screwed up your python installation previously and should use something called a `virtual environment`.
 I'm not going to go through how to do this here, but you can learn more on... the internet, I guess.

Congratulations, you have installed the things we need!

# Running the app.
To run the app, we need to use the Terminal to get to the folder where the code for the app is located.  
To do this, we're going to use a command called `cd`.  It stands for `change directory`.
When you are using the Finder and opening folders, you are doing the exact same thing as `cd`.

Before we do so, we can run the `ls` command to get a list of the files that are located in the current directory where our terminal session is located.

Since we previously placed the project folder on the Desktop (if you didn't, do so, or nothing below will work), we can navigate to it by running:
```
cd ~/Desktop/minimal-flask-app
```
This command is telling the Terminal to change directory to the path in the second part of the command: `Desktop/minimal-flask-app`.

You may be wondering what the `~` symbol is for.  
This is a shortcut that automatically substitutes itself with the full path to the home directory of your user account.  
In my case, `~` = `/Users/mattdelaney/`, since `mattdelaney` is my username on this computer, and all user accounts live in the `/Users/` folder in macOS.
The point is that:
```
cd ~/Desktop/minimal-flask-app
```
is exactly identical to:
```
cd /Users/mattdelaney/Desktop/minimal-flask-app
```

Once you've done that, run the `ls` command.
The output should show a few files: specifically, `run.py`, `README.md` and a folder called `templates`.  
If you don't see these things, you have done something wrong.

Now that we've navigated to the right directory, we can open Atom and look at the code.  
You can open Atom like a normal program and then select this folder as a project, or you can start it from the Terminal by running: `Atom .`.  
The `.` means roughly: "open the program and set the current directory as the project to work on."  
Assuming you have not closed the Terminal session we used before, the current directory should still be `~/Desktop/minimal-flask-app`.

You can now use atom to read and edit the code.
When you're ready to run the program, open the terminal, make sure you're located in the right directory (again, `cd ~/Desktop/minimal-flask-app`), and type
```
python run.py
```
This will start the flask app and make it available to you on your local machine.
To interact with it, open a web browser, and go to `http://127.0.0.1:8080`.
To shut down the app, go back to the terminal, and hold down `command+C`.  
