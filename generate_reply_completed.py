from linguistic import getPOS
from sentiment import getSentiment
import random

greetings = [ "hi", "hello", "hey", "yo", "greetings" ]
greetings_responses = [ "Hi there." , "Greetings human.", "Hello there.", "Hey." ]

# Returns JJ if sentence structure is You Are {word}+ JJ {word}+.
def findYouAreJJ(pos):
    foundYou = False
    foundYouAre = False

    for e in pos:
        if e[0].lower() == 'you':
            foundYou = True
        elif e[0].lower() == 'are' and foundYou:
            foundYouAre = True
        elif foundYou and not foundYouAre:
            foundYou = False
        elif foundYouAre and e[1] == 'JJ':
            return e[0]
    return False

# Generates a bot response from a user message
def generateReply(message):
    pos = getPOS(message)
    sentiment = getSentiment(message)

    # If error occurred getting POS
    if not pos:
        return "I am not functioning at the moment. Perhaps check your API keys."

    # If user greeted
    if pos[0][0].lower() in greetings:
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


# Returns JJ if sentence structure is I Am {word}+ JJ {word}+.
def findIAmJJ(pos):
    foundI = False
    foundIAm = False

    for e in pos:
        if e[0].lower() == 'i':
            foundI = True
        elif e[0].lower() == 'am' and foundI:
            foundIAm = True
        elif foundI and not foundIAm:
            foundI = False
        elif foundIAm and e[1] == 'JJ':
            return e[0]
    return False