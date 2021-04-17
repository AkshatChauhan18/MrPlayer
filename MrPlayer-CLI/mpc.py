'''
              ___ _                              ___   __   _______
  /\/\  _ __ / _ \ | __ _ _   _  ___ _ __       / __\ / /   \_  _ /
 /    \| '__/ /_)/ |/ _` | | | |/ _ \ '__|____ / /   / /     / /
/ /\/\ \ | / ___/| | (_| | |_| |  __/ | |_____/ /___/ /___/\/ /_  
\/    \/_| \/    |_|\__,_|\__, |\___|_|       \____/\____/\____/  
                          |___/                                   
'''
#############################################################################
#(c) Akshat Chauhan ,2021                                                   #
#This is the command line interface for MrPlayer                            #
#this can play any Mp3 file                                                 #
#MrPlayer can be downloaded from https://AkshatChauhan18.github.io/MrPlayer #
#############################################################################
import argparse
import pygame
from rich import console
from rich.syntax import Syntax
from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout import HSplit, Layout, VSplit
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import Box, Button, Frame, Label, TextArea
import lyricsgenius
import os.path

pygame.mixer.init()
console = console.Console()
console.print('[green]v1.0.0')

def player(args):
    if args.playsong:
        pygame.mixer.music.load(args.playsong.strip())
        pygame.mixer.music.play()

        def play_clicked():
            pygame.mixer.music.unpause()

        def pause_clicked():
            pygame.mixer.music.pause()

        def exit_clicked():
            pygame.mixer.music.stop()
            get_app().exit()

        def rewind():
            pygame.mixer.music.rewind()

        # All the widgets for the UI.
        play_btn = Button("Play", handler=play_clicked)
        pause_btn = Button("Pause", handler=pause_clicked)
        rewind_btn = Button("Rewind", handler=rewind)
        exit_btn = Button("Exit", handler=exit_clicked)
        text_area = TextArea(focusable=False, height=10, width=70)
        timeLabel = Label(text=f'{pygame.mixer.music.get_pos()}')
        text_area.text = '''
              ___ _                              ___   __   _______
  /\/\  _ __ / _ \ | __ _ _   _  ___ _ __       / __\ / /   \_  _ /
 /    \| '__/ /_)/ |/ _` | | | |/ _ \ '__|____ / /   / /     / /
/ /\/\ \ | / ___/| | (_| | |_| |  __/ | |_____/ /___/ /___/\/ /_  
\/    \/_| \/    |_|\__,_|\__, |\___|_|       \____/\____/\____/  
                          |___/                                   
'''
        copy_right_label = Label(text='Copyright (c)\n2021,\nAkshat Chauhan')

        # Combine all the widgets in a UI.
        # The `Box` object ensures that padding will be inserted around the containing
        # widget. It adapts automatically, unless an explicit `padding` amount is given.
        root_container = Box(
            HSplit(
                [
                    Label(text="Press `Tab` to move down and `Shift+Tab` to move up"),
                    VSplit(
                        [
                            Box(
                                body=HSplit(
                                    [play_btn, pause_btn, rewind_btn, exit_btn, copy_right_label], padding=1),
                                padding=1,
                                style="class:left-pane",
                            ),
                            Box(body=Frame(text_area), padding=1,
                                style="class:right-pane"),
                        ]
                    )
                ]
            ),
        )

        layout = Layout(container=root_container, focused_element=pause_btn)

        # Key bindings.
        kb = KeyBindings()
        kb.add("tab")(focus_next)
        kb.add("s-tab")(focus_previous)

        # Styling.
        style = Style(
            [
                ("left-pane", "bg:#888800 #000000"),
                ("right-pane", "bg:#00aa00 #000000"),
                ("button", "#000000"),
                ("button-arrow", "#000000"),
                ("button focused", "bg:#ff0000"),
                ("text-area focused", "bg:#ff0000"),
            ]
        )

        # Build a main application object.
        application = Application(
            layout=layout, key_bindings=kb, style=style, full_screen=True)
        application.run()

    if args.getlyrics:
        song=None
        try:
            api_key = open(
                f"{os.path.expanduser('~')}\\.MrPlayer\\api_key.txt").read()
            genius = lyricsgenius.Genius(api_key)
            if args.singer:
                song = genius.search_song(args.getlyrics.strip(), args.singer.strip())
            else:
                song = genius.search_song(args.getlyrics.strip(),'')
            lyrics = song.lyrics
            console.rule(f'[bold red]{args.getlyrics}')
            console.print(lyrics)
        except:
            console.print_exception()
    if args.version:
        console.print('[green]v1.0.0')
    if args.sourcecode:
        console.rule('[bold red]Code')
        codeFile = Syntax.from_path(f"{os.path.expanduser('~')}.MrPlayer\\SourceCode.py",line_numbers=True)
        console.print(codeFile)


if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-ps','--playsong', help='This command is for playing mp3')
    parse.add_argument('-gl','--getlyrics', help='This command gets lyrics')
    parse.add_argument('-si','--singer', help='This command is used with --gl command to enter singer')
    parse.add_argument('-v','--version',help='This command shows current version',action='store_true')
    parse.add_argument('-sc','--sourcecode',help='This command shows the source code.',action='store_true')
    args = parse.parse_args()
    player(args)
