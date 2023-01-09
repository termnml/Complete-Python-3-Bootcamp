# %%
my_list = [1, 2, 3]
my_list.append(42)
my_list.append("foo")
my_list

# %%
# pop removes (pops) last item by default
my_list = ['foo', 'bar', 'baz']
print("List: ", my_list)
print("pop default (last): ", my_list.pop())
print("pop first (0): ", my_list.pop(0))
print("List: ", my_list)

# %%
new_list = ['a', 'x', 'b', 'w', 'r']
num_list = [2, 8, 3, 6, 9, 0]
# sorts in-place
# clone list if you want to have both
sorted_list = new_list[:]
sorted_list.sort()
print(new_list, "\n", sorted_list)

# %%
# assign nothing because
# inplace sorting returns nothing
my_list = [1, 2, 3, 4]
my_list = my_list.sort()
type(my_list)

# %%
