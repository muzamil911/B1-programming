
#Given data
passwords = [ "Pass123",
"SecurePassword1", "weak",
"MyP@ssw0rd", "NOLOWER123"]

validPasskeys = 0
invalidPasskeys = 0

print("Validating Passwords:\n")
#loop to go through the given passwords:
for passkey in passwords:

    #requirements:
    passwordLength = len(passkey) >=8
    uppeCase = False
    LowerCase = False
    oneDigit = False

    #loop to go through each character of a password:
    for char in passkey:
        #checking each condition of the acceptable password:
        if len(passkey) >= 8:
            passwordLength = True
        if char.islower():
            LowerCase = True
        if char.isupper():
            uppeCase = True
        if char.isdigit():
            oneDigit = True
    
    #checking if there is a valid password.
    if passwordLength == True and uppeCase == True and LowerCase == True and oneDigit == True:
        print(f"Pass:\n'{passkey}' meets all requirments.")
        #counting valid passwords
        validPasskeys += 1
    #checking for incalid passwords
    else:
        print(f"Fail:\n '{passkey}' -",end=" ")
        errors = []
        #checking errors... .
        if not passwordLength:
            errors.append("too short")
        if not uppeCase:
            errors.append("no upper case character.")
        if not LowerCase:
            errors.append("no lower case character.")
        if not oneDigit:
            errors.append("No digit.")

        #counting invalid passwords
        invalidPasskeys += 1
        print(", " .join(errors))

print(f"Summary:\n{validPasskeys} Complaints\n{invalidPasskeys} non_complaint")
        


    