import sys

#take a string, find the first occurring number and the last occurring number, and then append them and return it
def get_calibrate(line):
    first = None
    last = None
    firstdigitenc = False
    for char in line:
        if char in ["0","1","2","3","4","5","6","7","8","9"]:
            if firstdigitenc:
                last = char
            else:
                #we are encountering a digit for the first time
                first = char
                last = char
                firstdigitenc=True
    res = first+last
    return int(res)

def find_l_strnums(line):
    n="-1"
    n_ind=-1
    for strnum in ['one','two','three','four','five','six','seven','eight','nine']:
        temp=line.lower().rfind(strnum)
        if temp>n_ind:
            n_ind=temp
            n=strnum
    return (n,n_ind)

def find_strnums(line):
    earliest_num="-1"
    earliest_num_index=-1
    first_enc=False
    for strnum in ['one','two','three','four','five','six','seven','eight','nine']:
        temp=line.lower().find(strnum)
        if first_enc:
            if temp>-1:
                if earliest_num_index>temp:
                    earliest_num=strnum
                    earliest_num_index=temp
        else:
            if temp>-1:
                earliest_num=strnum
                earliest_num_index=temp
                first_enc=True
    return (earliest_num,earliest_num_index)

def find_numnums(line):
    first = "-1"
    last = "-1"
    f_index = -1
    l_index = -1
    firstdigitenc = False
    index = 0
    for char in line:
        if char in ["0","1","2","3","4","5","6","7","8","9"]:
            if firstdigitenc:
                last = char
                l_index=index
            else:
                first = char
                last = char
                f_index=index
                l_index=index
                firstdigitenc=True
        index+=1
    return (first, last, f_index, l_index)

def translate_strnum(num):
    mapping={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    return mapping[num]


#modify get_calibrate to return the indices as well, then strnums, compare indices to find which is earlier
def get_calibrate_p2(line):
    e_strnum, e_strnum_index = find_strnums(line)
    l_strnum, l_strnum_index = find_l_strnums(line)
    f_num, l_num, f_index, l_index = find_numnums(line)
    res=None
    earl = None
    late = None
    #check for negs
    if e_strnum=="-1":
        earl = f_num
        late = l_num
    elif f_num=="-1":
        earl=str(translate_strnum(e_strnum))
        late=str(translate_strnum(l_strnum))
    else:
        #find earliest index
        if e_strnum_index<f_index:
            #strnum earlier
            earl = str(translate_strnum(e_strnum))
        else:
            #numnum earlier
            earl = f_num
        #find latest index
        if l_strnum_index>l_index:
            #strnum last
            late = str(translate_strnum(l_strnum))
        else:
            late = l_num
    res = str(earl)+str(late)
    return int(res)


if __name__=="__main__":
    f = open(sys.argv[1],'r')
    cali_sum = 0
    for l in f:
        #cali_sum += get_calibrate(l)
        print('*********')
        print(l)
        print(get_calibrate_p2(l))
        cali_sum += get_calibrate_p2(l)
    f.close()
    print(cali_sum)
    print('qxtbbtwo7jrdgxlcpxbczxhnpjthreetwogcfl')
    print(find_numnums('qxtbbtwo7jrdgxlcpxbczxhnpjthreetwogcfl'))
    print(find_strnums('qxtbbtwo7jrdgxlcpxbczxhnpjthreetwogcfl'))
    print(find_l_strnums('qxtbbtwo7jrdgxlcpxbczxhnpjthreetwogcfl'))
