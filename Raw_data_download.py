from pathlib import Path
# urlretrieve: download tool
from urllib.request import urlretrieve
import time

# Set location and creat folder for raw data
save_folder = Path(__file__).resolve().parent / "Data" / "raw data"
##creat folder if not exist
save_folder.mkdir(parents=True, exist_ok=True)


###################################################################################
### Flight data download from BTS (Bureau of Transportation Statistics) website
######################################################################################

## Set the base URL and construct the download URL for the specific year and month
base_url = "https://transtats.bts.gov/PREZIP/"

# download_url from 2022 Jan to 2026 Jul
for year in range(2022, 2027):

    if year == 2026:
        year_month = 7
    else:
        year_month = 12

    for month in range(1, year_month + 1):

        #download address
        file_name = f"On_Time_Reporting_Carrier_On_Time_Performance_1987_present_{year}_{month}.zip"
        download_url = base_url + file_name

        # save path
        flight_folder = save_folder / "bts"
        flight_folder.mkdir(parents=True, exist_ok=True)
        save_path = flight_folder / f"bts_{year}_{month}.zip"
        save_temporary_path = flight_folder / f"bts_{year}_{month}.part"

        # download
        print("Downloading：", year, month)

        if save_path.exists():
            print("Download complete：", year, month)
            continue

        else:
            ## Download the file and rename it to the final path
            urlretrieve(download_url, save_temporary_path)
            save_temporary_path.rename(save_path)

        print("Download complete：", year, month)

print("All months downloaded.")



###############################################################################
### Weather data download from 
################################################################################
## Download
weather_folder = save_folder / "Weather"
weather_folder.mkdir(parents=True, exist_ok=True)

### 1. Historical hourly weather, 1999–2021
# Same download as the BOS weather above, repeated for each station and year.
history_folder = weather_folder / "history"
history_folder.mkdir(parents=True, exist_ok=True)
stations = {"BOS": "MA_ASOS", "DCA": "VA_ASOS", "LGA": "NY_ASOS",
            "JFK": "NY_ASOS", "ORD": "IL_ASOS", "PHL": "PA_ASOS"}

for station, network in stations.items():
    # Local midnight on January 1 is 06:00 UTC in Chicago and 05:00 at the other stations.
    midnight = "06:00:00Z" if station == "ORD" else "05:00:00Z"
    for year in range(1999, 2027):
        save_path = history_folder / f"{station}_{year}.csv"
        if save_path.exists():
            continue

        history_url = "https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?"
        history_url += f"station={station}&network={network}"
        # Wind, visibility, the weather report text, and cloud cover/height at four layers.
        history_url += "&data=tmpf,relh,sknt,gust,vsby,metar,skyc1,skyl1,skyc2,skyl2,skyc3,skyl3,skyc4,skyl4"
        if year == 2026:
            august_midnight = "05:00:00Z" if station == "ORD" else "04:00:00Z"
            history_url += f"&sts={year}-01-01T{midnight}&ets=2026-08-01T{august_midnight}"
        else:
            history_url += f"&sts={year}-01-01T{midnight}&ets={year + 1}-01-01T{midnight}"
        history_url += "&tz=UTC&report_type=3&format=onlycomma&missing=M&latlon=no&elev=no"

        print("Downloading historical weather:", station, year)
        save_temporary_path = save_path.with_suffix(".part")
        time.sleep(2)  # 每次下载前等 2 秒
        urlretrieve(history_url, save_temporary_path)
        save_temporary_path.rename(save_path)


### 2. BOS airport forecasts (TAF), one ZIP per month
taf_folder = weather_folder / "taf"
taf_folder.mkdir(parents=True, exist_ok=True)

for year in range(2021, 2027):
    # Include forecasts issued just before the first January 2022 flights.
    first_month = 12 if year == 2021 else 1
    last_month = 7 if year == 2026 else 12
    for month in range(first_month, last_month + 1):
        save_path = taf_folder / f"TAFBOS_{year}_{month:02d}.zip"
        if save_path.exists():
            continue

        start = f"{year}-{month:02d}-01"
        if year == 2021:
            start = "2021-12-30"
        if month == 12:
            end = f"{year + 1}-01-01"
        else:
            end = f"{year}-{month + 1:02d}-01"

        taf_url = "https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py?"
        taf_url += f"pil=TAFBOS&sdate={start}T00:00Z&edate={end}T00:00Z&fmt=zip&limit=9999&order=asc"
        print("Downloading BOS forecasts:", year, month)
        save_temporary_path = save_path.with_suffix(".part")
        time.sleep(2)  # 每次下载前等 2 秒
        urlretrieve(taf_url, save_temporary_path)
        save_temporary_path.rename(save_path)


### 3. Airport time zones, one file for matching scheduled arrival times
airport_path = save_folder / "airports.dat"
if not airport_path.exists():
    airport_url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat"
    save_temporary_path = airport_path.with_suffix(".part")
    urlretrieve(airport_url, save_temporary_path)
    save_temporary_path.rename(airport_path)
