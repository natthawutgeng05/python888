import sqlite3

# เชื่อมต่อกับฐานข้อมูล SQLite3 (จะสร้างไฟล์ .db ขึ้นมาในโฟลเดอร์ที่ใช้)
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# สร้างตารางหากยังไม่มี
cursor.execute('''
CREATE TABLE IF NOT EXISTS SalesData (
    Date TEXT,
    ProductCode TEXT,
    Sold INTEGER,
    Returned INTEGER,
    Damaged INTEGER,
    PRIMARY KEY (Date, ProductCode)
)
''')

# อ่านข้อมูลจากไฟล์ .txt
data_list = []

with open('data.txt', 'r') as file:
    for line in file:
        # แยกข้อมูลในแต่ละบรรทัดโดยใช้เครื่องหมาย "|" เป็นตัวแบ่ง
        data = line.strip().split('|')
        date = data[0]
        product_code = data[1]
        sold = int(data[2])
        returned = int(data[3])
        damaged = int(data[4])
        
        # เก็บข้อมูลในรูปแบบ tuple ลงใน list
        data_list.append((date, product_code, sold, returned, damaged))

# เรียงข้อมูลตามวันที่และรหัสสินค้า
data_list.sort(key=lambda x: (x[0], x[1]))  # เรียงตามวันที่และรหัสสินค้า

# ลบข้อมูลเดิมที่ตรงกับข้อมูลใหม่ก่อน
for data in data_list:
    date, product_code, sold, returned, damaged = data
    
    # เช็คก่อนว่ามีข้อมูลนี้ในฐานข้อมูลหรือไม่
    cursor.execute('''
    SELECT COUNT(*) FROM SalesData WHERE Date = ? AND ProductCode = ?
    ''', (date, product_code))
    
    count = cursor.fetchone()[0]
    
    if count > 0:
        # ถ้ามีข้อมูลอยู่แล้ว ทำการ UPDATE
        cursor.execute('''
        UPDATE SalesData
        SET Sold = ?, Returned = ?, Damaged = ?
        WHERE Date = ? AND ProductCode = ?
        ''', (sold, returned, damaged, date, product_code))
    else:
        # ถ้ายังไม่มีข้อมูลนี้, ทำการ INSERT
        cursor.execute('''
        INSERT INTO SalesData (Date, ProductCode, Sold, Returned, Damaged)
        VALUES (?, ?, ?, ?, ?)
        ''', (date, product_code, sold, returned, damaged))

# บันทึกการเปลี่ยนแปลง
conn.commit()

# ตรวจสอบข้อมูลในตาราง
cursor.execute('SELECT * FROM SalesData')
rows = cursor.fetchall()

# แสดงข้อมูล
for row in rows:
    print(row)

# ปิดการเชื่อมต่อ
conn.close()
