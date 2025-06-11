from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from core.db import SessionLocal
from rfq.schemas import RFQCreate
from .models import RFQ
import uuid
from . import Supplier
from core.db import Base


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# ---------- CRUD Views ----------
def create_rfq(rfq: RFQCreate, db: Session = Depends(get_db)):
    db_rfq = RFQ(**rfq.model_dump())
    db.add(db_rfq)
    db.commit()
    db.refresh(db_rfq)
    return db_rfq

def list_rfqs(db: Session = Depends(get_db)):
    return db.query(RFQ).all()

def get_rfq(rfq_id: uuid.UUID, db: Session = Depends(get_db)):
    rfq = db.query(RFQ).filter(RFQ.pr_id == rfq_id).first()
    if not rfq:
        raise HTTPException(status_code=404, detail="RFQ not found")
    return rfq

def update_rfq(rfq_id: uuid.UUID, rfq_data: RFQCreate, db: Session = Depends(get_db)):
    rfq = db.query(RFQ).filter(RFQ.pr_id == rfq_id).first()
    if not rfq:
        raise HTTPException(status_code=404, detail="RFQ not found")

    for key, value in rfq_data.model_dump().items():
        setattr(rfq, key, value)

    db.commit()
    db.refresh(rfq)
    return rfq

def delete_rfq(rfq_id: uuid.UUID, db: Session = Depends(get_db)):
    rfq = db.query(RFQ).filter(RFQ.pr_id == rfq_id).first()
    if not rfq:
        raise HTTPException(status_code=404, detail="RFQ not found")

    db.delete(rfq)
    db.commit()
    return {"detail": "RFQ deleted successfully"}

Supplier = Base.classes.supplier_supplier

def get_suppliers(db: Session = Depends(get_db)):
    
    a = db.query(Supplier).all()
    print
    return a
