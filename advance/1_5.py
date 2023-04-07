
file_path = r"C:\Users\Alemo\Downloads\found.txt"
    #תוכנית שמדפיסה למסך את השם הארוך ביותר בקובץ
    with open(file_path, 'r') as f1:
        print(functools.reduce(lambda x,y: x if x > y else y, [x for x in f1]))

    #תוכנית שמדפיסה למסך את סכום האורכים של השמות בקובץ
    with open(file_path, 'r') as f1:
        print(functools.reduce(lambda x,y: x+y, [len(x.strip()) for x in f1]))

    #תוכנית שמדפיסה למסך את השמות הכי קצרים בקובץ, כל שם בשורה נפרדת
    with open(file_path, 'r') as f1:
        min_len = len(functools.reduce(lambda x,y: x if len(x) < len(y) else y, [x.strip() for x in f1]))
    with open(file_path, 'r') as f1:
        [print(x.strip()) for x in f1 if len(x.strip()) == min_len]

    #תוכנית שיוצרת קובץ חדש בשם name_length.txt המכיל את האורך של כל שם בקובץ names.txt, לפי הסדר, אחד בכל שורה.
    with open(file_path, 'r') as f1, open("name_length.txt", 'w') as nlf2:
        ls = [len(x.strip()) for x in f1]
        [nlf2.write(str(x) + '\n') for x in ls]

    #תוכנית שקולטת מהמשתמש מספר המייצג אורך של שם ומדפיסה את כל השמות בקובץ names.txt שהם באורך הזה.
    n = int(input("Enter name length: "))
    with open(file_path, 'r') as f1:
        [print(x.strip()) for x in f1 if len(x.strip()) == n]

