def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    phrase = phrase.lower()
    freq_map = {}
    
    for char in phrase:
        if char in vowels:
            if char in freq_map:
                freq_map[char] += 1
            else:
                freq_map[char] = 1
                
    return freq_map
