import numpy as np
data = np.array([[1, 2, 3], [4, 5, 6]])

# .shape: ดูมิติของ Array (แถว, คอลัมน์)
print(f"Shape: {data.shape}") # ผลลัพธ์: (2, 3) -> 2 แถว 3 คอลัมน์

# .dtype: ดูชนิดข้อมูล
print(f"Data type: {data.dtype}") # ผลลัพธ์: int32 (หรือ int64 ขึ้นอยู่กับระบบ)

# .sum(): หาผลรวมของข้อมูลทั้งหมด
print(f"Sum: {data.sum()}") # ผลลัพธ์: 21

# .mean(): หาค่าเฉลี่ย
print(f"Mean: {data.mean()}") # ผลลัพธ์: 3.5

# .max(): หาค่าสูงสุด
print(f"Max: {data.max()}") # ผลลัพธ์: 6

# .min(): หาค่าต่ำสุด
print(f"Min: {data.min()}") # ผลลัพธ์: 1

