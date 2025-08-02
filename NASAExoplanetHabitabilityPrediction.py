import requests  # ->allows Python to send HTTP requests (like GET/POST) to APIs or websites
                 # -> to Fetch the data 
import pandas as pd # -> Store the data you will get from AI response in a Structred DataFrame



BaseUrl = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&select=pl_name,pl_orbper,pl_rade,pl_bmasse,st_teff,st_rad&format=json"

try :

    response = requests.get(BaseUrl) # -> Stores the response 
    response.raise_for_status() # -> Rasies an error for bad status code 
    data = response.json() # ->  Converts raw API data into a structure Python 
    df = pd.DataFrame(data)  # -> Converts the JSON data into a Pandas DataFrame (a tabular structure)
    
    df.to_csv('nasa_exoplanets.csv' , index= False) # -> index = false for removing index column 

    NewData = pd.read_csv('nasa_exoplanets')
    print(NewData.head())
except requests.exceptions.RequestException as e :
    print("API Error:" , e)
except pd.errors.EmptyDataError:
    print("NO received Data")
except Exception as e:
    print("UnExpected error occured: ",e)        


