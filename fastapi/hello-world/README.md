Step 1:

Create a folder like fastapi/hello-world
CD to hello-world

Step 2: Create and activate venv
python3 -m venv .venv
source .venv/bin/activate

Step 3: Install fastapi and uvicorn
pip install fastapi uvicorn

Step 4: Create main.py

Step 5: Run the FastAPI app using uvicorn

uvicorn main:app --reload
main -> Python file name without .py extension
app -> variable name for FastAPI app object
--reload -> automatic reload on code change