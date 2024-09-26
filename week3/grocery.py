shopping_dict = {}
while True:
    try:
        item = input().upper()
        if item not in shopping_dict.keys():
            shopping_dict[item] = 1
        else:
            shopping_dict[item] += 1

    except EOFError:
        shopping_list = sorted(shopping_dict)
        sorted_dict = {i: shopping_dict[i] for i in shopping_list}

        for i in sorted_dict:
            print(sorted_dict[i], i)
        break
        
