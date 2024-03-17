import random as rnd
import time 

print("A.Yavuz İLHAN-2021502132")
print()
print("!!!Our Excuse,\nWhen you request a letter, the play may not give. This error will be fixed as soon as possible. We apology for this mistake. When this error happens, request a letter until the play gives letter , Do not worry, your score will not be affected.")
time.sleep(2)
print()
print("Welcome to WORD GAME\n    1-Start the Game\n    2-Exit the Game")

    
words = (["lust", "ball", "soul"], ["faust", "sloth", "greed"], ["lilith", "farabi", "empire"])
f = [0,1,2]
random = rnd.choice(f)
random_1 = words[0][random]
random_2 = words[1][random]
random_3 = words[2][random]

def word_game(word):
    tahmin_edilen = ['*' if letter.isalpha() else letter for letter in word]
    deneme = 0
    score = 0
    while '*' in tahmin_edilen:
        print(''.join(tahmin_edilen))
        try:
            if tahmin_edilen.count("*") != 1:
                secim= int(input("Enter the answer 1 or request a letter 2:"))
            if secim == 2:
                if deneme <= len(word):
                    deneme += 1
                if tahmin_edilen.count("*") == 1:
                    print()
                    print("!!!!Your right to request letter is over, please answer!!!")
                    print()
                    tahmin = (input("Enter your guess: ").lower())
                    if tahmin == word:
                        score += tahmin_edilen.count("*") * 100
                        print("Congratulations! Your guess is correct, you gain:", score, "point")
                        return score
                    else:
                        score -= (tahmin_edilen.count("*") * 100)
                        print("Wrong answer, you lose:", score, "point")
                        print("The correct answer is:", word)
                        return score
                    
                letter = rnd.choice([letter for letter in word if letter.isalpha()])
                for i in range(len(word)):
                    if word[i] == letter and letter:
                        tahmin_edilen[i] = letter
            elif secim == 1:
                tahmin = (input("Enter your guess: ").lower())
                if tahmin == word:
                    score += tahmin_edilen.count("*") * 100
                    print("Congratulations! Your guess is correct, you gain:", score, "point")
                    return score
                else:
                    score -= (tahmin_edilen.count("*") * 100)
                    print("Wrong answer, you lose:", score, "point")
                    print("The correct answer is:", word)
                    return score
        except Exception as yavuz:
            print("Please Enter 1 to answer or 2 to request a letter:")
           
while True:
    try:        
        a = int(input())
        print()
        if a == 1:
            if random_1 == words[0][0]: 
                print("This word is one of the seven sins in Christianity. According to Abrahamic religions, Sodom and Gomorrah were destroyed by God, and one of the reasons for this is the meaning associated with this word. Nowadays, this word is commonly used in various fields such as movies, theaters, etc.\n\nFirst Word")
                word = words[0][0]
                result_1 = word_game(word)
                print()
            elif random_1 == words[0][1]:
                print("A solid or hollow spherical or egg-shaped object that is kicked, thrown, or hit in a game.\n\nFirst Word")
                word = words[0][1]
                result_1 = word_game(word)
                print()
            elif random_1 == words[0][2]:
                print("The spiritual or immaterial part of a human being or animal, regarded as immortal.\n\nFirst Word")
                word = words[0][2]
                result_1 = word_game(word)
                print()                
            if random_2 == words[1][0]:    
                print("\nThe book, superficially portraying a wise who sells his soul to the devil named Mephistopheles, delves into criticizing the scientific rationalism brought by the Renaissance and secularism, and humanity's succumbing to this illusion. This book is considered among world classics and still subject to debates.\n\nSecond Word")
                word = words[1][0]
                result_2 = word_game(word)
                print()
            elif random_2 == words[1][1]:
                print("It is one of the seven deadly sins in Catholic teachings. It is the most difficult sin to define and credit as sin, since it refers to an assortment of ideas, dating from antiquity and including mental, spiritual, pathological, and conditional states. One definition is a habitual disinclination to exertion, or laziness. Views concerning the virtue of work to support society and further God's plan suggest that through inactivity, one invites sin: For Satan finds some mischief still for idle hands to do.\n\nSecond Word")
                word = words[1][1]
                result_2 = word_game(word)
                print()
            elif random_2 == words[1][2]:
                print("It is one of the seven deadly sins in Catholic teachings.It is an insatiable desire for material gain (be it food, money, land, or animate/inanimate possessions) or social value, such as status, or power. It has been identified as undesirable throughout known human history because it creates behavior-conflict between personal and social goals.\n\nSecond Word")
                word = words[1][2]
                result_2 = word_game(word)
                print()
            if random_3 == words[2][0]:   
                print("\nAccording to the Middle Ages belief of the Hebrews, she believed that she was created at the same time and simultaneously with Adam, so she believed that she was equal to Adam. She vehemently refuses to be with Adam. When Adam insists, she escapes with magic and leaves him. The angels find her to bring him back, but she informs them that there are more than 100 jinn children because she is with Samael, so she can no longer be faithful to Adam. Meanwhile, God sends three angels to stop her. The angels tell her that if she does not return, they will kill one of her children every day, and if she does not return and obey God and Adam, they will kill one of her children for every day he disobeys. Thereupon, she begins to kill the children of those descended from Adam and Eve. According to the tradition, she tries to kill men within 8 days of birth and girls within 20 days. The jinns believed to exist in the world today are said to have originated from the union of Adam and his sister Naama and Tuval Cain. Before Adam and Eve were cursed with limited life before leaving paradise, they were immortal. After that, God creates another wife whose name is unknown, and Adam watches this creation. He is very affected by what he sees and does not accept the new wife. Thirdly, he later puts Adam to sleep and creates Eve from his rib bone. Eve, being created from a part of Adam, is subject to him.\n\nThird word")
                word = words[2][0]
                result_3 = word_game(word)
                print()
            elif random_3 == words[2][1]:
                print("He known in the Latin West as Alpharabius, was an early Islamic philosopher and music theorist. He has been designated as Father of Islamic Neoplatonism, and the Founder of Islamic Political Philosophy\n\nThird word")
                word = words[2][1]
                result_3 = word_game(word)
                print()
            elif random_3 == words[2][2]:
                print("An extensive group of states or countries ruled over by a single monarch, an oligarchy, or a sovereign state.\n\nThird word")
                word = words[2][2]
                result_3 = word_game(word)
                
            print()
            print(f"Total Score: {result_1+result_2+result_3}")
            print("The game will close in 10 seconds after it ends.")
            time.sleep(10)
            break
        elif a == 2:
            print("Game is closing ...")
            break
        else:
            print("You entered a number other than 1 or 2, Please restart the game!!!")
            break
    except Exception:
        print("Please Enter 1 to start the game or Enter 2 to exit the game")   
