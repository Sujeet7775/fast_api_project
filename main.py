from fastapi import FastAPI
# from rfq.routes import router as rfq_router
from purchase_request.routes import router as purchase_request_router

app = FastAPI(title="RFQ System")

# Register routes
# app.include_router(rfq_router, prefix="/api", tags=["RFQ"])
app.include_router(purchase_request_router, prefix="/api", tags=["Purchase Request"])

@app.get("/")
def root():
    return {"message": "🚀 FastAPI + SQLAlchemy is running!"}
