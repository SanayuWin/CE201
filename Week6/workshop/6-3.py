import numpy as np

scores = np.array([
    [80, 85, 88],
    [92, 89, 94],
    [78, 82, 80],
    [88, 90, 85]
])

weights = np.array([0.3, 0.3, 0.4])

# 1. ใช้ Broadcasting คูณคะแนนกับน้ำหนักโดยตรง
# NumPy จะกระจาย weights ไปคูณกับทุกแถวของ scores
weighted_scores = scores * weights

print("--- คะแนนหลังคูณกับน้ำหนัก ---")
print(weighted_scores)

# 2. หาผลรวมของคะแนนถ่วงน้ำหนักในแต่ละแถว (ของนักเรียนแต่ละคน)
# axis=1 หมายถึง "หาผลรวมตามแนวนอน" (รวมคอลัมน์ทั้งหมดในแถวเดียว)
final_scores = weighted_scores.sum(axis=1)

print("\n--- คะแนนรวมถ่วงน้ำหนักของนักเรียนแต่ละคน ---")
for i, score in enumerate(final_scores):
    print(f"นักเรียนคนที่ {i+1}: {score:.2f} คะแนน")