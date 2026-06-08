#Creating a dictionary with 4 words and thier dwfinations
programming_dictionary = {
    "Bug" : "An error or flaw in a computer program that causes it to behave unexpectedly.",
    "String" : "A sequence of charaters, like text, enclosed in quotation marks.",
    "Loop" : "A piece of code that repeats a set of instructions until a specific condition is met.",
    "Variable" : "A container or storage location used to hold data that can change."

}

#how to look up a word inside your dictionary
word_to_find = "Loop"
print(f"The definition of {word_to_find} is:")
print(programming_dictionary[word_to_find])