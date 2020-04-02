import os
import names
import secrets
import pandas as pd
import multiple_seat_ranking_methods
from models import Candidate, Ballot
import glob

def generate_candidates(numCandidate):
    candidates = []
    for i in range(numCandidate):
        tempName = names.get_full_name()
        while (tempName in candidates):
            tempName = names.get_first_name()
        candidates.append(tempName)

    return candidates

def generate_ballot(numCandidate, numSeats, r = False):
    ballot = ['']*numCandidate
    choices = ('').join([str(i) for i in list(range(numCandidate))])
    if r == True:
        temp = int(numCandidate/2)
        if int(numCandidate%2) != 0:
            temp += 1
        n = secrets.randbelow(numCandidate-temp+1)+temp
    else:
        n = numSeats


    for i in range(n):
        temp = secrets.choice(choices)
        index = int(temp)

        while (ballot[index] != ''):
            temp = secrets.choice(choices)
            index = int(temp)
        
        ballot[index] = str(int(i)+1)
    
    return ballot

def write_ballots(ballots, fileName):
    f = open(fileName, 'a')

    for b in ballots:
        f.write('\n'+','.join(b))

    f.close()


def write_ballots_to_files(ballots, files, numFiles, numBallots):
    if numFiles > 1:
        if (numFiles == numBallots):
            for i in range(numFiles):
                write_ballots(list([ballots[i]]), files[i])
        else:
            partition = []

            for i in range(numFiles-1):
                temp = secrets.randbelow(numBallots-2)+1

                while (temp in partition):
                    temp = secrets.randbelow(numBallots-2)+1
                
                partition.append(temp)
            
            partition = sorted(partition)
            # print(partition)
            
            for i in range(numFiles):
                if i == 0:
                    curBallots = ballots[0: partition[0]]
                elif i == numFiles-1:
                    curBallots = ballots[partition[i-1]: numBallots]
                else:
                    curBallots = ballots[partition[i-1]: partition[i]]
                
                write_ballots(curBallots, files[i])
    else:
        write_ballots(ballots, files[0])

def run_plurality(ballots, candidates, numCandidate, numBallots):
    count = [0]*numCandidate
    for b in ballots:
        pick = b.index('1')
        count[pick] += 1

    percentage = []
    for c in count:
        percentage.append(round(c/numBallots, 4))

    maxP = max(percentage)
    maxIdx = []
    for i in range(numCandidate):
        if percentage[i] == maxP:
            maxIdx.append(i)

    winnerIdx = secrets.randbelow(len(maxIdx))
    winner = list([candidates[maxIdx[winnerIdx]], str(percentage[maxIdx[winnerIdx]])])
    losers = []
    for i in range(numCandidate):
        if i != maxIdx[winnerIdx]:
            losers.append(list([candidates[i], str(percentage[i])]))

    return winner, losers

def run_STV(ballots, numSeats, candidates):
    c = []
    b = []
    for i in candidates:
        c.append(Candidate(i))
    
    ba = ballots[0]
    for ba in ballots:
        tempb = []
        for i in range(int(max(ba))):
            for j in range(len(ba)):
                if ba[j] == str(i+1):
                    tempb.append(c[j])
        # print(ba)
        # print(tempb)
        # print(Ballot(ranked_candidates = tempb))
        # print("======================================")
        b.append(Ballot(ranked_candidates = tempb))
    
    election_result = multiple_seat_ranking_methods.single_transferable_vote(c, b, number_of_seats=numSeats)
    return election_result

def create_plurality_test_files(numCandidate, numBallots, testFileName, numFiles):
    # create files
    if (numFiles <= 0):
        print("Number of test files is less than or equal to 0. Please enter a positive number.")
        return
    
    if (numBallots < numFiles):
        print("Number of ballotes cannot be less than number of files. Please enter again.")
        return

    if os.path.isdir(os.path.join(os.getcwd(), str(testFileName))) != True:
        os.makedirs(os.path.join(os.getcwd(), str(testFileName)))
    else:
        print("Test file directory " + str(testFileName) +  " already existed. Please call funtion again and enter a new test file name.")
        return
    
    files = []
    for i in range(numFiles):
        filePath = os.path.join(os.getcwd(), testFileName, testFileName + "_" + str(i+1) +".csv")
        if os.path.exists(filePath):
            print("Test file " + str(filePath) +  " already existed. Please call funtion again and enter a new test file name.")
            return
        else:
            files.append(filePath)
    
    # generate candidates
    candidates = generate_candidates(numCandidate)

    # write candidates to test file
    candidatesStr = ','
    candidatesStr = candidatesStr.join(candidates)
    for fileName in files:
        f = open(fileName, "a")
        f.write(candidatesStr)
        f.close()

    # generate ballots
    ballots = []
    for i in range(numBallots):
        tempBallot = generate_ballot(numCandidate, 1, False)
        ballots.append(tempBallot)

    # write ballots into test files
    write_ballots_to_files(ballots, files, numFiles, numBallots)

    # compute plurality voting result
    winner, losers = run_plurality(ballots, candidates, numCandidate, numBallots)

    resultFileName = os.path.join(os.getcwd(), str(testFileName), str(testFileName) + "_result.csv")
    f = open(resultFileName, 'a')
    f.write("Winners:\n")
    f.write(' : '.join(winner))
    f.write("\nLosers:")
    for l in losers:
        f.write('\n'+" : ".join(l))
    f.close()

def create_STV_test_files(numCandidate, numBallots, numSeats, testFileName, numFiles):
    if numSeats > numCandidate:
        print("Number of seats is greater than the number of candidates. Please enter again.")
        return

    if numSeats <= 0:
        print("Number of seats is less than equal to 0. Please enter again.")
        return
    
    # create files
    if (numFiles <= 0):
        print("Number of test files is less than or equal to 0. Please enter a positive number.")
        return
    
    if (numBallots < numFiles):
        print("Number of ballotes cannot be less than number of files. Please enter again.")
        return

    if os.path.isdir(os.path.join(os.getcwd(), str(testFileName))) != True:
        os.makedirs(os.path.join(os.getcwd(), str(testFileName)))
    else:
        print("Test file directory " + str(testFileName) +  " already existed. Please call funtion again and enter a new test file name.")
        return
    
    files = []
    for i in range(numFiles):
        filePath = os.path.join(os.getcwd(), testFileName, testFileName + "_" + str(i+1) +".csv")
        if os.path.exists(filePath):
            print("Test file " + str(filePath) +  " already existed. Please call funtion again and enter a new test file name.")
            return
        else:
            files.append(filePath)
    
    # generate candidates
    candidates = generate_candidates(numCandidate)

    # write candidates to test file
    candidatesStr = ','
    candidatesStr = candidatesStr.join(candidates)
    for fileName in files:
        f = open(fileName, "a")
        f.write(candidatesStr)
        f.close()

    # generate ballots
    ballots = []
    for i in range(numBallots):
        tempBallot = generate_ballot(numCandidate, numSeats, True)
        ballots.append(tempBallot)

    # write ballots into test files
    write_ballots_to_files(ballots, files, numFiles, numBallots)

    # generate results
    STV(testFileName, numSeats)
    # result = run_STV(ballots, numSeats, candidates)

    # resultFileName = os.path.join(os.getcwd(), str(testFileName), str(testFileName) + "_result.csv")
    # f = open(resultFileName, 'a')
    # f.write(str(result))
    # f.close()

def STV(dirName, numSeats):
    dirPath = os.path.join(os.getcwd(), dirName)
    if os.path.isdir(dirPath) == False:
        print('The directory does not exist.')
    
    fileNames = glob.glob(os.path.join(dirPath, '*'))

    candidates = []
    ballots = []
    f = open(fileNames[0], 'r')
    data = f.readline()
    candidates = data.replace('\n', '').split(',')
    f.close()
    # print(candidates)

    for name in fileNames:
        f = open(name, 'r')
        data = f.readlines()
        data = data[1:]
        temp = []
        for d in data:
            temp = d.replace('\n', '').split(',')
            ballots.append(temp)
    
    # print(ballots)
    # generate results
    # run_STV(ballots, numSeats, candidates)
    result = run_STV(ballots, numSeats, candidates)

    resultFileName = os.path.join(os.getcwd(), str(dirName), str(dirName) + "_result.csv")
    f = open(resultFileName, 'a')
    f.write(str(result))
    f.close()