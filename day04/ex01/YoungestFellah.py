def youngest_fellah(data, olympicYear) :
    try :
        return {
            'yongestWoman' : data[(data['Year'] == olympicYear) & (data['Sex'] == 'F')]['Age'].min(),
            'yongestMan' : data[(data['Year'] == olympicYear) & (data['Sex'] == 'M')]['Age'].min()
            }
    except :
        return None