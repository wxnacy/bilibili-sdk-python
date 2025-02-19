#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:

from wpy import Enum, EnumMem


class ArchiveStatus(Enum):
    ALL = EnumMem('is_pubing,pubed,not_pubed', '全部')
    IS_PUBING = EnumMem('is_pubing', '进行中')
    PUBED = EnumMem('pubed', '已发布')
    NOT_PUBED = EnumMem('not_pubed', '未发布')


class ArchiveState(Enum):
    OPEN = EnumMem(0, '开放浏览')
    LOCKED = EnumMem(-4, '已锁定')
    BACKED = EnumMem(-2, '已退回')
    UPDATED = EnumMem(-6, '修改审核')
    UNDER_REVIEW = EnumMem(30, '审核中')
    WAITING = EnumMem(-40, '审核通过，等待发布')
