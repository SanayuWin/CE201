student_scores = [
    [80, 85, 88, 90],  # แถว 0: คะแนนของนักเรียนคนที่ 1
    [92, 89, 94, 88],  # แถว 1: คะแนนของนักเรียนคนที่ 2
    [78, 82, 80, 84]   # แถว 2: คะแนนของนักเรียนคนที่ 3
]

# ลูปนอก วนแต่ละแถว (แต่ละนักเรียน)
for row_index in range(len(student_scores)):
    # ลูปใน วนแต่ละคอลัมน์ (แต่ละคะแนนในแถวนั้น)
    for col_index in range(len(student_scores[row_index])):
        score = student_scores[row_index][col_index]
        print(f"นักเรียนคนที่ {row_index + 1}, วิชาที่ {col_index + 1}: คะแนน {score}")

# วิธีที่ง่ายกว่าในการแสดงผล
print("\n--- แสดงผลแบบตาราง ---")
for row in student_scores: # วนลูปนอกได้ list ของแต่ละแถวมา
    for score in row: # วนลูปในได้คะแนนแต่ละตัว
        print(score, end="\t") # \t คือการเว้นวรรคแบบ tab
    print() # ขึ้นบรรทัดใหม่เมื่อจบแถว

    