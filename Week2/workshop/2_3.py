# รับปีปัจจุบันและปีเกิด
current_year = int(input("กรุณาใส่ปี พ.ศ. ปัจจุบัน: "))
birth_year = int(input("กรุณาใส่ปี พ.ศ. ที่คุณเกิด: "))

# คำนวณอายุ
age = current_year - birth_year

# แสดงผล
print(f"คุณอายุ {age} ปี")