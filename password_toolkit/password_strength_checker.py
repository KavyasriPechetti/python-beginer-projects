print("\n--- Password Strength Checker ---")

password = input("Enter a password to check its strength :")
# print("You entered :", password)



has_lower = any(char.islower() for char in password)
has_upper = any(char.isupper() for char in password)
has_digit = any(char.isdigit() for char in password)

symbols = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
has_symbol = any(char in symbols for char in password)

score = 0
if len(password) >= 8 :
    score += 1
if has_lower :
        score += 1
if has_upper :
        score += 1
if has_digit :
        score += 1
if has_symbol :
        score += 1

if score <= 2 :
    strength = "Weak"
elif score == 3 or score == 4 :
    strength = "Medium"
else : 
    strength = "Strong"
print("The password you entered is",password, "and its strength is", strength)