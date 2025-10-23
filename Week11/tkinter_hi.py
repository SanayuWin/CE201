import tkinter as tk

# --- 1. สร้างฟังก์ชันที่จะให้ปุ่มเรียกใช้ ---
def say_hello():
    # 1.1 ดึงข้อความจากช่อง Entry
    user_name = entry_name.get()
    
    # 1.2 สร้างข้อความทักทาย
    greeting_message = f"สวัสดี, {user_name}!"
    
    # 1.3 เปลี่ยนข้อความบน Label ผลลัพธ์
    label_result.config(text=greeting_message)

# --- 2. สร้างหน้าต่างหลัก ---
root = tk.Tk()
root.title("Greeter App")
root.geometry("300x200")

# --- 3. สร้าง Widgets ---
# ป้ายข้อความ (Label)
label_prompt = tk.Label(root, text="กรุณาใส่ชื่อของคุณ:")
label_prompt.pack(pady=5) # pack() คือการแปะลงไปในหน้าต่าง

# ช่องกรอกข้อความ (Entry)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

# ปุ่มกด (Button)
# command=say_hello (ไม่ต้องมีวงเล็บ!)
button_greet = tk.Button(root, text="กดเลย!", command=say_hello)
button_greet.pack(pady=10)

# ป้ายข้อความสำหรับแสดงผลลัพธ์ (เริ่มจากว่างๆ)
label_result = tk.Label(root, text="")
label_result.pack(pady=5)

# --- 4. สั่งเริ่มโปรแกรม ---
root.mainloop()