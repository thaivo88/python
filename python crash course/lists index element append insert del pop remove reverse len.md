List:
list = is a collection of items in a particular order
square brackets ([]) indicate a list, and individual elements in the list are separated by commas.
```
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```
```
['trek', 'cannondale', 'redline', 'specialized']
```
If you ask Python to print a list, Python returns its representation of the
list, including the square brackets:


Indexing:
you can access any element in a list by telling Python the position, or index, of the item desired.
Indexing start with 0 from the left to right or
-1 from the right to left (-1, Python always returns the last item in the list)
```
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
```
```
trek
```


Element:
To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new
value you want that item to have.
```
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# modifying the first element of the list
motorcycles[0] = 'ducati'
print(motorcycles)
```
```
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki']
```



append
The simplest way to add a new element to a list is to append the item to the list. When you append an item to a list, the new 
element is added to the end of the list.
```
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
```
```
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']
```

insert:
You can add a new element at any position in your list by using the insert() method. You do this by specifying the index of the 
new element and the value of the new item.
```
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
```
```
['ducati', 'honda', 'yamaha', 'suzuki']
```



del:
If you know the position of the item you want to remove from a list, you can use the del statement.
```
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
```
```
['honda', 'yamaha', 'suzuki']
['yamaha', 'suzuki']
```



pop:
The pop() method removes the last item in a list, but it lets you work with that item after removing it.
```
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
```
```
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
suzuki
```

You can use pop() to remove an item from any position in a list by including the index of the item you want to remove in
parentheses.
```
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
```
```
The first motorcycle I owned was a Honda.
```



remove:
If you only know the value of the item you want to remove, you can use the remove() method.
```
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
```
```
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']
```
The remove() method deletes only the first occurrence of the value you specify. If there’s a possibility the value appears more 
than once in the list, you’ll need to use a loop to make sure all occurrences of the value are removed.



sort:
Python’s sort() method makes it relatively easy to sort a list; change the order of the list to store them alphabetically.
```
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
```
```
['audi', 'bmw', 'subaru', 'toyota']
```
You can also sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method.
    cars.sort(reverse=True)

sorted:
To maintain the original order of a list but present it in a sorted order, you can use the sorted() function. The
sorted() function lets you display your list in a particular order but doesn’t affect the actual order of the list.
    sorted(cars)



reverse:
To reverse the original order of a list, you can use the reverse() method.
```
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
```
```
['subaru', 'toyota', 'audi', 'bmw']
```
Notice that reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list.
The reverse() method changes the order of a list permanently.



len:
You can quickly find the length of a list by using the len() function.
    len(cars)
    






