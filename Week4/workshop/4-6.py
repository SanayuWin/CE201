# โปรแกรม Transcript คำนวณ GPA แบบถ่วงน้ำหนัก
# ใช้ while loop และตัวแปรธรรมดา

# dictionary แปลงเกรดตัวอักษร -> ค่าคะแนน
grade_point = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "D+": 1.5,
    "D": 1.0,
    "F": 0.0
}

# รับจำนวนวิชา
n = int(input("กรอกจำนวนวิชา: "))

# ตัวแปรสะสม
total_credit = 0
total_point = 0
count = 0

# ใช้ while loop รับข้อมูลทีละวิชา
while count < n:
    print(f"\nวิชา {count+1}:")
    name = input("ชื่อวิชา: ")
    credit = int(input("หน่วยกิต: "))
    grade = input("เกรด (A, B+, B, C+, C, D+, D, F): ")

    # ตรวจสอบเกรด
    if grade not in grade_point:
        print(f"เกรด {grade} ไม่ถูกต้อง (นับเป็น F)")
        grade_value = 0
    else:
        grade_value = grade_point[grade]

    # คำนวณสะสม
    total_point += grade_value * credit
    total_credit += credit

    count += 1  # เพิ่มจำนวนวิชาที่นับไปแล้ว

# คำนวณ GPA
gpa = total_point / total_credit if total_credit > 0 else 0

# แสดงผล
print("\n------------------------------")
print(f"เกรดเฉลี่ย (GPA): {gpa:.2f}")
