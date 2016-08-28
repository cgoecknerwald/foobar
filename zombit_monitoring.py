# Check if list of lists already contains a list.
def shift_exists(all_shifts, specific_shift):
	for shift in all_shifts:
		if (specific_shift[0] == shift[0] and specific_shift[1] == shift [1]):
			return True
	return False


# Merge two shifts.
def combine(shift1, shift2):
    total_shift = [min(shift1[0], shift2[0]), max(shift1[1], shift2[1])]
    return total_shift

# Main function definition; calculates total monitoring time.
def answer(intervals):
    # Sort intervals based on start time.
    intervals.sort(key = lambda x: x[0]);
    # Merge all shifts, as relevant.
    merged_shifts = []
    index = 0
    # Primary interval to merge. Changes when merges are complete.
    primary_focus = intervals[index]

    # While loop will merge shifts as necessary. Could be separate function, but no.
    while (index < len(intervals)):
        # The second interval to merge is the current interval.
        secondary_focus = intervals[index]
        
        # If the two intervals should be merged, do so.
        if (primary_focus[1] >= secondary_focus[0]):
        	primary_focus = combine(primary_focus, secondary_focus)

       	# Otherwise, select a new primary interval. 
        else:
        	# Only append the combined shifts when changing primary_focus
        	merged_shifts.append(primary_focus)
        	primary_focus = secondary_focus
        index += 1
    # If the last primary_focus never got added.
    if not shift_exists(merged_shifts, primary_focus):
    	merged_shifts.append(primary_focus)

    # Calculate the total monitoring time, based on merged shifts.
    total_time = 0
    for shift in merged_shifts:
    	total_time += shift[1] - shift[0]
    return total_time

# Testing.
intervals = [[1, 3], [3, 6]]

print answer(intervals)


