import utils
import read_csv
import charts
import pandas as pd

def run():
    
    '''
    Primer reto graficar la poblacion de un pais en diferentes
    periodos de tiempo
    '''

    data = read_csv.read_csv("data.csv")
    country = input('Type Country => ')
    result = utils.population_by_country(data, country)
    name_country = country

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values, name_country)
        #print(labels, values)
    
    
    '''
    Segundo reto: Graficar esta columna contra los paises
    '''
    if len(data) > 0:
        
        ##Usando lambda
        #data = list(filter(lambda x: x['Continent'] == 'South America', data))
        #country_list = list(map(lambda x: x['Country'], data))
        #population_list = list(map(lambda x: x['World Population Percentage'], data))
        #new_data = {keys: values for keys, values in zip(country_list, population_list)}
        #labels = new_data.keys()
        #values = new_data.values()

        #Usando pandas
        df = pd.read_csv('data.csv')
        df = df[df['Continent'] == 'Africa']
        labels = df['Country'].values
        values = df['World Population Percentage'].values

        charts.generate_pie_chart(labels, values)


if __name__ == '__main__':
    run()