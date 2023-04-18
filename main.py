print("===============================")
print("|| Word Snack Word Generator ||")
print("===============================")
print("||      @ Matei Popescu      ||")
print("===============================")
print("This is a program which generates words for the Word Snack mobile game. Word Snack can be downloaded here:")
print("Apple: https://apps.apple.com/us/app/word-snack-picnic-with-words/id1257539184")
print("Google Play: https://play.google.com/store/apps/details?id=com.apnax.wordsnack&hl=en")
print("\n")

m = input("How many letters do you have?: ")
m = int(m)
while m < 3 or m > 5 or type(m) != int:
    print("Sorry! Invalid number. We can only generate words for 3, 4 or 5 letters\n")
    m = input("How many letters do you have?: ")

n= input("How long is your word?: ")
n = int(n)
while n < 3 or n > 5 or type(n) != int:
    print("Sorry! Invalid number. We can only generate 3, 4 or 5 letters long words\n")
    n = input("How long is your word?: ")

#v = np.empty((3,3))
v = []

if m == 3:
    for i in range(0, 3):
        l = input("Letter No. " + str(i+1) + ": ")
        if(l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u' or l == 'ă' or l == 'î' or l == 'â'):
            v.append([l,0])
        else:
            v.append([l,1])
elif m == 4:
    for i in range(0, 4):
        l = input("Letter No. " + str(i + 1) + ": ")
        if (l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u' or l == 'ă' or l == 'î' or l == 'â'):
            v.append([l, 0])
        else:
            v.append([l, 1])
elif m == 5:
    for i in range(0, 5):
        l = input("Letter No. " + str(i + 1) + ": ")
        if (l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u' or l == 'ă' or l == 'î' or l == 'â'):
            v.append([l, 0])
        else:
            v.append([l, 1])

#SORTING
if (m == 3):
    for i in range(0, 3):
        for j in range(0, 3):
            if(v[i][0] < v[j][0]):
                l = v[j][0]
                v[j][0] = v[i][0]
                v[i][0] = l

                l = v[j][1]
                v[j][1] = v[i][1]
                v[i][1] = l

if (m == 4):
    for i in range(0, 4):
        for j in range(0, 4):
            if (v[i][0] < v[j][0]):
                l = v[j][0]
                v[j][0] = v[i][0]
                v[i][0] = l

                l = v[j][1]
                v[j][1] = v[i][1]
                v[i][1] = l

if (m == 5):
    for i in range(0, 5):
        for j in range(0, 5):
            if (v[i][0] < v[j][0]):
                l = v[j][0]
                v[j][0] = v[i][0]
                v[i][0] = l

                l = v[j][1]
                v[j][1] = v[i][1]
                v[i][1] = l

c = 1

#WORD GENERATION
if (n == 3):
    for i in range(0, m):
        for j in range (0, m):
            for k in range (0, m):
                #print(str(i) + str(j) + str(k))
                if(i != j and i != k and j != k and v[i][1]+v[j][1]+v[k][1] != 3):
                    print(str((c)) + '.) ' + str(v[i][0]) + str(v[j][0]) + str(v[k][0]))
                    c = c + 1

if (n == 4):
    for i in range(0, m):
        for j in range (0, m):
            for k in range (0, m):
                for h in range (0, m):
                    #print(str(i) + str(j) + str(k))
                    if(i != j and i != k and i != h and j != k and j != h and k != h and v[i][1]+v[j][1]+v[k][1] != 3 and v[j][1]+v[k][1]+v[h][1] != 3):
                        print(str((c)) + '.) ' + str(v[i][0]) + str(v[j][0]) + str(v[k][0]) + str(v[h][0]))
                        c = c + 1


if (n == 5):
    for i in range(0, m):
        for j in range (0, m):
            for k in range (0, m):
                for h in range(0, m):
                    for g in range(0, m):
                        #print(str(i) + str(j) + str(k))
                        if(i != j and i != k and i != h and i != g and j != k and j != h and j != g and k != h and k != g and h != g and v[i][1]+v[j][1]+v[k][1] != 3 and v[j][1]+v[k][1]+v[h][1] != 3 and v[k][1]+v[h][1]+v[g][1] != 3):
                            print(str((c)) + '.) ' + str(v[i][0]) + str(v[j][0]) + str(v[k][0]) + str(v[h][0]) + str(v[g][0]))
                            c = c + 1

print('\n')
input("Press any key to close the window.")
