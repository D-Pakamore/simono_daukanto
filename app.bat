set BatchDir=%~dp0
cd /d %BatchDir%
call venv\Scripts\activate
start /b python simono_daukanto/manage.py runserver

start http://127.0.0.1:8000/
