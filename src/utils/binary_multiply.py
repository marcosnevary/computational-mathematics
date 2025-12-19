from src.utils.multiply_integers import multiply_integers

def binary_multiply(bin1: str, bin2: str) -> str:
    """Multiply two binary numbers (supports fractions) directly in binary."""

    # Count fractional bits
    frac1 = len(bin1.split(".")[1]) if "." in bin1 else 0
    frac2 = len(bin2.split(".")[1]) if "." in bin2 else 0
    total_frac = frac1 + frac2

    # Remove binary points
    int_bin1 = bin1.replace(".", "")
    int_bin2 = bin2.replace(".", "")

    # Multiply as integers in binary
    prod_int = multiply_integers(int_bin1, int_bin2)

    # Insert binary point
    if total_frac > 0:
        if len(prod_int) <= total_frac:
            # Pad with leading zeros
            prod_int = prod_int.zfill(total_frac + 1)
        result = prod_int[:-total_frac] + "." + prod_int[-total_frac:]
    else:
        result = prod_int

    # Remove leading zeros (but keep at least one digit before '.')
    if "." in result:
        int_part, frac_part = result.split(".")
        int_part = int_part.lstrip("0") or "0"
        frac_part = frac_part.rstrip("0")  # optional: trim trailing zeros
        result = int_part + ("." + frac_part if frac_part else "")
    else:
        result = result.lstrip("0") or "0"

    return result