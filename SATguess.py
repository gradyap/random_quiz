import random
#setting variables
ranwins = 0
conwins = 0
ties = 0
takes = 1000
for quiz in range (0, takes):
    rancorrect=0
    ranincorrect=0
    concorrect=0
    conincorrect=0
    revisions=1000
    possible = 4

# the consistent variable remains constant through the entire sequence
# and is compared to the same set of random answers as the random user
    consistent = random.randint(1,possible)

    for iteration in range (0,revisions):
        question = random.randint(1,possible)
        answer = random.randint(1,possible)
        if question == answer:
            rancorrect += 1
        if consistent == answer:
            concorrect += 1

        #r = 100*(float(rancorrect)/float(revisions))
        #c = 100*(float(concorrect)/float(revisions))

    #print ("The random user is correct {:.1f} percent of the time".format(r))
    #print ("The consisent user is correct {:.1f} percent of the time".format(c))
    #print ("The random user's score was {}/{}".format(rancorrect,revisions))
    #print ("The consistent user's score was {}/{}".format(concorrect,revisions))

    if rancorrect > concorrect:
        ranwins += 1
    if concorrect >rancorrect:
        conwins += 1
    elif concorrect == rancorrect:
        ties += 1
if ranwins > conwins:
    print ("it is better to answer randomly {:.1f}% of the time".format(100*(float(ranwins)/float(takes - ties))))
if conwins > ranwins:
    print ("it is better to answer consistently {:.1f}% of the time".format(100*(float(conwins)/float(takes - ties))))
print ("In a total of {} quizzes with {} questions each:".format(takes, revisions))
print ("Random Answer Wins: {}".format (ranwins))
print ("Consistent Answer Wins: {}".format (conwins))
print ("Ties: {}".format(ties))
