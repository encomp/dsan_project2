### PROBLEM #4

### Design
The approach to determine if a user belong to a group is to search if the given user is part of the array of user of 
the current group. If this is not the case then from the array of groups a recursive search will be performed until all 
the groups from the array have been explored. 

### Space Complexity
The function make use of recursion which creates a stack that is populated every time the function is called. In the 
stack the user and group are being stored. As a result, the space complexity of space complexity of recursive algorithm 
is proportional to maximum depth of recursion tree generated. If each function call of recursive algorithm takes O(M) 
space and if the maximum depth of recursion tree is "N" then space complexity of recursive algorithm would be O(NM).

### Running Time Complexity
The running time complexity to determine if the user is O(M*N). The approach is to look for a user in a group is O(M). 
Because it performs a linear search on the array of users in a give group. And O(N) is the total number of groups that 
needs to be verified to determine if a user belong to the given group. The overall running time in big will be O(N).

