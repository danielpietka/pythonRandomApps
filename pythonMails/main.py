import os
import re
import itertools

from matplotlib.pyplot import loglog

path = "emails"
emails = []
os.chdir(path)

# Extract all emails to list
for file in os.listdir():
    if file.endswith(".txt"):
        f = open(file, 'r').readlines()
        for x in f:
            emails.append(x)


    if file.endswith(".csv"):
        f = open(file, 'r').readlines()
        for row in f:
            mail = row.partition(";")[2]
            emails.append(mail)   
result = []     
# Delete newlines
for i in emails:
    result.append(i.strip())



def validMail(result):
    regex = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{1,4})+'
    valid = []
    for mail in result:
        if re.search(regex,mail):
            valid.append(mail)
        else:
            pass
    return valid

# Task 1
def checkMail():
    regex = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{1,4})+'
    invalid = []
    for mail in result:
        if re.search(regex,mail):
            pass
        else:
            invalid.append(mail)
    #invalid = list(dict.fromkeys(invalid))
    print(f'Invalid emails ({len(invalid)})')
    print(*invalid, sep='\n')
    print("\n")

# Task 2
def search():
    word = input("Enter your text to search for email: ")
    valid = validMail(result)
    str_match = list(filter(lambda x: word in x, valid))
    print(f"Found emails with '{word}' in email ({len(str_match)})")
    print(*str_match, sep = "\n")
    print("\n")
# Task 3
# Turn into 'user' 'domain' and reverse it for sort by domain
def keyFunction(s):
    return s.split('@')[::-1]

def groupByDomain():
    valid = validMail(result)
    sortedbyDomain = sorted(valid, key=keyFunction)
    x = []
    iterator = itertools.groupby(sortedbyDomain, lambda string: string.split("@")[1])

    for element, group in iterator:
        x.append(list(group))
    
    for lista in x:
        for mail in lista:
            print(mail)
        print('Domain', mail.split("@")[1], f'({len(lista)})')
    print("\n")

# Task 4
def findLogEmail():
    valid = validMail(result)
    passPath = input("Pass to log file: ")
    log = open(passPath, 'r')
    logList = []
    for line in log:
        m = re.search(".*?\'(.*)\'.*", line).group(1)
        logList.append(m)
    
    diff = [x for x in valid if x not in set(logList)]
    diff.sort()
    print(f"Email not sent {(len(diff))}:\n")
    print(*diff, sep="\n")
    print("\n")
    

while True:
    x = input("Your commands:\n  --incorrect-emails | -ic\n  --search | -s\n  --group-by-domain | -gbd\n  --find-emails-not-in-logs | -feil\n")
    match x:
        case '--incorrect-emails' | '-ic':
            checkMail()
        case '--search' | '-s':
            search()
        case '--group-by-domain' | '-gbd':
            groupByDomain()
        case '--find-emails-not-in-logs' | '-feil':
            findLogEmail()
        
