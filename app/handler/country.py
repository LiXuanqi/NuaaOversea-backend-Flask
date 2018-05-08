#!/usr/bin/env python
# encoding: utf-8

"""
    File name: country.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from app.models import Country

def get_all_countries():
    countries = Country.query.all()
    return countries