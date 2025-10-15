# วิธีที่ 1: ใช้เครื่องหมายปีกกา {} นิยมใช้มากที่สุด
student = {
    "name": "sanayu",
    "student_id": "65010001",
    "major": "Computer Engineering",
    "gpa": 3.89
}

# วิธีที่ 2: ใช้ฟังก์ชัน dict() 
teacher = dict(
    name="Ajarn", 
    subject="Math", 
    room=205
)

# สร้าง Dictionary ว่าง
empty_dict = {}

# แสดงผลลัพธ์
# print(f"ข้อมูลนักศึกษา: {student}")
# print(f"ข้อมูลอาจารย์: {teacher}")
# print(f"Dictionary ว่าง: {empty_dict}")


# การเข้าถึงข้อมูล (Accessing)
# 1. ใช้ Square Brackets [] (ถ้า Key ไม่มีอยู่ จะเกิด Error!)
# print(f"ชื่อ: {student['name']}") # ผลลัพธ์: ชื่อ: Sanayu

# กรณี Key ไม่มีอยู่
# print(f"ชื่อ: {student['age']}") # จะเกิด Error

# 2. ใช้เมธอด .get() (ถ้า Key ไม่มีอยู่ จะคืนค่า None หรือค่าที่เรากำหนด ไม่เกิด Error)
# print(f"คณะ: {student.get('faculty')}") # ผลลัพธ์: คณะ: None
# print(f"คณะ: {student.get('faculty', 'ไม่ระบุ')}") # ผลลัพธ์: คณะ: ไม่ระบุ


# เพิ่ม Key ใหม่
student['email'] = 'sanayu.s@example.com'
# print(f"ข้อมูลนักศึกษา: {student}")

# แก้ไข Value ของ Key ที่มีอยู่แล้ว
student['gpa'] = 3.95
# print(f"เกรดเฉลี่ยใหม่: {student['gpa']}")


# 1. ใช้คำสั่ง del (จะลบ Key และ Value ทิ้งไปเลย)
del student['major']

# 2. ใช้เมธอด .pop() (จะลบและคืนค่า Value ออกมาด้วย)
removed_gpa = student.pop('gpa')
# print(f"เกรดที่ถูกลบไปคือ: {removed_gpa}")
# print(f"ข้อมูลนักศึกษา: {student}")


# การวนลูปใน Dictionary มี 3 วิธี

product = {
    "code": "P-001",
    "name": "Keyboard",
    "price": 1500,
    "stock": 50
}

# 1. วนลูปเพื่อเอา Keys (เป็นค่า default)
# for key in product:
#     print(f"Key: {key}, Value: {product[key]}")

# 2. วนลูปเพื่อเอา Values
# for value in product.values():
#     print(f"Value: {value}")

# 3. วนลูปเพื่อเอาทั้ง Key และ Value (วิธีที่นิยมที่สุด)
for key, value in product.items():
    print(f"Key: {key}, Value: {value}")

