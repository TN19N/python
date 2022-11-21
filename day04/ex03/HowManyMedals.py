
def how_many_medals(data, name) :
    data = data[data['Name'] == name]

    dec = {}
    for year in data['Year'] :
        mid = {'G': 0, 'S': 0, 'B': 0}
        for medel in data[data['Year'] == year]['Medal'] :
            if medel in ['Gold', 'Silver', 'Bronze'] : 
                mid[medel[0]] += 1
        dec[str(year)] = mid
    return dec