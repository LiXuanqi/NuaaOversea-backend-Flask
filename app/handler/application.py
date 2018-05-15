#!/usr/bin/env python
# encoding: utf-8

"""
    File name: application.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from app.models import Application, Tag, Applicant

from app.models import db

from app.utils.auto_tags import auto_tags
def get_all_applications():
    applications = Application.query.all()
    return applications

def get_applications_by_applicantid(applicant_id):
    applications = Application.query.filter_by(applicant_id=applicant_id).all()
    return applications

def get_applications_by_university(university):
    applications = Application.query.filter_by(university=university).all()
    return applications

def create_application(country_id, university, major, degree, term, result, applicant_id, is_transfer):
    # TODO: add the authentication of power.
    # TODO: verify the repeation of datas.
    application = Application(
        country_id=country_id,
        university=university,
        major=major,
        degree=degree,
        term=term,
        result=result,
        applicant_id=applicant_id
    )
    # new_tags = [Tag.query.filter_by(name="渣三维").first(), Tag.query.filter_by(name="转专业").first()];
    # application.tags.extend(new_tags)
    # Auto Tag
    applicant = Applicant.query.filter_by(id=applicant_id).first()
    # FIXME : if language_type is not toefl.
    toefl = applicant.language_reading + applicant.language_listening + applicant.language_speaking + applicant.language_writing
    gre = applicant.gre_quantitative + applicant.gre_verbal
    gpa = applicant.gpa
    new_tags = auto_tags(gre, gpa, is_transfer, toefl)
    application.tags.extend(new_tags)
    db.session.add(application)
    db.session.commit()
    return {
        'id': application.id
    }


def get_application_by_id(application_id):
    application = Application.query.filter_by(id=application_id).first()
    print(application.tags)
    return application

def update_application():
    # TODO: update the application(handler)
    pass

def rm_application(application_id):
    application = Application.query.filter_by(id=application_id).first()
    if application is not None:
        db.session.delete(application)
        db.session.commit()
        return {'success': 1}

