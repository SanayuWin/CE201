# รับค่าแม่สูตรคูณสุดท้ายที่ต้องการจากผู้ใช้
last_mother = int(input("ต้องการดูสูตรคูณถึงแม่ไหน: "))

# ลูปด้านนอก (Outer Loop) สำหรับควบคุม "แม่สูตรคูณ"
# เราเริ่มที่แม่ 2 และไปจนถึงแม่ที่ผู้ใช้ป้อน (ต้อง +1 ใน range)
for mother_table in range(2, last_mother + 1):
    print(f"--- แม่ {mother_table} ---")
    
    # ลูปด้านใน (Inner Loop) สำหรับตัวคูณ 1 ถึง 12
    for i in range(1, 13):
        result = mother_table * i
        print(f"{mother_table} x {i} = {result}")