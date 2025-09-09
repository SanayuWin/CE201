# รับค่าความกว้างและความสูง (แปลงเป็น float)
width = float(input("ป้อนความกว้าง: "))
height = float(input("ป้อนความสูง: "))

# คำนวณพื้นที่
area = width * height

# คำนวณเส้นรอบรูป
perimeter = 2 * (width + height)

# แสดงผล
print(f"พื้นที่ของสี่เหลี่ยมคือ: {area}")
print(f"ความยาวเส้นรอบรูปคือ: {perimeter}")