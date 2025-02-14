from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_users(db: Session):

    users_all = db.query(models.Users).all()
    users_all = [new_data.to_dict() for new_data in users_all] if users_all else users_all

    res = {
        'users_all': users_all,
    }
    return res

async def get_users_id(db: Session, id: int):

    users_one = db.query(models.Users).filter(models.Users.id == id).first() 
    users_one = users_one.to_dict() if users_one else users_one

    res = {
        'users_one': users_one,
    }
    return res

async def post_users(db: Session, raw_data: schemas.PostUsers):
    id:int = raw_data.id
    created_at:str = raw_data.created_at
    username:str = raw_data.username
    email:str = raw_data.email
    password:str = raw_data.password
    role:str = raw_data.role


    record_to_be_added = {'id': id, 'created_at': created_at, 'username': username, 'email': username, 'password': username, 'role': username}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    user_response = new_users.to_dict()



    bs_jwt_payload = {
        'exp': int((datetime.datetime.utcnow() + datetime.timedelta(seconds=1800000)).timestamp()),
        'data': user_response
    }

    userToken = jwt.encode(bs_jwt_payload, 'a3f1e2d4c6b8a0d9e7f5c3b1a9e8d6c4b2f0a1e3d5c7b9a8f2d4e6c0b1a3f5
', algorithm='HS256')

    res = {
        'finalTokens': user_response,
        'tokenUser': userToken,
    }
    return res

async def put_users_id(db: Session, raw_data: schemas.PutUsersId):
    id:str = raw_data.id
    created_at:str = raw_data.created_at


    users_edited_record = db.query(models.Users).filter(models.Users.id == id).first()
    for key, value in {'id': id, 'created_at': created_at}.items():
          setattr(users_edited_record, key, value)
    db.commit()
    db.refresh(users_edited_record)
    users_edited_record = users_edited_record.to_dict() 

    res = {
        'users_edited_record': users_edited_record,
    }
    return res

async def delete_users_id(db: Session, id: int):

    users_deleted = None
    record_to_delete = db.query(models.Users).filter(models.Users.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict() 

    res = {
        'users_deleted': users_deleted,
    }
    return res

async def get_leads(db: Session):

    leads_all = db.query(models.Leads).all()
    leads_all = [new_data.to_dict() for new_data in leads_all] if leads_all else leads_all

    res = {
        'leads_all': leads_all,
    }
    return res

async def get_leads_id(db: Session, id: int):

    leads_one = db.query(models.Leads).filter(models.Leads.id == id).first() 
    leads_one = leads_one.to_dict() if leads_one else leads_one

    res = {
        'leads_one': leads_one,
    }
    return res

async def post_leads(db: Session, id: str, created_at: str, name: str, email: str, phone: str, message: str, attachments: str, source: str, status: str, address_city: str, address_state: str):

    record_to_be_added = {'id': id, 'created_at': created_at, 'name': name, 'email': email, 'phone': phone, 'address_city': address_city, 'address_state': address_state, 'message': message, 'attachments': attachments, 'source': source, 'status': status}
    new_leads = models.Leads(**record_to_be_added)
    db.add(new_leads)
    db.commit()
    db.refresh(new_leads)
    leads_inserted_record = new_leads.to_dict()

    res = {
        'leads_inserted_record': leads_inserted_record,
    }
    return res

async def put_leads_id(db: Session, raw_data: schemas.PutLeadsId):
    id:str = raw_data.id
    created_at:str = raw_data.created_at


    leads_edited_record = db.query(models.Leads).filter(models.Leads.id == id).first()
    for key, value in {'id': id, 'created_at': created_at}.items():
          setattr(leads_edited_record, key, value)
    db.commit()
    db.refresh(leads_edited_record)
    leads_edited_record = leads_edited_record.to_dict() 

    res = {
        'leads_edited_record': leads_edited_record,
    }
    return res

async def delete_leads_id(db: Session, id: int):

    leads_deleted = None
    record_to_delete = db.query(models.Leads).filter(models.Leads.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        leads_deleted = record_to_delete.to_dict() 

    res = {
        'leads_deleted': leads_deleted,
    }
    return res

async def get_formsubmission(db: Session):

    formsubmission_all = db.query(models.Formsubmission).all()
    formsubmission_all = [new_data.to_dict() for new_data in formsubmission_all] if formsubmission_all else formsubmission_all

    res = {
        'formsubmission_all': formsubmission_all,
    }
    return res

async def get_formsubmission_id(db: Session, id: int):

    formsubmission_one = db.query(models.Formsubmission).filter(models.Formsubmission.id == id).first() 
    formsubmission_one = formsubmission_one.to_dict() if formsubmission_one else formsubmission_one

    res = {
        'formsubmission_one': formsubmission_one,
    }
    return res

async def post_formsubmission(db: Session, raw_data: schemas.PostFormsubmission):
    id:str = raw_data.id
    created_at:str = raw_data.created_at


    record_to_be_added = {'id': id, 'created_at': created_at}
    new_formsubmission = models.Formsubmission(**record_to_be_added)
    db.add(new_formsubmission)
    db.commit()
    db.refresh(new_formsubmission)
    formsubmission_inserted_record = new_formsubmission.to_dict()

    res = {
        'formsubmission_inserted_record': formsubmission_inserted_record,
    }
    return res

async def put_formsubmission_id(db: Session, raw_data: schemas.PutFormsubmissionId):
    id:str = raw_data.id
    created_at:str = raw_data.created_at


    formsubmission_edited_record = db.query(models.Formsubmission).filter(models.Formsubmission.id == id).first()
    for key, value in {'id': id, 'created_at': created_at}.items():
          setattr(formsubmission_edited_record, key, value)
    db.commit()
    db.refresh(formsubmission_edited_record)
    formsubmission_edited_record = formsubmission_edited_record.to_dict() 

    res = {
        'formsubmission_edited_record': formsubmission_edited_record,
    }
    return res

async def delete_formsubmission_id(db: Session, id: int):

    formsubmission_deleted = None
    record_to_delete = db.query(models.Formsubmission).filter(models.Formsubmission.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        formsubmission_deleted = record_to_delete.to_dict() 

    res = {
        'formsubmission_deleted': formsubmission_deleted,
    }
    return res

async def get_admin_logs(db: Session):

    admin_logs_all = db.query(models.AdminLogs).all()
    admin_logs_all = [new_data.to_dict() for new_data in admin_logs_all] if admin_logs_all else admin_logs_all

    res = {
        'admin_logs_all': admin_logs_all,
    }
    return res

async def get_admin_logs_id(db: Session, id: int):

    admin_logs_one = db.query(models.AdminLogs).filter(models.AdminLogs.id == id).first() 
    admin_logs_one = admin_logs_one.to_dict() if admin_logs_one else admin_logs_one

    res = {
        'admin_logs_one': admin_logs_one,
    }
    return res

async def post_admin_logs(db: Session, raw_data: schemas.PostAdminLogs):
    id:str = raw_data.id
    created_at:str = raw_data.created_at


    record_to_be_added = {'id': id, 'created_at': created_at}
    new_admin_logs = models.AdminLogs(**record_to_be_added)
    db.add(new_admin_logs)
    db.commit()
    db.refresh(new_admin_logs)
    admin_logs_inserted_record = new_admin_logs.to_dict()

    res = {
        'admin_logs_inserted_record': admin_logs_inserted_record,
    }
    return res

async def put_admin_logs_id(db: Session, raw_data: schemas.PutAdminLogsId):
    id:str = raw_data.id
    created_at:str = raw_data.created_at


    admin_logs_edited_record = db.query(models.AdminLogs).filter(models.AdminLogs.id == id).first()
    for key, value in {'id': id, 'created_at': created_at}.items():
          setattr(admin_logs_edited_record, key, value)
    db.commit()
    db.refresh(admin_logs_edited_record)
    admin_logs_edited_record = admin_logs_edited_record.to_dict() 

    res = {
        'admin_logs_edited_record': admin_logs_edited_record,
    }
    return res

async def delete_admin_logs_id(db: Session, id: int):

    admin_logs_deleted = None
    record_to_delete = db.query(models.AdminLogs).filter(models.AdminLogs.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        admin_logs_deleted = record_to_delete.to_dict() 

    res = {
        'admin_logs_deleted': admin_logs_deleted,
    }
    return res

