# Error Handling, Edge cases, Multiple categories,

import random
import time

print("Welcome to Nathan's MadLibs. Read the following prompt and fill in the blanks.")
print("")

def check_for_errors(word):

    while word.isalpha() == False:
        word = raw_input("Input must contain letters, please enter your word again: ")
    while word.isspace():
        word = raw_input("No whitespace allowed! Try Again: ")



name = raw_input("Name of your character?")
check_for_errors(name)
first_noun = raw_input("First Noun?")
check_for_errors(first_noun)
first_adjective = raw_input("First Adjective?")
second_noun = raw_input("Second Noun?")
second_adjective = raw_input("Second Adjective?")
third_noun = raw_input("Third Noun?")
first_verb = raw_input("First Verb?")

noun_list = [first_noun, second_noun, third_noun]
adj_list = [first_adjective, second_adjective]

random.shuffle(noun_list)
random.shuffle(adj_list)
random.shuffle(verb_list)


# def shuffle_list():
#     for noun in noun_list:
#         rand_index = randint(0, len(noun_list) - 1)
#         noun_list.pop(rand_index)


print("___name___ was taking a walk with his ___(noun)___ on a Sunday morning. ___name___ was making his way to the bakery when a ____adjective____ ____noun______ crossed his path. ____name____ took out his ___noun___ and  ___verb___ the ___noun____")

print("Processing...")
time.sleep(2)
print("")

print(name + "was taking a walk with his " + noun_list[0] + " on a Sunday morning. "+ name + " was making his wy to the bakery when a " + adj_list[1] + " " + noun_list[1] + "crossed his path. " + name + " took out his " + noun_list[2] + " and " + first_verb + " " + noun_list[1] + "!")