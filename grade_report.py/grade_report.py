score = {72, 45, 90, 61, 38}

passed = 0
failed = 0
total = 0

for score in scores:
    if score>= 80:
        grede = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:   
        grade = "F"

    print(f"Score: {score}, Grade: {grade}")

total = total + score

if score >= 50:
    passed = passed + 1
else:
    failed = failed + 1

average = total / len(scores)

print("passed:", passed)
print("failed:", failed)
print("average:", round(average, 1))

