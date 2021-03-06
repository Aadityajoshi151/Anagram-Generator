from itertools import permutations
import enchant
d = enchant.Dict("en_US")
chars = input("Enter Space Separated Letters\n").split()
anagrams = list(permutations(chars,len(chars)))
file = open("All-Anagrams.txt","w")
mfile = open("Meaningful Anagrams.txt","w")
for i in range(len(anagrams)):
    anagrams[i] = "".join(k for k in anagrams[i])
    if d.check(anagrams[i]): mfile.write(anagrams[i]+"\n")
    else: file.write(anagrams[i]+"\n")
file.close()
mfile.close()
ch1 = str(input(("Do You Have A First Letter? (y/n)\n")))
if ch1 == "y" or ch1 == "Y":
    startletter = str(input("Enter The Letter\n"))
    file = open(startletter+"-Anagrams.txt","w")
    for i in anagrams:
        if i[0] == startletter:
            file.write(i+"\n")
    file.close()
print("Files Created Successfully.")