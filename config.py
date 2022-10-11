#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# /home/deve/.dotfiles/qtile/.config/qtile/config.py
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
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras.resources import wallpapers

import utils
import os
import subprocess
from libqtile import hook, qtile

clipboard_manager = "clipman pick -t rofi"
screenshot = 'grim -g "$(slurp)" - | swappy -f -'
screenrecord = '~/.scripts/record-screen'
screenanonation = '/home/deve/.scripts/screen-annonation.sh'


# x11 variable apps
if qtile.core.name == "x11":
    clipboard_manager = "clipmenu -i -fn Iosevka"
    screenshot = 'flameshot gui'
    screenrecord = 'peek'

terminal = "alacritty -e tmuxa"
mod = "mod4"
# terminal = 'stmux'
filemanager = 'pcmanfm'
runner = "rofi -modi run -show run"
app_runner = "rofi -modi drun -show drun"

# clipboard_manager_daemon = 'wl-paste -t text --watch clipman store --max-items=100'

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    # Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),


    # Toggle between different layouts as defined below
    Key([mod, 'shift'], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, 'shift'], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle between layouts"),

    Key([mod, "shift"], "c", lazy.reload_config(), desc="Reload the config"),
    # Key([mod, "shift"], "c", lazy.restart(), desc="Reload the config"),
    # Key([mod, "shift"], "e", lazy.function(utils.show_power_menu)),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),


    ## backlight and sound
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%")),

    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10-")),

    # Floating keybind
    Key([mod], "Tab", utils.toggle_focus_floating(), desc="Toogle Floating window mode"),
    Key([mod, 'shift'], "space", lazy.window.toggle_floating(), desc="Toogle Floating window mode"),


    # aplication binding
    Key([mod], "n", lazy.spawn(filemanager), desc="Open file manager"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key(['mod1', 'control'], "h", lazy.spawn(clipboard_manager), desc="Clipboard manager"),
    Key([mod], "r", lazy.spawn(runner), desc="runner"),
    Key([mod], "space", lazy.spawn(app_runner), desc="app_runner"),
    Key([mod, 'shift'], "b", lazy.spawn('qbpm choose'), desc="qbpm choose"),

    Key([mod, 'shift'], "s", lazy.spawn('start-scrcpy'), desc="scrcpy"),
    Key(['mod1'], "Tab", lazy.spawn('rofi -show window'), desc="window switcher"),


    # screen tools
    Key([], 'Print', lazy.spawn(screenshot), desc="Screen shoot"),
    Key([mod], 'Print', lazy.spawn(screenrecord), desc="screen record"),
    Key([mod, 'shift'], "a", lazy.spawn(screenanonation), desc="screen annonation"),

]

groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#ff0000", "#00ff00"], border_focus="#d75f5f", border_width=5, margin=5),
    layout.Max(
        margin=59
    ),

    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Iosevka",
    fontsize=10,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        # wallpaper=wallpapers.WALLPAPER_TRIANGLES,
        # wallpaper_mode="fill",
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(
                    disable_drag=True
                ),
                # widget.Prompt(),
                # widget.WindowName(),
                widget.TaskList(),
                # widget.WindowTabs(
                #     max_chars=10
                # ),
                # widget.Spacer(),
                # widget.Chord(
                #     chords_colors={
                #         "launch": ("#ff0000", "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),

                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),

                widget.CPUGraph(type='line', line_width=1),
                widget.Net(),
                widget.Battery(),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        # *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="scrcpy")
    ]
)



@hook.subscribe.startup_once
def autostart():
    autostart_file = '~/.config/qtile/autostart-wayland.sh'
    if qtile.core.name == "x11":
        autostart_file = '~/.config/qtile/autostart-x11.sh'

    home = os.path.expanduser(autostart_file)
    subprocess.Popen([home])


auto_fullscreen = True
focus_on_window_activation = "smart"
# reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None
bring_front_click = False
# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
