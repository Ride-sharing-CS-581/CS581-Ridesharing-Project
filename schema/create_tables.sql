CREATE TABLE `taxitrips_v2` (
  `RideID` int NOT NULL AUTO_INCREMENT,
  `pickup_latitude` float DEFAULT NULL,
  `pickup_longitude` float DEFAULT NULL,
  `dropoff_latitude` float DEFAULT NULL,
  `dropoff_longitude` float DEFAULT NULL,
  `tpep_pickup_datetime` datetime DEFAULT NULL,
  `dist_airport` float DEFAULT NULL,
  PRIMARY KEY (`RideID`)
);

CREATE TABLE `pool_details` (
  `pool_id` int NOT NULL,
  `count_of_rides` int DEFAULT NULL,
  `time_taken` float DEFAULT NULL,
  `dist_saved` float DEFAULT NULL,
  `rideLabel` varchar(20) DEFAULT NULL,
  `pool_window` int DEFAULT NULL,
  `record_entry` datetime DEFAULT NULL,
  `trips_saved` int DEFAULT NULL,
  `final_trips` int DEFAULT NULL,
  `unshared_trips` int DEFAULT NULL,
  `initial_trips_distance` int DEFAULT NULL,
  `initial_trips` int DEFAULT NULL,
  `DateRunFor` date DEFAULT NULL,
  PRIMARY KEY (`pool_id`),
  KEY `RideID_idx` (`rideLabel`)
) ;

CREATE TABLE `intersections` (
  `int_id` int NOT NULL AUTO_INCREMENT,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  `distance` float DEFAULT NULL,
  PRIMARY KEY (`int_id`)
); 