#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# jtcat_tg_bot - function.py
# Created by Jiting on 2017/12/25 0:19.
# Blog: https://blog.jtcat.com/
# 
__author__ = '寂听 <jiting@jtcat.com>'
import requests


def blive_stream(room_id):
    if not isinstance(room_id, int):
        return '错误的数据类型'
    api_approom = 'http://api.live.bilibili.com/AppRoom/index'
    approom_param = {'room_id': room_id, 'platform': 'android', 'otype': 'json'}
    approom = requests.get(api_approom, params=approom_param)
    if approom.json()["code"] != 0:
        return "%s%d%s" % ('不存在', room_id, '号直播间')
    if approom.json()["data"]["schedule"]["status"] == "ROUND":
        return "%s号直播间正在轮播(未开播)" % room_id
    if approom.json()["data"]["schedule"]["status"] == "PREPARING":
        return "%s号直播间准备中(未开播)" % room_id
    api_playurl = 'http://api.live.bilibili.com/api/playurl'
    cid = approom.json()["data"]["room_id"]
    playurl_param = {'cid': cid, 'otype': 'json'}
    playurl = requests.get(api_playurl, params=playurl_param)
    if not playurl.json():
        return '获取失败'
    else:
        stream_url = playurl.json()["durl"][0]["url"]
        return "%d号直播间地址: %s" % (room_id, stream_url)
