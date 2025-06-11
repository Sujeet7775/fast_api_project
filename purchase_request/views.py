from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from core.db import SessionLocal
from purchase_request.schemas import PRCreate
from purchase_request.models import PurchaseRequest
import uuid
from .import Supplier
from core.db import Base


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# ---------- CRUD Views ----------
def create_purchase_request(pr: PRCreate, db: Session = Depends(get_db)):
    db_pr = PurchaseRequest(**pr.model_dump())
    db.add(db_pr)
    db.commit()
    db.refresh(db_pr)
    return db_pr

def list_purchase_requests(db: Session = Depends(get_db)):
    return db.query(PurchaseRequest).all()

def get_purchase_request(pr_id: uuid.UUID, db: Session = Depends(get_db)):
    pr = db.query(PurchaseRequest).filter(PurchaseRequest.pr_id == pr_id).first()
    if not pr:
        raise HTTPException(status_code=404, detail="Purchase Request not found")
    return pr

def update_purchase_request(pr_id: uuid.UUID, pr_data: PRCreate, db: Session = Depends(get_db)):
    pr = db.query(PurchaseRequest).filter(PurchaseRequest.pr_id == pr_id).first()
    if not pr:
        raise HTTPException(status_code=404, detail="Purchase Request not found")

    for key, value in pr_data.model_dump().items():
        setattr(pr, key, value)

    db.commit()
    db.refresh(pr)
    return pr

def delete_purchase_request(pr_id: uuid.UUID, db: Session = Depends(get_db)):
    pr = db.query(PurchaseRequest).filter(PurchaseRequest.pr_id == pr_id).first()
    if not pr:
        raise HTTPException(status_code=404, detail="Purchase Request not found")

    db.delete(pr)
    db.commit()
    return {"detail": "Purchase Request deleted successfully"}

Supplier = Base.classes.supplier_supplier

def get_suppliers(db: Session = Depends(get_db)):
    
    a = db.query(Supplier).all()
    print
    return a
