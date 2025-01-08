import pyodbc

# การเชื่อมต่อกับ SQL Server
conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=localhost;'
                      'DATABASE=test;'
                      'UID=sa;'
                      'PWD=YourPassword123!')
cursor = conn.cursor()

# ฟังก์ชันนำข้อมูลเข้า
def import_data_to_db(file_path):
    # อ่านข้อมูลจากไฟล์
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # จัดเตรียมข้อมูลที่อ่านได้
    data = []
    for line in lines:
        fields = line.strip().split('|')
        if len(fields) < 5:
            print(f"ข้อมูลไม่ครบ: {line}")
            continue
        record_date, record_id, value1, value2, value3 = fields
        data.append((record_date, record_id, value1, value2, value3))

    # จัดเรียงข้อมูลตามวันที่และรหัส
    data = sorted(data, key=lambda x: (x[0], x[1]))

    # ตรวจสอบช่วงข้อมูลในฐานข้อมูล
    if data:
        start_date = data[0][0]  # วันที่เริ่มต้นของข้อมูล
        end_date = data[-1][0]  # วันที่สิ้นสุดของข้อมูล

        # ลบข้อมูลช่วงที่ซ้ำ
        print(f"ลบข้อมูลในช่วงวันที่ {start_date} ถึง {end_date}")
        cursor.execute("""
            DELETE FROM your_table
            WHERE record_date BETWEEN ? AND ?
        """, start_date, end_date)

        # เพิ่มข้อมูลใหม่
        print("นำเข้าข้อมูลใหม่")
        for record in data:
            cursor.execute("""
                INSERT INTO your_table (record_date, record_id, value1, value2, value3)
                VALUES (?, ?, ?, ?, ?)
            """, record)

    # ยืนยันการเปลี่ยนแปลง
    conn.commit()
    print("นำข้อมูลเข้าสำเร็จ")

# เรียกใช้งานฟังก์ชัน
import_data_to_db('data.txt')

# ปิดการเชื่อมต่อ
conn.close()
