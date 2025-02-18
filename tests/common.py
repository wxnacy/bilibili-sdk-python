#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

import os
from wpy.path import read_dict
from bilibili_sdk import (
    api_client,
    member_client,
    ApiClient,
    MemberClient,
)

COOKIES_PATH = os.path.expanduser('~/Downloads/bili_cli/config/xinxin-cookies.json')

def get_cookies_info():
    data = read_dict(COOKIES_PATH)
    return data

def get_cookies():
    data = read_dict(COOKIES_PATH)
    cookies = data.get("cookie_info").get("cookies")
    cookies_map = {}
    for cookie in cookies:
        cookies_map[cookie.get("name")] = cookie.get("value")
    return cookies_map

def get_api_client() -> ApiClient:
    api_client.set_cookies(get_cookies())
    return api_client

def get_member_client() -> MemberClient:
    member_client.set_cookies(get_cookies())
    return member_client
