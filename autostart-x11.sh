#!/bin/sh
# /home/deve/.dotfiles/qtile/.config/qtile/autostart-x11.sh
# Copyright (c) 2022 Mohamad Supangat <moha.supangat@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

# gnome-polkit
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# clipboard manager
clipmenud --disable-primary &

# x11 compositor for better perfomance and rendering
# xcompmgr &
# picom --no-use-damage &
