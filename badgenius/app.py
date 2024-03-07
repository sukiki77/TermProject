def run01():
    reduce_string = ''
    multiple_choice_answer = ''
    for i, char in enumerate(original_string):
        if i % 2 == 0:
            reduce_string += char
        else:
            multiple_choice_answer += char
    return reduce_string, multiple_choice_answer


def run02():
    expand_string = ''
    for i, char in enumerate(reduced_string):
        expand_string += char + multiple_choice_answers[i]
    return expand_string + multiple_choice_answers[len(reduced_string):]


original_string = "abcd" * 10
reduced_string, multiple_choice_answers = run01()
expanded_string = run02()
print("Original string:", original_string)
print("Reduced string:", reduced_string)
print("Expanded string:", expanded_string)
