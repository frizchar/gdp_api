# source : https://datahelpdesk.worldbank.org/knowledgebase/articles/898581-api-basic-call-structures

import fetch_api_data as fad
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


if __name__ == "__main__":
    population_url = "https://api.worldbank.org/v2/country/gr/indicator/SP.POP.TOTL?format=json"
    df = fad.bring_data(population_url)
    print("last 5 rows of pandas dataframe: ", "\n", df.tail(), "\n")

    # plot Greek population
    fig, ax = plt.subplots()
    ax.plot(df["year"], df["population"], linestyle="--", marker="o")
    first_year = min(df["year"])
    last_year = max(df["year"])
    ax.set_title(f"Greek Population from {first_year} until {last_year}", fontweight="bold")
    ax.set_xlabel("Year", fontweight='bold')
    ax.set_ylabel("Population", fontweight='bold')
    ax.xaxis.set_major_locator(MultipleLocator(7))

    plt.show()
