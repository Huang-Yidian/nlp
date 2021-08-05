import os

train_path ="./train1.txt"
test_path = "./testright1.txt"

train_bmes = "./train.bmes"
test_bmes = "./test.bmes"

dict = {"NR":"NAME","NT":"ORG","NS":"CONT"}

def converter(origin_path,save_path):
    origin = open(origin_path, "r", encoding="utf-8")
    save = open(save_path,"w",encoding="utf-8")

    lines = origin.readlines()
    for line in lines:
        line = line.strip()
        words = line.split()
        for data in words:
            char_lable = data.split("/")
            index = 0

            for i in char_lable[0]:
                if i in ['。', '！', '？'] and char_lable[1].lower() == "o":
                    save.write(i + ' ' + char_lable[1].upper() + '\n')

                elif char_lable[1] == "o":

                    save.write(i + " " + char_lable[1].upper() + '\n')


                else:
                    if len(char_lable[0]) == 1:
                        save.write(i + ' S-' + char_lable[1].upper() + '\n')
                    elif i == char_lable[0][0] and index == 0:
                        save.write(i + ' B-' + char_lable[1].upper() + '\n')
                        index += 1

                    elif i == char_lable[0][-1] and index != len(char_lable[0]):
                        save.write(i + ' E-' + char_lable[1].upper() + '\n')
                        index += 1

                    else:
                        save.write(i + ' M-' + char_lable[1].upper() + '\n')
                        index += 1

        save.write('\n')
    print("Sequences with BMESO format in: "+save_path+" !")
    origin.close()
    save.close()


converter(train_path,train_bmes)
converter(test_path,test_bmes)