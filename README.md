# Mormon Missionary Communities

Data visualization for the [LDS Missionary Database](https://history.churchofjesuschrist.org/chd/landing?lang=eng). 

### About the Code

The folder `data_collection` contains python scripts to download the initial data set from the missionary database. The folder `data_cleaning` contains Jupyter notebooks used in preparing the data for visualization. Some edits to the data set were also done manually. 

I have provided `cities.zip` to show how I grouped missionary residences together. The top line of each file is the standardized format; all other lines in each file get changed to match the top line. 

The main data analysis and visualization notebook is `Mission Communities.ipynb`. Here you can group sets of missions together and view communities that proportionally sent the most missionaries to that group of missions. Some other visualizations are also included.


### Tableau Visualizations

Another set of missionary residence visualizations are hosted on my [Tableau Public](https://public.tableau.com/app/profile/nathan.cordner/viz/mha_missionary_maps/MissionaryResidenceCityMap) profile. Views include
* A map of missionary residence cities (can filter by year and mission)
* Where missionaries served by residence (city or region; can filter by year and residence)
* Where missionaries came from by mission (city or region; can filter by year and mission)
* When missionaries were sent to missions (can filter by year, city, or region) 

Hovering over parts of the visuals will bring up more detailed information. Clicking on parts of visuals will present an option to View Data (top right button). Click to get a popup window, and select Full Data to view the actual rows of the data set corresponding to the selection (can also click "Show Fields" to reveal additional columns in the data set). 


### Contact

Please send any questions about the visualizations or how to use the code to ncordner at uvu dot edu. Please include "Mission Communities" (or something to that effect) in the subject line. 