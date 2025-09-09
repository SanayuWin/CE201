# รับค่าชั่วโมง, นาที, และวินาที
hours = int(input("ป้อนจำนวนชั่วโมง: "))
minutes = int(input("ป้อนจำนวนนาที: "))
seconds = int(input("ป้อนจำนวนวินาที: "))

# แปลงแต่ละหน่วยเป็นวินาทีแล้วรวมกัน
total_seconds = (hours * 3600) + (minutes * 60) + seconds

# แสดงผล
print(f"เวลารวมทั้งหมดคือ {total_seconds} วินาที")