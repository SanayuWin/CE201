# ===============================================
# Week 8: Function ในภาษา Python
# หัวข้อ: ฟังก์ชันแบบต่างๆ (4 ประเภท)
# ===============================================

"""
ฟังก์ชันแบ่งออกเป็น 4 ประเภทตามการรับและส่งค่า:

1. ฟังก์ชันแบบที่ 1: ไม่มี Input และไม่มี Output
2. ฟังก์ชันแบบที่ 2: มี Input แต่ไม่มี Output  
3. ฟังก์ชันแบบที่ 3: ไม่มี Input แต่มี Output
4. ฟังก์ชันแบบที่ 4: มี Input และมี Output
"""

print("=" * 60)
print("ฟังก์ชันแบบต่างๆ ในภาษา Python")
print("=" * 60)

# ===============================================
# ฟังก์ชันแบบที่ 1: ไม่มี Input และไม่มี Output
# ===============================================

print("\n1. ฟังก์ชันแบบที่ 1: ไม่มี Input และไม่มี Output")
print("-" * 50)

# 1. การสร้างฟังก์ชัน (Define)
def show_welcome_message():
    """ฟังก์ชันนี้ใช้สำหรับแสดงข้อความต้อนรับ"""
    print("=============================")
    print("ยินดีต้อนรับสู่โปรแกรมของเรา")
    print("=============================")

# 2. การเรียกใช้งาน (Call)
print("เริ่มต้นโปรแกรม...")
show_welcome_message() # เรียกให้ฟังก์ชันทำงาน
print("จบโปรแกรม...")

# 1. การสร้างฟังก์ชัน (Define)
def show_welcome_message():
    """ฟังก์ชันแสดงข้อความต้อนรับ"""
    print("ยินดีต้อนรับสู่โปรแกรม Python!")
    print("หวังว่าคุณจะสนุกกับการเรียนรู้")

def draw_line():
    """ฟังก์ชันวาดเส้น"""
    print("*" * 30)

def show_current_time():
    """ฟังก์ชันแสดงเวลาปัจจุบัน"""
    import datetime
    now = datetime.datetime.now()
    print(f"เวลาปัจจุบัน: {now.strftime('%Y-%m-%d %H:%M:%S')}")

def clear_screen_simulation():
    """ฟังก์ชันจำลองการเคลียร์หน้าจอ"""
    print("\n" * 3)
    print("=== หน้าจอใหม่ ===")

# 2. การเรียกใช้งาน (Call)
print("เริ่มต้นโปรแกรม...")
show_welcome_message()
draw_line()
show_current_time()
clear_screen_simulation()
print("จบโปรแกรม...")

# ===============================================
# ฟังก์ชันแบบที่ 2: มี Input แต่ไม่มี Output
# ===============================================

print("\n2. ฟังก์ชันแบบที่ 2: มี Input แต่ไม่มี Output")
print("-" * 50)

def greet_user(name):
    """ฟังก์ชันทักทายผู้ใช้ด้วยชื่อ"""
    print(f"สวัสดีครับ/ค่ะ คุณ{name}!")

def print_multiplication_table(number):
    """ฟังก์ชันแสดงตารางสูตรคูณ"""
    print(f"ตารางสูตรคูณ {number}:")
    for i in range(1, 13):
        result = number * i
        print(f"{number} x {i} = {result}")

def display_student_grade(name, score):
    """ฟังก์ชันแสดงเกรดของนักเรียน"""
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    
    print(f"นักเรียน: {name}")
    print(f"คะแนน: {score}")
    print(f"เกรด: {grade}")

def draw_rectangle(width, height, char="*"):
    """ฟังก์ชันวาดสี่เหลี่ยมผืนผ้า"""
    print(f"สี่เหลี่ยมผืนผ้า {width}x{height}:")
    for i in range(height):
        print(char * width)

# การใช้งานฟังก์ชันแบบที่ 2
print("ตัวอย่างการใช้งาน:")
greet_user("สมชาย")
print()

print_multiplication_table(7)
print()

display_student_grade("นางสาวสมหญิง", 85)
print()

draw_rectangle(8, 4, "#")

# ===============================================
# ฟังก์ชันแบบที่ 3: ไม่มี Input แต่มี Output
# ===============================================

print("\n\n3. ฟังก์ชันแบบที่ 3: ไม่มี Input แต่มี Output")
print("-" * 50)

def get_current_year():
    """ฟังก์ชันรับปีปัจจุบัน"""
    import datetime
    return datetime.datetime.now().year

def generate_random_number():
    """ฟังก์ชันสร้างเลขสุ่ม"""
    import random
    return random.randint(1, 100)

def get_pi_value():
    """ฟังก์ชันคืนค่า π"""
    import math
    return math.pi

def input_user_name():
    """ฟังก์ชันรับชื่อผู้ใช้จากคีย์บอร์ด"""
    name = input("กรุณาใส่ชื่อของคุณ: ")
    return name

def calculate_fibonacci_10():
    """ฟังก์ชันคำนวณเลขฟีโบนัชชี 10 ตัวแรก"""
    fib_sequence = [0, 1]
    for i in range(2, 10):
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_fib)
    return fib_sequence

# การใช้งานฟังก์ชันแบบที่ 3
print("ตัวอย่างการใช้งาน:")

current_year = get_current_year()
print(f"ปีปัจจุบัน: {current_year}")

random_num = generate_random_number()
print(f"เลขสุ่ม: {random_num}")

pi_value = get_pi_value()
print(f"ค่า π = {pi_value}")

# ตัวอย่างการรับชื่อ (ใช้ชื่อตัวอย่างแทน)
# user_name = input_user_name()
# ใช้ค่าตัวอย่างแทน
print("ตัวอย่างการรับชื่อ: (จำลอง)")
example_name = "ผู้ใช้ตัวอย่าง"
print(f"ชื่อที่รับมา: {example_name}")

fibonacci_numbers = calculate_fibonacci_10()
print(f"เลขฟีโบนัชชี 10 ตัวแรก: {fibonacci_numbers}")

# ===============================================
# ฟังก์ชันแบบที่ 4: มี Input และมี Output
# ===============================================

print("\n\n4. ฟังก์ชันแบบที่ 4: มี Input และมี Output")
print("-" * 50)

def add_two_numbers(a, b):
    """ฟังก์ชันบวกเลข 2 จำนวน"""
    result = a + b
    return result

def calculate_rectangle_area(width, height):
    """ฟังก์ชันคำนวณพื้นที่สี่เหลี่ยมผืนผ้า"""
    area = width * height
    return area

def convert_celsius_to_fahrenheit(celsius):
    """ฟังก์ชันแปลงอุณหภูมิจากเซลเซียสเป็นฟาเรนไฮต์"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def find_max_number(numbers):
    """ฟังก์ชันหาเลขที่มากที่สุดในลิสต์"""
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def calculate_discount_price(original_price, discount_percent):
    """ฟังก์ชันคำนวณราคาหลังหักส่วนลด"""
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    return final_price, discount_amount

def check_prime_number(number):
    """ฟังก์ชันตรวจสอบว่าเลขเป็นจำนวนเฉพาะหรือไม่"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def calculate_bmi(weight, height):
    """ฟังก์ชันคำนวณค่า BMI และแปลผล"""
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "น้ำหนักต่ำกว่าเกณฑ์"
    elif bmi < 25:
        category = "น้ำหนักปกติ"
    elif bmi < 30:
        category = "น้ำหนักเกิน"
    else:
        category = "อ้วน"
    
    return bmi, category

# การใช้งานฟังก์ชันแบบที่ 4
print("ตัวอย่างการใช้งาน:")

# ฟังก์ชันบวกเลข
sum_result = add_two_numbers(15, 25)
print(f"15 + 25 = {sum_result}")

# ฟังก์ชันคำนวณพื้นที่
area = calculate_rectangle_area(8, 12)
print(f"พื้นที่สี่เหลี่ยมผืนผ้า 8x12 = {area} ตารางหน่วย")

# ฟังก์ชันแปลงอุณหภูมิ
temp_f = convert_celsius_to_fahrenheit(30)
print(f"30°C = {temp_f}°F")

# ฟังก์ชันหาเลขที่มากที่สุด
numbers_list = [45, 23, 78, 12, 67, 34, 89, 56]
max_number = find_max_number(numbers_list)
print(f"เลขที่มากที่สุดใน {numbers_list} คือ {max_number}")

# ฟังก์ชันคำนวณส่วนลด
original = 1000
discount = 20
final_price, discount_amount = calculate_discount_price(original, discount)
print(f"ราคาเดิม: {original} บาท")
print(f"ส่วนลด {discount}%: {discount_amount} บาท")
print(f"ราคาสุดท้าย: {final_price} บาท")

# ฟังก์ชันตรวจสอบจำนวนเฉพาะ
test_number = 17
is_prime = check_prime_number(test_number)
print(f"{test_number} {'เป็น' if is_prime else 'ไม่เป็น'}จำนวนเฉพาะ")

# ฟังก์ชันคำนวณ BMI
weight = 70
height = 1.75
bmi_value, bmi_category = calculate_bmi(weight, height)
print(f"น้ำหนัก: {weight} กก., ส่วนสูง: {height} ม.")
print(f"BMI: {bmi_value:.2f} ({bmi_category})")

# ===============================================
# สรุปความแตกต่างของฟังก์ชันแต่ละแบบ
# ===============================================

print("\n\n" + "=" * 60)
print("สรุปความแตกต่างของฟังก์ชันแต่ละแบบ")
print("=" * 60)

print("""
แบบที่ 1: ไม่มี Input และไม่มี Output
- ไม่รับพารามิเตอร์
- ไม่มี return statement
- ใช้สำหรับการแสดงผล หรือทำงานเบื้องต้น
- ตัวอย่าง: show_welcome_message(), draw_line()

แบบที่ 2: มี Input แต่ไม่มี Output
- รับพารามิเตอร์ 1 ตัวขึ้นไป
- ไม่มี return statement
- ใช้สำหรับการประมวลผลและแสดงผล
- ตัวอย่าง: greet_user(name), print_multiplication_table(number)

แบบที่ 3: ไม่มี Input แต่มี Output
- ไม่รับพารามิเตอร์
- มี return statement
- ใช้สำหรับการสร้างค่า หรือรับข้อมูล
- ตัวอย่าง: get_current_year(), generate_random_number()

แบบที่ 4: มี Input และมี Output
- รับพารามิเตอร์ 1 ตัวขึ้นไป
- มี return statement
- เป็นแบบที่ใช้งานมากที่สุด
- ตัวอย่าง: add_two_numbers(a, b), calculate_bmi(weight, height)
""")

print("\n" + "=" * 60)
print("การเลือกใช้ฟังก์ชันแต่ละแบบ")
print("=" * 60)

print("""
เลือกแบบที่ 1 เมื่อ:
- ต้องการทำงานแบบเดิมทุกครั้ง
- ไม่ต้องการข้อมูลจากภายนอก
- ไม่ต้องการส่งค่ากลับ

เลือกแบบที่ 2 เมื่อ:
- ต้องการข้อมูลจากภายนอกเพื่อประมวลผล
- ผลลัพธ์เป็นการแสดงผลหรือการกระทำ
- ไม่ต้องการนำผลไปใช้ต่อ

เลือกแบบที่ 3 เมื่อ:
- ต้องการสร้างค่าแบบคงที่
- ต้องการรับข้อมูลจากผู้ใช้
- ต้องการค่าสำหรับใช้ในการคำนวณต่อ

เลือกแบบที่ 4 เมื่อ:
- ต้องการประมวลผลข้อมูลที่ส่งเข้ามา
- ต้องการส่งผลลัพธ์กลับไปใช้ต่อ
- ต้องการความยืดหยุ่นในการใช้งาน
""")