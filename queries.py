import sqlite3

# เชื่อมต่อกับฐานข้อมูล
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# คำสั่ง SQL เพื่อดูข้อมูลทั้งหมดจากตาราง
query = "SELECT * FROM your_table"
cursor.execute(query)

# ดึงข้อมูลทั้งหมด
rows = cursor.fetchall()

# แสดงผลลัพธ์
for row in rows:
    print(row)

# ปิดการเชื่อมต่อ
cursor.close()
conn.close()
