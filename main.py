# source : https://datahelpdesk.worldbank.org/knowledgebase/articles/898581-api-basic-call-structures

import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


# get status code of the API below and raise exception in case of HTTP errors
URL = 'https://api.worldbank.org/v2/country/gr/indicator/NY.GDP.MKTP.CD?format=json'

try:
    response_API = requests.get(URL)
    response_API.raise_for_status()
    print("status_code: ", response_API.status_code, "\n")
except requests.exceptions.HTTPError as err:
    raise SystemExit(err)

# generate json object obj
data = response_API.text
obj = json.loads(data)

# print element 0 of json object 0 to inspect json structure
gdp = json.dumps(obj[1][0], indent=4)
print("example :\n", gdp, "\n")

# generate lists year_list, gdp_list parsing the json object obj
year_list = [obj[1][i]["date"] for i in reversed(range(len(obj[1][:])))]
gdp_list = [obj[1][i]["value"] for i in reversed(range(len(obj[1][:])))]

# calling DataFrame constructor after zipping both lists
df = pd.DataFrame(list(zip(year_list, gdp_list)), columns=["year", "gdp"])
print("last 5 rows of pandas dataframe: ", "\n", df.tail(), "\n")

# plot Greek GDP
fig, ax = plt.subplots()
ax.plot(df["year"], df["gdp"], linestyle="--", marker="o")
first_year = min(df["year"])
last_year = max(df["year"])
ax.set_title(f"Greek GDP in USD($) from {first_year} until {last_year}", fontweight="bold")
ax.set_xlabel("Year", fontweight ='bold')
ax.set_ylabel("GDP ($)", fontweight ='bold')
ax.xaxis.set_major_locator(MultipleLocator(7))

plt.show()
