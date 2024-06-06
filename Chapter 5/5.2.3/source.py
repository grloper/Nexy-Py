from itertools import product

# הכמויות המוגבלות של כל סוג שטר
limits = {
    20: 3,
    10: 5,
    5: 2,
    1: 5
}

# סכום היעד
target = 100

# יצרנו את כל הקומבינציות האפשריות במסגרת המגבלות
combinations = [
    (twenty * 20 + ten * 10 + five * 5 + one * 1, twenty, ten, five, one)
    for twenty in range(limits[20] + 1)
    for ten in range(limits[10] + 1)
    for five in range(limits[5] + 1)
    for one in range(limits[1] + 1)
]

# סינון הקומבינציות שסכומן שווה ל-100
valid_combinations = [
    (twenty, ten, five, one) for total, twenty, ten, five, one in combinations if total == target
]

# הדפסת התוצאות
print("הקומבינציות האפשריות ליצירת סכום של 100 דולרים הן:")
for combination in valid_combinations:
    print(f"20$: {combination[0]}, 10$: {combination[1]}, 5$: {combination[2]}, 1$: {combination[3]}")

# הדפסת מספר האפשרויות
print("מספר האפשרויות הוא:", len(valid_combinations))
