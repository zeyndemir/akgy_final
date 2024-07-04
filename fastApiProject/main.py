from fastapi import FastAPI
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
from typing import Dict, Any

app = FastAPI()


cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)


@app.get("/weather")
def get_weather() -> Dict[str, Any]:
    try:

        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": 39,
            "longitude": 35,
            "hourly": "temperature_2m,relative_humidity_2m",
            "start_date": "2024-07-03",
            "end_date": "2024-07-05"
        }
        responses = openmeteo.weather_api(url, params=params)
        response = responses[0]

        weather_info = {
            "coordinates": f"{response.Latitude()}°N {response.Longitude()}°E",
            "elevation": f"{response.Elevation()} m asl",
            "timezone": f"{response.Timezone()} {response.TimezoneAbbreviation()}",
            "utc_offset": f"{response.UtcOffsetSeconds()} s"
        }

        hourly = response.Hourly()
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
        hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()

        hourly_data = {
            "date": pd.date_range(
                start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
                end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
                freq=pd.Timedelta(seconds=hourly.Interval()),
                inclusive="left"
            )
        }
        hourly_data["temperature_2m"] = hourly_temperature_2m
        hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m

        hourly_dataframe = pd.DataFrame(data=hourly_data)
        weather_info["hourly_data"] = hourly_dataframe.to_dict(orient="records")

        return weather_info

    except Exception as e:
        return {"error": str(e)}

print(get_weather())

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

