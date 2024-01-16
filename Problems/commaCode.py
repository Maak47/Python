# Problem 2
# Write a function that takes a list value as an argument and returns
# a string with all the items separated by a comma and a space, with and
# inserted before the last item. For example, passing the previous spam list to
# the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test
# the case where an empty list [] is passed to your function.


def commaCodeFunc(spam):
    if spam == []:
        print('There is no list to work with. Try Entering a list')

    else:
        # iterates the list till the last 2 items according to index
        for item in spam[:-2]:

            # prints every item in the list excluding the last 2 with a comma(,) and a space( ).
            print(str(item) + ',',  end=' ')

        # prints the last two items on the list with a ' and ' inbetween.
        print(str(spam[-2]) + ' and ' + str(spam[-1]))


spam = [[1, 2, 3], 2, 3, 4, 5]
commaCodeFunc(spam)
print(str(spam))
