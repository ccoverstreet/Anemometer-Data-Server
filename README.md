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

Given the above, each timestep requires 72 bytes of memory. Before dumping in a 24 hour period, there would be 103 kB of data in memory. If stored as a CSV, it will take ~240 bytes to store each timestep. The end file size for a 24-hour period would be ~350 kB.

For analysis, these CSV's will likely be combined into larger chunks and then plotted using Python. 
