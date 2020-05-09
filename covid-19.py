def per_person_on_km(people,area):
    p_per_area=people/area
    print('People on per km',p_per_area)
    percent=people/100
    print('1% percent of total population',percent)
    per_per_area=percent/area
    print('1% percent population per km',per_per_area)


print('Population Bangladesh : ')
bdpeople=164453003
bdarea=147570
per_person_on_km(bdpeople,bdarea)

print('\nPopulation on Dhaka : ')
dhakapeople=21005860
dhakaarea=306.4
per_person_on_km(dhakapeople,dhakaarea)

print('\nPopulation on New York : ')
newpopulation=19440469
newarea=783.8
per_person_on_km(newpopulation,newarea)

print('\nPopulation on England : ')
engpopulation=67834548
engarea=130395
per_person_on_km(engpopulation,engarea)

print('\nPopulation of italy : ')
italypopulation=60461826
itlayarea=301338
per_person_on_km(italypopulation,itlayarea)

