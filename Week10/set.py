# วิธีที่ 1: ใช้ {} แต่ต้องมีข้อมูลข้างใน
tags = {"python", "programming", "developer", "code"}
# print(tags) # ลำดับอาจเปลี่ยนไปทุกครั้งที่รัน

# วิธีที่ 2: สร้างจาก List (เพื่อลบตัวซ้ำ)
numbers = [1, 2, 5, 2, 3, 4, 1, 5, 5]
unique_numbers = set(numbers)
# print(f"ตัวเลขที่ไม่ซ้ำ: {unique_numbers}") # ผลลัพธ์: {1, 2, 3, 4, 5}

# การสร้าง Set ว่าง (สำคัญมาก!)
empty_dict = {}       # แบบนี้ได้ Dictionary
empty_set = set()     # ต้องใช้ set() เท่านั้น!
# print(f"empty_dict: {type(empty_dict)}") # ผลลัพธ์: <class 'dict'>
# print(f"empty_set: {type(empty_set)}")   # ผลลัพธ์: <class 'set'>


# tags = {"python", "programming", "developer", "code"}

# เพิ่มสมาชิก 1 ตัว
tags.add("software")
tags.add("python") # "python" มีอยู่แล้ว จะไม่เพิ่มซ้ำ

# เพิ่มสมาชิกหลายตัวจาก List หรือ Set อื่น
tags.update(["engineer", "coding"])

# print(tags)

# การลบสมาชิก
# 1. ใช้คำสั่ง remove() (ถ้าสมาชิกไม่มีอยู่ จะเกิด Error)
# tags.remove("software") 

tags = {"python", "programming", "developer", "code"}
# 2. ใช้คำสั่ง discard() (ถ้าสมาชิกไม่มีอยู่ จะไม่เกิด Error)
tags.discard("software")

# print(tags)

tags = {"python", "programming", "developer", "code"}
# การวนลูปใน Set
# for tag in tags:
#     print(f"Tag: {tag}")


# dev_team_A = {"Alice", "Bob", "Charlie"}
# dev_team_B = {"Charlie", "David", "Eve"}

# 1. Union (รวมกันทั้งหมด เอาตัวซ้ำมาแค่ตัวเดียว)
# all_devs = dev_team_A.union(dev_team_B)
# # หรือใช้ตัวย่อ |
# # all_devs = dev_team_A | dev_team_B
# print(f"พนักงานทั้งหมด: {all_devs}")


# dev_team_A = {"Alice", "Bob", "Charlie"}
# dev_team_B = {"Charlie", "David", "Eve"}

# 2. Intersection (เอาเฉพาะตัวที่อยู่ทั้ง 2 เซต)
# common_devs = dev_team_A.intersection(dev_team_B)
# # หรือใช้ตัวย่อ &
# # common_devs = dev_team_A & dev_team_B
# print(f"พนักงานที่อยู่ทั้งสองทีม: {common_devs}")

dev_team_A = {"Alice", "Bob", "Charlie"}
dev_team_B = {"Charlie", "David", "Eve"}

# 3. Difference (เอาสมาชิกที่อยู่ในเซตแรก แต่ไม่อยู่ในเซตที่สอง)
a_only = dev_team_A.difference(dev_team_B)
# หรือใช้ตัวย่อ -
# a_only = dev_team_A - dev_team_B
print(f"พนักงานที่อยู่ทีม A เท่านั้น: {a_only}")

b_only = dev_team_B.difference(dev_team_A)
print(f"พนักงานที่อยู่ทีม B เท่านั้น: {b_only}")

