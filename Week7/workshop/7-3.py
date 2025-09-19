"""
โจทย์ที่ 3: ฟังก์ชันสร้างเลขสุ่ม
สร้างฟังก์ชันชื่อ generate_lucky_number ที่:
1. ไม่รับพารามิเตอร์
2. สร้างเลขสุ่มระหว่าง 1-100
3. คืนค่าเลขสุ่มนั้น
4. เรียกใช้ฟังก์ชัน 5 ครั้ง และเก็บผลลัพธ์ในลิสต์
5. แสดงผลลิสต์เลขสุ่มทั้งหมด
6. หาและแสดงเลขที่มากที่สุดและน้อยที่สุด

หมายเหตุ: ใช้ import random และ random.randint(1, 100)
"""


import random
import numpy as np

def generate_lucky_number():
    """ฟังก์ชันสร้างเลขโชค"""
    lucky_num = random.randint(1, 100)
    return lucky_num

# สร้างลิสต์เลขโชค
lucky_numbers = []
for i in range(5):
    number = generate_lucky_number()
    lucky_numbers.append(number)

# แสดงผล
print(f"เลขโชคทั้งหมด: {lucky_numbers}")
print(f"เลขโชคที่มากที่สุด: {np.max(lucky_numbers)}")
print(f"เลขโชคที่น้อยที่สุด: {np.min(lucky_numbers)}")

