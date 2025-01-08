import sqlite3
from datetime import datetime

# เชื่อมต่อฐานข้อมูล SQLite (หรือสร้างไฟล์ใหม่ถ้าไม่มี)
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# ฟังก์ชั่นสร้างตารางถ้ายังไม่มี
def create_table():
    query = '''
    CREATE TABLE IF NOT EXISTS your_table (
        id TEXT NOT NULL,
        date TEXT NOT NULL,
        PRIMARY KEY (id, date)
    );
    '''
    cursor.execute(query)
    conn.commit()

# ฟังก์ชั่นสำหรับนำข้อมูลจากไฟล์ .txt เข้า DB พร้อมกับตรวจสอบและอัปเดตข้อมูล
def import_data_to_db(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # ลบช่องว่างที่ไม่จำเป็นออก
            line = line.strip()
            
            # ถ้ามีข้อมูลในบรรทัด
            if line:
                # เปลี่ยนการแยกข้อมูลจากช่องว่างเป็นแยกด้วย '|'
                fields = line.split('|')
                
                # ตรวจสอบความยาวของ fields ก่อน
                if len(fields) >= 2:
                    record_date = fields[0]
                    record_id = fields[1]
                    
                    # เช็กว่ามีข้อมูลนี้ในฐานข้อมูลหรือไม่ (เช็กตาม id และช่วงวันที่)
                    query = "SELECT * FROM your_table WHERE id = ? AND date = ?"
                    cursor.execute(query, (record_id, record_date))
                    existing_record = cursor.fetchone()
                    
                    # ถ้ามีข้อมูลเดิม ให้ลบข้อมูลเก่าออกก่อน
                    if existing_record:
                        delete_query = "DELETE FROM your_table WHERE id = ? AND date = ?"
                        cursor.execute(delete_query, (record_id, record_date))
                        print(f"ลบข้อมูลเก่า: {record_id}, {record_date}")
                    
                    # เพิ่มข้อมูลใหม่เข้าไป
                    insert_query = "INSERT INTO your_table (id, date) VALUES (?, ?)"
                    cursor.execute(insert_query, (record_id, record_date))
                    conn.commit()
                    print(f"เพิ่มข้อมูลใหม่: {record_id}, {record_date}")
                else:
                    print(f"ข้อมูลไม่ครบ: {line}")
            else:
                print("บรรทัดว่างหรือไม่ถูกต้อง")

# เรียกใช้ฟังก์ชั่นสร้างตารางถ้าจำเป็น
create_table()

# เรียกใช้ฟังก์ชั่นในการนำข้อมูลจากไฟล์เข้า DB
import_data_to_db('data.txt')

# ปิดการเชื่อมต่อ
cursor.close()
conn.close()
