score = int(input("กรุณาป้อนคะแนนของคุณ: "))

if score >= 50:
    print("ยินดีด้วย! คุณสอบผ่าน")
    print("อย่าลืมไปฉลองนะ!")

print("--- จบการทำงาน ---")


a = 0
print(a)

a = 0
a = a + 1
print(a)

a = 0
if a == 0:
    a = a + 1

print(a)

a = 0
if a == 1:
    a = a + 1

print(a)

a = 0
if a == 0:
    a = a + 1
a = a + 1
print(a)


a = 0           # Executed
if a == 0:      # Executed
    a = a + 1   # Executed
if a == 0:      # Executed
    a = a + 2   # Skipped
a = a + 1       # Executed
print(a)        # Executed

