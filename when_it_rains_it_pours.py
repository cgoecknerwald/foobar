# Takes an array, assuming that index 0 and len(array) are proper boundaries
# Ex: [3, 1, 2] returns 1; [5, 1, 2, 2, 5] returns 10
def fill_helper(heights):
	# Any array of length 2 or less cannot be filled.
	if len(heights) <= 2:
		return 0;
	# Find the least height of the edges of the array
	min_boundary = min(heights[0], heights[-1])
	# Return the sum of the difference between the least boundary height and
	# the depth of the bottoms of the well. Can also be done with mapping
	# and a lambda function.
	return sum([min_boundary - el for el in heights[1:-1]])

# Recursive function that returns the area that is filled with water.
def answer_helper(heights, boundary=None):
	# Any array of length 2 or less cannot be filled. 
	if len(heights) <= 2:
		return 0

	# Locate the maximum value in the array
	max_index = heights.index(max(heights))

	# If this is a sub-array, boundary will be defined as 'left' or 'right'.
	# The 'left' or 'right' denotes the location in the array of the previously
	# found value that was a maximum- we do not want to re-find this value.

	# If 'left', locate the max_index that is NOT the previously found maximum.
	if boundary == 'left':
		max_index = heights[1:].index(max(heights[1:])) + 1
	# If 'right', locate the max_index that is NOT the previously found maximum.
	if boundary == 'right':
		max_index = heights.index(max(heights[:-1]))

	# If the boundary was defined, and the new max-index is on the edge, we can
	# send the array to fill_helper to find its fill.
	if max_index in (0, len(heights) - 1) and boundary:
		return fill_helper(heights)

	# Split the array into two parts, with a 'right' and 'left' focus, 
	# dependent on the location of the maximum value.
	# Ex: [3, 4, 5, 1] becomes [3, 4, 5] for 'left' and [5, 1] for 'right'.
	else:
		fill = answer_helper(heights[0:max_index + 1], 'right')
		return fill + answer_helper(heights[max_index:], 'left')

# This exists because foobar necessitates it. 
# This solution is much like a binary search, except it searches for wells.
def answer(heights):
	return answer_helper(heights)

