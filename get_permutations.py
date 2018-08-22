def getPermutations(string):
    if len(string) <= 1:
        return set([string])

    allCharsExceptLast = string[:-1]
    lastChar = string[-1]

    permutationsOfAllCharsExceptLast = getPermutations(allCharsExceptLast)

    permutations = set()
    for permutationOfAllCharsExceptLast in permutationsOfAllCharsExceptLast:
        for position in range(len(allCharsExceptLast) + 1):
            permutation = (
                permutationOfAllCharsExceptLast[:position]
                + lastChar
                + permutationOfAllCharsExceptLast[position]
            )
            permutations.add(permutation)

    return permutations