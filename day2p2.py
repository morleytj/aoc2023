import sys


def max_game(game):
    pulls = game.split(',')
    g_max=0
    r_max=0
    b_max=0
    for p in pulls:
        p=p.strip()
        if 'red' in p:
            r_max = max(int(p[:-3].strip()),r_max)
        elif 'green' in p:
            g_max = max(int(p[:-5].strip()),g_max)
        elif 'blue' in p:
            b_max = max(int(p[:-4].strip()),b_max)
        else:
            print('error! should not see this!!!!')
    return [r_max,g_max,b_max]


'''
need to remove text before colon before passing to function, extract id number
Input:
    line: a line of format "comma separated values by color, semicolon separating each trial
'''
def get_power(line):
    games = line.split(';')
    maxes = [0,0,0]
    for g in games:
        t_maxes = max_game(g)
        for i in [0,1,2]:
            maxes[i]=max(maxes[i],t_maxes[i])
    return maxes[0]*maxes[1]*maxes[2]



if __name__=="__main__":
    f = open(sys.argv[1],'r')
    res_sum = 0
    for line in f:
        #get id number
        p1, p2 = line.split(':')
        #pass remainder of line to function
        res_sum+=get_power(p2)
    print(res_sum)
