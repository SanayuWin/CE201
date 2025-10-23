# print("=" * 60)
# print("ตัวอย่างที่ 1: การเขียนไฟล์ (Write Mode)")
# print("=" * 60)
# with open('example.txt', 'w', encoding='utf-8') as file:
#     file.write("สวัสดีครับ\n")
#     file.write("นี่คือตัวอย่างการเขียนไฟล์\n")
#     file.write("บรรทัดที่ 3\n")
    
# print("เขียนไฟล์ example.txt เรียบร้อย")
# print()

# อ่านไฟล์

# print("=" * 60)
# print("ตัวอย่างที่ 2: การอ่านไฟล์ (Read Mode)")
# print("=" * 60)

# วิธีที่ 1: อ่านทั้งหมดด้วย read()
# print("\n[วิธีที่ 1] อ่านทั้งหมดด้วย read():")
# with open('example.txt', 'r', encoding='utf-8') as file:
#     content = file.read()
#     print(content)

# วิธีที่ 2: อ่านทีละบรรทัดด้วย readline()
# print("\n[วิธีที่ 2] อ่านทีละบรรทัดด้วย readline():")
# with open('example.txt', 'r', encoding='utf-8') as file:
#     line1 = file.readline()
#     line2 = file.readline()
#     print(f"บรรทัด 1: {line1.strip()}")
#     print(f"บรรทัด 2: {line2.strip()}")

# วิธีที่ 3: อ่านทั้งหมดเป็น list ด้วย readlines()
# print("\n[วิธีที่ 3] อ่านทั้งหมดเป็น list ด้วย readlines():")
# with open('example.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#     for i, line in enumerate(lines, 1):
#         print(f"บรรทัด {i}: {line.strip()}")

# วิธีที่ 4: อ่านด้วย for loop (แนะนำสำหรับไฟล์ใหญ่)
# print("\n[วิธีที่ 4] อ่านด้วย for loop (ประหยัดหน่วยความจำ):")
# with open('example.txt', 'r', encoding='utf-8') as file:
#     for i, line in enumerate(file, 1):
#         print(f"บรรทัด {i}: {line.strip()}")


# เพิ่มข้อมูลต่อท้ายไฟล์
with open('example.txt', 'a', encoding='utf-8') as file:
    file.write("บรรทัดที่ 4 (เพิ่มด้วย append)\n")
    file.write("บรรทัดที่ 5 (เพิ่มด้วย append)\n")

print("เพิ่มข้อมูลต่อท้ายไฟล์ example.txt เรียบร้อย")

# อ่านไฟล์หลังจาก append
print("\nอ่านไฟล์หลังจาก append:")
with open('example.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)


