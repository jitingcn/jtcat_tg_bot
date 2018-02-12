#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# jtcat_tg_bot - function.py
# Created by Jiting on 2017/12/25 0:19.
# Blog: https://blog.jtcat.com/
# 
__author__ = '寂听 <jiting@jtcat.com>'
import requests


def get_stream(room_id):
    if not isinstance(room_id, int):
        return 'Wrong Type'
    api_approom = 'http://api.live.bilibili.com/AppRoom/index'
    approom_param = {'room_id': room_id, 'platform': 'android', 'otype': 'json'}
    approom = requests.get(api_approom, params=approom_param)
    if approom.json()["code"] != 0:
        return "%s %d %s" % ('Room', room_id, 'is not find.')
    if approom.json()["data"]["schedule"]["status"] == "ROUND":
        return "Room %s is in round." % room_id
    if approom.json()["data"]["schedule"]["status"] == "PREPARING":
        return "Room %s is preparing." % room_id
    api_playurl = 'http://api.live.bilibili.com/api/playurl'
    cid = approom.json()["data"]["room_id"]
    playurl_param = {'cid': cid, 'otype': 'json'}
    playurl = requests.get(api_playurl, params=playurl_param)
    if not playurl.json():
        return 'Request failure'
    else:
        stream_url = playurl.json()["durl"][0]["url"]
        return stream_url


def dl(room_id):
    stream_url = get_stream(room_id)
    local_filename = stream_url.split('/')[-1].split('?')[0]
    r = requests.get(stream_url, stream=True)
    with open(local_filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return 'Download finished'
