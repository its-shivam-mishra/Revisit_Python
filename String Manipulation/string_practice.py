def string_practice():

    text = "   Python is Easy and Python is Powerful   "

    print("Original String:")
    print(text)

    # 1. strip() - remove spaces from beginning and end
    print("\n1. strip():")
    print(text.strip())

    # 2. lstrip() - remove left spaces
    print("\n2. lstrip():")
    print(text.lstrip())

    # 3. rstrip() - remove right spaces
    print("\n3. rstrip():")
    print(text.rstrip())

    # 4. lower() - convert to lowercase
    print("\n4. lower():")
    print(text.lower())

    # 5. upper() - convert to uppercase
    print("\n5. upper():")
    print(text.upper())

    # 6. title() - first letter of each word uppercase
    print("\n6. title():")
    print(text.title())

    # 7. replace() - replace text
    print("\n7. replace():")
    print(text.replace("Python", "Java"))

    # 8. find() - find position
    print("\n8. find():")
    print(text.find("Python"))

    # 9. count() - count occurrences
    print("\n9. count():")
    print(text.count("Python"))

    # 10. startswith()
    print("\n10. startswith():")
    print(text.strip().startswith("Python"))

    # 11. endswith()
    print("\n11. endswith():")
    print(text.strip().endswith("Powerful"))

    # 12. split() - string to list
    print("\n12. split():")
    words = text.strip().split()
    print(words)

    # 13. join() - list to string
    print("\n13. join():")
    print("-".join(words))

    # 14. len() - length
    print("\n14. len():")
    print(len(text))

    # 15. slicing
    print("\n15. slicing:")
    print(text.strip()[0:6])

    # 16. reverse string
    print("\n16. reverse:")
    print(text.strip()[::-1])

    # 17. sorted() - sort characters
    print("\n17. sorted():")
    print(sorted("listen"))

    # 18. isalpha()
    print("\n18. isalpha():")
    print("Python".isalpha())

    # 19. isdigit()
    print("\n19. isdigit():")
    print("12345".isdigit())

    # 20. isalnum()
    print("\n20. isalnum():")
    print("Python123".isalnum())

    # 21. isspace()
    print("\n21. isspace():")
    print("   ".isspace())


string_practice()