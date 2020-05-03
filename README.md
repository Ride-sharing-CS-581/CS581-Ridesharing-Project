# Ridesharing
  - CS-581 Ridesharing Project
  - This project analyzes the NYC yellow cabs taxi trips data for the period of Jan 2016 - June 2016 and extrapolates the result for an year.
  - Taxi trips data link : https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
  - **Team Members (Team 8)**
      - Arvind Ganesan
      - Varunya Yanamadala
      - Rakshitha Jayarame Gowda
      - Sachin Dattatraya Hegde
# Objective of the project
 - The objective of this project is to provide an analysis of ride-shared trips with unshared trips to:
    - Run the algorithm for different pool window sizes : 5 mins, 7 mins and 10 mins
    - Determine the distance saved per pool with respect to total unshared trips
    - Determine the trips saved per pool with respect to total unshared trips
    - Compare the average computation time for different pool sizes
    - Run the algorithm for peak period with different delays for a day of month
    - Extrapolate the 6 month results to produce yearly average results
    - Identify the impact of intersections on computation time in the form of graphs
# System setup
  - Install MySQL server 8 and MySQL workbench. Ensure that workbench is able to connect to local mysql server using 'root' user and password as 'root'. This user name and password is used inside the project.
  - Install Python 3.5 and above. If 'pip' module is not installed, it has to be installed separately
  - Install these python modules: pandas, networkx, mysql-connector
  - Install Docker or Docker Toolbox from the following links : 
      - **Docker**
          - Windows: https://docs.docker.com/docker-for-windows/install/
          - Ubuntu : https://docs.docker.com/engine/install/ubuntu/
      - **Docker Toolbox**
          - Windows: https://docs.docker.com/toolbox/toolbox_install_windows/
      For Windows 10 users, Windows 10 Pro edition is required to setup Docker. If Windows 10 Home is present, Install Docker ToolBox.
  - Download newyork osrm file from the link : http://download.geofabrik.de/north-america/us/new-york-latest.osm.pbf
  - Follow the instructions for setting up local osrm server from this link : https://hub.docker.com/r/osrm/osrm-backend/
  - The minimum ram requirement is 12GB with no other higher process consuming ram. Depending on system configuration, the process may 
    take from 10 minutes - 1.5 hours. The process was tested on Mac System, Google Cloud VM with 16GB ram and 30GB SSD free space.
    
# Analysing tables
  - Create a database called 'ride_sharing'
  - Create the tables: taxitrips_v2, intersections, pool_details. Use the schema given inside Schema Folder.
  - In database folder, there is a .sql file with preexisting data of taxitrips_v2 using MySQL workbench , the data can be populated to your MySQL database by importing the .sql file and running it.
  - Populate pool_details table with existing data only if you just want to run queries to get insights on already processed data. Else, there is no need to populate that table's contents to your local table.
  - Populate intersections table with the given .sql file. This is very important for the algorithm to use precomputed intersections.
  
# Before running the algorithm, check the Configuration Parameters section in Wiki.
-   Link : https://github.com/Ride-sharing-CS-581/ridesharing/wiki

# Results are shown in the Wiki page depicting the analysis
  - For each of pool window size : 5, 7, and 10 mins, average distance saved per pool, average trips saved per pool and average computation time is shown
  - Delay variation affecting the distance saved, trips saved and computation time for a day.
  - Comparision of distance saved, trips saved, computation time if x% of passengers are willing to ride share. The chosen values of x are 30%, 50%, 70% for a day.
  - Extrapolation results of 6 months data to an year depicting best possible total trips, average distance saved per pool, average trips saved per pool and average computation time.
  - Impact of the count of intersection points on computation time of forming pools for few days in the month of May 2016.
  

