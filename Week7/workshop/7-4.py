"""
โจทย์ที่ 4: ฟังก์ชันคำนวณเกรด
สร้างฟังก์ชันชื่อ calculate_grade ที่:
1. รับพารามิเตอร์ score (คะแนน)
2. คืนค่าเกรดตามเกณฑ์:
   - 80-100: "A"
   - 70-79: "B"
   - 60-69: "C"
   - 50-59: "D"
   - 0-49: "F"
3. ทดสอบด้วยคะแนน: 95, 82, 76, 65, 58, 45, 120, -5 (ใช้ for loop ในการทดสอบ)
4. แสดงผลในรูปแบบ "คะแนน [score] ได้เกรด [grade]"
5. จัดการกรณีคะแนนผิดปกติ (น้อยกว่า 0 หรือมากกว่า 100) ให้ส่งค่า "Invalid"
"""

def calculate_grade(score):
    """ฟังก์ชันคำนวณเกรดจากคะแนน"""
    # ตรวจสอบคะแนนผิดปกติ
    if score < 0 or score > 100:
        return "Invalid"
    
    # คำนวณเกรด
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

# ทดสอบฟังก์ชัน
test_scores = [95, 82, 76, 65, 58, 45, 120, -5]

print("ผลการทดสอบ:")
for score in test_scores:
    grade = calculate_grade(score)
    if grade == "Invalid":
        print(f"คะแนน {score} ไม่ถูกต้อง (ต้องอยู่ระหว่าง 0-100)")
    else:
        print(f"คะแนน {score} ได้เกรด {grade}")
