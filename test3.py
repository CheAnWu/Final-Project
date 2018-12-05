def if_bust(sum, ace):
    while sum > 21:
        if ace > 0:
            sum = sum - 10
            ace -= 1
        else:
            break
    if sum > 21:
        return (-1, ace)
    else:
        return (sum, ace)

r =if_bust(22,0)
print(r[0]==-1)