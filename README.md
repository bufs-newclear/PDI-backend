## How to run
### Windows
```powershell
py -m venv venv

# Powershell의 경우 아래 행을 실행
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser

./venv/Scripts/Activate.ps1
pip install -r requirements.txt

./manage.py migrate
./manage.py createsuperuser

./manage.py runserver
```
