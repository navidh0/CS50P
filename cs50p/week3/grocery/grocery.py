grocery = {}


while True:
    try:
        item = input().upper().strip()
        if item not in grocery :
            grocery[item] = 1

        else:
            grocery[item] += 1



    except EOFError:
        sorted_list = dict(sorted(grocery.items()))
        for item in sorted_list:
            print (sorted_list[item], item, sep=' ')
        break

