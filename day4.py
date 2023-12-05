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

def win_num(wnums, mnums):
    res = 0
    for num in mnums:
        if num in wnums:
            res+=1
    return res

def calculate_num_total_tickets(all_wnums, all_mnums, card_nums):
    #make dict to track number of each ticket we see, initialize with 1 of each to count originals
    card_dict = dict(zip(card_nums,[1 for x in card_nums]))
    #now traverse through from start and add to the next n card_nums based on number of wins
    for i in range(len(card_nums)):
        #get number of wins for the current card
        wins = win_num(all_wnums[i],all_mnums[i])
        #add current number of plays on this card to the next WIN_NUM cards
        for nw in range(wins):
            card_dict[str(i+2+nw)]+=card_dict[str(i+1)]
    return sum(card_dict.values())


if __name__=="__main__":
    f = open(sys.argv[1])
    winnums, mynums, cns = parse_nums(f)
    res = 0
    for i in range(len(winnums)):
        res+=calculate_ticket_value(winnums[i], mynums[i])
    print(res)
    f.close()
    print(calculate_num_total_tickets(winnums,mynums,cns))
