import requests
import pandas as pd

# Define the API endpoint for the exoplanet archive
url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"

# Define the query to retrieve exoplanet names and coordinates
query = """
SELECT 
    pl_name AS planet_name, 
    ra AS right_ascension, 
    dec AS declination 
FROM 
    ps_1_exoplanet 
WHERE 
    pl_name IS NOT NULL
"""

# Send the request
response = requests.post(url, data={'query': query, 'format': 'csv'})

# Check if the request was successful
if response.status_code == 200:
    # Read the CSV data into a DataFrame
    exoplanets = pd.read_csv(pd.compat.StringIO(response.text))
    print(exoplanets)
else:
    print("Error fetching data:", response.status_code)
