# suite de Conway

def next_number(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)

def generate_sequence(depth):
    sequence = "1"
    for _ in range(depth - 1):
        sequence = next_number(sequence)
    return sequence

depth = 15
sequence = generate_sequence(depth)
print(f"à la profondeur {depth} c'est cette séquence : {sequence}")

depth = 40
sequence = generate_sequence(depth)
print(f"à la profondeur {depth} c'est cette séquence : {sequence}")
