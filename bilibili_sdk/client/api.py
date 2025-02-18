#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
from typing import Self, Optional
from .base import BaseClient
from bilibili_sdk import dto
from bilibili_sdk.config.settings import settings
from bilibili_sdk.common.sign import sign_wbi


class ApiClient(BaseClient):
    #  wbi_img: str
    #  wbi_sub: str

    #  def set_wbi_img(self, img: str) -> Self:
        #  self.wbi_img = img
        #  return self

    #  def set_wbi_sub(self, sub: str) -> Self:
        #  self.wbi_sub = sub
        #  return self

    async def get_online(self, cid: int, *, aid: int = 0, bvid: str = ''):
        if not aid and not bvid:
            raise ValueError("aid or bvid 需要有一个有值")
        params = {"cid": cid}
        if bvid:
            params['bvid'] = bvid
        if aid:
            params['aid'] = aid
        res = self.get("/x/player/online/total", params=params)
        print(res)
        return res

    async def get_acc_info(self, mid: int, wbi_img: str, wbi_sub: str) -> Optional[dto.GetAccInfoRes]:
        '''用户空间详细信息
        https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/user/info.md
        '''
        wbi_img = wbi_img.rsplit('/', 1)[-1].split('.')[0]
        wbi_sub = wbi_sub.rsplit('/', 1)[-1].split('.')[0]

        params = {'mid': mid}
        params = sign_wbi(params, wbi_img, wbi_sub)
        return await self.get(
            "/x/space/wbi/acc/info",
            params=params,
            res_clz=dto.GetAccInfoRes,
        )

    async def get_web_inferface_nav(self) -> dto.GetWebInferfaceNavRes:
        '''导航栏用户信息
        https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/docs/login/login_info.md
        '''
        return await self.get("/x/web-interface/nav", res_clz=dto.GetWebInferfaceNavRes)



api_client = ApiClient(host=settings.HOST_API)
