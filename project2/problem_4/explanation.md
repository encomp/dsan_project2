###PROBLEM #4

###Design
The approach to determine if a user belong to a group is to search if the given user is part of the array of user of 
the current group. If this is not the case then from the array of groups a recursive search will be performed until all 
the groups from the array have been explored. 

###Space Complexity
The function to determine if the user belongs to a groups does not use auxiliary memory.

###Running Time Complexity
The running time complexity to determine if the user is O(M*N). The approach is to look for a user in a group is O(M). 
Because it performs a linear search on the array of users in a give group. And O(N) is the total number of groups that 
needs to be verified to determine if a user belong to the given group. The overall running time in big will be O(N).

