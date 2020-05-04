# Ridesharing
  - CS-581 Ridesharing Project
  - This project analyzes the NYC yellow cabs taxi trips data for the period of Jan 2016 - June 2016 and extrapolates the result for an year.
  - Taxi trips data link : https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
  - **Team Members (Team 8)**
      - Arvind Ganesan
      - Varunya Yanamadala
      - Rakshitha Jayarame Gowda
      - Sachin Dattatraya Hegde
## Objective of the project
The objective of this project is to provide an analysis of ride-shared trips with unshared trips to:
  - Run the algorithm for different pool window sizes : 5 mins, 7 mins and 10 mins
  - Determine the distance saved per pool with respect to total unshared trips
  - Determine the trips saved per pool with respect to total unshared trips
  - Compare the average computation time for different pool sizes
  - Run the algorithm for peak period with different delays for a day of month
  - Extrapolate the 6 month results to produce yearly average results
  - Identify the impact of intersections on computation time in the form of graphs
  - Analyzing distance and trips saved based of percentage of passengers willing to ride-share
    
## System setup
  - Install MySQL server 8 and MySQL workbench. Ensure that workbench is able to connect to local mysql server using 'root' user and password as 'root'. This user name and password is used inside the project.
  - Install Python 3.5 or above. If 'pip' module is not installed, it has to be installed separately
  - Install these python modules: pandas, networkx, mysql-connector-python, requests
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
  - Test the docker instance in hitting the url to make sure you get a response of the form (shown below)
     - url : http://localhost:5000/route/v1/driving/-73.8733,40.7741;-73.9456,40.7743?overview=false
     - Sample reponse: ``` {"routes":[{"legs":[{"summary":"","weight":1473.8,"duration":1324.5,"steps":[],"distance":16319.9}],"weight_name":"routability","weight":1473.8,"duration":1324.5,"distance":16319.9}],"waypoints":[{"hint":"AQvAg____38OAAAAJQAAACAAAACJAAAAqHnrQOOvQkBtv4hBPUMZQg4AAAATAAAAIAAAAEYAAAAYSAAAp8eY-2spbgKkx5j7cCluAgIAXw92OrVT","distance":0.6102746825522855,"name":"","location":[-73.873497,40.773995]},{"hint":"vl1ggP___38fAAAAWAAAAAAAAABDAAAABxlyQXXpY0EAAAAAP--yQR8AAAAsAAAAAAAAACIAAAAYSAAAPvqY-20jbwII-pj7cCNvAgAAfwt2OrVT","distance":4.56758322813358,"name":"Metropolitan Avenue","location":[-73.860546,40.837997]}],"code":"Ok"} ```
## Analysing tables
  - Create a database called 'ride_sharing'
  - Create the tables: taxitrips_v2, intersections, pool_details. Use the schema given inside Schema Folder.
  - In database folder, there is a .sql file with preexisting data of taxitrips_v2 using MySQL workbench , the data can be populated to your MySQL database by importing the .sql file and running it.
  - Populate pool_details table with existing data only if you just want to run queries to get insights on already processed data. Else, there is no need to populate that table's contents to your local table.
  - Populate intersections table with the given .sql file. This is very important for the algorithm to use precomputed intersections.
  
# Before running the algorithm, check the Configuration Parameters below in each of the algorithm file.
-   **Algorithm Files** :   
    -       Forming_pairs_delay_algo.py 
            Forming_pairs_delay_algo_specific_rides.py ( Has logic to support x% of passengers willing to rideshare)
-   The files, each, has following variables to change algorithm behaviour
    -    **pool_window_time1** = 5 (Pool window size in minutes)
    -    **pool_window_time2** = 10 (Pool window size in minutes)
    -    **tripWindow_start_time** = "2016-04-23 00:00:00" (Starting time range to analyze trips)
    -    **tripWindow_end_time** = "2016-04-23 23:59:59" (Ending time range to analyze trips)
    -    **delay_factor_percent** = 20 (Delay factor as a percent to apply for ride-sharing constraints)
    -    **Average_speedinmiles** = 22 (Calculated by taking average speed of each month's trips' data : January 2016 - June 2016)
    -    **random_pool_Ids** = list(range(4262000, 4300000)) (Assign a unique pool id for the pools formed. To analyze for different trip start and end window, use a different pool range)
    -    **percent_of_ride_willing_to_ride_share** = 30 ( Only in Forming_pairs_delay_algo_specific_rides.py file)
    -   #### Laguardia Airport Co-ordinates
        -    source_latitude_min = 40.7714
        -    source_latitude_max = 40.7754
        -    source_longitude_max = -73.8572
        -    source_longitude_min = -73.8875
        
        

# Graph results depicting the analysis
  - The results are shown in **graphresults.pdf**. It is also available in the **finalreport.pdf**
  
# Running the program for only 5 mins.
  - In each of the algorithm file, the line below has to be uncommented
  ```
  #alarm.start()
  ```
  - To stop the program automatically after 6 mins (360 seconds) instead of 5 mins (300 seconds), the following line has to be changed.
    - Before
        ``` alarm = Alarm(300) ```
    - After
        ``` alarm = Alarm(360) ```

# Instructions to run the ridesharing algorithm files
  - The system has to be setup as specified in the system configuration.
  - Ensure that MySQL and docker api is functional.
  - Ensure that python is sucessfuly installed and modules are installed.
  - Ensure that the two **algorithm files**,mysqlUtilites.py, datapreprocessing.py are in the same project folder
  - Open command prompt, type 'python fileName.py', where fileName is one of the algorithm files.
