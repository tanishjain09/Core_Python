list = ["banana","litchi","apple"]
#.append() -> adds one elements at the end
list.append("cheery")
print(list)

#.sort() ->sort in ascending order
#also sort will work on list having homo data type only
list.sort()
print(list)

#.sort(reverse=True) -> sort in descending order
list.sort(reverse=True)
print(list)

#.reverse() ->reverse the list
list.reverse()
print(list)

#.insert(idx,ele) ->insert at particular index
list.insert(2,"pineapple")
print(list)

#.remove(ele) ->remove first occurence of element
list.remove("pineapple")
print(list)

#.pop(idx) ->remove value present at idx
list.pop(3)
print(list)

#many more list methods are present...

