def funct(instance, result_label):
        import random
        file = open('ricepts.txt', 'r')
        list1 = file.readlines()

        size = len(list1)
        list2 = []

        for i in range(size):
            for j in range(len(list1[i])):
                if list1[i][j] == '#':
                    rep = int( list1[i][j+1:].strip())
                    for k in range(rep):
                        list2.append(list1[i])

        size = len(list2)

        for i in range(size):
            print(list2[i])

        num = random.randrange(size)

        #print("\nThe extracted dish is::" + list2[num])
        extracted_dish = list2[num].split('#')[0]
        result_label.text = "The extracted dish is: " + extracted_dish
        file.close()
