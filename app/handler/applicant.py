#!/usr/bin/env python
# encoding: utf-8

"""
    File name: applicant.py
    Function Des: ...
    ~~~~~~~~~~

    author: 1_x7 <lixuanqi1995@gmail.com> <http://lixuanqi.github.io>

"""

from app.models import Applicant, User

from app.models import db

def get_all_applicants():
    applicants = Applicant.query.all()
    return applicants

def create_applicant(user_id,
                    college,
                    major,
                    gpa,
                    language_type,
                    language_reading,
                    language_listening,
                    language_speaking,
                    language_writing,
                    gre_verbal,
                    gre_quantitative,
                    gre_writing,
                    research_id,
                    project_id,
                    recommendation_id):
    # TODO: add the authentication of power.
    # TODO: verify the repeation of datas.
    applicant = Applicant(
        college=college,
        major=major,
        gpa=gpa,
        language_type=language_type,
        language_reading=language_reading,
        language_listening=language_listening,
        language_speaking=language_speaking,
        language_writing=language_writing,
        gre_verbal=gre_verbal,
        gre_quantitative=gre_quantitative,
        gre_writing=gre_writing,
        research_id=research_id,
        project_id=project_id,
        recommendation_id=recommendation_id
    )
    db.session.add(applicant)
    db.session.commit()

    user = User.query.filter_by(id=user_id).first()
    user.applicant_id = applicant.id;
    db.session.commit()

    db.session.add(applicant)
    db.session.commit()

    return {
        'id': applicant.id
    }


def get_applicant_by_id(applicant_id):
    applicant = Applicant.query.filter_by(id=applicant_id).first()
    return applicant

def update_applicant(applicant_id,
                    college,
                    major,
                    gpa,
                    language_type,
                    language_reading,
                    language_listening,
                    language_speaking,
                    language_writing,
                    gre_verbal,
                    gre_quantitative,
                    gre_writing,
                    research_id,
                    project_id,
                    recommendation_id):

    applicant = Applicant.query.filter_by(id=applicant_id).first();

    applicant.college = college
    applicant.major = major
    applicant.gpa = gpa
    applicant.language_type = language_type
    applicant.language_reading = language_reading
    applicant.language_listening = language_listening
    applicant.language_speaking = language_speaking
    applicant.language_writing = language_writing
    applicant.gre_verbal = gre_verbal
    applicant.gre_quantitative = gre_quantitative
    applicant.gre_writing = gre_writing
    applicant.research_id = research_id
    applicant.project_id = project_id
    applicant.recommendation_id = recommendation_id

    db.session.commit()

    return {
        'id': applicant.id
    }

def rm_applicant(applicant_id):
    applicant = Applicant.query.filter_by(id=applicant_id).first()
    if applicant is not None:
        db.session.delete(applicant)
        db.session.commit()
        return {'success': 1}


def patch_applicant(applicant_id,
                    college,
                    major,
                    gpa,
                    language_type,
                    language_reading,
                    language_listening,
                    language_speaking,
                    language_writing,
                    gre_verbal,
                    gre_quantitative,
                    gre_writing,
                    research_id,
                    project_id,
                    recommendation_id):

    applicant = Applicant.query.filter_by(id=applicant_id).first();
    if college is not None:
        applicant.college = college
    if major is not None:
        applicant.major = major
    if gpa is not None:
        applicant.gpa = gpa
    if language_type is not None:
        applicant.language_type = language_type
    if language_reading is not None:
        applicant.language_reading = language_reading
    if language_listening is not None:
        applicant.language_listening = language_listening
    if language_speaking is not None:
        applicant.language_speaking = language_speaking
    if language_writing is not None:
        applicant.language_writing = language_writing
    if gre_verbal is not None:
        applicant.gre_verbal = gre_verbal
    if gre_quantitative is not None:
        applicant.gre_quantitative = gre_quantitative
    if gre_writing is not None:
        applicant.gre_writing = gre_writing
    if research_id is not None:
        applicant.research_id = research_id
    if project_id is not None:
        applicant.project_id = project_id
    if recommendation_id is not None:
        applicant.recommendation_id = recommendation_id

    db.session.commit()

    return applicant