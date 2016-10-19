#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/10/19 下午3:02
# @Author  : HECV
# @File    : __init__.py
from flask import Blueprint
main = Blueprint('main', __name__)


# 末尾倒入是为了避免循环倒入依赖
from . import views, errors
