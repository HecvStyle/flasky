#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 16/10/19 下午3:03
# @Author  : HECV
# @File    : views.py

from  datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .. import db
from . forms import NameForm
from .. models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['know'] = False
        else:
            session['know'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form,
                           name=session.get('name'),
                           know=session.get('know', False),
                           current_time=datetime.utcnow())
