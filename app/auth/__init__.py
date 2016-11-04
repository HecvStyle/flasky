#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/11/4 下午3:20
# @Author  : HECV
# @File    : __init__.py

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views