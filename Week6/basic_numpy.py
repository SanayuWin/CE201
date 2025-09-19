import numpy as np
















# สร้าง 1D Array
list_a = [1, 2, 3, 4, 5]
arr_a = np.array(list_a)
print(f"1D Array: {arr_a}")
print(f"ชนิดข้อมูล: {arr_a.dtype}") # แสดงชนิดข้อมูลใน Array

# สร้าง 2D Array
list_b = [[1, 2, 3], [4, 5, 6]]
arr_b = np.array(list_b)
print(f"2D Array:\n{arr_b}")


# สร้าง Array ที่มีแต่เลข 0 ขนาด 1x5
zeros_arr = np.zeros(5)
print(f"Zeros Array: {zeros_arr}")

# สร้าง Array ที่มีแต่เลข 1 ขนาด 3x3
ones_arr = np.ones((3, 3))
print(f"Ones Array:\n{ones_arr}")

# สร้าง Array ที่มีตัวเลขเรียงกัน คล้าย range()
# สร้างตั้งแต่ 0 ถึงก่อน 10
range_arr = np.arange(10)
print(f"Arange Array: {range_arr}")