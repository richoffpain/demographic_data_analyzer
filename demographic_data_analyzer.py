import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult_data.csv')
    data = pd.DataFrame(df)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = data['race'].value_counts()
    #print(race_count)
    # see how many men they are in the data set
    men = data[data['sex'] == 'Male']
    total_men = len(men)
    #hombres = data['sex'].value_counts().get('Male')
    #print(hombres)
    #print(total_men)
    # What is the average age of men?
    age_men = men['age'].sum()
    average_age_men = round((age_men / total_men), 1)
    #print(average_age_men)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((data['education'].value_counts().get('Bachelors') / len(data)) * 100, 1)
    #print(percentage_bachelors)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    salario = data[data['salary'] == '>50K']
    #print(salario)
    higher_education = len(data[data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])])
    #print(higher_education)
    
  
    lower_education = len(data[~data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])])
    #print(lower_education)

    # percentage with salary >50K
    higher_education_rich = round((len(salario[salario['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]) / higher_education) *100, 1)
    #print(higher_education_rich)
    lower_education_rich = round((len(salario[~salario['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]) / lower_education) * 100, 1)
    #print(lower_education_rich)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = data['hours-per-week'].min()
    #print(min_work_hours)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(data[data['hours-per-week'] == min_work_hours])
    

    rich_percentage = len(salario[salario['hours-per-week'] == min_work_hours]) / num_min_workers * 100
    #print(rich_percentage)

    # What country has the highest percentage of people that earn >50K?
   
    """  #print(highest_earning_country)
        country_salary = data[['native-country', 'salary']]
        #print(country_salary)
        country_salary['salary'] = country_salary['salary'].apply(lambda x: 1 if x.strip() == '>50K' else 0)
        country_salary_sum = country_salary.groupby('native-country')['salary'].sum()
        highest_earning_salary = country_salary_sum.max()
        #print(highest_earning_salary)"""
    country_data = data['native-country'].value_counts()
    rich_country = data[data['salary'] == '>50K']['native-country'].value_counts()
    highest_earning_country = ((rich_country / country_data) * 100).idxmax()
    #print(highest_earning_country)
    #total_salary_sum = country_salary['salary'].sum()
    #print(total_salary_sum)
    highest_earning_country_percentage = round(((rich_country / country_data) * 100), 1).max()
    #print(highest_earning_country_percentage)

    # Identify the most popular occupation for those who earn >50K in India.
    total_indians = salario[salario['native-country'] == 'India']
    top_IN_occupation = total_indians['occupation'].value_counts().idxmax()

    #print(top_IN_occupation)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

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


