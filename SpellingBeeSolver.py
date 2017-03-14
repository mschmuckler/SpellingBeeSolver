# This program produces all of the answers for the Spelling Bee game by Frank Longo in the New York Times Magazine.
# The rules of Spelling Bee are as follows:
#
# "How many common words of 5 or more letters can you spell using the letters in the hive?
# Every answer must use the center letter at least once. Letters may be reused in a word.
# At least 1 word will use all 7 letters. Proper names and hyphenated words are not allowed.
# Score 1 point for each answer, and 3 points for a word that uses all 7 letters."
#
# Sidenote: this program can accept more or less than 7 letters when setting parameters.
# Written by Matthew Schmuckler, January 2017


#Sets up the letters of the game.
def inputLetters():
    while True:
        center = input("Enter the center letter: ").lower().strip()
        if center.isalpha() and len(center) == 1:
            break
        else:
            print("Only a single, alphabetical letter is allowed.", end=" ")

    while True:
        rules = input("Enter all letters (including the center letter): ").lower().replace(' ','')
        if rules.isalpha():
            break
        else:
            print("Only alphabetical letters are allowed.", end=" ")

    return center, rules


#Contains the center letter?
def containsCenter(word_list,center_letter):
    refine_list1 = []

    for word in word_list:
        center_count = 0
        for letter in word:
            if letter == center_letter:
                center_count += 1
        if center_count > 0:
            refine_list1.append(word)

    return refine_list1


#Contains at least 5 letters?
def containsFive(word_list):
    refine_list2 = []

    for word in word_list:
        if len(word) >= 5:
            refine_list2.append(word)

    return refine_list2


#Each letter is in the 'rule_list'?
def containsRules(word_list, rules):
    refine_list3 = []

    def containsOnly(test_word, test_rules):
        for letter in test_word:
            if letter not in test_rules:
                return False
        return True

    for word in word_list:
        if containsOnly(word, rules):
            refine_list3.append(word)

    return refine_list3

#Prints out the answers and score, with 3 point answers printed last.
def print_answers(word_list, rules, points):

    def containsAll(word, rules):
        return not set(rules).difference(word)

    print("-----------")
    print("All 1 point words:\n")
    for word in word_list:
        if not containsAll(word, rules):
            points += 1
            print(word)
    print("-----------")

    print("All 3 point words:\n")
    for word in word_list:
        if containsAll(word, rules):
            points += 3
            print(word)
    print("-----------")

    print("Total score: {}".format(points))

english_dictionary = open("DictionaryList1.txt").read().split()

score = 0

centerLetter, rule_list = inputLetters()

final_words = containsRules(containsFive(containsCenter(english_dictionary,centerLetter)),rule_list)

print_answers(final_words, rule_list, score)