def greatestCommonDivisor(a, b):
	lowest = min(a, b)
	highest = max(a, b)

	if lowest == 0:
		return highest
	elif lowest == 1:
		return 1
	else:
		return greatestCommonDivisor(lowest, highest%lowest)