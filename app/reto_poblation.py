import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    #print(data[0])

    #reto filtar año y poblacion
    new_dict = []
    for item in data:
        list_anio = []
        list_poblation = []
        for key, values in item.items():
            if key[0] == '1' or key[0] == '2':
                list_anio.append(key[:4])
                list_poblation.append(int(values))

        new_dict.append({list_an: list_pob for list_an, list_pob in zip(list_anio, list_poblation)})
    print(new_dict)

  #print(result_filters)

