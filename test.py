#!/usr/bin/env python
# -*- coding: utf-8 -*-

# jtcat_tg_bot - test.py
# Created by JT on 20-Aug-18 05:40.
# Blog: https://blog.jtcat.com/
# 
# author = 'JT <jiting@jtcat.com>'

from function import get_stream

my_room = get_stream(74151)
assert my_room is "Room 74151 is preparing." or my_room is "Room 74151 is in round."
print(get_stream(3))
