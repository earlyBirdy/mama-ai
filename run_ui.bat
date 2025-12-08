@echo off
setlocal
cd /d %~dp0
set PYTHONPATH=%cd%
streamlit run src.ui_demo.py
