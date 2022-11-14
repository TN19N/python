kata = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf'
}

if __name__ == '__main__' :
    print(*[f'{key} was created by {kata[key]}' for key in kata], sep='\n')