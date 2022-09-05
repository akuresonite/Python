#  ⬜⬛🟫🟪🟦🟩🟨🟧🟥❎❌❎❎❎❎❎❎❌ ❎❎❌❌
row1 = ["🟩", "🟩", "🟩"]
row2 = ["🟩", "🟩", "🟩"]
row3 = ["🟩", "🟩", "🟩"]
Tmap = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
xy = input("Where do you want to put the treasure? ")

r = int(xy[0])
c = int(xy[1])
#  rc
# if r == 1 and c == 1:
#     row1[0] = "❌"
# elif r == 1 and c == 2:
#     row1[1] = "❌"
# elif r == 1 and c == 3:
#     row1[2] = "❌"
# elif r == 2 and c == 1:
#     row2[0] = "❌"
# elif r == 2 and c == 2:
#     row2[1] = "❌"
# elif r == 2 and c == 3:
#     row2[2] = "❌"
# elif r == 3 and c == 1:
#     row3[0] = "❌"
# elif r == 3 and c == 2:
#     row3[1] = "❌"
# elif r == 3 and c == 3:
#     row3[2] = "❌"
Tmap[r-1][c-1] = '❌'
print(f"{row1}\n{row2}\n{row3}")
