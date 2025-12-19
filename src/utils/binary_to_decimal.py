def binary_to_decimal(binary_str: str) -> float:
    """Convert binary string (with fractional part) to decimal float."""
    if '.' in binary_str:
        int_part, frac_part = binary_str.split('.')
    else:
        int_part, frac_part = binary_str, ''

    # Integer part
    int_value = int(int_part, 2) if int_part else 0

    # Fractional part
    frac_value = 0
    for i, bit in enumerate(frac_part, start=1):
        frac_value += int(bit) * (2 ** -i)

    return int_value + frac_value