from fastapi import FastAPI
from rfq.routes import router as rfq_router

app = FastAPI(title="RFQ System")

# Register routes
app.include_router(rfq_router, prefix="/api", tags=["RFQ"])

@app.get("/")
def root():
    return {"message": "🚀 FastAPI + SQLAlchemy is running!"}
