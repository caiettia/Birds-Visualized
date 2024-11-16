# README
LAST UPDATED: 2020-11-13  
ORGANIZATION: spatial-data-discovery  
REPOSITORY: ay2021-1  
FOLDER: project/caiettia

## Files
### Scripts
* [caiettia_processing_script.py](https://github.com/spatial-data-discovery/ay2021-1/blob/master/project/caiettia/caiettia_processing_script.py)
* [caiettia_process_doc.txt](https://github.com/spatial-data-discovery/ay2021-1/blob/master/project/caiettia/caiettia_process_doc.txt)
### Inputs
* [Swainson's Hawks.csv](https://github.com/spatial-data-discovery/ay2021-1/blob/master/project/caiettia/data_files/Swainson's%20Hawks.csv)
* [Swainson's Hawks_raw.geojson](https://github.com/spatial-data-discovery/ay2021-1/blob/master/project/caiettia/data_files/Swainson's%20Hawks_raw.geojson)
* [uwnd_data.nc](https://github.com/spatial-data-discovery/ay2021-1/blob/master/project/caiettia/data_files/uwnd_data.nc)
* [vwnd_data.nc](https://github.com/spatial-data-discovery/ay2021-1/blob/master/project/caiettia/data_files/vwnd_data.nc)
### Outputs
* [SwainsonsHawks_filtered.csv](https://github.com/spatial-data-discovery/ay2021-1/blob/master/project/caiettia/data_files/SwainsonsHawks_filtered.csv)
* [SwainsonHawks_linestrings.geojson](https://github.com/spatial-data-discovery/ay2021-1/blob/master/project/caiettia/data_files/SwainsonHawks_linestrings.geojson)

# caiettia_processing_script.py

## How it Works
The script reads the two files in the file's directory: a geojson and csv file. First, the script reads the original migratory data in .csv format, and  filters the data out to include only the year of study with the most data, 1996 - 1997. The filtered dataframe is then output as a .csv in the directory. Secondly, the script reads the geojson file, reads out each POINT shape and creates a Linestring from them. The script reads coordinates for the previous 5 days, and creates LineStrings from them, to show a path of a bird. Finally, the LineStrings are read into a geopandas dataframe and output as a geojson file.

## How to Run the Script
To successfully run this script, one needs to first have all of the input files in the some folder as the processing script. Then, run the processing script and it will read said input data files, and output each of the output files in the same folder directory. 



## Packages Needed
* [Geopandas](https://geopandas.org/)
* [Shapely](https://pypi.org/project/Shapely/)
* [Pandas](https://pandas.pydata.org/)
* [Datetime](https://docs.python.org/3/library/datetime.html)
* [os](https://docs.python.org/3.4/library/os.html)

## File Types
* [geojson](https://geojson.org/)
* [csv](https://www.computerhope.com/issues/ch001356.htm)
* [netcdf](https://www.unidata.ucar.edu/software/netcdf/docs/netcdf_introduction.html)


## Swainson's Hawk Migratory Data
The migratory dataset is in both CSV and GeoJSON format for my project. 
* Provider: [Movebank](https://www.movebank.org/cms/webapp?gwt_fragment=page=studies,path=study204253)
* Variables: 
  * event-id : unique identifier of recorded bird location (integer)
  * visible : If the Hawk is visually (TRUE/FALSE)
  * timestamp : Time Recorded (mm/DD/YYYY HH:MM:ss)
  * location-long: Longitude (-180,180; degrees)
  * location-lat : Latitude (-90,90; degrees)
  * sensor-type : method of recording location (satellite string)
  * individual-taxon-canonical-name : scientific name of hawk (string)
  * tag-local-identifier : unique identifier for each bird (integer)
  * individual-local-identifier : unique identifier for each bird (string)
  * study-name : name of Movebank study (string)
* Contact info: sdavidson@ab.mpg.de
* Institution : Max Planck Institue of Animal Behavior
* Dates Covered : 1995-07-29 to 1998-06-24
  * Dates Used : 1996-07-01 to 1997-07-07

## Migratory Variables Used
* location-long 
* location-lat 
* individual-local-identifier 

## Wind Vector Data
This dataset is broken into two components, Zonal wind data(u wind) and Meridional wind data (v wind). As such, both data sets had to be acquired in tandem to create a wind vector map.
* Provider : [NOAA Physical Sciences Laboratory (PSL)](https://psl.noaa.gov/about/)
  * [U Wind Data](https://psl.noaa.gov/cgi-bin/GrADS.pl?dataset=NCEP%20Reanalysis%20Daily%20Averages;DB_did=195;file=%2FDatasets%2Fncep.reanalysis.dailyavgs%2Fsurface%2Fuwnd.sig995.1948.nc%20uwnd.sig995.y4.nc%20105523;variable=uwnd;DB_vid=228;DB_tid=89420;units=m%2Fs;longstat=Mean;DB_statistic=Mean;stat=;lat-begin=90.00S;lat-end=90.00N;lon-begin=0.00E;lon-end=357.50E;dim0=time;year_begin=1996;mon_begin=Jul;day_begin=1;year_end=1997;mon_end=Jul;day_end=7;X=lon;Y=lat;output=file;bckgrnd=black;use_color=on;fill=lines;cint=;range1=;range2=;scale=100;maskf=%2FDatasets%2Fncep.reanalysis.dailyavgs%2Fsurface%2Fland.nc;maskv=Land-sea%20mask;submit=Create%20Plot%20or%20Subset%20of%20Data;time-begin=17715%20Jul%201%201996;time-end=18086%20Jul%207%201997)
  * [V Wind Data](https://psl.noaa.gov/cgi-bin/GrADS.pl?dataset=NCEP%20Reanalysis%20Daily%20Averages;DB_did=195;file=%2FDatasets%2Fncep.reanalysis.dailyavgs%2Fsurface%2Fvwnd.sig995.1948.nc%20vwnd.sig995.y4.nc%20105523;variable=vwnd;DB_vid=278;DB_tid=89420;units=m%2Fs;longstat=Mean;DB_statistic=Mean;stat=;lat-begin=90.00S;lat-end=90.00N;lon-begin=0.00E;lon-end=357.50E;dim0=time;year_begin=1996;mon_begin=Jul;day_begin=1;year_end=1997;mon_end=Jul;day_end=7;X=lon;Y=lat;output=file;bckgrnd=black;use_color=on;fill=lines;cint=;range1=;range2=;scale=100;maskf=%2FDatasets%2Fncep.reanalysis.dailyavgs%2Fsurface%2Fland.nc;maskv=Land-sea%20mask;submit=Create%20Plot%20or%20Subset%20of%20Data;time-begin=17715%20Jul%201%201996;time-end=18086%20Jul%207%201997)
* Variables:
  * lat : Latitude (-90,90; degrees)
  * lon : Longitude (0, 360; degrees)
  * time : Time (hours since 1800-01-01 00:00:0.0)
  * level : Level (millibar)
  * uwnd : Mean Daily U-wind (m/s)
  * vwnd : Mean Daily V-wind (m/s)
* Missing Data Value :  -9.96921E36
* Contact info: psl.data@noaa.gov
* Institution Name: Physical Sciences Laboratory NOAA
* Date Created: 1996 (spans 1948-2020)
  * Dates Used: (1996-1997) 

## Wind Data Variables Used
* lat
* long
* uwnd
* vwnd 
* time

## Wind Data Variables Created
* vector : vector component created from uwnd and vwnd in Panoply (aggregated by day)

## Webpage
* https://spatial-data-discovery.github.io/project-caiettia.html




