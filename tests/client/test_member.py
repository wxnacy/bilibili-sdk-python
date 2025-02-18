#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
import pytest
from bilibili_sdk.dto import (
    GetArchiveListReq,
)
from tests.common import (
    get_cookies,
    get_cookies_info,
    get_member_client,
)

pytest_plugins = ('pytest_asyncio',)

member_client = get_member_client()

@pytest.mark.asyncio(loop_scope="session")
async def test_get_archive_list():
    req = GetArchiveListReq()
    res = await member_client.get_archive_list(req)
    assert res.is_success

    arc_audits = res.data.arc_audits
    assert len(arc_audits) > 1

    archive = arc_audits[0].archive
    assert archive.mid
    assert archive.aid
    assert archive.bvid

    res = await member_client.get_archive_list(None)
    assert res.is_success

    arc_audits = res.data.arc_audits
    assert len(arc_audits) > 1

    archive = arc_audits[0].archive
    assert archive.mid
    assert archive.aid
    assert archive.bvid
