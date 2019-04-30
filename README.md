# HTTP-Link Hardcoded Version

## Setup:
requires python3, pip (for python3)
Install bottle.py library using your pip (or pip3)


## Running:
Use tmux to open a shell 
```bash
tmux
```
This adds a gren highlight bar at the bottom of the terminal window.
Then run the http server itself:
```bash
python3 http_link.py
```
you should see something like:
```
ros@ubuntu-slammer:~/workspace/http_link_hardcoded$ python3 http-link.py 
Bottle v0.12.16 server starting up (using WSGIRefServer())...
Listening on http://localhost:18590/
Hit Ctrl-C to quit.

```
You can then hit ``control+b`` then ``d`` to detatch from the tmux session. See below to reattach.

## Checking if it's Running

To check for the python3 process:
```bash
ps -a
```
you can then kill it with ``kill``  followed by the number of the process.

To check for floating tmux terminals, use
```bash
tmux list-sessions
```
then use the following to reconect to the specific tmux session, in this case 0:
```bash
tmux attach-session -t 0
```