# Create the lists below
station_names= None
station_start_years= None
# YOUR CODE HERE
station_names= list(('lighthouse', 'Harmaja', 'Suomenlinna', 'Kumpula', 'Kaisaniemi'))
station_start_years= list((2003,1989, 2016, 2005, 1844))


# This is a test cell that checks that the list lengths are correct
# Running this cell should not produce any errors
assert len(station_names) == 5, 'The station_names list should have 5 items.'
assert len(station_start_years) == 5, 'The station_start_years list should have 5 items.'

# This is a test cell that checks that the first item in the lists is correct
# Running this cell should not produce any errors
assert station_names[0] == 'lighthouse', 'The first item in the station_names list should be "lighthouse"'
assert station_start_years[0] == 2003, 'The first item in the station_start_years list should be 2003'
# Add the additional stations to the lists below

# YOUR CODE HERE
station_names.append("Malmi airfield")
station_names.append("Vuosaari harbour")
station_names.append("Kaivopuisto")
station_start_years.append(1937)
station_start_years.append(2012)
station_start_years.append(1904)

# This is a test cell that checks that the list lengths are correct
# Running this cell should not produce any errors
assert len(station_names) == 8, 'The station_names list should have 8 items.'
assert len(station_start_years) == 8, 'The station_start_years list should have 8 items.'
# This is a test cell that checks that the last item in the lists is correct
# Running this cell should not produce any errors
assert station_names[-1] == 'Kaivopuisto', 'The last item in the station_names list should be "Kaivopuisto"'
assert station_start_years[-1] == 1904, 'The last item in the station_start_years list should be 1904'
# Sort the lists as directed below
station_names.sort()
station_start_years.sort(reverse=True)
# This is a test cell that checks that the last item in the lists is correct
# Running this cell should not produce any errors
assert station_names[0] == 'Harmaja', 'The first item in the station_names list should be "Harmaja"'
assert station_start_years[0] == 2016, 'The first item in the station_start_years list should be 2016'

