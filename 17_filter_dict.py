matchets = [
  {
    'home_team':'Colombia',
    'away_team':'Venezuela',
    'home_team_score':1,
    'away_team_score':1,
    'home_team_result':'Draw'
  },
  {
    'home_team':'Brazil',
    'away_team':'Mexico',
    'home_team_score':5,
    'away_team_score':0,
    'home_team_result':'Win'
  },
  {
    'home_team':'Argentina',
    'away_team':'Paraguay',
    'home_team_score':1,
    'away_team_score':3,
    'home_team_result':'Lose'
  }
]

print(matchets)
print(len(matchets))

results = list(filter(lambda winner : winner['home_team_result'] == 'Win',matchets))

print(results)
print(len(results))

#No se modifica el array original, no como map (donde hay que usar .copy)
print(matchets)
print(len(matchets))