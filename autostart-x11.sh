#!/bin/sh

# gnome-polkit
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# clipboard manager
clipmenud --disable-primary &
picom --no-use-damage &
