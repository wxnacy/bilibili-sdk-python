#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
from typing import List, Optional, Dict
from pydantic import Field, BaseModel
from bilibili_sdk.enums.archive import ArchiveStatus
from .base import BaseListReq, BaseResponse

class GetArchiveListReq(BaseListReq):
    keyword: str = Field("", title="搜索关键字")
    order: str = Field("senddate", title="")
    status: str = Field(ArchiveStatus.ALL, title="")
    ps: int = Field(10, title="每页条数")
    pn: int = Field(1, title="页码")


class WebOperation(BaseModel):
    id: Optional[int] = Field(default=None)
    icon: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    type: Optional[int] = Field(default=None)
    url: Optional[str] = Field(default=None)
    disabled: Optional[int] = Field(default=None)
    disable_reason: Optional[str] = Field(default=None)

class DisplayField(BaseModel):
    name: Optional[str] = Field(default=None)
    desc: Optional[str] = Field(default=None)
    value: Optional[int] = Field(default=None)
    icon_url: Optional[Dict[str, str]] = Field(default=None)

class Appeal(BaseModel):
    open_apid: Optional[int] = Field(default=None)
    reject: Optional[str] = Field(default=None)
    jump_url: Optional[str] = Field(default=None)

class WebRule(BaseModel):
    more_oper: Optional[List[WebOperation]] = Field(None)

class Archive(BaseModel):
    aid: Optional[int] = Field(default=None)
    bvid: Optional[str] = Field(default=None)
    mid: Optional[int] = Field(default=None)
    tid: Optional[int] = Field(default=None)
    title: Optional[str] = Field(default=None)
    author: Optional[str] = Field(default=None)
    cover: Optional[str] = Field(default=None)
    reject_reason: Optional[str] = Field(default=None)
    reject_reason_url: Optional[str] = Field(default=None)
    modify_advise: Optional[str] = Field(default=None)
    problem_description: Optional[str] = Field(default=None)
    problem_description_title: Optional[str] = Field(default=None)
    reject_reason_id: Optional[int] = Field(default=None)
    duration: Optional[int] = Field(default=None)
    copyright: Optional[int] = Field(default=None)
    no_reprint: Optional[int] = Field(default=None)
    ugcpay: Optional[int] = Field(default=None)
    online_time: Optional[int] = Field(default=None)
    desc: Optional[str] = Field(default=None)
    forward: Optional[int] = Field(default=None)
    attribute: Optional[int] = Field(default=None)
    state: Optional[int] = Field(default=None, title="状态", description="0 开发浏览 -4 已锁定 -30 审核中、-40 审核通过，等待发布")
    state_desc: Optional[str] = Field(default=None)
    state_panel: Optional[int] = Field(default=None)
    source: Optional[str] = Field(default=None)
    desc_format_id: Optional[int] = Field(default=None)
    attrs: Optional[Dict[str, int]] = Field(default=None)
    dtime: Optional[int] = Field(default=None)
    ptime: Optional[int] = Field(default=None)
    ctime: Optional[int] = Field(default=None)
    interactive: Optional[int] = Field(default=None)
    no_background: Optional[int] = Field(default=None)
    dynamic_video: Optional[int] = Field(default=None)
    limit_state: Optional[bool] = Field(default=None)
    appeal: Optional[str] = Field(default=None)
    appeal_state: Optional[int] = Field(default=None)
    premiere: Optional[int] = Field(default=None)
    is_ugcpay_v2: Optional[int] = Field(default=None)
    political_media: Optional[int] = Field(default=None)
    political_editable: Optional[int] = Field(default=None)
    charging_pay: Optional[int] = Field(default=None)
    charge_2_free: Optional[int] = Field(default=None)
    music_tort: Optional[str] = Field(default=None)
    is_only_self: Optional[int] = Field(default=None)
    is_playlet: Optional[int] = Field(default=None)

class Stat(BaseModel):
    aid: Optional[int] = Field(default=None)
    now_rank: Optional[int] = Field(default=None)
    his_rank: Optional[int] = Field(default=None)
    dislike: Optional[int] = Field(default=None)
    vt: Optional[int] = Field(default=None)
    vv: Optional[int] = Field(default=None)
    view: int = Field(0, title="播放")
    danmaku: int = Field(0, title="弹幕")
    reply: int = Field(0, title="回复")
    favorite: int = Field(0, title="收藏")
    coin: float = Field(0, title="硬币")
    share: int = Field(0, title="分享")
    like: int = Field(0, title="点赞")


class ArcAudit(BaseModel):
    archive: Optional[Archive] = Field(default=None, alias='Archive')
    videos: Optional[List] = Field(default=None, alias='Videos')
    stat: Optional[Stat] = Field(default=None)
    state_panel: Optional[int] = Field(default=None)
    parent_tname: Optional[str] = Field(default=None)
    typename: Optional[str] = Field(default=None)
    open_appeal: Optional[int] = Field(default=None)
    appeal: Optional[Appeal] = Field(default=None)
    fast_pub: Optional[Dict[str, str]] = Field(default=None)
    captions_count: Optional[int] = Field(default=None)
    ai_captions_count: Optional[int] = Field(default=None)
    web_rules: Optional[WebRule] = Field(default=None)
    display_fields: Optional[List[DisplayField]] = Field(default=None)

class ApplyCount(BaseModel):
    neglected: Optional[int] = Field(default=None)
    pending: Optional[int] = Field(default=None)
    processed: Optional[int] = Field(default=None)

class ClassModel(BaseModel):
    pubed: Optional[int] = Field(default=None)
    not_pubed: Optional[int] = Field(default=None)
    is_pubing: Optional[int] = Field(default=None)

class TypeModel(BaseModel):
    tid: Optional[int] = Field(default=None)
    name: Optional[str] = Field(default=None)
    count: Optional[int] = Field(default=None)

class ArchiveData(BaseModel):
    class_: Optional[ClassModel] = Field(default=None, alias="class")
    apply_count: Optional[ApplyCount] = Field(default=None)
    type_: Optional[List[TypeModel]] = Field(default=None, alias='type')
    archives: Optional[List[Archive]] = Field(default=None)
    arc_audits: Optional[List[ArcAudit]] = Field(default=None)


class GetArchiveListRes(BaseResponse):
    data: Optional[ArchiveData] = Field(default=None)


class Video(BaseModel):
    cid: int = Field(0, title="p1 id")
    title: str = Field("", title="标题")
    filename: str = Field("", title="猜测是md5")
    desc: str = Field("", title="描述")
    index: int = Field(0, title="")
    duraction: int = Field(0, title="时长")


class ArchiveVideoListData(BaseModel):
    archive: Archive = Field(None)
    videos: List[Video] = Field([])

class GetArchiveVideoListRes(BaseResponse):
    data: Optional[ArchiveVideoListData] = Field(default=None)
