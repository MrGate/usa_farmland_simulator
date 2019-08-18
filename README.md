# usa_farmland_simulator

A simple farmland to population simulator.
The purpose is to estimate the amount of land that will be used over the
next {x} amount of years.

This was also just a fun tiny project to do in python.

Example Usage
./sim.py {years} {output_csv_filename}

{years} = amount of years you want the simulation to run. *Required Param
{output_csv_filename} = is if you want to supply a output filename *Optional (Default : sim_results.csv)


Example Output: 

[CONSOLE] : Simulating US Farmland to Food Per Person.
[CONSOLE] : SIMULATING YEAR : 2019
[CONSOLE] : Population (341596800.0) +14396800.0
[CONSOLE] : Farmland Needed (254000000) +300000
[CONSOLE] : SIMULATING YEAR : 2020
[CONSOLE] : Population (341596800.0) +14396800.0
[CONSOLE] : Farmland Needed (254300000) +600000
[CONSOLE] : SIMULATING YEAR : 2021
[CONSOLE] : Population (341596800.0) +14396800.0
[CONSOLE] : Farmland Needed (254600000) +900000
... {how ever many years you want}


If you want to adjust this, google is a amazing resources to find the values you need about your population growth to increase of farmland per year. etc...
