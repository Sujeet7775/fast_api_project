from fastapi import APIRouter
from . import views
from .schemas import RFQOut  # ✅ Fix: import from schemas, not views

router = APIRouter(prefix="/rfq", tags=["RFQ"])

router.get("/suppliers")(views.get_suppliers)
router.post("/", response_model=RFQOut)(views.create_rfq)
router.get("/", response_model=list[RFQOut])(views.list_rfqs)
router.get("/{rfq_id}", response_model=RFQOut)(views.get_rfq)
router.put("/{rfq_id}", response_model=RFQOut)(views.update_rfq)
router.delete("/{rfq_id}")(views.delete_rfq)
