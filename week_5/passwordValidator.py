
import string
import random

characters = string.ascii_letters + string.digits + string.punctuation

# Functions to validate different requirements of a passwrod.
def length_passwordValidator(password): #length should be 8 or greater
        if len(password) >= 8:
            return True
        else:
            return False
        
def upperCase_passwordValidator(password):# there should be an upercase
        for char in password:
            if char.isupper():
                return True
           
        return False
            
def lowerCase_passwordValidator(password):# there should be a lowercase
        for char in password:
            if char.islower():
                return True
            
        return False
            
def digitsIn_passwordValidator(password):#there should be a digit
        for char in password:
            if char.isdigit():
                return True
    
        return False
            
def specialChar_passwordValidator(password):# there should be a digit
     for char in password:
          if char in string.punctuation:
               return True
         
     return False
            
def randomly_validatePassword(password):

    #if length is less than 8 this loop will add all type of charactere if they are missing.
    
    if not upperCase_passwordValidator(password): #uppercase
        password += random.choice(string.ascii_uppercase)
        
    if not lowerCase_passwordValidator(password): #lower Case
        password += random.choice(string.ascii_lowercase)
        
    if not digitsIn_passwordValidator(password): #digits
        password += random.choice(string.digits)
        
    if not specialChar_passwordValidator(password): #special Characters
        password += random.choice(string.punctuation)

    while not length_passwordValidator(password):
         password += random.choice(characters)

    return password # Returning randomly modified password


def validatepassword(password):
     
     # we will store errorss for each incomplete requirment here.
     errors = []

     if length_passwordValidator(password) and upperCase_passwordValidator(password) and lowerCase_passwordValidator(password) and digitsIn_passwordValidator(password) and specialChar_passwordValidator(password):
          return True, errors
     
     else:
          

          if not length_passwordValidator(password):
               errors.append("Password must be atleast 8 characters. ")

          if not upperCase_passwordValidator(password):
               errors.append("Atleast one upper Case character is required. ")

          if not lowerCase_passwordValidator(password):
               errors.append("Atleast one lower Case character is required. ")

          if not digitsIn_passwordValidator(password):
               errors.append("Atleast one digit is required. ")

          if not specialChar_passwordValidator(password):
               errors.append("Atleast on special character is required. ")


          #print(f"Suggested Password: {randomly_validatePassword(password)}")
          return False, errors


            
             

