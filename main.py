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
    Serial: str = Form(...),
    BabyID: str = Form(...),
    Weight: str = Form(...),
    Site: str = Form(...),
    Device: str = Form(...),
    MBJ20: str = Form(None),
    JM103: str = Form(None),
    TSB: str = Form(None),
    F1: int = Form(None),
    F2: int = Form(None),
    F3: int = Form(None),
    F4: int = Form(None),
    F5: int = Form(None),
    F6: int = Form(None),
    F7: int = Form(None),
    F8: int = Form(None),
    F9: int = Form(None),
    F10: int = Form(None)
):
    sheet = get_sheet(SHEET_ID, WORKSHEET_NAME)
    row = [
        Date, Day, Serial, BabyID, Weight, Site, Device, MBJ20, JM103, TSB,
        F1, F2, F3, F4, F5, F6, F7, F8, F9, F10
    ]
    sheet.append_row(row)
    return RedirectResponse("/", status_code=303)
