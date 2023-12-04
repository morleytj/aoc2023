import sys
import numpy as np

#need to read each line, whenever we detect a "symbol", keep track of the index it is at
#also keep track of each of the indices for runs of numbers in a dict
#at the end, for each run of numbers set the var to true if it has a symbol near it (go through each symbol and turn var to true for number


#so for this function, built a list of lists containing this
def build_matrix(filehandle):
    res = []
    for line in filehandle:
        res.append(line.strip())
    return res

def explore_paths(matrix):
    nums = dict()
    symbols = set()
    row = 0
    crun=''
    run_start=-1
    inrun = False
    for l in matrix:
        col = 0
        for c in l:
            if c in ['1','2','3','4','5','6','7','8','9','0']:
                #a number
                if inrun:
                    #continue run
                    crun+=c
                else:
                    #starting a new run
                    inrun=True
                    crun+=c
                    run_start=(row,col)
            else:
                #not a number
                if inrun:
                    #just finished a run
                    inrun = False
                    #nums will be accessed through index of end, contains (num, start)
                    nums[(row,col-1)]=(int(crun), run_start)
                    crun=''
                if c != '.':
                    #is a symbol
                    print((row,col,c))
                    symbols.add((row,col))
                else:
                    #is .
                    pass
            #increment col
            col += 1
        #increment row
        #need to do an ending check in case the last char is a number in the line
        if inrun:
            nums[(row,col)]=(int(crun), run_start)
            inrun=False
            crun=''
        row +=1
    return nums, symbols

def explore_paths_gears(matrix):
    nums = dict()
    gears = set()
    row = 0
    crun=''
    run_start=-1
    inrun = False
    for l in matrix:
        col = 0
        for c in l:
            if c in ['1','2','3','4','5','6','7','8','9','0']:
                #a number
                if inrun:
                    #continue run
                    crun+=c
                else:
                    #starting a new run
                    inrun=True
                    crun+=c
                    run_start=(row,col)
            else:
                #not a number
                if inrun:
                    #just finished a run
                    inrun = False
                    #nums will be accessed through index of end, contains (num, start)
                    nums[(row,col-1)]=(int(crun), run_start)
                    crun=''
                if c == '*':
                    #is a symbol
                    print((row,col,c))
                    gears.add((row,col))
                else:
                    #is not gear
                    pass
            #increment col
            col += 1
        #increment row
        #need to do an ending check in case the last char is a number in the line
        if inrun:
            nums[(row,col)]=(int(crun), run_start)
            inrun=False
            crun=''
        row +=1
    return nums, gears


def check_adjacent(gr,st,ed):
    #add sides
    adjacency=[(st[0],st[1]-1),(ed[0],ed[1]+1)]
    for i in range(st[1]-1,ed[1]+2):
        #add top
        adjacency.append((st[0]-1, i))
        #add bottom
        adjacency.append((st[0]+1, i))
    if gr in adjacency:
        return True
    else:
        return False

def sum_valid_gears(numbers, gears):
    res = 0
    #loop through all gears
    #find gears with only two numbers adjacent to it
    ##for those gears, multiple the two numbers and then add result to res
    for gear in gears:
        #gear is just a row,col tuple
        num_adjacent=0
        adj_nums = []
        for end, val in numbers.items():
            num, start = val
            #if gear adjacent to anything between start and end (inclusive), save num and increase num_adjacent
            if check_adjacent(gear,start,end):
                adj_nums.append(num)
                num_adjacent+=1
        if num_adjacent==2:
            res+=(adj_nums[0]*adj_nums[1])
    return res


def sum_valid_numbers(numbers, symbols):
    res = 0
    for key, value in numbers.items():
        #get start and end (and num)
        end = key
        num, start = value
        #build list of valid symbol locations using start and end of run -- consider edge cases of corners and sides
        tocheck = [(start[0],start[1]-1),(end[0],end[1]+1)]#add sides
        #add top
        for i in range(start[1]-1,end[1]+2):
            tocheck.append((start[0]-1, i))
            #add bottom
            tocheck.append((start[0]+1, i))
        #check if symbol locations are in symbols set
        oneSymb=False
        for location in tocheck:
            #add to res if at least one is
            if location in symbols:
                oneSymb=True
        print('****')
        print(tocheck)
        print((num,oneSymb))
        if oneSymb:
            res+=num
    return res


if __name__=='__main__':
    f = open(sys.argv[1],'r')
    matrix = build_matrix(f)
    ns, gears = explore_paths_gears(matrix)
    print(sum_valid_gears(ns,gears))
    #ns, syms = explore_paths(matrix)
    #print('matrix')
    #for l in matrix:
    #    print(l)
    #print('ns res below******')
    #print(ns)
    #print('****syms****')
    #print(syms)
    ##next i need to go through the symbols indices and compare to the number indices
    #print(sum_valid_numbers(ns,syms))
