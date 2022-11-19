
def proportion_by_sport(data, olympcYear, sport, gender) :
    try:
        data = data.drop_duplicates(subset=['ID', 'Year', 'Sport'])
        data = data[(data['Year'] == olympcYear) & (data['Sex'] == gender)]
        return  len(data.loc[data['Sport'] == sport]) / len(data)
    except:
        return None