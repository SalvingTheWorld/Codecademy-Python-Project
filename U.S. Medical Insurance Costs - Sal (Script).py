#Importing the CSV
import csv
#Importing the defaultdict library from the collections module
from collections import defaultdict

#Creating the lists for all the data that will be analyzed
ages = []
sexes = []
bmis = []
num_children = []
smoker_status = []
regions = []
insurance_charges = []

#Function that opens the dataset and populates all data into the variables
def load_list_file(dataList, csv_file, column_name):
    with open(csv_file) as csv_data:
        csv_dict = csv.DictReader(csv_data)
        for row in csv_dict:
            dataList.append(row[column_name])
        return dataList

#Loading all the data from the dataset to their respective lists
load_list_file(ages, 'insurance.csv', 'age')
load_list_file(sexes, 'insurance.csv', 'sex')
load_list_file(bmis, 'insurance.csv', 'bmi')
load_list_file(num_children, 'insurance.csv', 'children')
load_list_file(smoker_status, 'insurance.csv', 'smoker')
load_list_file(regions, 'insurance.csv', 'region')
load_list_file(insurance_charges, 'insurance.csv', 'charges')

#Function that checks all the individuals' age average
def avg_age(ages):
    total_age = 0

    for age in ages:
        total_age += int(age)

    avg_age = round(total_age / len(ages))
    return avg_age

#Displaying the average of all the individuals' ages
result_avg_age = avg_age(ages)
print("--- The age average of all individuals ---\n")
print(f"The age average of all individuals is {result_avg_age} years old")

#Function that finds the regions of all the individuals and list them
def region_finder(regions):
    individuals_regions = []

    for region in regions:
        if region not in individuals_regions:
            individuals_regions.append(region)
    return individuals_regions

#Displaying all the regions the individuals are from
people_regions = region_finder(regions)

print(f"These are the regions for all the individuals on the dataset:\n")
for new_region in people_regions:
    print("- " + new_region.capitalize())

#Function that analyzes the insurance cost differences between northeast and northwest regions

def diff_cost_region(regions, insurance_cost):
    insurance_cost_per_region = defaultdict(list)

    for reg, cost in zip(regions, insurance_cost):
        insurance_cost_per_region[reg].append(float(cost))

    list_northeast = [value for value in insurance_cost_per_region.get('northeast', [])]
    list_northwest = [value for value in insurance_cost_per_region.get('northwest', [])]
    
    #Calculate the mean insurance cost for the northeast region
    northeast_mean = sum(list_northeast) / len(list_northeast)

    #Calculate the mean insurance cost for the northwest region
    northwest_mean = sum(list_northwest) / len(list_northwest)

    #Calculating the northeast and northwest cost difference.
    percentage = ((northeast_mean - northwest_mean) / northwest_mean) * 100

    return northeast_mean, northwest_mean, percentage    

#Displaying the results of the insurance cost difference between northeast and northwest
ne_mean, nw_mean, percentage = diff_cost_region(regions, insurance_charges)

print("--- Insurance cost difference between the Northeast and Northwest region ---\n")

if percentage > 0:
    print(f"The insurance cost difference between the Northeast and Northwest regions is {percentage:.2f}%, with the Northeast region being higher.")
elif percentage < 0:
    print(f"The insurance cost difference between the Northeast and Northwest regions is {abs(percentage):.2f}%, with the Northeast region being lower.")
else:
    print("There are no cost differences between both regions as they have the same average insurance cost")

#Function that creates a dictionary with all the individuals information
def create_dict(age, sex, bmi, num_children, smoker_status, regions, insurance_cost):
    headers = ["age", "sex", "bmi", "children", "smoker", "region", "charges"]
    values = [age, sex, bmi, num_children, smoker_status, regions, insurance_cost]

    individual_dict = {header: values for header, values in zip(headers, values)}

    return individual_dict

individuals_dict = create_dict(ages, sexes, bmis, num_children, smoker_status, regions, insurance_charges)
# print(individuals_dict)

#Function that calculates the number of male and female individuals on the dataset
def check_individuals_sex(sexes):
    male = 0
    female = 0

    for sex in sexes:
        if sex == 'female':
            female += 1
        elif sex == 'male':
            male += 1
    print(f"The total number of male individuals is {male}")
    print(f"The total number of female individuals is {female}")    

#Outputing the number of the individuals of each sex from the dataset
print("--- Number of males and females individuals ---\n")
check_individuals_sex(sexes)

#Function that calculates the insurance cost between smokers and non-smokers
def ins_cost_smokers(smoker_status, insurance_cost):
    costs_by_smoker = defaultdict(list)

    for status, charge in zip(smoker_status, insurance_cost):
        costs_by_smoker[status].append(float(charge))
    
    smokers = {smoker for smoker in costs_by_smoker.get('yes', [])}
    non_smokers = {smoker for smoker in costs_by_smoker.get('no', [])}

    #Calculate the insurance cost mean for smokers
    mean_smokers = sum(smokers) / len(smokers)

    #Calculate the insurance cost mean for non-smokers
    mean_non_smokers = sum(non_smokers) / len(non_smokers)

    #calculating percentage difference of insurance cost between smokers and non-smokers
    diff_percentage_smokers = ((mean_smokers - mean_non_smokers) / mean_non_smokers) * 100

    return mean_smokers, mean_non_smokers, diff_percentage_smokers

#Displaying the results of the insurance cost difference between smokers and non-smokers
smokers_mean, non_smokers_mean, diff_pct = ins_cost_smokers(smoker_status, insurance_charges)

print("--- Insurance cost difference between Smokers and Non-smokers ---\n")

if diff_pct > 0:
    print(f"Smoker individuals pay, on average, {diff_pct:.2f}% more than non-smoker individuals")
elif diff_pct < 0:
    print(f"Smoker individuals pay, on average, {diff_pct:.2f}% less than non-smoker individuals")
else:
    print("There are no differences in cost between both groups.")