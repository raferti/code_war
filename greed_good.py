d = [4, 5, 5, 5, 1]

def score(dice):
    count_score = 0
    for i in range(1, 7):
        count_num = dice.count(i)
        if i == 1:
            i = 10
        if count_num == 3:
            count_score += i * 100
        elif count_num > 3:
            count_score += i * 100
            if i == 10 or i == 5:
                count_score += (count_num - 3) * (i * 10)
        elif count_num < 3:
            if i == 10 or i == 5:
                count_score += count_num * (i * 10)
    return count_score

print(score(d))
