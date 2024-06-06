import winsound

# מילון תדרים
freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
        }

# מחרוזת תווים
notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

# פיצול מחרוזת התווים לפי תו המקף
notes_list = notes.split("-")

# בדיקת סוג האובייקט המתקבל
print(type(notes_list))  # יציג: <class 'list'>

# נגינת השיר באמצעות לולאת for
for note in notes_list:
    # פיצול תו ומחלקת זמן
    note_info = note.split(",")
    note_name = note_info[0]
    note_duration = int(note_info[1])

    # נגינת תו בודד
    winsound.Beep(freqs[note_name], note_duration)

# נגינת השיר באמצעות פונקציית next
note_iterator = iter(notes_list)

while True:
    # פיצול תו ומחלקת זמן
    note_info = next(note_iterator).split(",")
    note_name = note_info[0]
    note_duration = int(note_info[1])

    # נגינת תו בודד
    winsound.Beep(freqs[note_name], note_duration)
