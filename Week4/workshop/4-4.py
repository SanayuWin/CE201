sales_data = [1500, 2000, -500, 3000, -250, 4500, 1800]

total_sales = 0
valid_days = 0

# วนลูปเพื่อดูยอดขายแต่ละวัน
for sale in sales_data:
    # ตรวจสอบข้อมูลที่ผิดพลาด
    if sale < 0:
        print(f"เจอยอดขายที่ผิดพลาด ({sale}) ข้ามรายการนี้ไป")
        continue # ข้ามไปทำงานรอบถัดไปทันที

    # บรรทัดข้างล่างนี้จะทำงานเฉพาะยอดขายที่ไม่ติดลบ
    total_sales += sale
    valid_days += 1

print("\n--- สรุปยอดขาย ---")
print(f"ยอดขายรวมทั้งหมด: {total_sales} บาท")
print(f"จำนวนวันที่ขายได้จริง: {valid_days} วัน")