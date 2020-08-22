import COVID19Py
#Exercise 1
covid19 = COVID19Py.COVID19(data_source="csbs")
latest = covid19.getLatest()
#print(latest)
location = covid19.getLocationByCountryCode("US")
#print (location)

#Exercise 2

stats = dict()

for i in location:
	if i["province"] not in stats:
		stats[i["province"]] = i["latest"]["confirmed"]
	else:
		stats[i["province"]] += i["latest"]["confirmed"]

highest = list(stats)[0]
lowest = list(stats)[0]
average = 0

for i in list(stats):
    if (stats[i] > stats[highest]):
        highest = i
    elif (stats[i] < stats[lowest]):
        lowest = i
    average += stats[i]

print("Highest:",highest, stats[highest])
print("Lowest:",lowest, stats[lowest])
print("Average: ", average/(len(list(stats))))

res = sorted(stats.items())

longest = 26 #hard coding the length wanted
print("State" + " "*(longest-5) + "Total Number of Cases")
for state in res:
	print(state[0] + " "*(longest-len(state[0])) + str(state[1]))