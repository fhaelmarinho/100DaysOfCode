# ✨ 100 Days of Code Challenge - Day 18/100 💻

import random
import string
 
class PasswordGenerator:
    def __init__(self, length=8, upper_case=True, lower_case=True, digits=True, symbols=True):
      self.length = length
      self.upper_case = upper_case
      self.lower_case = lower_case
      self.digits = digits
      self.symbols = symbols
    
    def generate(self):
        try:
            avaliable_chars = ''
            if self.lower_case:
                avaliable_chars += string.ascii_lowercase   # abcdefghijklmnopqrstuvwxyz
            if self.upper_case:
                avaliable_chars += string.ascii_uppercase   # ABCDEFGHIJKLMNOPQRSTUVWXYZ
            if self.digits:
                avaliable_chars += string.digits            # 0123456789
            if self.symbols:
                avaliable_chars += string.punctuation       # !@#$%^&*()_+[]{}|;:,.<>?/ etc.
            if not avaliable_chars:
                    raise ValueError("Nenhum tipo de caractere foi selecionado!")

            return ''.join(random.choice(avaliable_chars) for _ in range(self.length))      
        
        except ValueError as ve:
            print(f"[ERRO] {ve}")
            return None

def main():
    length = int(input("Enter password length: "))
    upper_case = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lower_case = input("Include lowercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'

    generator = PasswordGenerator(length, upper_case, lower_case, digits, symbols)
    password = generator.generate()
    print(f"Generated password: {password}")
    
    
main()