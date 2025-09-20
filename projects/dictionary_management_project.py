#MINI PROJECT
#Create a program that manages a dictionary of word meanings. The program should allow users to perform the 
#following actions:
#Add a Word: Allow users to add new words along with their meanings to the dictionary.
#Search for Meaning: Enable users to search for the meaning of a word in the dictionary.
#Display All Words: Provide an option to display all words and their meanings currently stored in the dictionary.
#Update Meaning: Implement a feature to update the meaning of an existing word in the dictionary.
#After updating, display the updated meaning.
#Delete Word: Implement a feature to delete a word and its meaning from the dictionary. Confirm the deletion and 
#handle cases where the word doesn't exist.
#Ensure the program handles invalid inputs gracefully. Use a while loop to keep the program running until the 
#user chooses to exit
dictionary = {}
while True:
    print("\nDictionary management system")
    print("1. Add a word")
    print("2. Search for Meaning")
    print("3. Display all words")
    print("4. Update meaning")
    print("5. Delete Word")
    print("6. Exit")
    choice = input("Enter the choice:")
    if choice == "1":
        word = input("Enter the word:").lower()
        meaning = input("Enter the meaning:")
        dictionary[word] = meaning
        print("word added successfully!")
    elif choice == "2":
        word = input("enter the word:").lower()
        if word in dictionary:
            print(f"{word}:{dictionary[word]}")
        else:
            print("word not found")
    elif choice == "3":
        if dictionary:
            print("\n All words in dictionary:")
            for word, meaning in dictionary.items():
                print(f"{word}:{meaning}")
        else:
            print("words not found in dictionary")
    elif choice == "4":
        word = input("enter the word:").lower()
        if word in dictionary:
            new_meaning = input("enter the meaning:")
            dictionary[word] = new_meaning
            print(f"word updated successfully {word} : {dictionary[word]}")
    elif choice == "5":
        word = input("enter the word:").lower()
        if word in dictionary:
            del dictionary[word]
            print("The word is deleted successfully")
        else:
            print("word not deleted")
    elif choice == "6":
        break

        
