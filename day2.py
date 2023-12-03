import sys


def check_game(game, red_l, green_l, blue_l):
    pulls = game.split(',')
    for p in pulls:
        p=p.strip()
        if 'red' in p:
            if int(p[:-3].strip())>red_l:
                return False
        elif 'green' in p:
            if int(p[:-5].strip())>green_l:
                return False
        elif 'blue' in p:
            if int(p[:-4].strip())>blue_l:
                return False
        else:
            print('error! should not see this!!!!')
    return True


'''
need to remove text before colon before passing to function, extract id number
Input:
    line: a line of format "comma separated values by color, semicolon separating each trial
    red_l: limit of reds to check
    green_l: limit of greens
    blue_l: limit of blues
'''
def check_validity(line,red_l,green_l,blue_l):
    games = line.split(';')
    for g in games:
        if check_game(g,red_l,green_l,blue_l):
            pass
        else:
            return False
    return True


if __name__=="__main__":
    f = open(sys.argv[1],'r')
    rl = int(sys.argv[2])
    gl = int(sys.argv[3])
    bl = int(sys.argv[4])
    res_sum = 0
    for line in f:
        #get id number
        p1, p2 = line.split(':')
        idnum=int(p1[5:])
        #pass remainder of line to function
        if check_validity(p2,rl,gl,bl):
            res_sum+=idnum
    print(res_sum)
