import numpy as np

# ตารางคะแนน (3 แถว, 4 คอลัมน์)
scores = np.array([
    [70, 75, 80, 82],  # นักเรียนคนที่ 1
    [85, 88, 84, 90],  # นักเรียนคนที่ 2
    [68, 72, 77, 80]   # นักเรียนคนที่ 3
])

# คะแนนช่วยสำหรับแต่ละวิชา (1 แถว, 4 คอลัมน์)
bonus_points = np.array([5, 3, 2, 1])

# --- การคำนวณด้วย Broadcasting ---
# NumPy จะ 'กระจาย' bonus_points ไปบวกกับทุกแถวของ scores
final_scores = scores + bonus_points

print("--- คะแนนเดิม ---")
print(scores)
print("\n--- คะแนนช่วย ---")
print(bonus_points)
print("\n--- คะแนนสุดท้าย ---")
print(final_scores)


# [5, 3, 2, 1]  --จะถูกยืดเป็น-->  [[5, 3, 2, 1],
#                                  [5, 3, 2, 1],
#                                  [5, 3, 2, 1]]

