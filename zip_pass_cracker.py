import zipfile

def extractFile(zfile, password): 

    # try blocks to display results 
    try: 
        zfile.extractall(pwd=bytes(password, 'utf-8'))
        return password 
    except:
        print('Incorrect password')
        return 

def main():
    # enter zip file name here 
    zfile = zipfile.ZipFile('test.zip')
    # enter password list here 
    passFile = open('list30.txt')

    # for loop to check every line from passFile 
    for line in passFile.readlines(): 
        password = line.strip('\n')
        guess = extractFile(zfile, password)

        # if password is found 
        if guess: 
            print('Password = ' + password)
            break

if __name__ == '__main__':
    main()