import numpy as np

player_stats = np.array([
    [25, 10, 5],
    [32, 8, 7],
    [18, 12, 9],
    [29, 9, 6],
    [22, 11, 11]
])

# 1. เลือกข้อมูลเฉพาะคอลัมน์แต้ม (คอลัมน์ที่ 0)
# синтаксис [:, 0] หมายถึง "เอาทุกแถว, แต่เอาเฉพาะคอลัมน์ที่ 0"
points_column = player_stats[:, 0]
print(f"ข้อมูลแต้มของผู้เล่นทั้งหมด: {points_column}")

# 2. ใช้ np.argmax() เพื่อหา index ของค่าที่สูงสุดใน points_column
mvp_index = np.argmax(points_column)

print(f"\nผู้เล่นที่ทำแต้มสูงสุดคือ: ผู้เล่นหมายเลข {mvp_index}")

