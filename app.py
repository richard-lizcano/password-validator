import re

def validate_password(password):
    
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%*!]).{8,}$' # Regex that is grouped by perentgheses and checks for each condition
    

    if re.fullmatch(pattern, password):
        print("VALID")
    else: # If the password does not match the pattern, print INVALID and specify which criteria were not met
        print("INVALID")
        if len(password) < 8:
            print(" - Length must be at least 8 characters.")
        if not re.search(r'[A-Za-z]', password):
            print(" - Must contain at least one letter.")
        if not re.search(r'\d', password):
            print(" - Must contain at least one digit.")
        if not re.search(r'[A-Z]', password):
            print(" - Must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', password):
            print(" - Must contain at least one lowercase letter.")
        if not re.search(r'[@#$%*!]', password):
            print(" - Must contain at least one of the special characters: (@, #, $, %, *, !)")

def main():
    user_input = input("Enter your password: ")
    validate_password(user_input)

if __name__ == '__main__':
    main()
