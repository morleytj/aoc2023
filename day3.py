import sys
import numpy as np

#need to read each line, whenever we detect a "symbol", keep track of the index it is at
#also keep track of each of the indices for runs of numbers in a dict
#at the end, for each run of numbers set the var to true if it has a symbol near it (go through each symbol and turn var to true for number


#so for this function, built a list of lists containing this
def build_matrix(filehandle):
    res = []
    for line in filehandle:
        res.append(line)
    return res

def explore_paths(matrix):
    nums = dict()
    symbols = []
    row = 0
    col = 0
    crun=''
    run_start=-1
    inrun = False
    for l in matrix:
        for c in l:
            if c in ['1','2','3','4','5','6','7','8','9']:
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
                    nums[(row,col)]=(int(crun), run_start)
                    crun=''
                if c != '.':
                    #is a symbol
                    symbols.append((row,col))
                else:
                    #is .
                    pass
            #increment col
            col += 1
        #increment row
        row += 1
        #need to do an ending check in case the last char is a number in the line
        if inrun:
            crun+=c
            nums[(row,col)]=(int(crun), run_start)
            inrun=False
    return nums, symbols


if __name__=='__main__':
    f = open(sys.argv[1],'r')
    matrix = build_matrix(f)
    ns, syms = explore_paths(matrix)
    #print('matrix')
    #for l in matrix:
    #    print(l)
    #print('res below******')
    #print(ns)
    #print(syms)
