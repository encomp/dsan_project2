### PROBLEM #2

### Design
The find files with specific suffix was design as a recursive function that perform a recursive search on the 
subdirectories of a given path. The function returns a list of paths if the provided file suffix is found.

### Space Complexity
The space of this problem is O(N). The reason being is that the size of array will be proportional to the number of 
files found with the given suffix.

### Running Time Complexity
The running time complexity for the find files recursive function is O(N). Since in only traverse once the 
subdirectories of the given path.