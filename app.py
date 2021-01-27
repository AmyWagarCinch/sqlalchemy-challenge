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


@app.route("/normal")
def normal():
    return hello_dict


@app.route("/jsonified")
def jsonified():
    return jsonify(hello_dict)


if __name__ == "__main__":
    app.run(debug=True)