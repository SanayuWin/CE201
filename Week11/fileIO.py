"""
ตัวอย่างการใช้งาน File I/O ด้วย with open()
ประกอบด้วย: read, write, และ append
"""

print("=" * 60)
print("ตัวอย่างที่ 1: การเขียนไฟล์ (Write Mode)")
print("=" * 60)
"""
Write Mode ('w'):
- สร้างไฟล์ใหม่หรือเขียนทับไฟล์เดิม (ข้อมูลเดิมจะหายหมด)
- ถ้าไฟล์ไม่มีอยู่ จะสร้างไฟล์ใหม่
- ใช้เมื่อต้องการเขียนข้อมูลใหม่ทั้งหมด
"""

# เขียนข้อมูลลงไฟล์
with open('example.txt', 'w', encoding='utf-8') as file:
    file.write("สวัสดีครับ\n")
    file.write("นี่คือตัวอย่างการเขียนไฟล์\n")
    file.write("บรรทัดที่ 3\n")
    
print("✓ เขียนไฟล์ example.txt เรียบร้อย")
print()

print("=" * 60)
print("ตัวอย่างที่ 2: การอ่านไฟล์ (Read Mode)")
print("=" * 60)
"""
Read Mode ('r'):
- อ่านข้อมูลจากไฟล์ที่มีอยู่แล้ว
- ถ้าไฟล์ไม่มี จะเกิด error
- ไม่สามารถแก้ไขหรือเขียนข้อมูลได้
"""

# วิธีที่ 1: อ่านทั้งหมดด้วย read()
print("\n[วิธีที่ 1] อ่านทั้งหมดด้วย read():")
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# วิธีที่ 2: อ่านทีละบรรทัดด้วย readline()
print("\n[วิธีที่ 2] อ่านทีละบรรทัดด้วย readline():")
with open('example.txt', 'r', encoding='utf-8') as file:
    line1 = file.readline()
    line2 = file.readline()
    print(f"บรรทัด 1: {line1.strip()}")
    print(f"บรรทัด 2: {line2.strip()}")

# วิธีที่ 3: อ่านทั้งหมดเป็น list ด้วย readlines()
print("\n[วิธีที่ 3] อ่านทั้งหมดเป็น list ด้วย readlines():")
with open('example.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for i, line in enumerate(lines, 1):
        print(f"บรรทัด {i}: {line.strip()}")

# วิธีที่ 4: อ่านด้วย for loop (แนะนำสำหรับไฟล์ใหญ่)
print("\n[วิธีที่ 4] อ่านด้วย for loop (ประหยัดหน่วยความจำ):")
with open('example.txt', 'r', encoding='utf-8') as file:
    for i, line in enumerate(file, 1):
        print(f"บรรทัด {i}: {line.strip()}")

print()

print("=" * 60)
print("ตัวอย่างที่ 3: การเพิ่มข้อมูลต่อท้าย (Append Mode)")
print("=" * 60)
"""
Append Mode ('a'):
- เพิ่มข้อมูลต่อท้ายไฟล์เดิม (ไม่ลบข้อมูลเก่า)
- ถ้าไฟล์ไม่มีอยู่ จะสร้างไฟล์ใหม่
- ใช้เมื่อต้องการเก็บข้อมูลเพิ่มเติมโดยไม่ลบของเดิม
"""

# เพิ่มข้อมูลต่อท้ายไฟล์
with open('example.txt', 'a', encoding='utf-8') as file:
    file.write("บรรทัดที่ 4 (เพิ่มด้วย append)\n")
    file.write("บรรทัดที่ 5 (เพิ่มด้วย append)\n")

print("✓ เพิ่มข้อมูลต่อท้ายไฟล์ example.txt เรียบร้อย")

# อ่านไฟล์หลังจาก append
print("\nอ่านไฟล์หลังจาก append:")
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

print()

print("=" * 60)
print("สรุป Modes ที่ใช้บ่อย:")
print("=" * 60)
print("""
Mode | คำอธิบาย
-----|----------
'r'  | Read - อ่านอย่างเดียว (ไฟล์ต้องมีอยู่แล้ว)
'w'  | Write - เขียนทับ (ลบข้อมูลเดิม, สร้างไฟล์ใหม่ถ้าไม่มี)
'a'  | Append - เพิ่มต่อท้าย (เก็บข้อมูลเดิม, สร้างไฟล์ใหม่ถ้าไม่มี)
'r+' | Read + Write - อ่านและเขียน (ไฟล์ต้องมีอยู่แล้ว)
'w+' | Write + Read - เขียนและอ่าน (ลบข้อมูลเดิม)
'a+' | Append + Read - เพิ่มต่อท้ายและอ่าน

หมายเหตุ: ใช้ encoding='utf-8' เพื่อรองรับภาษาไทย
""")

print("=" * 60)
print("ข้อดีของการใช้ with open():")
print("=" * 60)
print("""
1. ไม่ต้องเขียน file.close() เอง
2. ไฟล์จะถูกปิดอัตโนมัติเมื่อออกจาก with block
3. ปลอดภัยกว่า - แม้เกิด error ไฟล์ก็จะถูกปิด
4. โค้ดสะอาดและอ่านง่ายกว่า
""")
