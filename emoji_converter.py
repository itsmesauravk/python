def greet_user(name):  #the given name is parameter
    print(f'hello and welcome to {name}')

greet_user("New York")  #and the passed value to parameter is argument


#keyword argument 
# defining the values for parameters while passing the arguments
def name(first,last):
    print(f'first name :{first}{last}')


name(last="karki",first="Saurav")


#returning function
#converter
def converter(word):
    message = word.split()
    meaning = {
        'happy': 'smily',
        'not_happy': "sad"
    }
    result = ''
    for words in message:
        result += meaning.get(words,words) + ' '
    return result


word = input(":enter > ")
print(converter(word))


    