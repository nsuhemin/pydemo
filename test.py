while True:
    score = int(input("input a score:"))
    if score == -1: break
    level = 'A'
    if 0 <= score < 60:
        level = 'E'
    elif score < 70:
        level = 'D'
    elif score < 80:
        level = 'C'
    elif score < 90:
        level = 'B'
    print("{}对应等级{}".format(score, level))