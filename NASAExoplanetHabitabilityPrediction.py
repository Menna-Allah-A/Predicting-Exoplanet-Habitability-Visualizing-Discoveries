import pandas as pd # -> Store the data you will get from AI response in a Structred DataFrame


try :
    df = pd.read_csv('PSCompPars.csv')
    print(df.head())
except pd.errors.EmptyDataError:
    print("NO received Data")
except Exception as e:
    print("UnExpected error occured: ",e)        


keyColumns = [ # Identification
             'pl_name', 'hostname' ,
                #  Planet characteristics
              'pl_orbper', 'pl_orbsmax', 'pl_rade', 'pl_bmasse', 
              'pl_bmassprov', 'pl_eqt', 'pl_controv_flag',
              # Star characteristics
              'st_spectype', 'st_teff', 'st_rad', 'st_mass', 'st_met',
              # System characteristics
              'sy_snum', 'sy_pnum', 'sy_dist',
              # Discovery information
              'discoverymethod', 'disc_year', 'disc_facility']

df = df[keyColumns]










# BaseUrl = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars"
    #response = requests.get(BaseUrl) # -> Stores the response 
    #response.raise_for_status() # -> Rasies an error for bad status code 
    #data = response.json() # ->  Converts raw API data into a structure Python 
    #df = pd.DataFrame(data)  # -> Converts the JSON data into a Pandas DataFrame (a tabular structure)
    #df.to_csv('nasa_exoplanets.csv' , index= False) # -> index = false for removing index column 
#import requests  # ->allows Python to send HTTP requests (like GET/POST) to APIs or websites
                 # -> to Fetch the data 