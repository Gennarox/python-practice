import utils

data = [{
    'country': 'colombia',
    'population': 100
}, {
    'country': 'bolivia',
    'population': 200
}]


def run():
  keys, values = utils.get_population()
  print(keys, values)

  country = input("De que pais necesitas la informacion de su poblacion? ->")
  print(utils.population_by_country(data, country.lower()))


if __name__ == '__main__':
  run(
  )  #si es ejecutado desde la terminal corre, si es llamado desde otro archivo no
