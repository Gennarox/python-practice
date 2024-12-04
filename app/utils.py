def get_population():
  keys = ['col', 'ven']
  values = [100, 200]

  return keys, values


def population_by_country(data, country):
  result = list(filter(lambda item: item['country'] == country, data))
  return result
