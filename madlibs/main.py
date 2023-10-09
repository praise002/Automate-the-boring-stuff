
def mad_libs():
    adjective = input('Enter an adjective: ')
    noun = input('Enter an noun: ').capitalize()
    verb = input('Enter an verb: ')
    noun_2 = input('Enter an noun: ')
    sentence = f'The {adjective} panda walked to the {noun} and then {verb}. A nearby {noun_2} was unaffected by these events.'
    return sentence

if __name__ == '__main__':
    print(mad_libs())
