#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:
# Description:
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # 使用 env 字段来指定环境变量名称
    USER_AGENT: str = Field("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0")
    REFERER: str = Field("https://www.bilibili.com/")
    HOST_API: str = Field("https://api.bilibili.com", title="api 接口 host")
    HOST_MEMBER: str = Field("https://member.bilibili.com", title="member 接口 host")

    # 可以使用 env_prefix 来指定环境变量的前缀
    class Config:
        env_prefix = "BILIBILI_"

    #  @property
    #  def full_host(self):
        #  host = self.server_host
        #  if host == '0.0.0.0':
            #  host = 'localhost'
        #  return f"http://{host}:{self.server_port}"


# 创建 Settings 实例
settings = Settings()


if __name__ == "__main__":
    print(settings.model_dump())

