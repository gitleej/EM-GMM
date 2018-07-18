# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:00:10 2017

@author: Administrator
"""

"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    
    # TODO: Return the top n most frequent words.
    top_n = []
    n = s.split(' ')
    j = 0
    for i in range(len(n)):
        if n[i] in n[:i+1]:
            top_n[j][0] = n[i]
            top_n[j][1] = 
        
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()