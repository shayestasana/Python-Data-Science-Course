
# a phrase that is inputted by the user. The vowels must be replaced by "g" and then printed
'''
vowels -> g

example:
dog -> dgg
cat -> cgt
'''

def translate(phrase):
    translation= ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation+="G"
            else:
                translation+="g"
        else:
            translation+=letter
    return translation


print(translate(input("Enter a phrase: ")))