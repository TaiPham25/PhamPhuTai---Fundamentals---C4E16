numb = [1 ,0 ,-10 ,2018]

sort =[]
while True:
    min_numb = min(numb)
    sort.append(min_numb)
    numb.remove(min_numb)

    if len(numb) == 0:
        break
print(*sort, sep=', ')
