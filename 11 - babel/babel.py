import random
import os
#Writes i number of files with j number of lines with k number of characters each
txt="QWERTYUIOPLKJHGFDSAZXCVBNM" #text
nums = "1234567890"              #numbers
location = "//babel"             #output location

def write(ri = 10, rj = 1000, rk = 100):
    try:
        if not os.path.exists(location):
            os.makedirs(location)
        for i in range(0,ri,1):
            f=open(location + "book_{0}.txt".format(i),'a')
            # Number of lines per file
            for j in range(0,rj,1):
                line=""
                # Number of characters per line
                for k in range(0,rk,1):
                    n=random.randrange(0,len(txt),1)
                    line=line+txt[n]
                f.write(line+"\n")
        return True
    except:
        return False


def search(search_string):
    found_flag = False
    try:
        for i in range(0,10,1):
            filename = location + "book_{0}.txt".format(i)
            f=open(filename,'r')
            p=str(f.read())
            q=p.splitlines()
            for line_num, line in enumerate(q):
                if search_string in line:
                    found_flag = True
                    print ("{0} line in {1} file".format(line_num, filename))
                    print(line)
                else:
                    continue
    except:
        return False
    return found_flag

# Test script
#write(ri=10,rj=100,rk=100)
#search(search_string="BCD")

if __name__ =="__main__":
    func = input("Generate[G] or Search[S]: ")
    if func == "G":
        ri = int(input("Enter number of files "))
        if write(ri):
            print("successfully written to ", location)
        else:
            print("There was some issue in writing")
    elif func == "S":
        search_term = input("Enter Search Term: ")
        if search(search_term):
            print("found some search results")
        else:
            print("There was some issue in search")







