#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# utils.py
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
from libqtile.lazy import lazy

from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupImage,
    PopupText
)

def toggle_focus_floating():
    '''Toggle focus between floating window and other windows in group'''

    @lazy.function
    def _toggle_focus_floating(qtile):
        group = qtile.current_group
        switch = 'non-float' if qtile.current_window.floating else 'float'
        # logger.debug(f'toggle_focus_floating: switch = {switch}\t current_window: {qtile.current_window}')
        # logger.debug(f'focus_history: {group.focus_history}')


        for win in reversed(group.focus_history):
            # logger.debug(f'{win}: {win.floating}')
            if switch=='float' and win.floating:
                # win.focus(warp=False)
                group.focus(win)
                return
            if switch=='non-float' and not win.floating:
                # win.focus(warp=False)
                group.focus(win)
                return
    return _toggle_focus_floating

def show_power_menu(qtile):

    controls = [
        PopupImage(
            filename="~/Pictures/icons/lock.svg",
            pos_x=0.15,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={
                "Button1": lazy.spawn("/path/to/lock_cmd")
            }
        ),
        PopupImage(
            filename="~/Pictures/icons/sleep.svg",
            pos_x=0.45,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            mouse_callbacks={
                "Button1": lazy.spawn("/path/to/sleep_cmd")
            }
        ),
        PopupImage(
            filename="~/Pictures/icons/shutdown.svg",
            pos_x=0.75,
            pos_y=0.1,
            width=0.1,
            height=0.5,
            highlight="A00000",
            mouse_callbacks={
                "Button1": lazy.shutdown()
            }
        ),
        PopupText(
            text="Lock",
            pos_x=0.1,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Sleep",
            pos_x=0.4,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
        PopupText(
            text="Shutdown",
            pos_x=0.7,
            pos_y=0.7,
            width=0.2,
            height=0.2,
            h_align="center"
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=1000,
        height=200,
        controls=controls,
        background="00000060",
        initial_focus=None,
    )

    layout.show(centered=True)
