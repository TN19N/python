def how_many_medals_by_country(data, countryName):
    data = data[(data.Team == 'United States') & (data['Medal'].isnull() == False)]
    data = data.drop_duplicates(['Year', 'Sport', 'Medal'])

    res = {}
    for year in sorted(data.Year.unique()) :
        medals = {'G': 0, 'S': 0, 'B': 0}
        for medal in data[data['Year'] == year].Medal :
            medals[medal[0]] += 1
        res[year] = medals
    return res