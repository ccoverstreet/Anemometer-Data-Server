# Private EcoWitt Anemometer Server

This project is part of an evaluation of wind energy using Ecowitt's anemometers and wifi modules. Unfortunately, the Ecowitt wifi modules we received seem to be unable to use their cloud service and there is no way to easily update the new firmware. Additionally, leaving the default cloud route enabled with this flaw causes the entire device to hang indefinitely as it repeatedly sends requests to a server it cant reach. This server is meant to sit on the same local network as the anemometers and record the data. 

This implementation isn't very security focused, however, the minimum amount of functionality is exposed through a simple HTTP API. The anemometers send their data on the `/dump` route and the server logs the submitted data. Every hour, the current data in memory is dumped to a CSV file with the name `<moduleid>-<dumptime>`. On the `/` route is a bare HTML page that has a button for requesting a zip of all current data and a JSON prettified output of the current data in memory.

## Design Parameters

- Server Sample Rate: 1/60 seconds
- Data to store:
  - Unix Time (from dateutc)
  - Temperature (stored in C)
  - Humidity (percent)
  - Pressure (inches of mercury)
  - Wind Direction (Degrees from N, need to check this)
  - Wind Speed (m/s)
  - Wind Gust (m/s)
  - Solar Radiation (W/m^2?)
  - Battery Level (W-hr)
- Wifi Module Sends Post Request with URL encoded body
  - For setup:
    - Enter ip address of this server
	- Enter path "/dump"
	- Enter port 8080
	- Enter interval 60 seconds

___
**IMPORTANT: This math is just a rough estimate. May not reflect implementation**

Given the above, each timestep requires 72 bytes of memory. Before dumping in a 24 hour period, there would be 103 kB of data in memory. If stored as a CSV, it will take ~240 bytes to store each timestep. The end file size for a 24-hour period would be ~350 kB.

For analysis, these CSV's will likely be combined into larger chunks and then plotted using Python. 

## TODO

- Implement some kind of dashboard that allows you to see status/download data files
- Create simple Python script to plot all data of a certain prefix
