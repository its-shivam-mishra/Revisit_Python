#An iterator is an object that gives you one value at a time using next().

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))  # 10
print(next(iterator))  # 20
print(next(iterator))  # 30

'''
An iterator is an object that implements Python's `__iter__()` and `__next__()` methods and
allows us to retrieve data one item at a time. A generator is a simpler way to 
create an iterator using the `yield` keyword, with Python managing the iterator 
state automatically.

I prefer generators when I need lazy processing of large data, such as reading PDFs, 
processing RAG document chunks, streaming API responses, or processing large files without 
loading everything into memory. I would create a custom iterator when I need more
control over the iteration logic or state management.

So, in short: an iterator is the iteration mechanism, while a generator is an easy way to 
implement that mechanism.


'''
