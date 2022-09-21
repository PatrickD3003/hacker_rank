from huruf_kontol import huruf_kontol
def minion_game(string):
    stuart_consonants, kevin_vowels = 0, 0    
    vowel = ("A", "I", "U", "E", "O")
    i = 0
    if 0 < len(string) <= pow(10, 6):
        while 1:
            if i >= len(string):
                if stuart_consonants > kevin_vowels:
                    print(f"Stuart {stuart_consonants}")
                
                elif stuart_consonants == kevin_vowels:
                    print(f"Draw")
                
                else:
                    print(f"Kevin {kevin_vowels}")  
                break

            if string[i] in vowel:
                kevin_vowels += len(string) - i
            else:
                stuart_consonants += len(string) - i
            i += 1

if __name__ == '__main__':
    s = input()
    minion_game(huruf_kontol)