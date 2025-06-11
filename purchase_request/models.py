import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class PurchaseRequest(Base):
    __tablename__ = "purchase_requests"
    __table_args__ = {"extend_existing": True}  # ✅ Fix duplicate declaration issue

    pr_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pr_no = Column(String(100), nullable=False)
    rfo_no = Column(String(100), nullable=True)
    date = Column(DateTime, nullable=False)
    supplier_id = Column(ForeignKey("supplier_supplier.id"), nullable=True)
    initiated_by = Column(String(100), nullable=False)
    remark = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.now)

    # Optional relationship (if Supplier model is mapped)
    supplier = relationship("Supplier", backref="rfqs", lazy="joined", foreign_keys=[supplier_id])
