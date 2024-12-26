two_teams = ({'Smith': 34,'Wesson': 22,'Coleman': 45,'Abrahams': 19})
more_peopel = [{'Smith': 34,'Wesson': 22,'Coleman': 45,'Abrahams': 19,'Smith': 34,'Wesson': 22,'Coleman': 45,'Abrahams': 19, 'Brown': 50, 'Black': 10}]

first_team = sorted(list([key for key in two_teams if two_teams[key] > 40 or two_teams[key] < 20]))
second_team = sorted(list([key for key in two_teams if two_teams[key] <= 40 and two_teams[key] >= 20]))

print(two_teams)
print(first_team)
print(second_team)


# Původní "řešení"
def prvniPokus():
    for key, value in two_teams.items():
        if value > 40 or value < 20:
            first_team.append(key)
        else:
            second_team.append(key)



            