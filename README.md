# State of company registration in Maharashtra

#### To run this project-
* Create a virtual environment with the command: virtualenv new-env-name
* Now activate with: source new-env-name/bin/activate
* Install Python and pip.
* Install Matplotlib with the command- pip install matplotlib
* Clone repo (https://github.com/richa-desai/company-registration-maharashtra)
* Alternatively, download all files (Keep all files in the same folder).
* Run the above downloaded required Python file to see graphs/plots with: python python_filename.py

#### Problems

##### 1. Histogram of Authorized Cap

Plot a histogram on the "Authorized Capital" (column: AUTHORIZED_CAP) with the following intervals

  1. <= 1L
  2. 1L to 10L
  3. 10L to 1Cr
  4. 1Cr to 10Cr
  5. \> 10Cr

**Note:**
* The x-axis labels should be strings listed above, like "<= 1L".
* You will have to adjust the intervals if you have an un-balanced plot.

##### 2. Bar Plot of company registration by year

From the column, DATE_OF_REGISTRATION parse out the registration year. Using this data, plot a **bar plot** of the number of company registrations, vs. year.

##### 3. Company registration in the year 2015 by the district.

The district can be found by zip code. This [resource](https://www.goldenchennai.com/pin-code/maharashtra-postal-code/) has that data. Before you start on this problem please make a CSV of zip code vs. district.

In this exercise ...

  1. Only consider registrations for the year 2015.
  2. Find out the district of registration by the zip code. The zip code can be found at the end of the address column.
  3. Count the registration by the district.
  3. Plot a "Bar plot" of "Number of Registration" vs. district.
  4. If the plot is unbalanced consider plotting only the top districts.

##### 4. Grouped Bar Plot.

Plot a Grouped Bar Plot by aggregating registration counts over ...
  1. Year of registration
  2. Principal Business Activity

Plot only top 5 Prinicipal Business Activity for last 10 years
