from fastapi import APIRouter
from . import views
from .schemas import PRCreate, PROut  # ✅ Fix: import from schemas, not views

router = APIRouter(prefix="/pr", tags=["Purchase Requests"])

router.get("/suppliers")(views.get_suppliers)

router.post("/", response_model=PRCreate)(views.create_purchase_request)
router.get("/", response_model=list[PROut])(views.list_purchase_requests)
router.get("/{pr_id}", response_model=PROut)(views.get_purchase_request)
router.put("/{pr_id}", response_model=PROut)(views.update_purchase_request)
router.delete("/{pr_id}")(views.delete_purchase_request)
