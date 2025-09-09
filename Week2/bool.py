# การสร้างตัวแปรชนิด bool
is_student = True
has_passed = False
is_major_student = True

# ตรวจสอบชนิดของข้อมูล
print(type(is_student)) # ผลลัพธ์: <class 'bool'>

# Boolean มักจะมาจากผลของการเปรียบเทียบ
score = 75
passed_condition = (score >= 50) # 75 >= 50 เป็นจริง
print(passed_condition) # ผลลัพธ์: True
print(type(passed_condition)) # ผลลัพธ์: <class 'bool'>

age = 18
is_adult = (age >= 20) # 18 >= 20 เป็นเท็จ
print(is_adult) # ผลลัพธ์: False

