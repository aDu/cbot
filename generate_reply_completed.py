from linguistic import getPOS
from sentiment import getSentiment
import random

greetings = [ "hi", "hello", "hey", "yo", "greetings" ]
greetings_responses = [ "Hi there." , "Greetings human.", "Hello there.", "Hey." ]

# Generates a bot response from a user message
def generateReply(message):
    pos = getPOS(message)
    sentiment = getSentiment(message)

    # If error occurred getting POS
    if not pos:
        return "I am not functioning at the moment."

    # If user greeted
    if pos[0][0] in greetings:
        return random.choice(greetings_responses)

    # If user said 'You are ... {adjective} ...'
    youAreJJ = findYouAreJJ(pos)   
    if youAreJJ:
        if sentiment >= 0.5:
            return "Thank you, I know I'm "+youAreJJ+"."
        else:
            return "No! I'm not "+youAreJJ+"!"

    # If user said 'I am ... {adjective} ...'
    IAmJJ = findIAmJJ(pos)   
    if IAmJJ:
        if sentiment >= 0.5:
            return "I'm happy for you that you're "+IAmJJ+"."
        else:
            return "Don't be mean on yourself. I'm sure you're not really "+IAmJJ+"!"

    if sentiment >= 0.5:
        return "I'm happy to hear that!"
    else:
        return "I feel sad about that."


# Returns JJ if sentence structure is You Are {word}+ JJ {word}+.
def findYouAreJJ(pos):
    foundYou = False
    foundAre = False

    for e in pos:
        if e[0].lower() == 'you':
            foundYou = True
            continue
        if e[0].lower() == 'are':
            foundAre = True
            continue
        if foundYou and not foundAre:
            return False
        if foundAre and e[1] == 'JJ':
            return e[0]
    return False

# Returns JJ if sentence structure is I Am {word}+ JJ {word}+.
def findIAmJJ(pos):
    foundYou = False
    foundAre = False

    for e in pos:
        if e[0].lower() == 'i':
            foundYou = True
            continue
        if e[0].lower() == 'am':
            foundAre = True
            continue
        if foundYou and not foundAre:
            return False
        if foundAre and e[1] == 'JJ':
            return e[0]
    return False