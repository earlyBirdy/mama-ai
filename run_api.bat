@echo off
setlocal
cd /d %~dp0
set PYTHONPATH=%cd%
uvicorn src.api:app --reload
