#!/usr/bin/env python
# encoding: utf-8

"""
    File name: init_database.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from app import db
from app.models import User, Application, Applicant, Tag, Country, Recommendation, Research, Project

db.create_all()

# Init tag
db.session.add(Tag(id=1, name="渣三维"))
db.session.add(Tag(id=2, name="转专业"))
db.session.add(Tag(id=3, name="高GT"))
db.session.add(Tag(id=4, name="高GPA"))

# Init project
db.session.add(Project(id=1, name="无相关实习经历，有个人项目", value=2))
db.session.add(Project(id=2, name="国内小公司实习", value=2))
db.session.add(Project(id=3, name="国内大公司实习", value=3))
db.session.add(Project(id=4, name="BAT实习", value=4))
db.session.add(Project(id=5, name="外企实习", value=5))

# Init Recommendation
db.session.add(Recommendation(id=1, name="无推荐信", value=1))
db.session.add(Recommendation(id=2, name="国内普通推", value=2))
db.session.add(Recommendation(id=3, name="海外普通推", value=3))
db.session.add(Recommendation(id=4, name="国内牛推", value=4))
db.session.add(Recommendation(id=5, name="海外牛推", value=5))

# Init Research
db.session.add(Research(id=1, name="无科研经历", value=1))
db.session.add(Research(id=2, name="初步的科研经历", value=2))
db.session.add(Research(id=3, name="大学实验室做过较深入的研究", value=3))
db.session.add(Research(id=4, name="1~3个月的海外研究经历", value=4))
db.session.add(Research(id=5, name="大于3个月的海外研究经历", value=5))

# Init Country
db.session.add(Country(id=1, name="美国"))
db.session.add(Country(id=2, name="英国"))
db.session.add(Country(id=3, name="加拿大"))
db.session.add(Country(id=4, name="澳大利亚"))
db.session.add(Country(id=5, name="德国"))
db.session.add(Country(id=6, name="法国"))
db.session.add(Country(id=7, name="香港"))
db.session.add(Country(id=8, name="日本"))
db.session.add(Country(id=9, name="新加坡"))

db.session.commit()