from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    try:
        return await service.get_users(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id')
async def get_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db)):
    try:
        return await service.post_users(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(raw_data: schemas.PutUsersId, db: Session = Depends(get_db)):
    try:
        return await service.put_users_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id')
async def delete_users_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_users_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/leads/')
async def get_leads(db: Session = Depends(get_db)):
    try:
        return await service.get_leads(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/leads/id')
async def get_leads_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_leads_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/leads/')
async def post_leads(id: str, created_at: str, name: str, email: str, phone: str, message: str, attachments: str, source: str, status: str, address_city: str, address_state: str, db: Session = Depends(get_db)):
    try:
        return await service.post_leads(db, id, created_at, name, email, phone, message, attachments, source, status, address_city, address_state)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/leads/id/')
async def put_leads_id(raw_data: schemas.PutLeadsId, db: Session = Depends(get_db)):
    try:
        return await service.put_leads_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/leads/id')
async def delete_leads_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_leads_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/formsubmission/')
async def get_formsubmission(db: Session = Depends(get_db)):
    try:
        return await service.get_formsubmission(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/formsubmission/id')
async def get_formsubmission_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_formsubmission_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/formsubmission/')
async def post_formsubmission(raw_data: schemas.PostFormsubmission, db: Session = Depends(get_db)):
    try:
        return await service.post_formsubmission(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/formsubmission/id/')
async def put_formsubmission_id(raw_data: schemas.PutFormsubmissionId, db: Session = Depends(get_db)):
    try:
        return await service.put_formsubmission_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/formsubmission/id')
async def delete_formsubmission_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_formsubmission_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/admin_logs/')
async def get_admin_logs(db: Session = Depends(get_db)):
    try:
        return await service.get_admin_logs(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/admin_logs/id')
async def get_admin_logs_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_admin_logs_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/admin_logs/')
async def post_admin_logs(raw_data: schemas.PostAdminLogs, db: Session = Depends(get_db)):
    try:
        return await service.post_admin_logs(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/admin_logs/id/')
async def put_admin_logs_id(raw_data: schemas.PutAdminLogsId, db: Session = Depends(get_db)):
    try:
        return await service.put_admin_logs_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/admin_logs/id')
async def delete_admin_logs_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_admin_logs_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

