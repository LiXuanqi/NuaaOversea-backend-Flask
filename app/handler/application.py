#!/usr/bin/env python
# encoding: utf-8

"""
    File name: application.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""
from flask_restful import abort

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

def update_application(application_id, country_id, university, major, degree, term, result, applicant_id, is_transfer):
    application = Application.query.filter_by(id=application_id).first();

    application.country_id = country_id
    application.university = university
    application.major = major
    application.degree = degree
    application.term = term
    application.result = result
    application.applicant_id = applicant_id

    # delete "is_transfer" tag.
    transfer_tag = Tag.query.filter_by(name="转专业").first()
    if is_transfer is False:
        application.tags.remove(transfer_tag)
    else:
        application.tags.append(transfer_tag)

    db.session.commit()

    return {
        'id': application.id
    }

def patch_application(application_id, country_id, university, major, degree, term, result, applicant_id, is_transfer):

    application = Application.query.filter_by(id=application_id).first();
    if country_id is not None:
        application.country_id = country_id
    if university is not None:
        application.university = university
    if major is not None:
        application.major = major
    if degree is not None:
        application.degree = degree
    if term is not None:
        application.term = term
    if result is not None:
        application.result = result
    if applicant_id is not None:
        application.applicant_id = applicant_id
    if is_transfer is not None:
        # delete "is_transfer" tag.
        transfer_tag = Tag.query.filter_by(name="转专业").first()
        if is_transfer is False:
            application.tags.remove(transfer_tag)
        else:
            application.tags.append(transfer_tag)

    db.session.commit()

    return application


def rm_application(application_id):
    application = Application.query.filter_by(id=application_id).first()
    if application is not None:
        db.session.delete(application)
        db.session.commit()
        return True
    else:
        abort(404, error="案例不存在")

