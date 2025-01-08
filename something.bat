@echo off

:: รันไฟล์ readtxt.py
echo Running readtxt.py...
python D:\test\python333\readtxt.py

:: รันไฟล์ queries.py
echo Running queries.py...
python D:\test\python333\queries.py

:: คัดลอกไฟล์ data.txt ไปยังโฟลเดอร์ใหม่
echo Copying data.txt to new folder...
copy D:\test\python333\data.txt D:\test\

:: ข้อความเมื่อเสร็จสิ้น
echo All tasks completed successfully!
pause
