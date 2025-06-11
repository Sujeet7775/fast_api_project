from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum
import uuid


class PurchaseRequest(BaseModel):
    pr_no: str = Field(..., description="Purchase Request Number")
    rfo_no: Optional[str] = Field(None, description="RFO Number")
    date: datetime = Field(..., description="Date")
    supplier: Optional[str] = Field(None, description="Supplier")
    pr_attachment: Optional[str] = Field(None, description="PR Attachment file path/URL")
    initiated_by: str = Field(..., description="Initiated By")
    remark: Optional[str] = Field(None, description="Remark")
    items: List[PRItem] = Field(..., min_items=1, description="List of items")