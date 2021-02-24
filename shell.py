# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Using cmd module and specifically cmdloop and a shell for main program."""

import cmd
import card
import cardhand
import deck


class Shell(cmd.Cmd):
    """Class with command arguments to play the cardgame"""

    intro = 'Welcome to War. Type help or ? to list commands.\n'
    prompt = '(...) '

    def __init__(self):
        super().__init__()
        
