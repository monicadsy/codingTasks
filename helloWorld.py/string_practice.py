original_string = "Hello world!"
new_string = original_string[0:5]
print(new_string)

# ************ Example 2 ************
original_string = "Hello world!"
original_string = original_string.upper()
print(original_string)
original_string = original_string.lower()
print(original_string)


# ************ Example 3 ************
print("Example 3: ")
sentence = "ThisHELLOisHELLOrandomHELLOtextHELLOweHELLOareHELLOgoingHELLOtoHELLOsplitHELLOapart"
split_sentence = sentence.split("HELLO")
print(split_sentence)

# ************ Example 4 ************
print("Example 4: ")
fact2 = "          The$first$electronic$computer$ENIAC$weighed$more$than$27$tons.          "
fact2 = fact2.replace("$", "WOW!")
print(fact2)
fact2 = fact2.strip()
print(fact2)
fact2 = fact2.split("WOW!")
print(fact2)

# ************ Example 5 ************
print("Example 5: ")
string_list = ["I", "like", "to", "join", "lists", "to", "make", "strings"]
list_joined = " ".join(string_list)
print(list_joined)

# ************ Example 6 ************
print("Example 6: ")
people = "Person 1 \nPerson 2"
print(people)

# ************ Example 7 ************
print("Example 7: ")
wage = "Person 1: \t 123.22"
print(wage)

# ************ Example 8 ************
print("Example 8: ")
sentence = "\"The escape character (\\) is a character which invokes an alternative interpretation of subsequent characters in a character sequence.\""
print(sentence) 