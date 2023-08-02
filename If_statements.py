ball_color = "green"
box_a = 0
box_b = 0
box_c = 0
box_d = 0
if ball_color == "blue":
    box_a = box_a + 1
elif ball_color == "red":
    box_b = box_b + 1
elif ball_color == "green":
    box_c = box_c + 1
else:
    box_d = box_d + 1

print(box_a)
print(box_b)
print(box_c)
print(box_d)
print(ball_color)