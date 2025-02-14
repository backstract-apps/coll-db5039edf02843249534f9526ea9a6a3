from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Users(BaseModel):
    id: int
    created_at: str
    username: str
    email: str
    password: str
    role: str


class ReadUsers(BaseModel):
    id: int
    created_at: str
    username: str
    email: str
    password: str
    role: str
    class Config:
        from_attributes = True


class Leads(BaseModel):
    id: int
    created_at: str
    name: str
    email: str
    phone: str
    address_city: str
    address_state: str
    message: str
    attachments: str
    source: str
    status: str


class ReadLeads(BaseModel):
    id: int
    created_at: str
    name: str
    email: str
    phone: str
    address_city: str
    address_state: str
    message: str
    attachments: str
    source: str
    status: str
    class Config:
        from_attributes = True


class Formsubmission(BaseModel):
    id: int
    created_at: str
    name: str
    email: str
    phone: str
    message: str
    attachment: Any


class ReadFormsubmission(BaseModel):
    id: int
    created_at: str
    name: str
    email: str
    phone: str
    message: str
    attachment: Any
    class Config:
        from_attributes = True


class AdminLogs(BaseModel):
    id: int
    created_at: str
    adminId: str
    leadId: str
    action: str


class ReadAdminLogs(BaseModel):
    id: int
    created_at: str
    adminId: str
    leadId: str
    action: str
    class Config:
        from_attributes = True




class PostUsers(BaseModel):
    id: int
    created_at: str
    username: str
    email: str
    password: str
    role: str

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: str
    created_at: str

    class Config:
        from_attributes = True



class PutLeadsId(BaseModel):
    id: str
    created_at: str

    class Config:
        from_attributes = True



class PostFormsubmission(BaseModel):
    id: str
    created_at: str

    class Config:
        from_attributes = True



class PutFormsubmissionId(BaseModel):
    id: str
    created_at: str

    class Config:
        from_attributes = True



class PostAdminLogs(BaseModel):
    id: str
    created_at: str

    class Config:
        from_attributes = True



class PutAdminLogsId(BaseModel):
    id: str
    created_at: str

    class Config:
        from_attributes = True

