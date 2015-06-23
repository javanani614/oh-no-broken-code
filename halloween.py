# I can't be bothered to think of a Hallowe'en costume so
# can you help me generate one randomly?
import random

nouns = []
adjectives = []

with open('things.txt') as f:
    # We don't want those stinky \n newline characters
    # so we call strip() before adding it to our nouns list.
    for line in f:
        nouns.append(line.strip())


with open('descriptors.txt') as f:
    for line in f:
        adjectives.append(line.strip())


def generate_costume():

    # pick something random from the nouns and adjectives list
    pickanum = random.randrange(len(nouns))
    
    noun = nouns[pickanum]
    pickanum = random.randrange(len(adjectives))
    adj = adjectives[pickanum]
    
    return (noun, adj)


while True:
    (noun, adjective) = generate_costume()
    n = ''
    if adjective[0] in ['a', 'e', 'i', 'o', 'u']:
         n = 'n'
    print "You go dressed as a{} {} {} to the party.".format(n, adjective, noun)  

    happy = raw_input("Are you happy with this choice? ")

    # Check if the user typed something like 'yes' or 'y' and
    # quit the program if they are happy.
    if happy in ['y', 'yes', 'sure', 'good enough', 'ok']:   
        exit()
    else:
        print "OK, I will choose another costume. Hold on..."
        print