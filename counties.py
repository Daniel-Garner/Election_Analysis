counties=["Arapahoe", "Denver", "Jefferson"]
#print(counties)
counties[0]
#print(counties[0])
counties.append("El Paso")
counties.insert(2, "El Paso")
counties.remove("El Paso")
#print(counties)
# If you want to change Jefferson county to El Paso, you would type the following: counties[2] = "El Paso".
counties_tuple = ("Arapahoe","Denver","Jefferson")
counties_dict={}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
for county in counties:
    print(county)
for i in range(len(counties)):
    print(counties[i])
    