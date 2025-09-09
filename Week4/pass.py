users = [
    {"name": "Alice", "status": "active"},
    {"name": "Bob", "status": "banned"},
    {"name": "Charlie", "status": "active"}
]

for user in users:
    if user["status"] == "active":
        print(f"กำลังส่งอีเมลหาผู้ใช้: {user['name']}")
    
    elif user["status"] == "banned":
        # TODO: ยังไม่ได้คิดว่าจะทำอะไรกับผู้ใช้ที่ถูกแบน อาจจะต้องบันทึก log
        # ใส่ pass ไว้ก่อนเพื่อให้โปรแกรมไม่ error
        pass

    print("--- ตรวจสอบคนถัดไป ---")

print("จบการทำงาน")

