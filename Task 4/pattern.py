# using for loop and if statement to output the star pattern same as row number until row 5
# using else statement for row 6 to 9 where star number is 10 - row number
for row_number in range(1, 10):
    if row_number <= 5:
        star_count = row_number
    else:
        star_count = 10 - row_number
    print ("*" * star_count)
