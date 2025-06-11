import uuid
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

# ---------- Schemas ----------
class PRCreate(BaseModel):
    pr_no: str
    rfo_no: Optional[str]
    date: datetime
    supplier_id: Optional[int]
    initiated_by: str
    remark: Optional[str]

class PROut(PRCreate):
    pr_id: uuid.UUID
    created_at: datetime

    class Config:
        from_attributes = True
