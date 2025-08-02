import requests  # -> to make an API request  
import pandas as pd



BaseUrl = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_name,pl_orbper,pl_rade,pl_bmasse,st_teff,st_rad&format=json"

response = requests.get(BaseUrl)
data = response.json()
df = pd.DataFrame(data)
