#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/10/19 下午3:21
# @Author  : HECV
# @File    : forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('what is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')