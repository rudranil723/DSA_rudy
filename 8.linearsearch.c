// Linear Search in C

#include <stdio.h>

int search(int array[], int n, int x)
{

	// Going through array sequencially
	for (int i = 0; i < n; i++)
		if (array[i] == x)
			return i;
	return -1;
}
