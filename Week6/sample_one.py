
scores_list = [75, 80, 92, 68]
new_scores = []
for score in scores_list:
    new_scores.append(score + 5)
print(f"List แบบใหม่: {new_scores}")

import numpy as np
scores_arr = np.array([75, 80, 92, 68])
new_scores_arr = scores_arr + 5 
# บวก 5 เข้าไปตรงๆ ได้เลย!
print(f"NumPy แบบใหม่: {new_scores_arr}")

