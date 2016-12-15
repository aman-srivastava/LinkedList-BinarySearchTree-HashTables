# -*- coding: utf-8 -*-
# Python Version: Python 3.5.2
# Author: Aman Srivastava
# Date: Dec 15, 2016
# Email: Aman.Srivastava@asu.edu


class SinglyLinkedNode(object):

    def __init__(self, item=None, next_link=None):
        super(SinglyLinkedNode, self).__init__()
        self._item = item
        self._next = next_link

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next

    def __repr__(self):
        return repr(self.item)


class SinglyLinkedList(object):

    def __init__(self):
        super(SinglyLinkedList, self).__init__()
        self._head = None

    def __len__(self):
        count = 0
        x = self._head
        while x is not None:
            count += 1
            x = x._next
        return count

    def __iter__(self):
        x = self._head
        while x is not None:
            yield x._item
            x = x._next

    def __contains__(self, item):
        x = self._head
        while x is not None and x._item != item:
            x = x._next
        if (x is not None):
            return True
        return False

    def remove(self, item):
        if(item is None):
            return False
        temp = x = self._head
        while (x is not None and x._item != item):
            temp = x
            x = x._next
        if (x is not None and x._item == item):
            if (temp == x):
                self._head = self._head._next
            else:
                temp._next = x._next
            return True
        else:
            return False
        return False

    def prepend(self, item):
        if(item is None):
            return False
        newNode = SinglyLinkedNode(item)
        newNode._next = self._head
        self._head = newNode
        return True

    def __repr__(self):
        s = "List:" + "->".join([str(item) for item in self])
        return s


class BinaryTreeNode(object):

    def __init__(self, data=None, left=None, right=None, parent=None):
        super(BinaryTreeNode, self).__init__()
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def insertNode(self, key, value):
        if(next(iter(self.data.keys())) == key):
            return False
        elif(next(iter(self.data.keys())) > key):
            if self.left is not None:
                return self.left.insertNode(key, value)
            else:
                self.left = BinaryTreeNode({key: value})
                return True
        else:
            if self.right is not None:
                return self.right.insertNode(key, value)
            else:
                self.right = BinaryTreeNode({key: value})
                return True

    def contains(self, key):
        if(next(iter(self.data.keys())) == key):
            return True
        elif(next(iter(self.data.keys())) > key):
            if self.left is not None:
                return self.left.contains(key)
            else:
                return False
        else:
            if self.right is not None:
                return self.right.contains(key)
            else:
                return False

    def getItem(self, key):
        if(next(iter(self.data.keys())) == key):
            return next(iter(self.data.values()))
        elif(next(iter(self.data.keys())) > key):
            if self.left is not None:
                return self.left.getItem(key)
            else:
                return False
        else:
            if self.right is not None:
                return self.right.getItem(key)
            else:
                return False

    def height(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is not None and self.right is None:
            return 1 + max(self.left.height(), 0)
        elif self.right is not None and self.left is None:
            return 1 + max(self.right.height(), 0)
        else:
            return 1 + max(self.left.height(), self.right.height())

    def length(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder_keys()
            print(next(iter(self.data.keys())), end=" ")
            if self.right is not None:
                self.right.inorder_keys()

    def __iter__inorder(self):
            if self.left:
                for elt in self.left.__iter__inorder():
                    yield elt
            yield self.data
            if self.right:
                for elt in self.right.__iter__inorder():
                    yield elt

    def __iter__preorder(self):
            yield self.data
            if self.left:
                for elt in self.left.__iter__preorder():
                    yield elt
            if self.right:
                for elt in self.right.__iter__preorder():
                    yield elt

    def __iter__postorder(self):
            if self.left:
                for elt in self.left.__iter__postorder():
                    yield elt
            if self.right:
                for elt in self.right.__iter__postorder():
                    yield elt
            yield self.data

    def items(self, root):
        if self.left:
            for elt in self.left.__iter__inorder():
                yield [(next(iter(elt.keys()))), next(iter(elt.values()))]
        yield [(next(iter(self.data.keys()))), next(iter(self.data.values()))]
        if self.right:
            for elt in self.right.__iter__inorder():
                yield [(next(iter(elt.keys()))), next(iter(elt.values()))]

    def inorder_keys(self, root):
        if self.left:
            for elt in self.left.__iter__inorder():
                yield(next(iter(elt.keys())))
        yield (next(iter(self.data.keys())))
        if self.right:
            for elt in self.right.__iter__inorder():
                yield(next(iter(elt.keys())))

    def preorder_keys(self, root):
        yield(next(iter(self.data.keys())))
        if self.left:
            for elt in self.left.__iter__preorder():
                yield(next(iter(elt.keys())))
        if self.right:
            for elt in self.right.__iter__preorder():
                yield(next(iter(elt.keys())))

    def postorder_keys(self, root):
        if self.left:
            for elt in self.left.__iter__postorder():
                yield(next(iter(elt.keys())))
        if self.right:
            for elt in self.right.__iter__postorder():
                yield(next(iter(elt.keys())))
        yield(next(iter(self.data.keys())))


class BinarySearchTreeDict(object):

    def __init__(self):
        super(BinarySearchTreeDict, self).__init__()
        self.root = None
        pass

    @property
    def height(self):
        if self.root is None:
            return -1
        else:
            return self.root.height()

    @property
    def length(self):
        return self.__len__()

    def inorder_keys(self):
        if self.root is not None:
            return self.root.inorder_keys(self.root)
        else:
            raise StopIteration

    def postorder_keys(self):
        if self.root is not None:
            return self.root.postorder_keys(self.root)
        else:
            raise StopIteration

    def preorder_keys(self):
        if self.root is not None:
            return self.root.preorder_keys(self.root)
        else:
            raise StopIteration

    def items(self):
        if self.root is not None:
            return self.root.items(self.root)
        else:
            raise StopIteration

    def __getitem__(self, key):
        if self.root is not None:
            return self.root.getItem(key)
        else:
            return False

    def __setitem__(self, key, value):
        if(key is None):
            return False
        if self.root is not None:
            return self.root.insertNode(key, value)
        else:
            self.root = BinaryTreeNode({key: value})
            return True

    def __delitem__ifKey(self, key):
        if self.root.left is None and self.root.right is None:
            self.root = None
        elif self.root.left and self.root.right is None:
            self.root = self.root.left
        elif self.root.left is None and self.root.right:
            self.root = self.root.right
        elif self.root.left and self.root.right:
            delNodeParent = self.root
            delNode = self.root.right
            while delNode.left:
                delNodeParent = delNode
                delNode = delNode.left

            self.root.data = delNode.data
            if delNode.right:
                if(next(iter(delNodeParent.data.keys())) >
                   next(iter(delNode.data.keys()))):
                    delNodeParent.left = delNode.right
                elif(next(iter(delNodeParent.data.keys())) <
                     next(iter(delNode.data.keys()))):
                    delNodeParent.right = delNode.right
            else:
                if(next(iter(delNode.data.keys())) <
                   next(iter(delNodeParent.data.keys()))):
                    delNodeParent.left = None
                else:
                    delNodeParent.right = None
        return True

    def findNodeToRemove(self, key, node):
        if key < next(iter(node.data.keys())):
            return node.left
        elif key > next(iter(node.data.keys())):
            return node.right

    def hasLeftChild(self, key, parent, node):
            if key < next(iter(parent.data.keys())):
                parent.left = node.left
            else:
                parent.right = node.left
            return True

    def hasRightChild(self, key, parent, node):
        if key < next(iter(parent.data.keys())):
            parent.left = node.right
        else:
            parent.right = node.right
        return True

    def removeLeftRightChild(self, node):
        delNodeParent = node
        delNode = node.right
        while delNode.left:
            delNodeParent = delNode
            delNode = delNode.left
        node.data = delNode.data
        if delNode.right:
            if(next(iter(delNodeParent.data.keys())) >
               next(iter(delNode.data.keys()))):
                delNodeParent.left = delNode.right
            elif(next(iter(delNodeParent.data.keys())) <
                 next(iter(delNode.data.keys()))):
                delNodeParent.right = delNode.right
        else:
            if(next(iter(delNode.data.keys())) <
               next(iter(delNodeParent.data.keys()))):
                delNodeParent.left = None
            else:
                delNodeParent.right = None
        return True

    def __delitem__(self, key):
        if key is None or self.root is None:
            return False
        elif(next(iter(self.root.data.keys())) == key):
            return self.__delitem__ifKey(key)

        parent = None
        node = self.root

        while node and next(iter(node.data.keys())) != key:
            parent = node
            node = self.findNodeToRemove(key, node)

        if node is None or next(iter(node.data.keys())) != key:
            return False

        elif node.left is None and node.right is None:
            if key < next(iter(parent.data.keys())):
                parent.left = None
            else:
                parent.right = None
            return True

        elif node.left and node.right is None:
            return self.hasLeftChild(key, parent, node)

        elif node.left is None and node.right:
            return self.hasRightChild(key, parent, node)

        else:
            return self.removeLeftRightChild(node)

    def __contains__(self, key):
        if self.root is not None:
            return self.root.contains(key)
        else:
            return False

    def __len__(self):
        if self.root is None:
            return 0
        else:
            length = 0
            for items in self.inorder_keys():
                length += 1
            return length

    def display(self):
        inO = "Inorder:" + "->".join([str(item) for item in
                                      self.inorder_keys()])
        preO = "Preorder:" + "->".join([str(item) for item in
                                        self.preorder_keys()])
        return [inO, preO]


class ChainedHashDict(object):

    def __init__(self, bin_count=10, max_load=0.7, hashfunc=hash):
        super(ChainedHashDict, self).__init__()
        self._size = bin_count
        self._maxLoad = max_load
        self._hashTable = [None] * self._size
        self.hashfunc = hashfunc

    @property
    def load_factor(self):
        return self.__len__() / self._size

    @property
    def bin_count(self):
        return self._size

    @property
    def len(self):
        return self.__len__()

    def rebuild(self, bincount):
        if(bincount is None):
            return False
        old_hashTable = self._hashTable
        self._size = bincount
        self._hashTable = [None] * self._size
        for item in old_hashTable:
            if item is not None:
                for pair in item:
                    if pair is not None:
                        self.__setitem__(pair[0], pair[1])
        return True

    def __getitem__(self, key):
        if (key is None):
            return None
        else:
            key_hash = self.hashfunc(key) % self._size
            if self._hashTable[key_hash] is not None:
                for pair in self._hashTable[key_hash]:
                    if pair[0] == key:
                        return pair[1]
            return None
        return None

    def __setitem__(self, key, value):
        if(key is None):
            return False
        if self.load_factor >= self._maxLoad:
            self.rebuild(self._size * 2)
        key_hash = self.hashfunc(key) % self._size
        key_value = [key, value]

        if self._hashTable[key_hash] is None:
            self._hashTable[key_hash] = list([key_value])
            return True
        else:
            for pair in self._hashTable[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self._hashTable[key_hash] = list([key_value]) + \
                self._hashTable[key_hash]
            return True
        return False

    def __delitem__(self, key):
        if(key is None):
            return False
        key_hash = self.hashfunc(key) % self._size
        if self._hashTable[key_hash] is None:
            return False
        for i in range(0, len(self._hashTable[key_hash])):
            if self._hashTable[key_hash][i][0] == key:
                self._hashTable[key_hash].pop(i)
                if len(self._hashTable[key_hash]) == 0:
                    self._hashTable[key_hash] = None
                return True
        return False

    def __contains__(self, key):
        if(key is None):
            return False
        key_hash = self.hashfunc(key) % self._size
        if self._hashTable[key_hash] is not None:
                for pair in self._hashTable[key_hash]:
                        if pair[0] == key:
                                return True
        return False

    def __len__(self):
        length = 0
        for item in self._hashTable:
            if item is not None:
                for pair in item:
                    if pair is not None:
                        length += 1
        return length

    def display(self):
        s = ""
        x = ""
        binIndex = 0
        for item in self._hashTable:
                if item is not None:
                    x = "->".join(str(pair) for pair in item)
                    if (s == ""):
                        s = "".join([s, str(binIndex)+"List:"+x])
                        binIndex += 1
                        continue
                    s = "\n".join([s, str(binIndex)+"List:"+x])
                else:
                    if (s == ""):
                        s = "".join([s, str(binIndex)+"List:"])
                        binIndex += 1
                        continue
                    s = "\n".join([s, str(binIndex)+"List:"])
                binIndex += 1
        return s


class OpenAddressHashDict(object):

    def __init__(self, bin_count=10, max_load=0.7, hashfunc=hash):
        super(OpenAddressHashDict, self).__init__()
        self._size = bin_count
        self._maxLoad = max_load
        self._hashTable = [None] * self._size
        self.hashfunc = hashfunc

    @property
    def load_factor(self):
        return self.__len__() / self._size

    @property
    def bin_count(self):
        return self._size

    @property
    def len(self):
        return self.__len__()

    def rebuild(self, bincount):
        old_hashTable = self._hashTable
        # old_size = self._size
        self._size = bincount
        self._hashTable = [None] * self._size
        for item in old_hashTable:
            if item is not None:
                for pair in item:
                    if pair is not None:
                        self.__setitem__(pair[0], pair[1])
        return True

    def __getitem__(self, key):
        if(key is None):
            return None
        key_hash = self.hashfunc(key) % self._size
        while self._hashTable[key_hash] is not None:
            if self._hashTable[key_hash][0][0] == key:
                return self._hashTable[key_hash][0][1]
            else:
                key_hash = (key_hash + 1) % self._size
        return None

    def __setitem__(self, key, value):
        if(key is None):
            return False
        if self.load_factor >= self._maxLoad:
            self.rebuild(self._size * 2)
        key_hash = self.hashfunc(key) % self._size
        key_value = [key, value]

        if self._hashTable[key_hash] is None:
            self._hashTable[key_hash] = list([key_value])
            return True
        else:
            while self._hashTable[key_hash] is not None:
                if self._hashTable[key_hash][0][0] == key:
                    self._hashTable[key_hash][0][1] = value
                    return True
                key_hash = (key_hash + 1) % self._size
            if self._hashTable[key_hash] is None:
                self._hashTable[key_hash] = list([key_value])
                return True
        return False

    def __delitem__(self, key):
        if(key is None):
            return False
        key_hash = self.hashfunc(key) % self._size
        while self._hashTable[key_hash] is not None:
            if self._hashTable[key_hash][0][0] == key:
                self._hashTable[key_hash] = None
                self.rebuild(self._size)
                return True
            else:
                key_hash = (key_hash + 1) % self._size
        return False

    def __contains__(self, key):
        if(key is None):
            return False
        key_hash = self.hashfunc(key) % self._size
        if self._hashTable[key_hash] is not None:
                for pair in self._hashTable[key_hash]:
                        if pair[0] == key:
                                return True
        return False

    def __len__(self):
        length = 0
        for item in self._hashTable:
            if item is not None:
                length += 1
        return length

    def display(self):
        s = ""
        x = ""
        binIndex = 0
        for item in self._hashTable:
                if item is not None:
                    x = "->".join(str(pair) for pair in item)
                    if (s == ""):
                        s = "".join([s, "bin "+str(binIndex)+": "+x])
                        binIndex += 1
                        continue
                    s = "\n".join([s, "bin "+str(binIndex)+": "+x])
                else:
                    if (s == ""):
                        s = "".join([s, "bin "+str(binIndex)+": " +
                                     str([None, None])])
                        binIndex += 1
                        continue
                    s = "\n".join([s, "bin "+str(binIndex)+": " +
                                   str([None, None])])
                binIndex += 1
        return s


def terrible_hash(bin):
    """A terrible hash function that can be used for testing.

    A hash function should produce unpredictable results,
    but it is useful to see what happens to a hash table when
    you use the worst-possible hash function.  The function
    returned from this factory function will always return
    the same number, regardless of the key.

    :param bin:
        The result of the hash function, regardless of which
        item is used.

    :return:
        A python function that can be passed into the constructor
        of a hash table to use for hashing objects.
    """

    def hashfunc(item):
        return bin
    return hashfunc

def main():
    LL = SinglyLinkedList()
    BST = BinarySearchTreeDict()
    CHT = ChainedHashDict(10, 0.7)
    OAHT = OpenAddressHashDict(5, 0.7, terrible_hash(10))
    option = 0
    while (option != 5):
        displayMainMenu()
        option = int(input("Your Choice (1-5): "))
        if (option == 1):
            displaySinglyLinkedListMenu()
            option = int(input("Your Choice (1-5): "))
            print()
            if (option == 1):
                LL = singlyLinkedList_Insert(LL)
                option = 0
                continue
            elif (option == 2):
                LL = singlyLinkedList_Remove(LL)
                option = 0
                continue
            elif (option == 3):
                LL = singlyLinkedList_Search(LL)
                option = 0
                continue
            elif (option == 4):
                LL = singlyLinkedList_Display(LL)
                option = 0
                continue
            else:
                option = 0
                continue
        elif (option == 2):
            displayBinarySearchTreeMenu()
            option = int(input("Your Choice (1-5): "))
            print()
            if(option == 1):
                BST = binarySearchTree_Insert(BST)
                option = 0
                continue
            elif(option == 2):
                BST = binarySearchTree_Delete(BST)
                option = 0
                continue
            elif(option == 3):
                BST = binarySearchTree_Retrieve(BST)
                option = 0
                continue
            elif(option == 4):
                BST = binarySearchTree_Display(BST)
                option = 0
                continue
            else:
                option = 0
                continue
        elif (option == 3):
            displayChainedHashTableMenu()
            option = int(input("Your Choice (1-5): "))
            print()
            if(option == 1):
                CHT = chainedHashTable_Insert(CHT)
                option = 0
                continue
            elif(option == 2):
                CHT = chainedHashTable_Delete(CHT)
                option = 0
                continue
            elif(option == 3):
                CHT = chainedHashTable_Retrieve(CHT)
                option = 0
                continue
            elif(option == 4):
                CHT = chainedHashTable_Display(CHT)
                option = 0
                continue
            else:
                option = 0
                continue
        elif (option == 4):
            displayOpenAddHashTableMenu()
            option = int(input("Your Choice (1-5): "))
            print()
            if(option == 1):
                OAHT = openAddHashTable_Insert(OAHT)
                option = 0
                continue
            elif(option == 2):
                OAHT = openAddHashTable_Delete(OAHT)
                option = 0
                continue
            elif(option == 3):
                OAHT = openAddHashTable_Retrieve(OAHT)
                option = 0
                continue
            elif(option == 4):
                OAHT = openAddHashTable_Display(OAHT)
                option = 0
                continue
            else:
                option = 0
                continue
    


def displayMainMenu():
        print("\n\n################################")
        print("###         MAIN MENU        ###")
        print("################################")
        print("Select a Data Structure:")
        print("1. Singly Linked List")
        print("2. Binary Search Tree")
        print("3. Chained Hash Table")
        print("4. Open Address Hash Table")
        print("5. Exit")


def displaySinglyLinkedListMenu():
        print("\n################################")
        print("###    Singly Linked List    ###")
        print("################################")
        print("Select an Operation:")
        print("1. Insert Value")
        print("2. Remove Value")
        print("3. Search Value")
        print("4. Display List")
        print("5. Main Menu")


def displayBinarySearchTreeMenu():
        print("\n################################")
        print("### Binary Search Tree (BST) ###")
        print("################################")
        print("Select an Operation:")
        print("1. Insert Item")
        print("2. Delete Item")
        print("3. Retrieve Item")
        print("4. Display BST")
        print("5. Main Menu")


def displayChainedHashTableMenu():
        print("\n################################")
        print("### Chained Hash Table (CHT) ###")
        print("################################")
        print("Select an Operation:")
        print("1. Insert Item")
        print("2. Delete Item")
        print("3. Retrieve Item")
        print("4. Display CHT")
        print("5. Main Menu")


def displayOpenAddHashTableMenu():
        print("\n################################")
        print("#Open Address Hash Table (OAHT)#")
        print("################################")
        print("Select an Operation:")
        print("1. Insert Item")
        print("2. Delete Item")
        print("3. Retrieve Item")
        print("4. Display OAHT")
        print("5. Main Menu")


def singlyLinkedList_Insert(LL):
    x = int(input("Enter a value to Insert in Linked List: "))
    LL.prepend(x)
    return LL


def singlyLinkedList_Remove(LL):
    x = int(input("Enter a value to Remove from Linked List: "))
    if(LL.remove(x) is True):
        print("\nValue \"", x, "\" Found and Removed from Linked List",
              sep="")
    else:
        print("\nValue \"", x, "\" was NOT Found in the Linked List",
              sep="")
    return LL


def singlyLinkedList_Search(LL):
    x = int(input("Enter a value to Search: "))
    if (LL.__contains__(x) is True):
        print("\nValue \"", x, "\" Exists in the Linked List",
              sep="")
    else:
        print("\nValue \"", x, "\" does NOT Exist in the Linked List",
              sep="")
    return LL


def singlyLinkedList_Display(LL):
    print(LL.__repr__())
    print("Length:", LL.__len__())
    return LL


def binarySearchTree_Insert(BST):
    key = int(input("Enter a Key & Value to Insert in BST:\n\nKey: "))
    value = input("Value: ")
    if(BST.__setitem__(key, value)):
        print("Item:", {key: value}, "Inserted in BST")
    else:
        print("Item:", {key: value}, "Already Exists in BST")
    return BST


def binarySearchTree_Delete(BST):
    x = int(input("Enter a key to Delete from BST: "))
    if(BST.__delitem__(x) is True):
        print("\nValue \"", x, "\" Found and Removed from BST",
              sep="")
    else:
        print("\nValue \"", x, "\" was NOT Found in the BST",
              sep="")
    return BST


def binarySearchTree_Retrieve(BST):
    x = int(input("Enter a key to Retrieve its value: "))
    y = BST.__getitem__(x)
    if y is not None:
        print("\nValue \"", y, "\" Found for Key \"", x, "\" in the BST",
              sep="")
    else:
        print("\nKey \"", x, "\" does NOT Exist in the BST", sep="")
    return BST


def binarySearchTree_Display(BST):
    BST.display()
    print()
    BST.items()
    return BST


def chainedHashTable_Insert(CHT):
    key = int(input("Enter a Key & Value to Insert in CHT:\n\nKey: "))
    value = input("Value: ")
    if(CHT.__setitem__(key, value)):
        print("Item:", {key: value}, "Inserted in CHT")
    else:
        print("Item:", {key: value}, "Key could not be Inserted")
    return CHT


def chainedHashTable_Delete(CHT):
    x = int(input("Enter a key to Delete from BST: "))
    if(CHT.__delitem__(x) is True):
        print("\nItem with Key \"", x, "\" Removed from CHT", sep="")
    else:
        print("\nItem with Key \"", x, "\" was NOT Found in the CHT",
              sep="")
    return CHT


def chainedHashTable_Retrieve(CHT):
    x = int(input("Enter a key to Retrieve its value: "))
    y = CHT.__getitem__(x)
    if y is not None:
        print("\nValue \"", y, "\" Found for Key \"", x, "\" in the CHT",
              sep="")
    else:
        print("\nKey \"", x, "\" does NOT Exist in the CHT", sep="")
    return CHT


def chainedHashTable_Display(CHT):
    print(CHT.display())
    return CHT


def openAddHashTable_Insert(OAHT):
    key = int(input("Enter a Key & Value to Insert in OAHT:\n\nKey: "))
    value = input("Value: ")
    if(OAHT.__setitem__(key, value)):
        print("Item:", {key: value}, "Inserted in OAHT")
    else:
        print("Item:", {key: value}, "Key could not be Inserted")
    return OAHT


def openAddHashTable_Delete(OAHT):
    x = int(input("Enter a key to Delete from BST: "))
    if(OAHT.__delitem__(x) is True):
        print("\nItem with Key \"", x, "\" Removed from OAHT", sep="")
    else:
        print("\nItem with Key \"", x, "\" was NOT Found in the OAHT",
              sep="")
    return OAHT


def openAddHashTable_Retrieve(OAHT):
    x = int(input("Enter a key to Retrieve its value: "))
    y = OAHT.__getitem__(x)
    if y is not None:
        print("\nValue \"", y, "\" Found for Key \"", x, "\" in the OAHT",
              sep="")
    else:
        print("\nKey \"", x, "\" does NOT Exist in the OAHT", sep="")
    return OAHT


def openAddHashTable_Display(OAHT):
    print(OAHT.display())
    return OAHT


if __name__ == '__main__':
    main()

# ##############################??? ??????###################################
