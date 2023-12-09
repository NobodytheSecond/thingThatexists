print('password:')
password = input()

# array
savedPasswords = []
savedEmail = []
l = 0
if password == '0':
    while(True):
        print("success: " + password)
        print('passwords to save:')
        savePassword = input()
        print('email')
        if savePassword == 'q':
            print('quit')
            break
        saveEmail = input()
        
        savedPasswords.append(l)
        savedPasswords[l] = savePassword
        savedEmail.append(l)
        savedEmail[l] = saveEmail
        
        l += 1
        for i in range(len(savedPasswords)):
            print(i)
            print(savedPasswords[i])
            print(i)
            print(savedEmail[i])

else:
    print('failed')
