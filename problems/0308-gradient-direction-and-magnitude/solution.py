import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	mag = sum([grad**2 for grad in gradient])**0.5
	if mag == 0:
		return {'magnitude': 0.0, 'direction': [0.0 for grad in gradient], 'descent_direction': [0.0 for grad in gradient]}
	direc = [grad/mag for grad in gradient]
	desc_dir = [-c for c in direc]
	
	return {'magnitude': mag, 'direction': direc, 'descent_direction': desc_dir}