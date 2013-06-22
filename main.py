def combinations(elements, size):
	if len(elements) == size or size == 1:
		return elements

	ret = []
	for i, item in enumerate(elements):
		for j in combinations(elements[i + 1:], size - 1):
			ret.append(item + j)
	return ret


def variations(elements, size):
	ret = []
	for i in combinations(elements, size):
		ret.extend(permutations(i))
	return ret


def permutations(elements):
	if len(elements) <= 1:
		return elements

	ret = []
	for i, item in enumerate(elements):
		for j in permutations(elements[:i] + elements[i + 1:]):
			ret.append(item + j)
	return ret


def main():
	input = ["a", "b", "c", "d", "f"]
	print "Input {}:".format(input)
	print "Combinations:"
	print combinations(input, 3)
	print "Permutations:"
	print permutations(input)
	print "Variations:"
	print variations(input, 3)



if __name__ == '__main__':
	main()