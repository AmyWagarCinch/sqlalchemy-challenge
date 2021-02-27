# 1. import Flask
from flask import Flask, jsonify
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import pandas as pd

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite") #sqlite:///hawaii.sqlite

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# View all of the classes that automap found
Base.classes.keys()

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    List = ["/api/v1.0/precipitation", "/api/v1.0/stations", "/api/v1.0/tobs", "/api/v1.0/<start>","/api/v1.0/<start>/<end>"]
    return jsonify(List)
    
    


# 4. Define what to do when a user hits the /about route
@app.route("/api/v1.0/precipitation")
def One():
    import datetime
    # Design a query to retrieve the last 12 months of precipitation data and plot the results. 
    # Starting from the most recent data point in the database. 

    # Calculate the date one year from the last date in data set.
    end_date = datetime.datetime(2017, 8, 23)
    start_date = end_date - datetime.timedelta(days = 365)
    #print(start_date)


    # Perform a query to retrieve the data and precipitation scores

    prcp_results = session.query(measurement.date, measurement.prcp)\
    .filter(measurement.date>= start_date).all()
    #print(prcp_results)
    # Save the query results as a Pandas DataFrame and set the index to the date column

    prcp_df = pd.DataFrame(prcp_results)

    # Sort the dataframe by date
    prcp_df = prcp_df.sort_values("date")
    #prcp_df
    # Use Pandas Plotting with Matplotlib to plot the data

    #prcp_df.plot(x= "date", rot= 45)

    return jsonify(prcp_df.set_index('date').to_dict())



@app.route("/api/v1.0/stations")
def Two():
    stationss = session.execute('SELECT station FROM station ;').fetchall()

    return jsonify({'stations': [dict(row) for row in stationss]})


@app.route("/api/v1.0/tobs")
def three():
    import datetime
    # Using the most active station id
# Query the last 12 months of temperature observation data for this station and plot the results as a histogram
## Calculate the date one year from the last date in data set.
    end_date = datetime.datetime(2017, 8, 23)
    start_date = end_date - datetime.timedelta(days = 365)
##print(start_date)


## Perform a query to retrieve the data and precipitation scores

    tobs_results = session.query(measurement.date, measurement.tobs)\
    .filter(measurement.date>= start_date)\
    .filter(measurement.station == "USC00519281").all()
##print(prcp_results)
## Save the query results as a Pandas DataFrame and set the index to the date column

    tobs_df = pd.DataFrame(tobs_results)

## Sort the dataframe by date
#tobs_df = tobs_df.sort_values("date")
##prcp_df
## Use Pandas Plotting with Matplotlib to plot the data

#tobs_df.plot.hist()
#plt.xlabel("Temperature")
    
    
    
    #return jsonify({'temperatures': [dict(row) for row in tobs_df]})
    #return jsonify(tobs_df.set_index('tobs').to_dict())
    #return jsonify(tobs_df.tobs.to_dict())
    return jsonify(tobs_df['tobs'].tolist())
    #return jsonify(tobs_df['tobs']) #error

@app.route("/api/v1.0/<start>")
def four(start):
    #Return a JSON list of the minimum temperature, the average temperature, 
    # and the max temperature for a given start or start-end range.
    #When given the start only, calculate TMIN, TAVG, and TMAX for all 
    # dates greater than and equal to the start date.
    #2010-01-04
    
    tobs = session.execute(f'SELECT tobs FROM measurement where date >= {start}').fetchall()
    tobs_df = pd.DataFrame(tobs)
    return jsonify(tobs_df.describe().to_dict())


@app.route("/api/v1.0/<start>/<end>")
def five(start,end):
    #Return a JSON list of the minimum temperature, the average temperature, 
    # and the max temperature for a given start or start-end range.
    #When given the start and the end date, calculate the TMIN, TAVG, and 
    # TMAX for dates between the start and end date inclusive.
    tobss = session.execute(f'SELECT tobs FROM measurement where date >= {start} and date <= {end}').fetchall()
    tobss_df = pd.DataFrame(tobss)
    if tobss_df.empty: 
        return jsonify("sorry, that date range is whack")
    else:    
        return jsonify(tobss_df.describe().to_dict())
        

if __name__ == "__main__":
    app.run(debug=True)