@echo off

:: รันไฟล์ readtxt.py
echo Running readtxt_sql.py...
python .\readtxt_sql.py

:: รันไฟล์ queries.py
echo Running queries_SQL.py...
python .\queries_SQL.py

:: คัดลอกไฟล์ data.txt ไปยังโฟลเดอร์ใหม่
echo Copying data.txt to new folder...
copy .\data.txt D:\test\

:: ข้อความเมื่อเสร็จสิ้น
echo All tasks completed successfully!
pause
