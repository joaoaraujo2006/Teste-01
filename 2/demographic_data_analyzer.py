import pandas as pd


def calculate_demographic_data(print_data=True):
    
    dados = pd.read_csv("2/adult.csv")

    race_count = dados['race'].value_counts()
    
    mens = dados[dados['sex'] == 'Male']
    average_age_men = round(mens['age'].mean(), 1)

    bachelors = dados['education'].value_counts(normalize=True)
    percentage_bachelors = round(bachelors['Bachelors'] * 100, 1)

    higher_education = dados[dados['education'].isin(['Doctorate', 'Bachelors', 'Masters'])]
    rich = len(higher_education[higher_education['salary'] == '>50K'])
    todos = len(dados)
    todosRicos = len(higher_education)
    higher_education_rich = round((rich / todosRicos) * 100, 1)

    lower_education = dados[~dados['education'].isin(['Doctorate', 'Bachelors', 'Masters'])]
    lower = len(lower_education[lower_education['salary'] == '>50K'])
    todosSemEd = len(lower_education)
    lower_education_rich = round((lower/todosSemEd) * 100, 1)

    min_work_hours = dados['hours-per-week'].min()
    min_works = len(dados[dados['hours-per-week'] == min_work_hours])
    rich_percentage = round((len(dados[(dados['hours-per-week'] == 1) & (dados['salary'] == '>50K')]) / min_works) * 100, 2)

    #limitado = dados[dados['salary'] == '>50K']
    #paises = limitado['native-country'].value_counts(normalize=True)
    
    limitado = dados[dados['salary'] == '>50K']
    ricos_por_pais = limitado['native-country'].value_counts()
    pessoas_por_pais = dados['native-country'].value_counts()
    paises = ricos_por_pais / pessoas_por_pais
    highest_earning_country = paises.idxmax()
    highest_earning_country_percentage = round(paises.max() * 100, 1)

    indianos = dados[(dados['native-country'] == 'India') & (dados['salary'] == '>50K')]
    topIndianos = indianos['occupation'].value_counts()
    top_IN_occupation = topIndianos.idxmax()

    if print_data:
        print("Número de representantes de cada raça:\n", race_count) 
        print("Idade média dos homens:", average_age_men)
        print(f"% que possuem curso de bacharelado: {percentage_bachelors}%")
        print(f"% de ensino avançado que ganham + de 50K: {higher_education_rich}%")
        print(f"% sem ensino avançado que ganham + de 50K: {lower_education_rich}%")
        print(f"Mínimo de horas trabalhadas: {min_work_hours} hours/week")
        print(f"% que trabalham o mínimo e ganham + de 50k: {rich_percentage}%")
        print("Que país tem a maior % que ganham + de 50k:", highest_earning_country)
        print(f"Qual a porcentagem?: {highest_earning_country_percentage}%")
        print("Identifique a ocupação que ganhe mais de 50K na India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

     # Read data from file
    df = None

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = None

    # What is the average age of men?
    average_age_men = None

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = None

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = None
    lower_education = None

    # percentage with salary >50K
    higher_education_rich = None
    lower_education_rich = None

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = None

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    rich_percentage = None

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None
