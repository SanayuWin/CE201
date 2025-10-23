"""
เฉลย Workshop 11-2: Exception Handling - ตรวจสอบการหารเลข
"""

try:
    # รับตัวเลข 2 ตัวจากผู้ใช้
    num1 = float(input("กรุณากรอกตัวเลขที่ 1: "))
    num2 = float(input("กรุณากรอกตัวเลขที่ 2: "))
    
    # คำนวณผลหาร
    result = num1 / num2
    print(f"ผลลัพธ์: {num1} ÷ {num2} = {result}")
    
except ValueError:
    # จัดการกรณีที่ผู้ใช้กรอกไม่ใช่ตัวเลข
    print("ข้อผิดพลาด! กรุณากรอกเป็นตัวเลขเท่านั้น")
    
except ZeroDivisionError:
    # จัดการกรณีหารด้วย 0
    print("ข้อผิดพลาด! ไม่สามารถหารด้วย 0 ได้")
