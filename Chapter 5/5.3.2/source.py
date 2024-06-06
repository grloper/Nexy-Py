def create_music_notes_iterator():
    """
    Creates an iterator that yields musical note frequencies in the specified order:
    - All notes in La
    - All notes in Si
    - ... (following the order in the table)
    """

    notes_table = {
        "La": [55, 110, 220, 440, 880],
        "Si": [61.74, 123.48, 246.96, 493.92, 987.84],
        "Do": [65.41, 130.82, 261.64, 523.28, 1046.56],
        "Re": [73.42, 146.84, 293.68, 587.36, 1174.72],
        "Mi": [82.41, 164.82, 329.64, 659.28, 1318.56],
        "Fa": [87.31, 174.62, 349.24, 698.48, 1396.96],
        "Sol": [98, 196, 392, 784, 1568],
    }

    note_order = ["La", "Si", "Do", "Re", "Mi", "Fa", "Sol"]  # Order of notes

    for note in note_order:
        for frequency in notes_table[note]:
            yield frequency

# Example usage
notes_iter = create_music_notes_iterator()
for freq in notes_iter:
    print(freq)
