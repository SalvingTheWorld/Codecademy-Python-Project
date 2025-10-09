from collections import defaultdict

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

#Function that updates the damage numbers to float and store these new values into a new list
def updated_dmg(damage):
  damage_list_updated = []

  for dmg in damage:
    if dmg == "Damages not recorded":
      damage_list_updated.append(dmg)
    else:
      sufix = dmg[-1]
      num_str = dmg[:-1]
      num_float = float(num_str)
      multiplier = conversion[sufix]
      final_value = num_float * multiplier
      damage_list_updated.append(final_value)
  return damage_list_updated

#Storing the updated damage list to a new variable so it can be reused in the create hurricane dict function
damages_converted = updated_dmg(damages)

#Function that creates a new hurricane dictionary that combines all data about them
def create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages_converted, deaths):

  zipped_hurricane_data = zip(names, months, years, max_sustained_winds, areas_affected, damages_converted, deaths)

  hurricanes = { 
    name:{'Name': name,
      'Month': month,
      'Year': year,
      'Max Sustained Winds': max_wind,
      'Areas Affected': area,
      'Damages': dmg,
      'Deaths': death
    }
    for name, month, year, max_wind, area, dmg, death in zipped_hurricane_data 
  }
  return hurricanes

hurricanes = create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages_converted, deaths)

#Function that creates a new dictionary that organizes all hurricanes by year
def hurricanes_year(hurricanes):
  hurricane_year = {}

  for name, values in hurricanes.items():
    current_year = values['Year']
    if current_year not in hurricane_year:
      hurricane_year[current_year] = [values]
    else:
      hurricane_year[current_year].append(values)
  return hurricane_year

hurricane_by_year = hurricanes_year(hurricanes)


#Function that counts how often each area listed was affected by a hurricane
def affected_areas_count(hurricanes):
  affected_area_count = defaultdict(int)
  
  for name, value in hurricanes.items():
    for area in value['Areas Affected']:
      affected_area_count[area] += 1
  return affected_area_count

affected_areas = affected_areas_count(hurricanes)

print("----A list with the number of times each area was hit by a hurricane:----\n")

for area, count in sorted(affected_areas.items()):
  location = area
  num_times = count
  print(f" - The {location} was affected by a hurricane {num_times} time(s).")

#Function that checks the area affected by the most hurricanes and how often it was hit
def area_most_affected(affected_areas):
  max_area = ''
  max_area_count = 0

  for area_name, count in affected_areas.items():
    if max_area_count < count:
      max_area = area_name
      max_area_count = count
  return max_area, max_area_count

most_affected_area = area_most_affected(affected_areas)

location, num_times = most_affected_area
print("\n----The most affected location by hurricanes----")
print(f"The {location} was hit {num_times} time(s) by hurricanes.")


#Function that finds the deadliest hurricane and the number of deaths it caused
def num_deaths_hurricane(hurricanes):
  max_mortality_cane = ''
  max_mortality = 0

  for name, value in hurricanes.items():
    death_count = value["Deaths"]
    if max_mortality < death_count:
      max_mortality_cane = name
      max_mortality = death_count
  return max_mortality_cane, max_mortality

most_lethal_hurricane = num_deaths_hurricane(hurricanes)

hurricane_name, death_count = most_lethal_hurricane
print("\n----The deadliest hurricane----")
print(f"The {hurricane_name} was the deadliest hurricane by killing {death_count} people.\n")


#Function that rates on a mortality scale (0 to 4) the deadliest hurricanes and returns a dictionary by rating
def hurricane_rating_mortality(hurricanes):
  mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
  hurricanes_by_mortality = {i: [] for i in range(6)}

  for name, value in hurricanes.items():
    death_count = value["Deaths"]
    for rating, upper in mortality_scale.items():
      if death_count <= upper:
        hurricanes_by_mortality[rating].append(name)
        break
    else:
      hurricanes_by_mortality[5].append(name)
  
  if not hurricanes_by_mortality[0]:
    hurricanes_by_mortality[0] = ["None"]
  return hurricanes_by_mortality

deadliest_hurricanes = hurricane_rating_mortality(hurricanes)

print("----Here's a rating of all the deadliest hurricanes in a mortality scale (0-4)----\n")
for rate, hurricanes_names in sorted(deadliest_hurricanes.items()):
  rating = rate
  hurricane_names = hurricanes_names
  print(f"⦁ Mortality rating {rating} has the following hurricanes: {hurricane_names}")

#Function that finds the highest damage hurricane and its total cost
def greatest_dmg_hurricane(hurricanes):
  max_dmg_cane = ''
  max_damage = 0

  for name, value in hurricanes.items():
    damage_cost = value["Damages"]
    if damage_cost == "Damages not recorded":
      continue
    if max_damage < damage_cost:
      max_dmg_cane = name
      max_damage = damage_cost
  return max_dmg_cane, max_damage

print("\n----The hurricane the caused the highest damage----")
hurr_name, dmg_costs = greatest_dmg_hurricane(hurricanes)
print(f"The {hurr_name} was the hurricane that caused the highest damage among all hurricanes. It's total cost damage was {dmg_costs} dollars\n")

#Function that classifies hurricanes based on their damage rating and returns a dictionary by rating
def hurricane_rating_dmg(hurricanes):
  damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
  hurricanes_by_damage = {i: [] for i in range(6)}

  for name, value in hurricanes.items():
    dmg_value = value["Damages"]
    if isinstance(dmg_value,str):
      continue
    if dmg_value == 0:
      hurricanes_by_damage[0].append(name)
      continue
    for rating, upper in damage_scale.items():
      if dmg_value <= upper:
        hurricanes_by_damage[rating].append(name)
        break
    else:
      hurricanes_by_damage[5].append(name)

  if not hurricanes_by_damage[0]:
    hurricanes_by_damage[0] = ["None"]
  return hurricanes_by_damage

dmg_hurricane = hurricane_rating_dmg(hurricanes)

print("----Here's a rating list of the hurricanes based on the damage they caused (0-4)----\n")
for dmg_rate, hurricane_dmg_name in dmg_hurricane.items():
  dmg_rating = dmg_rate
  hurricane_dmg_name = hurricane_dmg_name
  print(f"⦁ The damage rating {dmg_rating} has the following hurricanes: {hurricane_dmg_name}")
