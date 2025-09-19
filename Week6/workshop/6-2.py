import numpy as np

matrix_list = [
    [10, 20, 30],
    [20, 40, 50],
    [30, 50, 30]
]

# 1. แปลง List ให้เป็น NumPy Array
matrix_np = np.array(matrix_list)

# 2. ใช้เมธอด .sum() ของ NumPy เพื่อหาผลรวมทั้งหมด
# สังเกตว่าโค้ดสั้นและกระชับกว่ามาก
total_sum_np = matrix_np.sum()

print(f"ผลรวมของตัวเลขทั้งหมด (วิธีใช้ NumPy): {total_sum_np}")