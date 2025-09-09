# while <เงื่อนไข>:
#     <คำสั่งที่ต้องการทำซ้ำ>
#     ...
#     <คำสั่งที่ต้องการทำซ้ำ>

# 1. Initialization: กำหนดตัวนับเริ่มต้น
# i = 1

# # 2. Condition: ตรวจสอบว่า i ยังน้อยกว่าหรือเท่ากับ 5 หรือไม่
# while i <= 5:
#     # 3. Loop Body: ชุดคำสั่งที่ต้องทำซ้ำ
#     print(f"รอบที่ {i}")
    
#     # 4. Update: เพิ่มค่า i ขึ้น 1 ในทุกๆ รอบ
#     i = i + 1 # หรือเขียนย่อว่า i += 1

# print("--- จบลูปแล้ว ---")

# 1. Initialization
# countdown = 10

# # 2. Condition
# while countdown > 0:
#     # 3. Loop Body
#     print(countdown)
    
#     # 4. Update (แบบลดค่า)
#     countdown -= 1 # countdown = countdown - 1

# print("Blast Off!")


# 1. Initialization
# command = ""

# # 2. Condition: ตราบใดที่คำสั่งที่รับเข้ามายังไม่ใช่ "exit"
# while command != "exit":
#     # 3. Loop Body
#     print("คุณสามารถพิมพ์ 'exit' เพื่อจบโปรแกรม")
    
#     # 4. Update: รับค่าใหม่จากผู้ใช้ในทุกรอบ
#     command = input("ป้อนคำสั่งของคุณ: ")
#     print(f"คุณป้อนว่า: {command}")

# print("--- ขอบคุณที่ใช้บริการ ---")


# a = 0
# while a < 1:
#     a = a + 1  
# print(a)

# a = 0
# while a < 2:
#     a = a + 1
# print(a)

# a = 0
# while a > 2:
#     a = a + 1
# print(a)

# a = 4
# while a > 0:
#     a = a - 1
# print(a)

# a = 0
# while a < 3:
#     if a < 2:
#         a = a + 1
# print(a)

# a = 8
# b = 12
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
# print(a)

