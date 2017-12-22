#Grace Talent
#gtalent2
#Credit hour: 4
#Final Project


import csv
import string
import re

#reads in the csv file with DictReader so that I can make use of the fieldnames
#to extract out data for each business entity storing in its own list which is then
#stored in the all_data list.
# with open("Business_Licenses_-_Current_Active.csv", newline='') as csvfile:
with open("Business_Licenses_-_Current_Active.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    all_data = []
    csv_headers = reader.fieldnames
    for row in reader:
        all_data.append([row[col] for col in reader.fieldnames])



#removes the punctuation from name except for & which is replaced with the word
# 'and'.  I want to keep the 'and' in the business name because I will use it later
#for when I need to differentiate between an organization versus human name.  For the
#entries that have two human names joined by "and", I count as an organization.  Only
#individual names will be considered a human name.
def remove_punc(line_str):
    nopunc_line = line_str.lower()
    for punc in string.punctuation:
        if punc == "&":
            nopunc_line = nopunc_line.replace(punc,"and")
        else:
            nopunc_line = nopunc_line.replace(punc, "")
    return nopunc_line



#checks if it is a organization name or a human name
def check_name(name_list):
    check = "no human"
    if len(name_list)==1:
        check = "yes organization"
    for word in name_list:
        if word in company_words:
            check = "yes organization"
            break
    return check



#creates a dictionary when a list is passed into the fucntion.  I used this to help detect duplicate ID's.
def position_Dict(list):
    positionDict = {}
    for position, item in enumerate(list):
        item_str = ''.join(item)
        if item_str in positionDict:
            positionDict[item_str].append(position)
        else:
            positionDict[item_str] = [position]
    return positionDict


#removes the stop words from the legal names so that they are not included in the id.  I decided to not include 'group'
#in my list of stop words because it can mean something else in a name other than referring to the business entity designation.
def remove_stopwords(name_str):
    stop_words_list = ['incorporated', 'corporation', 'llc', 'inc', 'of', 'the', 'co', 'ltd', 'ltdllc', 'limited', 'lp', 'and', 'aand', 'intl', 'incorporation']
    nostopwords_name = name_str
    for stopword in stop_words_list:
        for word in name_str.split():
            if stopword == word:
                nostopwords_name = nostopwords_name.replace(word, "")
            else:
                nostopwords_name = nostopwords_name
    return nostopwords_name



#a list of words used to indicate a company/organization vs a human name.  As I got more into my stop word list, I realized I should have done it another way
#to detect company names.  The length of the stop words was starting to get really long and ridiculous.
#Words like 'llc' or 'inc' always appear at the end of the name so I should have looked for those maybe using regex.  There
#were a lot of misspellings and joining of words which should not be put together in the names so I think the regex would have been better to detect
#the variations in the names like incorporation, incorporated, inc, etc, but I ran out of time to figure that out.
company_words = ['llc', 'inc', 'co', 'corporation', 'limited', 'llcltd', 'ltd', 'chicago', 'corp',
                 'lp', 'llp', 'company', 'apartments', 'contractors', 'international', 'incorporated', 'incoporated', 'incorporation', 'industries' 
                 'lab', ',', 'society', 'network', 'and', 'aaa', 'industries', 'lab', 'cleaners', 'artstock', 'indoor',
                 'group', 'organization', 'church', 'without', 'fund', 'academic', 'productions', 'industrial', 'center',
                 'project', 'school', 'community', 'illinois', 'possessions', 'lock', 'cleveland', 'distribution', 'broadway'
                 'markets', 'alternative', 'venture', 'services', 'plumbing', 'music', 'systems', 'casino',
                 'league', 'placement', 'american', 'repair', 'flood', 'construction', 'intl', 'shop', 'advertising',
                 'lotton', 'boutique', 'barbershop', 'pc', 'fitness', 'salon', 'rental', 'foundation', 'medicine',
                 'safaris', 'services', 'recycling', 'realtors', 'assistance', 'national', 'properties', 'bebe', 'parking',
                 'events', 'alliance', 'currency', 'jewelers', 'traders', 'vending', 'shift', 'ministry', 'museum', 'amphenol',
                 'system', 'staffing', 'biz', 'partners', 'business', 'club', 'auto', 'supply', 'liquors', 'diagnostic', 'custom',
                 'palace', 'foundation', 'programs', 'wireless', 'studios', 'security', 'nfp', 'merchants', 'research',
                 'bakery', 'hardware', 'technologies', 'entertainment', 'management', 'brothers', 'medical', 'ohare',
                 'housing', 'bodywork', 'discoteca', 'cuisine', 'jewelry', 'cafe', 'beef', 'studio', 'restaurant', 'service',
                 'asian', 'hotel', 'cocina', 'diner', 'tacos', 'consultants', 'contracting', 'legends', 'shell', 'grill', 'usa',
                 'automotive', 'taco', 'the', 'by', 'carriage', 'design', 'insurance', 'organic', 'central', 'books', 'terraza',
                 'grocer', 'centers', 'catering', 'pizza', '7eleven', 'education', 'technology', 'advisors', 'core', 'fiction',
                 'bridal', 'telecom', 'mart', 'creacciones', 'rainbow', 'animal', 'mechanical', 'dental', 'lawncare', 'cottage',
                 'midway', 'bananas', 'dba', 'consulting', 'college', 'laundromat', 'capitalinc', 'enterprises', 'institute', 'communications',
                 'partnership', 'computer', 'control', 'natividad', 'mept', 'foods', 'hundred', 'strength', 'habitat', 'express', 'road',
                 'association', 'neighborhood', 'assoc', 'production', 'browninc', 'plastics', 'travel', 'gospel', 'llcc', 'wilkowlimited',
                 'photography', 'laundrychicago', 'solutions', 'wellness', 'electricalinc', 'market', 'funeral', 'sc', 'towing', 'midwest',
                 'concrete', 'transportation', 'chicagoland', 'united', 'midland', 'california', 'vacations', 'associates', 'pacific',
                 'woodworking', 'headstart','conduct', 'eye', 'clothing', 'atlantis', 'hvac', 'academy', 'paradise', 'coaching', 'plastering',
                 'distributor', 'front', 'training', 'healthcare', 'food', 'style', 'hospital', 'cycle', 'petroleum', 'realty', 'capitol',
                 'laundry', 'new', 'shoemo', 'dog', 'marketing', 'mdsc', 'meals', 'produce', 'metals', 'authority', 'metal', 'vinegar',
                 'companyinc', 'healing', 'loungeinc', 'commissary', 'estate', 'clubinc', 'car', 'town', 'heating', 'pride', 'products',
                 'careinc', 'mattress', 'incs', 'naturals', 'productionsinc', 'family', 'sales', 'buildersinc', 'equipment', 'transmission',
                 'buildingmaterialsandsuppl', 'sushi', 'electrical', 'america', 'plating','equpt', 'dvm', 'mission', 'coinc', 'health', 'home',
                 'inspirationsinc', 'serviceinc', 'hospitals', 'noodlesinc', 'windows', 'schoolinc', 'estateinc', 'packaginginc', 'hungry', 'avenue',
                 'embossing', 'place', 'manor', 'msm','pbc', 'nomadic', 'shirts', 'travelinc', 'magic', 'constructioninc','shuttersinc', 'chicos',
                 'footwearinc', 'scotland', 'enterprisesinc', 'target', 'carrucelinc', 'cowork', 'workshop', 'boxesinc', 'hands', 'markets', 'constrinc',
                 'hauling', 'investmentcorp', 'burgers', 'plaza', 'garage', 'beach', 'contractorsinc', 'snack', 'development', 'trees', 'coffee', 'agency',
                 'automotiveinc', 'saloninc', 'european','skincare', 'plumbers', 'recovery', 'servicesinc', 'inninc', 'care', 'sports', 'poppininc',
                 'petroleuminc', 'investment', 'studiosinc', 'grocery', 'masonry', 'importer', 'mechanicalinc', 'communication', 'brothersinc', 'perfect',
                 'city', 'fireside', 'broadway', 'mercy', 'florist', 'traininginc', 'energy', 'landscape', 'iginc', 'information', 'trayinc', 'cleanersinc',
                 'cororation', 'cleanup', 'advantage', 'cleaning', 'cxinc', 'creative', '128inc', 'transmissions', 'creations', 'building', 'dancers',
                 'nativity', 'university', 'storage', 'tea', 'whitehouse', 'ff50', 'give', 'tanning', 'transport', 'accounting', 'pipe', 'manufacturing',
                 'world', 'wisconsin', 'notre', 'program', 'ff854', 'developmentllc', 'lcc', 'chicagos', 'chicagoinc', 'canteen', 'unlimited', 'youth',
                 'hospitality','sportsacro', 'grocers','corportation', 'taxcorp', 'tattoo', 'incorpoated','corporate', 'steel', 'associnc', 'enterprise',
                 'innovative','innovations', 'dreams', 'clinic', 'companies', 'of', 'aand', 'gallery', 'south', 'footwear', 'change', 'assc', 'nc','pyrotechnics',
                 'processing', 'party', 'general', 'store', 'framing', 'constructions', 'engineering', 'engineerslimited', 'lllp']




#----------------------- CODE

#putting the data into different lists so that it will be easier to manipulate
#as well as cleaning up the data of all punctuation and making everything lower case
legal_names = []
addresses = []
date_issued = []
for data in all_data:
    legal_names.append(remove_punc(data[4]))
    addresses.append(remove_punc(data[6]))
    date_issued.append(data[27])


#a number of addresses were redacted for privacy so in order to get the regular expressions
#to work when formatting the addresses later in the program I put in a fake address 000 a aaa
#so that I wouldn' be missing any entries.
mod_addresses = []
for position, address in enumerate(addresses):
    if address == "redacted for privacy":
        new_address = address.replace("redacted for privacy", "000 a aaa")
        mod_addresses.append(new_address)
    else:
        mod_addresses.append(address)


#extracting out the street name using regular expressions then cleaning up and formatting
#the name so that it does not include any street stop words like ave, blvd, etc.
full_address = re.compile('(^[0-9]*[ ]{0,2}[0-9]*[ ]{0,2}[a-z]{0,1}[ ]{0,2})([0-9]*[a-z]*[ ]{0,2}[a-z]*)', re.MULTILINE)
street_address = re.findall(full_address, "\n".join(mod_addresses))
street_stopwords = ['ave', 'st', 'plz', 'blvd', 'dr', 'rd', 'ln', 'pl', 'ct', 'hwy', 'pkwy']
formated_street_list = []

for number, street in street_address:
    streetname_list = street.split()
    if len(streetname_list) > 1:
        if streetname_list[1] in street_stopwords:
            formated_street_list.append(streetname_list.pop(0))
        else:
            formated_street_list.append(''.join(streetname_list))
    else:
        formated_street_list.append(''.join(streetname_list))


#creating the first part of the ID by processing the legal names, checking whether
#it is a organization name or a human name, then creating the ID based on the name
id = ''
unique_id = []
id_list = []
full_names = []
for name in legal_names:
    id = ''
    unique_id = []
    name_list = name.split()
    if check_name(name_list) == "yes organization":
        for word in remove_stopwords(name).split():
            if len(remove_stopwords(name).split())==1:
                id = word
            elif len(word)>=3:
                id = id + word[0:2]
            else:
                id = id + word
        unique_id.append(id)
        id_list.append(unique_id)
    elif check_name(name_list) == "no human":
        if len(name_list) > 3:
            len_name = len(name_list)
            for i in range(0,len_name):
                if i == 0:
                    id = id + name_list[i][0:3]
                elif i>0:
                    id = id + name_list[i][0]
        elif len(name_list) == 3:
            id = name_list[2][0:3]+name_list[0][0:3]+name_list[1][0]
        elif len(name_list) == 2:
            id = name_list[1][0:3]+name_list[0][0:3]
        else:
            id = name_list
        unique_id.append(id)
        id_list.append(unique_id)

# inserting the id into my all_data list. Not sure if this is necessary, but doing it in case I need it later.
w = 0
for data in all_data:
    data.insert(0, id_list[w])
    w += 1


#add the dates to the ID.  Split the date "/" and used indices to get the month and year.
date_id_list = []
m = 0
for date in date_issued:
    split_date = date.split('/')
    date_id = split_date[0]+split_date[2][2:4]
    full_id = ''.join(id_list[m]) + ' ' + str(date_id)
    date_id_list.append(full_id)
    m+=1


# finding the duplicate ID's and storing it in a dictionary where the ID is the key and
# the values are the positions of the duplicates
positionDict = {}
for position, item in enumerate(date_id_list):
    item_str = ''.join(item)
    if item_str in positionDict:
        positionDict[item_str].append(position)
    else:
        positionDict[item_str] = [position]


#finding the duplicate ID's and storing it in a dictionary where the ID is the key and
#the values are the positions of the duplicates using the position_Dict() function.  All
#the duplicate ID's then have the street name attached to it to help deferentiate it.
id_street_list = []
id_positionDict = position_Dict(date_id_list)
for key, value in id_positionDict.items():
    if len(value)>1:
        for i in value:
            # print(''.join(date_id_list[i]) + '-' + ''.join(formated_street_list[i]))
            id_street_list.append(''.join(date_id_list[i]) + '-' + ''.join(formated_street_list[i]))
    elif len(value)==1:
        for h in value:
            id_street_list.append(''.join(date_id_list[h]))
            # print(''.join(date_id_list[h]))


#checking for duplicates again after adding the street name and adding 1, 2, 3, etc. to the ID if there are duplicates.
full_id_list = []
dupID_Dict = position_Dict(id_street_list)
for key, value in dupID_Dict.items():
    count = 1
    if len(value)>1:
        for num in value:
            full_id_list.append(''.join(id_street_list[num]) +'_'+ str(count))
            count += 1
    elif len(value)==1:
        for num in value:
            full_id_list.append(''.join(id_street_list[num]))

#creating a dictionary where my full ID is used as the key and all the information taken from the csv file is used as the value.
#I noticed that the sorting didn't work out quite right because of the street names attached.  For the most part
#the ID's are in order except when it took into account the street names which are also in order, but that was not taken into
#account when I sorted the all_data by the ID column I inserted.
q = 0
sorted_data = sorted(all_data, key=lambda x : x[0])
print(sorted_data)
full_dataDict = {}
# sorted_data.pop(0)
for id in sorted(full_id_list):
    if id in full_dataDict:
        full_dataDict[id].append(sorted_data[q])
    else:
        full_dataDict[id] = sorted_data[q]
    q+=1

for key, value in full_dataDict.items():
    print(key)
    print(value)


