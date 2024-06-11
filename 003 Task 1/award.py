swimming_time = x #minutes
running_time = y #minutes
cycling_time = z #minutes
sum_time = x + y + z
print(sum_time)
if sum_time <= 100:
    print("Award: Provincial colours")
elif sum_time < 105 & sum_time >= 101:
    print("Award: Privincial half colors")
elif sum_time < 110 & sum_time >= 106:
    print("Award: Privincial scroll")
else:
    print("No award")