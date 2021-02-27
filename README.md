# sqlalchemy-challenge

Step 1 - Climate Analysis and Exploration

I used Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database. All of the following analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

I used the provided starter notebook and hawaii.sqlite files to complete the climate analysis and data exploration.

I used SQLAlchemy create_engine to connect to the sqlite database.

I used SQLAlchemy automap_base() to reflect the tables into classes and saved a reference to those classes called Station and Measurement.

I linked Python to the database by creating an SQLAlchemy session.


Precipitation Analysis


I found the most recent date in the data set.

Using this date, I retrieved the last 12 months of precipitation data by querying the 12 preceding months of data. 

I loaded the query results into a Pandas DataFrame and set the index to the date column.

I sorted the DataFrame values by date.

I plotted the results using the DataFrame plot method.

I used Pandas to print the summary statistics for the precipitation data.


Station Analysis


I designed a query to calculate the total number of stations in the dataset.

I designed a query to find the most active stations.

I listed the stations and observation counts in descending order.

Using the most active station id, I calculated the lowest, highest, and average temperature.

I designed a query to retrieve the last 12 months of temperature observation data (TOBS).

I filtered by the station with the highest number of observations.

I queried the last 12 months of temperature observation data for this station.

I plotted the results as a histogram with bins=12.

I closed out the session.


Step 2 - Climate App
I designed a Flask API based on the queries that I just developed.

I used Flask to create the following routes.

Routes
/
Home page.
Listed all routes that are available.

/api/v1.0/precipitation
Converted the query results to a dictionary using date as the key and prcp as the value.
Returned the JSON representation of your dictionary.

/api/v1.0/stations
Returned a JSON list of stations from the dataset.

/api/v1.0/tobs
Queried the dates and temperature observations of the most active station for the last year of data.
Returned a JSON list of temperature observations (TOBS) for the previous year.

/api/v1.0/<start> and /api/v1.0/<start>/<end>
Returned a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
When given the start only, calculated TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
When given the start and the end date, calculated the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
