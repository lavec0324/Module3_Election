# Module3 Challenge - Election Results

## Overview of Project

This project is intended to analyze election data and provide results by county and ultimate winner based on input from a csv file.  The csv has collected data comprised of ballot id, voter county, and selected candidate. 

## Election-Audit Results

####	How many votes were cast in this congressional election?  
369,711

####	Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct. 
County breakdown can be found here:

![here](https://github.com/lavec0324/Module3_Election/blob/main/Election%20Analysis/Resources/Election_Results_County.PNG)

####	Which county had the largest number of votes? 
Denver

#### 	Provide a breakdown of the number of votes and the percentage of the total votes each candidate received. 
Candidate breakdown can be found here:

![here](https://github.com/lavec0324/Module3_Election/blob/main/Election%20Analysis/Resources/Election_Results_Candidates.PNG)

#### 	Which candidate won the election, what was their vote count, and what was their percentage of the total votes? 
Winner information can be found here:

![here](https://github.com/lavec0324/Module3_Election/blob/main/Election%20Analysis/Resources/Election_Results_Winner.PNG)

## Election Audit Summary

Based on how this script was designed it an be used for almost any election where vote counts are provided in the same format as the current csv file (ballot id, county and candidate).  Number of candidates or counties do not impact the current scripts ability to use in the future as it will add unique candidates and counties are they are encountered.  There is also not hardcoding present in the script that would need to be modified.  The only real modification required is of the name of the input file would either need to be consistent with the current file name and be contained in the path run as contained or by changing the script for path and file name.  Code can be seen here:

![here](https://github.com/lavec0324/Module3_Election/blob/main/Election%20Analysis/Resources/file_name_code.PNG).

In addition to the above modifications can be made to the script to include information around ballot ids; for example to check to see that all ballot ids are unique (i.e. no duplicates).  If available there can also be data included in the csv file which represent voter demogrpahics where you could show a breakdown of voters by key demographics such as age allowing candidates to know what age bracket voted for them in the election the heaviest.

