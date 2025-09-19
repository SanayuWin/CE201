import numpy as np

f_temps = np.array([
    [86, 90, 91.4],
    [77, 80.6, 82.4],
    [89.6, 93.2, 95]
])

# ใช้ Vectorization กับสูตรโดยตรง
# NumPy จะทำการลบ, คูณ, หาร กับทุกสมาชิกใน Array โดยอัตโนมัติ
c_temps = (f_temps - 32) * 5 / 9

print("--- อุณหภูมิ (ฟาเรนไฮต์) ---")
print(f_temps)
print("\n--- อุณหภูมิ (เซลเซียส) ---")
print(np.round(c_temps, 2)) # np.round() เพื่อปัดทศนิยมให้สวยงาม

