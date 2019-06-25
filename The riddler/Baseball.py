import random
import statistics
#defining variables
# of = out at first, fo = foul out, fout = fly out, dp = double play
random.seed(20)
play = ('double','single','single','single','single','single','single','be','be','bb','bb',
    'st','st','st','st','st','st','st','fo','fo','of','of','of','of','of','of','of',
    'fout','fout','fout','fout','fout','dp','trip','trip','Hr')
total_runs = 0
total_runs_games = []
#left to do: double play,
#The beginnings of the baseball game
print(len(play))

def inning(plays = play, outs = 0, strikes = 0, inning_runs = 0, bases = []):
    """this function plays one innning and reports its runs"""
    while(outs < 3):
        current_play = random.choice(plays)
        if(current_play == 'Hr' or current_play == 'trip'):
            inning_runs = inning_runs + len(bases)
            if(current_play == 'Hr'):
                inning_runs = inning_runs + 1
                bases = []
            if(current_play == 'trip'):
                bases = [3]
            strikes = 0

        elif(current_play == 'double'):
            if(2 in bases):
                inning_runs += 1
                bases.remove(2)
            if(3 in bases):
                inning_runs += 1
                bases.remove(3)
            if(1 in bases):
                bases.remove(1)
                bases.append(3)
            strikes = 0
            bases.append(2)
            bases.sort()

        elif(current_play == 'single' or current_play == 'be'):
            if(2 in bases):
                inning_runs += 1
                bases.remove(2)
            if(3 in bases):
                inning_runs += 1
                bases.remove(3)
            if(1 in bases):
                bases.remove(1)
                bases.append(2)
            strikes = 0
            bases.append(1)
            bases.sort()

        elif(current_play == 'bb'):
            if(1 in bases):
                if(2 in bases):
                    if(3 in bases):
                        inning_runs += 1
                        bases.remove(3)
                    bases.append(3)
                    bases.remove(2)
                bases.append(2)
                bases.remove(1)
            strikes = 0
            bases.append(1)
            bases.sort()

        elif (current_play == 'st'):
            strikes += 1
            if(strikes > 2):
                outs += 1
                strikes = 0

        elif(current_play == 'fo' or current_play == 'of' or current_play == 'fout' or current_play == 'dp'):
            outs += 1
            strikes = 0
            if(outs < 3):
                if(current_play == 'fout'):
                    if(3 in bases):
                        inning_runs += 1
                        bases.remove(3)
                if(current_play == 'of'):
                    if(3 in bases):
                        inning_runs += 1
                        bases.remove(3)
                    if(2 in bases):
                        bases.remove(2)
                        bases.append(3)
                    if(1 in bases):
                        bases.remove(1)
                        bases.append(2)

                if(current_play == 'dp'):
                    if bases:
                        outs+= 1
                    if(outs < 3):
                        if(1 in bases):
                            bases.remove(1)
                            if(3 in bases):
                                inning_runs += 1
                                bases.remove(3)
                            if(2 in bases):
                                bases.remove(2)
                                bases.append(3)
                        elif(2 in bases and 1 not in bases):
                            if(3 in bases):
                                inning_runs += 1
                                bases.remove(3)
                            bases.remove(2)
                        elif((3 in bases) and (1 not in bases) and (2 not in bases)):
                            bases = []
        bases.sort()
    return inning_runs
for i in range(10001):
    for i in range(1,19):
        total_runs += inning(bases = [])
    total_runs_games.append(total_runs)
    total_runs = 0

print(statistics.mean(total_runs_games))



