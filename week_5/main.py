import passwordValidator

password = input("======>>""Enter your password: ")
isValid,errors = passwordValidator.validatepassword(password)

if isValid:
    print("="*30,"VALID PASSWORD\n","="*30)
else:

    while  not isValid:

        print("="*30,"INVALID PASSWORD!","="*30,"\nErrors:\n","\n ".join(errors))
        #suggested password:
        print("*"*30,f"Suggested Password: {passwordValidator.randomly_validatePassword(password)}","*"*30)
        
        password = input("======>>Enter another password: ")

        isvalid, errors = passwordValidator.validatepassword(password)
        if isvalid:
            print(">"*30,"Password validated:","<"*30)
            break
        


