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
