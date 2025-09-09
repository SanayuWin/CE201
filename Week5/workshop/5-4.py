# workshop_4.py
list_a = [10, 20, 30]
list_b = [40, 50, 60]

# วิธีที่ 1: ใช้ extend() (เปลี่ยน list_a เดิม)
# combined_list = list_a.copy() # ทำสำเนาเพื่อไม่ให้ list_a เดิมเปลี่ยน
# combined_list.extend(list_b)

# วิธีที่ 2: ใช้ + (สร้าง List ใหม่)
combined_list = list_a + list_b
print(f"List ที่รวมกัน (ก่อนเรียง): {combined_list}")

combined_list.sort() # จัดเรียงจากน้อยไปมาก (in-place)
print(f"List ที่รวมกัน (หลังเรียง): {combined_list}")