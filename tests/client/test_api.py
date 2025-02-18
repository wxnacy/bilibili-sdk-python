#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
import pytest
from bilibili_sdk import api_client, member_client
from tests.common import (
    get_cookies,
    get_cookies_info,
    get_api_client,
)

pytest_plugins = ('pytest_asyncio',)

api_client = get_api_client()

@pytest.mark.asyncio(loop_scope="module")
async def test_get_web_inferface_nav():
    info = get_cookies_info()
    res = await api_client.get_web_inferface_nav()
    assert res.is_success

    data = res.data
    assert data.mid == info.get("token_info").get("mid")


    img = data.wbi_img.img_url
    img = img.rsplit('/', 1)[-1].split('.')[0]
    sub = data.wbi_img.sub_url
    sub = sub.rsplit('/', 1)[-1].split('.')[0]
    res = await api_client.get_acc_info(data.mid, img, sub)
    assert res.is_success

@pytest.mark.asyncio(loop_scope="module")
async def test_get_online():
    info = get_cookies_info()
    res = await api_client.get_online(1313229659, aid = 365244281)
    assert res.is_success

    data = res.data
    assert data.total == "1"
    assert data.count == "1"
