#Name: Tran Quang Hien
#Student ID: GCS210109
#Class: GCS1003A

# Exercise 1:
# Prompt the user to enter their name
name = input("Type your name: ")

#Prompt the user to enter their age and convert it to an integer
age = int(input("Type your age: "))

#Prompt the user to enter their year of entrance and convert it to an integer
entrance = int(input("Type your entrance: "))

#Calculate the current year by subtracting the entrance year from 2023
year = 2023 - entrance

#Define a function to print the provided information
def get_information(name, age, entrance):
    #Print the name, age, and year of entrance
    print("My name is", name, ", I am", age, "years old", ", I am", entrance, "year student at Greenwich")

#Call the function to display the information
get_information(name, age, entrance)


#Exercise 2:
#Counts the number of words in a given text
def count_words(text):
    words = text.split()
    return len(words)

#Replaces a word in a given text at a specified order
def replace_words(text, order, word_replace):
    words = text.split()
    words[order] = word_replace
    return ' '.join(words)

#Prompt the user to enter the text
text = input("Enter the text: ")

#Count the number of words in the original text
word_count_original = count_words(text)

#Prompt the user to enter the number of words to replace
order = int(input("Enter the number of words you want to repalce with: "))

#Prompt the user to enter the replacement words
word_replace = input("Input the words to replace: ")

#Replace the specified word(s) in the text
text_modified = replace_words(text, order, word_replace)

#Count the number of words in the modified text
word_count_modified = count_words(text_modified)

#Define a function to print the number of words before and after modification
def change_word():
    print("---------------------------")

    #Print the number of words in the original text
    print(f"Number of words before modified: {word_count_original}")

    #Print the modified text that has been replaced
    print(f"Text modified: {text_modified}")
    
    #Print the number of words in the modified text
    print(f"Number of words after modified: {word_count_modified}")

#Call the function to display the information
change_word()