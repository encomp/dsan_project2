###PROBLEM #6

###Union

####Design
The approach to create a single linked list with the content from two linked list is to create a new empty linked list. 
That will be populated from the first linked list. Then all the elements from the second linked list will be 
appended.

####Space Complexity
The space of this problem is O(N*M). In which "M" are the number of elements from the first linked list and "N" will be 
the number of elements from the second linked list. The overall running time in big will be O(N).

####Running Time Complexity
The running time complexity for the union operation will be the same as the space complexity.

###Intersection

####Design
The approach to create an intersection from two linked list is as follows: First a brand new linked list will be 
created. This will be populated with the element from the first linked list. Then an empty linked list will be created.
Then the second linked list will be traverse and each element will be linearly search on the linked list copy. If the 
element is found such element will be removed and appended to the empty linked list that contains the elements that 
appear on both lists.

####Space Complexity
The space of this problem is O(N). The intersection will have at most N elements in case both linked list are identical.
As a result, the overall running time in big will be O(N).

####Running Time Complexity
The running time complexity for the intersection operation will be O(N^2). Although, the copy of the first linked list 
is reduced in size if the two linked list provided are completely different the decrease of the size of the linked list 
will not occurred as a result every single element for the second list will be compared against every single element 
from the first linked list.