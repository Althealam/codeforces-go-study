import random

# Confirmation:
# 1. is it possible to have duplicated keys or values?
# keys must be unique, and values can be dudplicated
# (10, "a"), (20, "a")


class RandomMagicMap:
    """
    Design and implement a data structure RandomMagicMap that supports the following operations
    in average O(1) time complexity.

    Operations:

    1. put(key, value)
       Insert a key-value pair into the data structure.
       - If the key does not exist, insert the new key-value pair.
       - If the key already exists, update its corresponding value.

    2. get(key)
       Return the value associated with the given key.
       - If the key exists, return the value.
       - If the key does not exist, return None.

    3. remove(key)
       Remove the key-value pair associated with the given key.
       - If the key exists, remove it from the data structure.
       - If the key does not exist, do nothing.

    4. size()
       Return the number of key-value pairs currently stored in the data structure.

    5. getRandomValue()
       Return a random value from the data structure.
       - Each value stored in the structure should have the same probability of being returned.
       - This method will only be called when the data structure is non-empty.

    Constraints:
    - All operations (put, get, remove, size, getRandomValue) should run in average O(1) time.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_to_index = {}
        self.nums = []

    def put(self, key, value): # time: O(1)
        """
        Insert or update a key-value pair.

        :param key: The key to insert or update.
        :param value: The value associated with the key.
        """
        if key in self.key_to_index:
            index = self.key_to_index[key]
            self.nums[index] = (key, value)
        else:
            index = len(self.nums)
            self.key_to_index[key] = index
            self.nums.append((key, value))


    def get(self, key): # time: O(1)
        """
        Get the value associated with a key.

        :param key: The key to look up.
        :return: The value associated with the key, or None if the key does not exist.
        """
        if key not in self.key_to_index:
            return None
        index = self.key_to_index[key]
        return self.nums[index][1]

    def remove(self, key): # time: O(1)
        """
        Remove a key-value pair from the data structure.

        :param key: The key to remove.
        """
        if key not in self.key_to_index:
            return
        
        remove_index = self.key_to_index[key]
        last_key, last_value = self.nums[-1]

        # move last element into remove position
        self.nums[remove_index] = (last_key, last_value)
        self.key_to_index[last_key] = remove_index

        # remove last
        self.nums.pop()
        del self.key_to_index[key]
        

    def size(self): # time: O(1)
        """
        Return the number of key-value pairs currently in the data structure.

        :return: Integer representing the size.
        """
        return len(self.nums)

    def getRandomValue(self): # time: O(1)
        """
        Return a random value from the data structure.

        :return: A randomly selected value.
        """
        key, value = random.choice(self.nums)
        return value


m = RandomMagicMap()
m.put("a", 10)
m.put("b", 10)
m.put("c", 30)
print(m.get("b"))