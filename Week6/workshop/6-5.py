import numpy as np

sales = np.array([
    [7500, 8200, 7800, 9000, 8500],
    [6500, 7900, 8100, 7700, 8300],
    [9100, 8900, 9200, 9500, 8800]
])
target = 8000

# 1. ใช้การเปรียบเทียบเพื่อสร้าง Boolean Array
# ผลลัพธ์จะเป็นตารางของ True/False
sales_over_target = sales > target
print("--- ตารางการขายที่ทะลุเป้า (True/False) ---")
print(sales_over_target)

# 2. หาผลรวมของ Boolean Array ตามแต่ละแถว (axis=1)
# NumPy จะนับ True เป็น 1 และ False เป็น 0
days_over_target = sales_over_target.sum(axis=1)

# อธิบาย enumerate 
# enumerate จะช่วยให้เราสามารถเข้าถึงทั้งดัชนีและค่าของอาร์เรย์ได้ในลูปเดียว

print("\n--- จำนวนวันที่แต่ละสาขามียอดขายทะลุเป้า ---")
for i, days in enumerate(days_over_target):
    print(f"สาขาที่ {i+1}: {days} วัน")