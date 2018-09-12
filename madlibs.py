# Error Handling, Edge cases, Multiple categories,

import random
import time

print("Welcome to Nathan's MadLibs. Read the following prompt and fill in the blanks. \n")

user_story = ""
name = ""
first_verb = ""
noun_list = list()
adj_list = list()
verb_list = list()

noun_count = 0
adj_count = 0
verb_count = 0


def check_for_errors(word):
    while word.isalpha() == False:
        word = raw_input("input must contain letters, please enter your word again: ")
    while word.isspace():
        word = input("No whitespace allowed! Try Again: ")


def default_story():
    name = input("Name of your character?")
    check_for_errors(name)
    first_noun = input("First Noun?")
    check_for_errors(first_noun)
    first_adjective = input("First Adjective?")
    check_for_errors(first_adjective)
    second_noun = input("Second Noun?")
    check_for_errors(second_noun)
    second_adjective = input("Second Adjective?")
    check_for_errors(second_adjective)
    third_noun = input("Third Noun?")
    check_for_errors(third_noun)
    first_verb = input("First Verb?")
    check_for_errors(first_verb)

    noun_list.append(first_noun)
    noun_list.append(second_noun)
    noun_list.append(third_noun)
    adj_list.append(first_adjective)
    adj_list.append(second_adjective)
    verb_list.append(first_verb)
#
# def write_your_own():
#     print("Writing your own story:")
#     print("Write your story and enter your special words with the shorthand code (see below) for nouns, adjectives, or verbs")
#     print("Nouns: NOUN")
#     print("Adjectives: ADJ")
#     print("Verbs: VERB")
#
#     user_story = input("Enter your story here: ")
#
#     noun_count = 0
#     adj_count = 0
#     verb_count = 0
#
#     noun_list = list()
#     adj_list = list()
#     verb_list = list()
#
#     spilt_user_story = user_story.split(" ")
#     print(spilt_user_story)
#     for word in spilt_user_story:
#         if spilt_user_story.contain("NOUN"):
#             noun_count += 1
#             noun_list.append(word)
#         if spilt_user_story.contain("ADJ"):
#             adj_count += 1
#             adj_list.append(word)
#         if spilt_user_story.contain("VERB"):
#             verb_count += 1
#             verb_list.append(word)



# def shuffle_list():
#     for noun in noun_list:
#         rand_index = randint(0, len(noun_list) - 1)
#         noun_list.pop(rand_index)




default_story()
# write_your_own()

random.shuffle(noun_list)
random.shuffle(adj_list)
# random.shuffle(verb_list)


def test():
    print(noun_list)
    print(adj_list)
    print(verb_list)

    print(noun_count)
    print(adj_count)
    print(verb_count)

test()


# print("Processing... \n")
# time.sleep(2)


print("%s was taking a walk with his %s on a Sunday morning. %s was making his way to the bakery when a %s %s crossed his path. %s took out his %s and %s %s!" % (name, noun_list[0],name, adj_list[1], noun_list[1], name, noun_list[2], first_verb, noun_list[1]))
