

import os
import subprocess
from typing import List  # noqa: F401
from libqtile import bar, layout, widget
from libqtile import hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
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
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
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
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    # Terminal

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Browser

    Key([mod], "b", lazy.spawn("firefox")),

    # Rofi Menu

    Key([mod], "m", lazy.spawn("rofi -show run")),

    # File Manager

    Key([mod], "e", lazy.spawn("thunar")),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
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

#BAR

widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=18,
    padding=6,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    padding=6
                ),
                widget.Image(
                    filename="~/.config/qtile/archlinux-icon-1024x1024-zpv2le9r.png",
                    scale="False"
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6
                ),
                widget.GroupBox(
                    active="#ffffff",
                    rounded=False,
                    highlight_color="#c4a7e7",
                    highlight_method="line",
                    borderwidth=0
                ),
                widget.WindowName(
                    foreground="#eb6f92",
                    markup=True,
                    font="CodeNewRoman Nerd Font",
                    fontsize=15,
                    max_chars=63
                ),
                widget.TextBox(
                    text='',
                    background="#232136",
                    foreground="#f6c177",
                    padding=0,
                    fontsize=42
                ),
                widget.TextBox(
                    text=' ',
                    background="#f6c177",
                    foreground="#191724",
                    padding=7
                ),
                widget.CurrentLayout(
                    background="#f6c177",
                    foreground="#191724"
                ),
                widget.TextBox(
                    text='',
                    background="#f6c177",
                    foreground="#e0def4",
                    padding=0,
                    fontsize=42
                ),
                widget.CPU(
                    background="#e0def4",
                    foreground="191724",
                    format="󰘚 {load_percent}%"
                ),
                widget.TextBox(
                    text='',
                    foreground="#eb6f92",
                    background="#e0def4",
                    padding=0,
                    fontsize=42
                ),
                widget.Memory(
                    format="{MemUsed: .0f}{mm}",
                    background="#eb6f92",
                    foreground="#191724",
                    interval=1.0
                ),
                widget.TextBox(
                    text='',
                    background="#eb6f92",
                    foreground="#9ccfd8",
                    padding=0,
                    fontsize=42
                ),
                widget.Net(
                    interface="enp1s0",
                    format=" {interface}: {down} ↓↑ {up}",
                    background="#9ccfd8",
                    foreground="#191724",
                    update_interval=1.0
                ),
                widget.TextBox(
                    text='',
                    background="#9ccfd8",
                    foreground="#c4a7e7",
                    padding=0,
                    fontsize=42
                ),
                widget.TextBox(
                    text='',
                    background="#c4a7e7",
                    foreground="#191724",
                    padding=7
                ),
                widget.Clock(
                    background="#c4a7e7",
                    foreground="#191724",
                    format="%H:%M - %d/%m/%Y",
                    update_interval=60.0
                ),
                widget.TextBox(
                    text='',
                    background="#c4a7e7",
                    foreground="#232136",
                    padding=0,
                    fontsize=42
                ),
                widget.Volume(
                    foreground="#e0def4",
                    fmt=" {}"
                ),
                widget.Systray(),
            ],
            25,
            background="#232136",
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    active="#ffffff",
                    rounded=False,
                    highlight_color="#c4a7e7",
                    highlight_method="line",
                    borderwidth=0
                ),
                widget.WindowName(
                    foreground="#eb6f92",
                    markup=True,
                    font="CodeNewRoman Nerd Font",
                    fontsize=15,
                ),
                widget.TextBox(
                    text='',
                    foreground="#e0def4",
                    padding=0,
                    fontsize=42
                ),
                widget.TextBox(
                    text=' ',
                    background="#e0def4",
                    foreground="#191724",
                    padding=2
                ),
                widget.CheckUpdates(
                    update_interval=18000,
                    display_format="{updates}",
                    colour_have_updates="#191724",
                    background="#e0def8"
                ),
                widget.TextBox(
                    text='',
                    background="#e0def8",
                    foreground="#c4a7e7",
                    padding=0,
                    fontsize=42
                ),
                widget.TextBox(
                    text='',
                    background="#c4a7e7",
                    foreground="#191724",
                    padding=7
                ),
                widget.Clock(
                    background="#c4a7e7",
                    foreground="#191724",
                    format="%H:%M",
                    update_interval=60.0
                ),
            ],
            25,
            background="#232136",
        ),
    ),sdfsdf

]

# Workspace

groups = [Group(i) for i in [
    "   ", "   ", " 󰌠  ", "   ", "   ", "   ", "   ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])


# Window style in layouts

layouts = [
    layout.MonadTall(border_focus="#9ccfd8",
                     border_normal="#31748f", border_width=1, margin=8),
    layout.Max(),
    layout.Bsp(border_focus="#9ccfd8", border_normal="#31748f",
               border_width=1, margin=8),
    layout.MonadWide(border_focus="#9ccfd8",
                     border_normal="#31748f", border_width=1, margin=8),
    layout.RatioTile(border_focus="#9ccfd8",
                     border_normal="#31748f", border_width=1, margin=8),
    layout.Matrix(),
]


# widget_defaults = dict(
#     font="sans",
#     fontsize=12,
#     padding=3,
# )
# extension_defaults = widget_defaults.copy()

# screens = [
#     Screen(
#         wallpaper='~/Themes/wallpapers/firewatch-sd-1920x1200.jpg',
#         wallpaper_mode='stretch',
#         bottom=bar.Bar(
#             [
#                 widget.CurrentLayout(),
#                 widget.GroupBox(),
#                 widget.Prompt(),
#                 widget.WindowName(),
#                 widget.Chord(
#                     chords_colors={
#                         "launch": ("#ff0000", "#ffffff"),
#                     },
#                     name_transform=lambda name: name.upper(),
#                 ),
#                 widget.TextBox("default config", name="default"),
#                 widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
#                 # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
#                 # widget.StatusNotifier(),
#                 widget.Systray(),
#                 widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
#                 widget.QuickExit(),
#             ],
#             24,
#             # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
#             # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
#         ),
#         # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
#         # By default we handle these events delayed to already improve performance, however your system might still be struggling
#         # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
#         # x11_drag_polling_rate = 60,
#     ),
# ]

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
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
