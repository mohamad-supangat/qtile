#!/bin/sh

# gnome-polkit
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# clipboard manager
wl-paste -t text --watch clipman store --max-items=1000 &
