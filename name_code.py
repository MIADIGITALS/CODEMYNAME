#NAME CODE
#iam_the_mia
print('THIS IS A NAME GAME WHERE WE DERIVE A CODE FOR YOUR NAME')
name=str.upper(input('WHAT iS YOUR NAME : '))
num=int(input('HOW MANY LETTERS ARE IN YOUR NAME : '))
print('INPUT YOUR NAME TO DERIVE A CODE FOR IT')
NAME=[]
for i in range(num):
    n=str.upper(input(''))
    NAME.append(n)
print(NAME)
#name_code={'A': 'AWESOME', 'B': 'BRAINAIC', 'C': 'CUTE', 'D': 'DECISIVE', 'E': 'ELEGANT', 'F': 'FRIENDLY', 'G': 'GLAMOROUS', 'H': 'HILLARIOUS', 'I': 'INTELLIGENT', 'J': 'JOYOUS', 'K': 'KIND', 'L': 'LOVELY', 'M': 'MAGNIFICIENT', 'N': 'NICE', 'O': 'OBEDIENT', 'P': 'PEACEFUL', 'Q': 'QUIET', 'R': 'RADICAL', 'S': 'SACRED', 'T': 'TOLERANT', 'U': 'UNDERSTANDING', 'V': 'VERY PATIENT', 'W': 'WONDERFUL', 'X': 'XENAS', 'Y': 'YOUTHFUL', 'Z': 'ZEALOUS'}
for i in NAME:
    if i == 'A':
        name_code = 'AWESOME'
    elif i == 'B':
        name_code= 'BRAINAIC'
    elif i == 'C':
        name_code= 'CUTE'
    elif i == 'D':
        name_code= 'DECISIVE'
    elif i == 'E':
        name_code= 'ELEGANT'
    elif i == 'F':
        name_code= 'FAITHFUL'
    elif i == 'G':
        name_code= 'GEOGEOUS'
    elif i == 'H':
        name_code= 'HILLARIOUS'
    elif i == 'I':
        name_code= 'INTELLIGENT'
    elif i == 'J':
        name_code= 'JOYOUS'
    elif i == 'K':
        name_code= 'KIND'
    elif i == 'L':
        name_code= 'LOVELY'
    elif i == 'M':
        name_code= 'MAGNIFICIENT'
    elif i == 'N':
        name_code= 'NICE'
    elif i == 'O':
        name_code= 'OBEDIENT'
    elif i == 'P':
        name_code= 'PEACEFUL'
    elif i == 'Q':
        name_code= 'QUIET'
    elif i == 'R':
        name_code= 'RADICAL'
    elif i == 'S':
        name_code= 'SACRED'
    elif i == 'T':
        name_code= 'TOLERANT'
    elif i == 'U':
        name_code= 'UNDERSTANDING'
    elif i == 'V':
        name_code= 'VERY PATIENT'
    elif i == 'W':
        name_code= 'WISE'
    elif i == 'X':
        name_code= 'XENAS'
    elif i == 'Y':
        name_code= 'YOUTHFUL'
    elif i == 'Z':
        name_code= 'ZEALOUS'
    else:
        print('YOU DIDNT ENTER A RIGHT LETTER IN YOUR NAME')
    print('{} YOU ARE {} FOR {}'.format(name,i,name_code))
'''name_code={'A': 'AWESOME', 'B': 'BRAINAIC', 'C': 'CUTE', 'D': 'DECISIVE', 'E': 'ELEGANT', 'F': 'FRIENDLY', 'G': 'GEOGEOUS', 'H': 'HILLARIOUS', 'I': 'INTELLIGENT', 'J': 'JOYOUS', 'K': 'KIND', 'L': 'LOVELY', 'M': 'MAGNIFICIENT', 'N': 'NICE', 'O': 'OBEDIENT', 'P': 'PEACEFUL', 'Q': 'QUIET', 'R': 'RADICAL', 'S': 'SACRED', 'T': 'TOLERANT', 'U': 'UNDERSTANDING', 'V': 'VERY PATIENT', 'W': 'WISE', 'X': 'XENAS', 'Y': 'YOUTHFUL', 'Z': 'ZEALOUS'}

for x,y in name_code.items():
    if x in NAME:
        print('{} YOU ARE {} FOR {}'.format(name,x,y))
'''
