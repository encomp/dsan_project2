### PROBLEM #5

### Design
A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it
is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a
timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the 
block was created, and text strings as the data.

![blockchain]

[blockchain]: blockchain.png

#### Add data to the blockchain
To add an element on the blockchain is done as follow:

![blockchain_add]

[blockchain_add]: blockchain_add.png

### Space Complexity
The space of this problem is O(N). The reason being is that every element will be wrapped into a Block object and 
later inserted on a double linked list.

### Running Time Complexity
The running time complexity are as follow:

* Add an element O(1)
* Print the elements in the blockchain O(N)
