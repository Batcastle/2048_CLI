# 2048_CLI

2048_CLI is a CLI clone of 2048 written in Python.
Should run nativly on Linux and MacOS, so long as Python 3 is installed, not Python 2

Dependencies
---
 * python3-json
 
 Can be instaled with either:
 `sudo apt install python3-json`
 or
 `pip3 install json`
 
 Only use `pip3` on MacOS or Windows so that it does not risk corrupting your `apt` version of the package on Linux.

Installation
---

`git clone https://github.com/Batcastle/2048_CLI`

Running
---

Play a Game:

`./2048_cli.py`

Check your stats:

`./2048_cli.py --stats`

Check your settings:

`./2048_cli.py --settings`


Known bugs
---
 * Say you have 2 cells with 2 to merge, and the new 4 cell will land next to another 4 cell. 2048_CLI will go ahead and merge those two 4 cells as well
 * Not all cells will move when the board is on the fuller-side
 * No top edge to the board
 
