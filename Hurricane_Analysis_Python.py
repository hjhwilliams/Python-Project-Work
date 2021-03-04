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
# test function by updating damages
def nl():
  Damages=[]
  for i in damages:
    if 'M' in i:
      x=float(i[0:-1])*conversion['M']
      Damages.append(x)
    elif 'B' in i:
      x=float(i[0:-1])*conversion['B']
      Damages.append(x)
    else:
      Damages.append(i)
  return Damages

Damages=nl()
# print(Damages)

 
# Create a Table
def Create_Dictionary():
  hurricane_record={} 
  for i in range(0,len(deaths)):
   hurricane_record[names[i]]={'Name':names[i], 'Month':months[i], 'Year':years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damage': Damages[i], 'Death': deaths[i]}
  return hurricane_record

# Create and view the hurricanes dictionary
hurricane_record=Create_Dictionary()
#print(hurricane_record['Bahamas'])


# Organising the hurrican by year

def Create_Hurricane_Order():
  hur_by_date={}
  for i in hurricane_record:
    current_year = hurricane_record[i]['Year']
    hur_now = [hurricane_record[i]]
    if current_year not in hur_by_date:
      hur_by_date[current_year]=hur_now
    else:
      hur_by_date[current_year].append(hur_now)
  return hur_by_date

# create a new dictionary of hurricanes with year and key
hur_by_date= Create_Hurricane_Order()
#print(hur_by_date[1932])

  
# Counting Damaged Areas
def Frequency_of_Hurricanes():
  hurricane_freq={}
  for locations in areas_affected:
    for area in locations:
      if area not in hurricane_freq:
        hurricane_freq[area]=1
      else:
        hurricane_freq[area]+=1
  return hurricane_freq

# create dictionary of areas to store the number of hurricanes involved in
hurricane_freq=Frequency_of_Hurricanes()
#print(hurricane_freq)

# Calculating Maximum Hurricane Count
def Max_Hur_Count():
  highest_value=0
  high_val={}
  for areas in hurricane_freq:
    if hurricane_freq[areas] > highest_value:
      highest_value=hurricane_freq[areas]
      high_val[areas]=highest_value
  return high_val


# find most frequently affected area and the number of hurricanes involved in
high_val=Max_Hur_Count()
# print(high_val)  
  

# Calculating the Deadliest Hurricane      
def Max_Hur_Deaths():
  hurricane_max_death={}
  for num in range(0,len(deaths)):
    if deaths[num] == max(deaths):
      hurricane_max_death[names[num]]= deaths[num]
  return hurricane_max_death
hurricane_max_death=Max_Hur_Deaths()
# print(hurricane_max_death)


# find highest mortality hurricane and the number of deaths
hurricane_max_death=Max_Hur_Deaths()
#print(hurricane_max_death)

# 7
# Rating Hurricanes by Mortality
def Rating_Canes_By_Mortality():

  cane_mortality_rating={0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}

  for num in range(0,len(deaths)):
    if deaths[num] == 0:
      cane_mortality_rating[0].append(names[num])
    elif deaths[num] >0 and deaths[num] <= 100:
      cane_mortality_rating[1].append(names[num])
    elif deaths[num] >100 and deaths[num] <=500:
      cane_mortality_rating[2].append(names[num])
    elif deaths[num] >500 and deaths[num] <=1000:
      cane_mortality_rating[3].append(names[num])
    elif deaths[num] >1000 and deaths[num] <=10000:
      cane_mortality_rating[4].append(names[num])
    else:
      cane_mortality_rating[5].append(names[num])
  return cane_mortality_rating

# categorize hurricanes in new dictionary with mortality severity as key
cane_mortality_rating=Rating_Canes_By_Mortality()
#print(cane_mortality_rating)

# 8 Calculating Hurricane Maximum Damage
def greatest_damage():
  max_damage=0
  Hur_damage=[]
  greatest_hur_damage={}
  for cane in hurricane_record:
    if hurricane_record[cane]['Damage'] == 'Damages not recorded' or hurricane_record[cane]['Damage'] < max_damage:
      max_damage=max_damage
      Hur_damage=Hur_damage
    elif hurricane_record[cane]['Damage'] > max_damage:
      max_damage=hurricane_record[cane]['Damage']
      Hur_damage=cane
  greatest_hur_damage[Hur_damage]=max_damage
  return greatest_hur_damage

# find highest damage inducing hurricane and its total cost
greatest_hur_damage=greatest_damage()
#print(greatest_hur_damage)


# 9
# Rating Hurricanes by Damage
damage_scale= {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def damage_rating():
  damage_hurricane_rating={0:[], 1:[], 2:[], 3:[], 4:[],5: []}
  for cane in hurricane_record:
    if hurricane_record[cane]['Damage']==damage_scale[0] or hurricane_record[cane]['Damage'] == 'Damages not recorded':
      damage_hurricane_rating[0].append(cane)
    elif hurricane_record[cane]['Damage'] >damage_scale[0] and hurricane_record[cane]['Damage'] <=damage_scale[1]:
      damage_hurricane_rating[1].append(cane)
    elif hurricane_record[cane]['Damage'] >damage_scale[1] and hurricane_record[cane]['Damage'] <=damage_scale[2]:
      damage_hurricane_rating[2].append(cane)
    elif hurricane_record[cane]['Damage'] >damage_scale[2] and hurricane_record[cane]['Damage'] <=damage_scale[3]:
      damage_hurricane_rating[3].append(cane)
    elif hurricane_record[cane]['Damage'] >damage_scale[3] and hurricane_record[cane]['Damage'] <=damage_scale[4]:
      damage_hurricane_rating[4].append(cane)
    else:
      damage_hurricane_rating[5].append(cane)
  return damage_hurricane_rating

damage_hurricane_rating= damage_rating()
print(damage_hurricane_rating)
