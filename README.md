# E4501 Tools For Analytics Final-Project: Tracking Squirrel Sightings

## Background

## Web Application Introduction

## Dataset
This application use the [**2018 Central Park Squirrel Census**](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) created by [**The Squirrel Census**](https://www.thesquirrelcensus.com/).
They count squirrels and present their findings to the public. This table contains squirrel data for each of the 3,023 sightings, including location coordinates, age, primary and secondary fur color, elevation, activities, communications, and interactions between squirrels and with humans.

## Management Commands
Import: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command. 
```sh
python manage.py import_squirrel_data /path/to/file.csv
```
Export: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command. 
```sh
python manage.py export_squirrel_data /path/to/file.csv
```

## Views
A view that shows a map that displays the location of the squirrel sightings on an [**OpenStreets map**](https://www.openstreetmap.org/about/).
[Map](https://instance-2-288912.appspot.com/map/)
