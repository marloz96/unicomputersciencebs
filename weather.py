'''
File: weather.py
Author: Marco Lopez
Description: Program that reports the amount of cloudiness in the weather today
'''

percent_of_clouds = float(input("What percentage of the sky has clouds today?:"))

if percent_of_clouds <= 30:
    print("Clear")

elif percent_of_clouds >=31 and percent_of_clouds <= 70:
    print("Partly cloudy")

elif percent_of_clouds >= 71 and percent_of_clouds <= 99:
    print("Cloudy")

elif percent_of_clouds == 100:
    print("Overcast")

else:
    print("invalid")
                            

