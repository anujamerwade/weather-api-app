from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

variable = "hello"
stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[['STAID', 'STANAME                                 ']]
@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())  # will look for templates folder by default

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    print(df.head())
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze()/10
    print(date)
    return {"station": station, "temperature": temperature, "date": date}

if __name__ == "__main__":
    app.run(debug=True) # add port param to change port number
