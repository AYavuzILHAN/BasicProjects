import random as rnd
import time

print("A.Yavuz İLHAN-2021502132")
print("Welcome to WORD GAME\n    1-Start the Game\n    2-Exit the Game")
words = ["lust", "faust", "lilith"]

def word_game(word):
    tahmin_edilen = ['*' if letter.isalpha() else letter for letter in word]
    deneme = 0
    score = 0
    while '*' in tahmin_edilen:
        print(''.join(tahmin_edilen))
        try:
            secim = int(input("Enter the answer 1 or request a letter 2:"))
            if secim == 2:
                deneme += 1
                letter = rnd.choice([letter for letter in word if letter.isalpha()])
                for i in range(len(word)):
                    if word[i] == letter:
                        tahmin_edilen[i] = letter
            elif secim == 1:
                tahmin = input("Enter your guess: ")
                if tahmin == word:
                    score += (len(word) - deneme) * 100
                    print("Congratulations! Your guess is correct, you gain:", score, "point")
                    return score
                else:
                    score -= ((len(word) - deneme) * 100)
                    print("Wrong answer, you lose:", score, "point")
                    print("The correct answer is:", word)
                    return score
        except Exception as yavuz:
            print("Enter the answer 1 or request a letter 2:")
           
while True:
        a = int(input())
        if a == 1:
            print("This word is one of the seven sins in Christianity. According to Abrahamic religions, Sodom and Gomorrah were destroyed by God, and one of the reasons for this is the meaning associated with this word. Nowadays, this word is commonly used in various fields such as movies, theaters, etc.\n\n!!!Please write your answers in lowercase letters, otherwise the system will perceive them as wrong even if you guess correctly.!!!\n\nFirst Word")
            word = words[0]
            result_1 = word_game(word)
    
            print("\nThe book, superficially portraying a wise who sells his soul to the devil named Mephistopheles, delves into criticizing the scientific rationalism brought by the Renaissance and secularism, and humanity's succumbing to this illusion. This book is considered among world classics and still subject to debates.\n\n!!!Please write your answers in lowercase letters, otherwise the system will perceive them as wrong even if you guess correctly.!!!\n\nSecond Word")
            word = words[1]
            result_2 = word_game(word)
    
            print("\nAccording to the Middle Ages belief of the Hebrews, she believed that she was created at the same time and simultaneously with Adam, so she believed that she was equal to Adam. She vehemently refuses to be with Adam. When Adam insists, she escapes with magic and leaves him. The angels find her to bring him back, but she informs them that there are more than 100 jinn children because she is with Samael, so she can no longer be faithful to Adam. Meanwhile, God sends three angels to stop her. The angels tell her that if she does not return, they will kill one of her children every day, and if she does not return and obey God and Adam, they will kill one of her children for every day he disobeys. Thereupon, she begins to kill the children of those descended from Adam and Eve. According to the tradition, she tries to kill men within 8 days of birth and girls within 20 days. The jinns believed to exist in the world today are said to have originated from the union of Adam and his sister Naama and Tuval Cain. Before Adam and Eve were cursed with limited life before leaving paradise, they were immortal. After that, God creates another wife whose name is unknown, and Adam watches this creation. He is very affected by what he sees and does not accept the new wife. Thirdly, he later puts Adam to sleep and creates Eve from his rib bone. Eve, being created from a part of Adam, is subject to him.\n\n!!!Please write your answers in lowercase letters, otherwise the system will perceive them as wrong even if you guess correctly.!!!\n\nThird word")
            word = words[2]
            result_3 = word_game(word)
            print()
            print(f"Total Score: {result_1+result_2+result_3}")
            print("The game will close in 10 seconds after it ends")
            time.sleep(10)
            break
        elif a == 2:
            print("Game is closing ...")
            break
        else:
            print("You entered a number other than 1 or 2, Please start again!!!")
            break