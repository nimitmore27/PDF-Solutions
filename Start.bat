@echo off
cd /d "D:\path\to\your\project"

call env\Scripts\activate.bat

start "chrome.exe" http://127.0.0.1:5505/merge

python app.py