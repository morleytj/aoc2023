import sys


def parse_nums(filehandle):
    winning_nums = []
    my_nums = []
    card_nums = []
    for line in filehandle:
        l = line[5:].strip()
        cn,all_nums =l.split(':')
        card_nums.append(cn)
        p1, p2 = all_nums.strip().split('|')
        winning_nums.append(p1.strip().split())
        my_nums.append(p2.strip().split())
    return (winning_nums,my_nums,card_nums)


def calculate_ticket_value(wnums, mnums):
    res = 0
    for num in mnums:
        if num in wnums:
            if res==0:
                res=1
            else:
                res*=2
    return res


if __name__=="__main__":
    f = open(sys.argv[1])
    winnums, mynums, cns = parse_nums(f)
    print(winnums)
    print(mynums)
    print(cns)
    res = 0
    for i in range(len(winnums)):
        res+=calculate_ticket_value(winnums[i], mynums[i])
    print(res)
    f.close()
