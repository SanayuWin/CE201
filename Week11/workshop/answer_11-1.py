"""
เฉลย Workshop 11-1: File I/O - เขียนและอ่านไฟล์
"""

# รับข้อมูลจากผู้ใช้
name = input("กรุณากรอกชื่อของคุณ: ")
age = input("กรุณากรอกอายุของคุณ: ")

# เขียนข้อมูลลงไฟล์
with open("student_info.txt", "w", encoding="utf-8") as file:
    file.write(f"ชื่อ: {name}\n")
    file.write(f"อายุ: {age} ปี\n")

print("บันทึกข้อมูลเรียบร้อย!\n")

# อ่านข้อมูลจากไฟล์
print("--- ข้อมูลที่บันทึกในไฟล์ ---")
with open("student_info.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
