# # ตัวอย่างที่ 2
# # 1. การสร้างฟังก์ชัน (Define)
# def show_welcome_message():
#     """ฟังก์ชันแสดงข้อความต้อนรับ"""
#     print("ยินดีต้อนรับสู่โปรแกรม Python!")
#     print("หวังว่าคุณจะสนุกกับการเรียนรู้")

# def draw_line():
#     """ฟังก์ชันวาดเส้น"""
#     print("*" * 30)

# def show_current_time():
#     """ฟังก์ชันแสดงเวลาปัจจุบัน"""
#     import datetime
#     now = datetime.datetime.now()
#     print(f"เวลาปัจจุบัน: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# def clear_screen_simulation():
#     """ฟังก์ชันจำลองการเคลียร์หน้าจอ"""
#     print("\n" * 3)
#     print("=== หน้าจอใหม่ ===")

# # 2. การเรียกใช้งาน (Call)
# print("เริ่มต้นโปรแกรม...")
# show_welcome_message()
# draw_line()
# show_current_time()
# clear_screen_simulation()
# print("จบโปรแกรม...")


# Parameter คือ 'name' และ 'course'
# # ตัวอย่างที่ 3
# def show_student_info(name, course):
#     """ฟังก์ชันนี้รับชื่อและวิชาเรียนเพื่อนำมาแสดงผล"""
#     print(f"สวัสดี, {name}")
#     print(f"คุณกำลังเรียนวิชา: {course}")

# # การเรียกใช้งาน
# # 'Elon Musk' และ 'Computer Programming' คือ Arguments
# show_student_info("Elon Musk", "Computer Programming")
# show_student_info("Tim Cook", "Introduction to AI")


# # ตัวอย่างที่ 4
# def print_multiplication_table(number):
#     """ฟังก์ชันแสดงตารางสูตรคูณ"""
#     print(f"ตารางสูตรคูณ {number}:")
#     for i in range(1, 13):
#         result = number * i
#         print(f"{number} x {i} = {result}")

# print_multiplication_table(7)
# print_multiplication_table(12)

# # ตัวอย่างที่ 5
# def display_student_grade(name, score):
#     """ฟังก์ชันแสดงเกรดของนักเรียน"""
#     if score >= 80:
#         grade = "A"
#     elif score >= 70:
#         grade = "B"
#     elif score >= 60:
#         grade = "C"
#     elif score >= 50:
#         grade = "D"
#     else:
#         grade = "F"
    
#     print(f"นักเรียน: {name}")
#     print(f"คะแนน: {score}")
#     print(f"เกรด: {grade}")

# display_student_grade("นางสาวสมหญิง", 85)
# display_student_grade("นายสมชาย", 67)


# # ตัวอย่างที่ 6
# import random

# def get_random_lotto_number():
#     """ฟังก์ชันนี้สุ่มตัวเลข 2 หลักแล้วส่งค่ากลับมา"""
#     number = random.randint(10, 99)
#     return number

# # การเรียกใช้งาน: ต้องสร้างตัวแปรมารับค่าที่ return กลับมา
# lucky_number_1 = get_random_lotto_number()
# lucky_number_2 = get_random_lotto_number()

# print(f"เลขนำโชคงวดนี้คือ: {lucky_number_1}")
# print(f"เลขท้าย 2 ตัวที่น่าสนใจ: {lucky_number_2}")

# # ตัวอย่างที่ 7
# def input_user_name():
#     """ฟังก์ชันรับชื่อผู้ใช้จากคีย์บอร์ด"""
#     name = input("กรุณาใส่ชื่อของคุณ: ")
#     return name

# user_name = input_user_name()
# print(f"ยินดีต้อนรับ, {user_name}!")


# # ตัวอย่างที่ 8
# def calculate_area(width, height):
#     """รับความกว้างและความสูงมาคำนวณพื้นที่ แล้วส่งผลลัพธ์กลับไป"""
#     area = width * height
#     return area

# # การเรียกใช้งาน
# area_of_room1 = calculate_area(10, 5) # ผลลัพธ์ 50 จะถูกเก็บในตัวแปร
# area_of_room2 = calculate_area(7, 3) # ผลลัพธ์ 21 จะถูกเก็บในตัวแปร

# print(f"พื้นที่ห้องที่ 1: {area_of_room1} ตร.ม.")
# print(f"พื้นที่ห้องที่ 2: {area_of_room2} ตร.ม.")
# print(f"พื้นที่รวม: {calculate_area(10, 5) + calculate_area(7, 3)} ตร.ม.")

# ตัวอย่างที่ 9
# def calculate_bmi(weight, height):
#     """ฟังก์ชันคำนวณค่า BMI และแปลผล"""
#     bmi = weight / (height ** 2)
    
#     if bmi < 18.5:
#         category = "น้ำหนักต่ำกว่าเกณฑ์"
#     elif bmi < 25:
#         category = "น้ำหนักปกติ"
#     elif bmi < 30:
#         category = "น้ำหนักเกิน"
#     else:
#         category = "อ้วน"
    
#     return bmi, category

# # ฟังก์ชันคำนวณ BMI
# weight = 70
# height = 1.75
# bmi_value, bmi_category = calculate_bmi(weight, height)
# print(f"น้ำหนัก: {weight} กก., ส่วนสูง: {height} ม.")
# print(f"BMI: {bmi_value:.2f} ({bmi_category})")


# ตัวอย่างที่ 10
def square_number(num):
    """ฟังก์ชันคืนค่ากำลังสองของตัวเลขที่รับมา"""
    return num * num
numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for n in numbers:
    squared = square_number(n)
    squared_numbers.append(squared)

print("ตัวเลขต้นฉบับ:", numbers)   
print("ตัวเลขยกกำลังสอง:", squared_numbers)


