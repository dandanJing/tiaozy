#!/usr/bin/env python
# -*- coding: utf-8 -*-

from termcolor import colored

def _wrap_with(color):
    def inner(text, on_color=None, attrs=None):
        return colored(text, color, on_color, attrs)
    return inner

grey    = _wrap_with('grey')
red     = _wrap_with('red')
green   = _wrap_with('green')
yellow  = _wrap_with('yellow')
blue    = _wrap_with('blue')
magenta = _wrap_with('magenta')
cyan    = _wrap_with('cyan')
white   = _wrap_with('white')
