def funct(instance, result_label):
        import random
        file = open('ricepts.txt', 'r')
        list1 = file.readlines()

        size = len(list1)
        primi_list = []
        secondi_list = []
        primi = True

        for i in range(size):
            if list1[i] == 'Primi\n':
                primi = True
            elif list1[i] == 'Secondi\n':
                primi = False
            if primi:
                for j in range(len(list1[i])):
                    if list1[i][j] == '#':
                        rep = int( list1[i][j+1:].strip())
                        for _ in range(rep):
                            primi_list.append(list1[i])
            else :
                 for j in range(len(list1[i])):
                    if list1[i][j] == '#':
                        rep = int( list1[i][j+1:].strip())
                        for _ in range(rep):
                            secondi_list.append(list1[i])

        size = len(primi_list)
        primo_extracted = random.randrange(size)

        size = len(secondi_list)
        secondo_extracted = random.randrange(size)

        extracted_dish = primi_list[primo_extracted].split('#')[0].lstrip('-').strip()
        extracted_dish += " and as second dish: "
        extracted_dish += secondi_list[secondo_extracted].split('#')[0].lstrip('-').strip()
        result_label.text = "The extracted dishes are: \n\n" + extracted_dish

        file.close()
