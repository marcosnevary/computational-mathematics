def multiply_integers(bin1: str, bin2: str) -> str:
    """Helper: multiply two integer binary strings."""
    bin1 = bin1[::-1]
    bin2 = bin2[::-1]
    result = [0] * (len(bin1) + len(bin2))

    for i in range(len(bin1)):
        for j in range(len(bin2)):
            result[i + j] += int(bin1[i]) * int(bin2[j])

    for k in range(len(result)):
        if result[k] >= 2:
            carry = result[k] // 2
            result[k] %= 2
            result[k + 1] += carry

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return ''.join(map(str, result[::-1]))