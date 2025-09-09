# for <ตัวแปรชั่วคราว> in <กลุ่มข้อมูล (Iterable)>:
# <กลุ่มข้อมูล (Iterable)>: สิ่งที่เก็บข้อมูลเป็นชุด เช่น List, String
# <ตัวแปรชั่วคราว>: ตัวแปรที่จะถูกสร้างขึ้นมาชั่วคราวเพื่อรับค่าสมาชิกแต่ละตัวจากกลุ่มข้อมูลในแต่ละรอบ

# i = [1, 2, 3, 4, 5]  # สร้าง List ที่มีสมาชิกเป็นตัวเลข 1 ถึง 5
# for i in i:  # ใช้ for-loop เพื่อวนรอบผ่านสมาชิกของ List i
#     print(i)  # แสดงค่าของตัวแปรชั่วคราว i ในแต่ละรอบของลูป
# # ผลลัพธ์จะเป็นการแสดงตัวเลข 1 ถึง 5 ทีละบรรทัด
# # ในที่นี้ i จะเป็นตัวแปรชั่วคราวที่รับค่าจากสมาชิกของ List [1, 2, 3, 4, 5]
# # ในรอบแรก i จะเป็น 1, รอบที่สอง i จะเป็น 2, และต่อไปเรื่อยๆ จนถึง 5


# fruits = ["Apple", "Banana", "Cherry", "Mango"]

# # "สำหรับผลไม้แต่ละชนิดในลิสต์ fruits"
# for fruit in fruits:
#     print(f"วันนี้ฉันอยากกิน {fruit}")

# course_name = "Python"

# # "สำหรับตัวอักษรแต่ละตัวในคำว่า Python"
# for character in course_name:
#     print(character)



# ใช้งาน range(stop)
# print("--- range(5) ---")
# for i in range(5): # จะได้เลข 0, 1, 2, 3, 4
#     print(i)

# # ใช้งาน range(start, stop)
# print("\n--- range(1, 6) ---")
# for i in range(1, 6): # จะได้เลข 1, 2, 3, 4, 5
#     print(i)
    
# # ใช้งาน range(start, stop, step)
# print("\n--- range(0, 11, 2) ---")
# for i in range(0, 11, 2): # จะได้เลข 0, 2, 4, 6, 8, 10
#     print(i)



a = 0
for i in range(1):
    a = a + 1
print(a)

a = 0
for i in range(0):
    a = a + 1
print(a)


a = 0
for i in range(3):
    if a < 2:
        a = a + 1
print(a)

