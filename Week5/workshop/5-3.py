# workshop_3.py
colors = ["red", "blue", "green", "red", "yellow"]
print(f"List สีเริ่มต้น: {colors}")

# เปลี่ยน 'green' เป็น 'emerald'
try:
    green_index = colors.index("green")
    colors[green_index] = "emerald"
    print(f"List หลังเปลี่ยน 'green' เป็น 'emerald': {colors}")
except ValueError:
    print("ไม่พบ 'green' ใน List")

# นับจำนวน 'red'
red_count = colors.count("red")
print(f"จำนวน 'red' ใน List: {red_count}")