names = ["สมชาย", "สมศรี", "สมปอง", "สมศักดิ์", "สมหญิง"]
name_to_find = "สมศักดิ์"

for name in names:
    print(f"กำลังตรวจสอบชื่อ: {name}")
    if name == name_to_find:
        print(f"เจอแล้ว! {name_to_find} อยู่ในลิสต์")
        break # ออกจาก for loop ทันที

print("--- สิ้นสุดการค้นหา ---")

