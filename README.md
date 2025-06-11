# FastAPI Project Setup Guide

This guide will walk you through setting up a FastAPI project from scratch, including creating a virtual environment, installing dependencies, and running your application.

## Prerequisites

- Python 3.7+ installed on your system
- pip (Python package installer)

## Project Structure

Create your project directory with the following structure:

```
my-fastapi-project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   └── __init__.py
│   ├── routers/
│   │   └── __init__.py
│   └── dependencies.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Step 1: Create Project Directory

```bash
mkdir my-fastapi-project
cd my-fastapi-project
```

## Step 2: Create Virtual Environment

Create and activate a Python virtual environment to isolate your project dependencies:

### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### On macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt, indicating the virtual environment is active.

## Step 3: Create Requirements File

Create a `requirements.txt` file with the following essential packages:

```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
python-multipart==0.0.6
pydantic==2.5.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-decouple==3.8
sqlalchemy==2.0.23
alembic==1.13.1
```

### Package Descriptions:

- **fastapi**: The FastAPI framework itself
- **uvicorn**: ASGI server for running FastAPI applications
- **python-multipart**: For handling form data and file uploads
- **pydantic**: Data validation and settings management
- **python-jose**: For JWT token handling (authentication)
- **passlib**: Password hashing utilities
- **python-decouple**: Environment variable management
- **sqlalchemy**: SQL toolkit and ORM
- **alembic**: Database migration tool for SQLAlchemy

## Step 4: Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

## Step 5: Create Basic FastAPI Application

Create the main application file `app/main.py`:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="My FastAPI Project",
    description="A sample FastAPI application",
    version="1.0.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
```

## Step 6: Create Additional Files

### Create `app/__init__.py`:
```python
# This file makes the app directory a Python package
```

### Create `.env` file for environment variables:
```env
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### Create `.gitignore`:
```gitignore
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environment
venv/
env/
ENV/

# Environment variables
.env
.env.local
.env.*.local

# IDE
.vscode/
.idea/
*.swp
*.swo

# Database
*.db
*.sqlite

# Logs
*.log
```

## Step 7: Run the Application

Start your FastAPI development server:

```bash
python -m uvicorn app.main:app --reload
```

### Command Breakdown:
- `python -m uvicorn`: Run uvicorn as a Python module
- `app.main:app`: Import path to your FastAPI instance
- `--reload`: Enable auto-reload on code changes (development only)

### Additional Uvicorn Options:
```bash
# Run on specific host and port
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Run with specific log level
python -m uvicorn app.main:app --reload --log-level debug

# Run for production (without reload)
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Step 8: Access Your Application

Once the server is running, you can access:

- **API**: http://localhost:8000
- **Interactive API docs (Swagger)**: http://localhost:8000/docs
- **Alternative API docs (ReDoc)**: http://localhost:8000/redoc

## Development Workflow

1. **Activate virtual environment** (if not already active):
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

2. **Install new packages**:
   ```bash
   pip install package-name
   pip freeze > requirements.txt  # Update requirements
   ```

3. **Run the application**:
   ```bash
   python -m uvicorn app.main:app --reload
   ```

4. **Deactivate virtual environment** when done:
   ```bash
   deactivate
   ```

## Production Deployment

For production deployment, consider:

1. **Use environment-specific requirements**:
   ```bash
   pip install gunicorn  # For production WSGI server
   ```

2. **Run with Gunicorn**:
   ```bash
   gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
   ```

3. **Set proper environment variables**
4. **Configure reverse proxy (Nginx)**
5. **Set up SSL certificates**
6. **Configure logging and monitoring**

## Common Issues and Solutions

### Virtual Environment Issues
- **Problem**: `venv\Scripts\activate` not found
- **Solution**: Ensure you're in the correct directory and Python is properly installed

### Import Errors
- **Problem**: Module not found errors
- **Solution**: Ensure virtual environment is activated and packages are installed

### Port Already in Use
- **Problem**: `Address already in use`
- **Solution**: Use a different port: `--port 8001` or kill the process using the port

## Next Steps

1. Add database models using SQLAlchemy
2. Implement authentication and authorization
3. Create API routers for better organization
4. Add input validation with Pydantic models
5. Implement error handling and logging
6. Write tests using pytest
7. Set up CI/CD pipeline

## Useful Commands Reference

```bash
# Virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS/Linux
deactivate

# Package management
pip install -r requirements.txt
pip freeze > requirements.txt
pip list

# Run application
python -m uvicorn app.main:app --reload
python -m uvicorn app.main:app --reload --port 8001
```

This guide provides a solid foundation for starting your FastAPI project. Customize the structure and dependencies based on your specific requirements.