#!/bin/sh

# gnome-polkit
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# clipboard manager
clipmenud --disable-primary &

# x11 compositor for better perfomance and rendering
# xcompmgr &
# picom --no-use-damage &
