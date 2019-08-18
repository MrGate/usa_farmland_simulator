#!/usr/bin/python
import csv
import sys

us_population_count = 327200000
current_used_acres = 253700000
acres_per_person = 0.5
# population multiplier is 4.4% of current value
population_multiplier = 0.044 
increase_per_year = 300000
starting_year = 2019

csv_rows = ['year', 'population', 'acres_needed']

def simulate_time(amount_of_loops, csv_filename):
	current_loop = 1
	loop_year = starting_year
	with open(csv_filename, 'w') as writeFile:
		writer = csv.writer(writeFile)
		header_rows = ['year', 'population', 'farmland']
		writer.writerow(header_rows)
		# Now we gonna do a loop to simulate the years.
		while ( loop_year < (starting_year + amount_of_loops)):
			new_acres_needed = ((current_loop * increase_per_year) + current_used_acres)
			population_increased = ((us_population_count * population_multiplier) + us_population_count)
			print("SIMULATING YEAR : " + str(loop_year) + "\n")
			amount_increased = (population_increased - us_population_count)
			print("Population (" + str(population_increased) + ") +" + str(amount_increased) + "\n")
			acres_increased = (new_acres_needed - current_used_acres)
			print("Farmland Needed (" + str(new_acres_needed) + ") +" + str(acres_increased) + "\n\n")
			# We are gonna save the results to a csv
			insert_csv_rows = [str(loop_year), str(population_increased), str(new_acres_needed)]
			writer.writerow(insert_csv_rows)
			# Increase year and loop counters
			loop_year += 1
			current_loop += 1
	# close csv file when done.
	writeFile.close()
	
# Lets run the simulation
print('Simulating US Farmland to Food Per Person.\n')

if len(sys.argv) == 3:
	outputfilename = sys.argv[2]
else:
	outputfilename = "sim_results.csv"
	
simulate_time(int(sys.argv[1]), outputfilename) 
