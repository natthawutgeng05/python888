import pyodbc

# ตั้งค่าการเชื่อมต่อ
conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=localhost;'
                      'DATABASE=test;'
                      'UID=sa;'
                      'PWD=YourPassword123!')

cursor = conn.cursor()

# ตัวอย่าง: การรันคำสั่ง SQL
def run_queries():
    query = "SELECT * FROM your_table"
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

# เรียกใช้ฟังก์ชัน
run_queries()

conn.close()
