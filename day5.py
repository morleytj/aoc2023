import sys

def travel_maps(amaps,starts):
    ends = []
    for start in starts:
        curr_position=start
        for bmap in amaps:
            #check if start_p1<=start<start_p1+len, if it is we have found the path and move to the next
            #if we don't have a valid mapping, curr_position stays the same and we just go to the next map
            for entry in bmap:
                if entry[1]<=curr_position and curr_position<(entry[1]+entry[2]):
                    #found path, now get new curr_position using this map
                    #get difference between curr_position and entry[1], apply that to the entry[0] to get new position
                    curr_position = entry[0]+(curr_position-entry[1])
                    break
        ends.append(curr_position)
    return ends

#seed_to_soil.txt soil_to_fert.txt fert_to_water.txt  water_to_light.txt light_to_temp.txt temp_to_hum.txt hum_to_loc.txt
if __name__=='__main__':
    #first, enter all the seeds and all the maps
    seeds = [202517468, 131640971, 1553776977, 241828580, 1435322022, 100369067, 2019100043, 153706556, 460203450, 84630899, 3766866638, 114261107, 1809826083, 153144153, 2797169753, 177517156, 2494032210, 235157184, 856311572, 542740109]
    all_maps = []
    for mapfile in ['seed_to_soil.txt','soil_to_fert.txt','fert_to_water.txt','water_to_light.txt','light_to_temp.txt','temp_to_hum.txt','hum_to_loc.txt']:
        f = open(mapfile,'r')
        this_map = []
        for line in f:
            l = line.strip().split()
            this_map.append([int(x) for x in l])
        f.close()
        all_maps.append(this_map)
    #all maps entered, now traverse it
    #each map is a list of lists, where inner lists are (start_p2, start_p1, len)
    res=travel_maps(all_maps,seeds)
    print(res)
    print(min(res))
