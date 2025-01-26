import random

class HashTable:
    def __init__(self, size=10):
        self.size = size
        #list for each hash to handle colision
        self.table = [[] for _ in range(size)]
          #large prime number for hashing 
        self.p = 2**31 - 1
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def hash_function(self, key):
        #universal hash function to calculate index 
        return ((self.a * hash(key) + self.b) % self.p) % self.size

    def insert(self, key, value):
        #insert a key-value pair in hash table
        index = self.hash_function(key)
        for pair in self.table[index]:
            #update value if key already exists
            if pair[0] == key:
                pair[1] = value  
                return
        self.table[index].append([key, value])

    def search(self, key):
        #search for a value with key
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        #if key not in hash table    
        return None  

    def delete(self, key):
        #deletes key-value pair from hash table
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                #if successfully found
                return True
        #if not found    
        return False 

    def __repr__(self):
        #returns string representation of hash table
        return "\n".join(f"{i}: {bucket}" for i, bucket in enumerate(self.table))


if __name__ == "__main__":

    hasht = HashTable(size=7)

    #inserting elements
    hasht.insert(1, "Detergent")
    hasht.insert(2, "Papet towel")
    hasht.insert(7, "Chicken")
    hasht.insert(3, "banana")
    hasht.insert(11, "almonds")

    print("Hash Table:")
    print(hasht)

    #search
    print("\nSearch:")
    print("1:", hasht.search(1))
    print("2:", hasht.search(2))
    print("71:", hasht.search(71))

    #deleteing
    print("\nDelete '1':", hasht.delete(1))

    print("\nHash Table after deletion:")
    print(hasht)
