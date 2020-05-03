-- Average distance saved per pool as a % of unshared trips
select pool_window,rideLabel,avg(dist_saved)/avg(initial_trips_distance) * 100 as saved from 
pool_details group by rideLabel, pool_window;


-- Average trips saved per pool as a % of unshared trips
select pool_window,rideLabel,avg(trips_saved)/avg(initial_trips) * 100 as saved from 
pool_details group by rideLabel, pool_window;

-- Average Computation Time per pool
select pool_window, rideLabel, avg(time_taken)
                    from pool_details
                    group by pool_window, rideLabel;