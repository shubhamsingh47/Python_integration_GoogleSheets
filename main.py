from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from utils import get_sheet
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Your Google Sheet ID and Worksheet Name
SHEET_ID = "1ayzRdWJZUZLx4xkrESsth-uak5tm3mbJdFjQtN1qMzo"
WORKSHEET_NAME = "Sheet1"

@app.get("/", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/submit")
def submit(
    Date: str = Form(...),
    Day: str = Form(...),
    ID: str = Form(...),
    Name: str = Form(...),
    Weight: str = Form(...),
    Site: str = Form(...),
    Dev: str = Form(...),
    Old: str = Form(None),
    new: str = Form(None),
    Standard: str = Form(None),
    X1: int = Form(None),
    X2: int = Form(None),
    X3: int = Form(None),
    X4: int = Form(None),
    X5: int = Form(None),
    X6: int = Form(None),
    X7: int = Form(None),
    X8: int = Form(None),
    X9: int = Form(None),
    X10: int = Form(None)
):
    sheet = get_sheet(SHEET_ID, WORKSHEET_NAME)
    row = [
        Date, Day, ID, Name, Weight, Site, Dev, old, new, standard,
        X1, X2, X3, X4, X5, X6, X7, X8, X9, X10
    ]
    sheet.append_row(row)
    return RedirectResponse("/", status_code=303)
