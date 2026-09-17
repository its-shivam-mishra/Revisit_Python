"""
. Count total words in a string
. Count top K frequency of each word
. Find the most frequent word
. Count characters excluding spaces
. Find the longest and smallest word
. Count occurrences of a specific word
. Find duplicate words
. Length of each word
. Find first non-repeating word
. Count vowels and consonants
. Word Frequency (Most Asked Interview Question)
"""
text = "apple banana apple orange banana apple grape orange apple olw"

#Count total words in a string

def count_words(s):
    word=s.split()
    return len(word)

#print(count_words(text))

def ram(w,k):
    dic={}
    m=w.split()
    for i in m:
        if i in dic:
            dic[i]+=1
        else:dic[i]=1
    si=sorted(dic.items(),key=lambda x:x[1],reverse=True)
    print(si)
    return si[:k]

#print(ram(text,3))       


def mfw(w):
    dic={}
    for i in w.split():
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    return sorted(dic.items(),key= lambda x:x[1],reverse=True)[0], sorted(dic.items(),key= lambda x:x[1],reverse=True)[-1]

#print(mfw(text))

def count_characters(s):
    count=0
    for i in s:
        if i!=" ":
            count+=1
    return count

def longest_and_smallest_word(s):
    words=s.split()
    dic={}
    for i in words:
        if i not in dic:
            dic[i]=len(i)
    sorted_dic=sorted(dic.items(),key=lambda x:x[1])
    return sorted_dic[0],sorted_dic[-1]

#print(longest_and_smallest_word(text))
      
      

def find_duplicate_words(w):
    dic={}
    m=w.split()
    for i in m:
        if i in dic:
            dic[i]+=1
        else:dic[i]=1
    
    return filter(lambda x:x[1]>1,dic.items())

print(list(find_duplicate_words(text)))


