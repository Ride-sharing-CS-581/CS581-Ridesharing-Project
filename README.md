# ridesharing
CS-581 Ridesharing project final 

# System setup
  - Install MySQL server 8 and MySQL workbench. Ensure that workbench is able to connect to local mysql server using 'root' user and password as 'root'. This user name and password is used inside the project.
  - Install Python 3.5 and above. If 'pip' module is not installed, it has to be installed separately
  - Install these python modules: pandas, networkx, mysql-connector
  - Install Docker or Docker Toolbox from the following links : 
      - TBD
      - TBD
      For Windows 10 users, Windows 10 Pro edition is required to setup Docker. If Windows 10 Home is present, Install Docker ToolBox.
  - Download newyork osrm file from the link : TBD
  - Follow the instructions for setting up local osrm server from this link : 
  - The minimum ram requirement is 12GB with no other higher process consuming ram. Depending on system configuration, the process may 
    take from 10 minutes - 1.5 hours. The process was tested on Mac System, Google Cloud VM with 16GB ram and 30GB SSD free space.
    
# Analysing tables
  - Create a database called 'ride_sharing'
  - Create the tables: taxitrips_v2, intersections, pool_details. Use the schema given inside Schema Folder.
  - In database folder, there is a .sql file to taxitrips_V2 table. Using MySQL workbench , the data can be populated to your MySQL database by importing the .sql file and running it.
  - Populate pool_details table with data only if you just want to run queries to get insights on already processed data. Else, there is no need to populate that table's contents to your local table.
 
# Running the algorithm
  - File : *Forming_pairs_delay_algo.py* :  
      - This file has logic to perform ride sharing for pool window of 2 sizes. The default size given in the code is 5 and 10. To  
        change the values, assign different values to the following variables.
          - pool_window_time1 = <new_Integer_value>
          - pool_window_time2 = <new_Integer_value>
      - The default delay percent is 20 %. To change it, assign a new value to the following variable
          - delay_factor_percent = <new_Integer_value>. As an Example, delay_factor_percent = 20
      
