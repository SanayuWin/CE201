# มีชมรม 2 ชมรม คือชมรมดนตรี (Music Club) และชมรมกีฬา (Sport Club) ซึ่งมีรายชื่อสมาชิกดังนี้ 
# จงเขียนโปรแกรมเพื่อตอบคำถามต่อไปนี้:
# ใครบ้างที่อยู่ ทั้งสองชมรม?
# ใครบ้างที่อยู่ ชมรมดนตรีเท่านั้น?

# โค้ดเริ่มต้น
music_club = {"Alice", "Bob", "Charlie", "David"}
sport_club = {"Charlie", "David", "Eve", "Frank"}

# 1. หาสมาชิกที่อยู่ทั้งสองชมรม (Intersection)
both_clubs = music_club.intersection(sport_club)
# หรือใช้ตัวย่อ: both_clubs = music_club & sport_club
print(f"สมาชิกที่อยู่ทั้งสองชมรม: {both_clubs}")

# 2. หาสมาชิกที่อยู่ชมรมดนตรีเท่านั้น (Difference)
only_music = music_club.difference(sport_club)
# หรือใช้ตัวย่อ: only_music = music_club - sport_club
print(f"สมาชิกที่อยู่ชมรมดนตรีเท่านั้น: {only_music}")

