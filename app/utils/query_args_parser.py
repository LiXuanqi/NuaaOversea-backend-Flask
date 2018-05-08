#!/usr/bin/env python
# encoding: utf-8

"""
    File name: query_args_parser.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

def query_args_parser(str):
    list = str.split(' ')
    dict = {}
    for item in list:
        key_value = item.split(':')
        key = key_value[0];

        if key == 'tags' or key == 'topic':
            tags = key_value[1].split('*')
            value = tags
        else:
            value = key_value[1]

        dict.update({
            key: value
        })
    return dict