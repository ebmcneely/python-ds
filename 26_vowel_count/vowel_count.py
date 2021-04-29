def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    low_phrase = phrase.lower()
    vowel_count_dict = {}
    only_vowels = [char for char in low_phrase if char in ['a','e','i','o','u']]
    for char in only_vowels:
        vowel_count_dict[char] = only_vowels.count(char)
    return vowel_count_dict
