# Device Data Entry Web App

A lightweight internal tool built using Flask that allows users to enter readings and push the data securely to a Google Sheet and no login or dashboard required.

---

## Features

- Simple web form for recording data into google sheets
- Real time submission to Google Sheets
- Built using Python, Flask, HTML, CSS
- Easily scalable and internally deployable
- No authentication needed

### 1. Clone this repo
```bash
git clone https://github.com/shubhamsingh47/Python_integration_GoogleSheets.git
cd Python_integration_GoogleSheets

2. Set up your Python environment
conda create -n venv python=3.10
conda activate venv
pip install -r requirements.txt

3. Setup Google Sheets API
- Go to Google Cloud Console
- Create a new project
- Enable Google Sheets API and Google Drive API
- Create a Service Account and download the creds.json file
- Save the creds.json in your project root

4. Share your Google Sheet
- Open your target Google Sheet
- Click Share
- Add the service account email from creds.json as Editor
      Example: (your-service-account@your-project.iam.gserviceaccount.com)

5. Update Sheet ID and worksheet name
- SHEET_ID = "your_google_sheet_id_here"
- WORKSHEET_NAME = "Sheet1"


