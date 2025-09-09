# รับค่าตัวเลขที่ 1 (เป็น str)
num1_str = input("ป้อนตัวเลขที่ 1: ")
# รับค่าตัวเลขที่ 2 (เป็น str)
num2_str = input("ป้อนตัวเลขที่ 2: ")

# แปลง str เป็น int เพื่อคำนวณ
num1_int = int(num1_str)
num2_int = int(num2_str)

# คำนวณผลบวก
sum_result = num1_int + num2_int

# แสดงผล
print(f"ผลบวกคือ: {sum_result}")