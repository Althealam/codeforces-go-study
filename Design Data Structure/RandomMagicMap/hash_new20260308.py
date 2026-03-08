# key_value = {} e.g: key_value = {1: "a", 2: "b", 3: "c"}
# key_array = [] e.g: key_array = [1, 2, 3]
# key_index = {} e.g: key_index = [1: 0, 2: 1, 3: 2]

# remove
# 1. del key_value[key]
# 2. delete_index = key_index[key]
# 3. swap with the last element: delete(2)==>[1, 3, 2], {1: 0, 2: 2, 3: 1}, {1: "a", 2: "b", 3: "c"} ==> [1, 3], {1:0, 3:1}, {1: "a", 3: "c"}



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
        self.key_value = {}
        self.key_array = []
        self.key_index = {}


    def put(self, key, value):
        """
        Insert or update a key-value pair.

        :param key: The key to insert or update.
        :param value: The value associated with the key.
        """
        if key in self.key_value:
            self.key_value[key] = value
            current_index = self.key_index[key]
            self.key_array[current_index] = key
        else:
            self.key_value[key] = value
            self.key_index[key] = len(self.key_index)
            self.key_array.append(key)


    def get(self, key): 
        """
        Get the value associated with a key.

        :param key: The key to look up.
        :return: The value associated with the key, or None if the key does not exist.
        """
        if key in self.key_value:
            return self.key_value[key]
        else:
            return None

    def remove(self, key): 
        """
        Remove a key-value pair from the data structure.

        :param key: The key to remove.
        """
        if key in self.key_value:
            delete_index = self.key_index[key]
            del self.key_value[key]
            self.key_index[self.key_array[-1]] = delete_index
            self.key_array[delete_index], self.key_array[-1] = self.key_array[-1], self.key_array[delete_index]
            self.key_array.pop()
            del self.key_index[key]


    def size(self):
        """
        Return the number of key-value pairs currently in the data structure.

        :return: Integer representing the size.
        """
        return len(self.key_array)

    def getRandomValue(self): # time: O(1)
        """
        Return a random value from the data structure.

        :return: A randomly selected value.
        """
        import random
        random_key = random.choice(self.key_array)
        return self.key_value[random_key]


m = RandomMagicMap()
m.put("a", 10)
m.put("b", 10)
m.put("c", 30)
m.put("a", 20)
print(m.get("a"))

