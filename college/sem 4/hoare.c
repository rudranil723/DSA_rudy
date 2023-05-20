void swap(int* a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
int partition(int arr[], int low, int high)
{
    int pivot = arr[low];
    int i = low - 1;
    int j = high + 1;
    while (1)
    {
        do
        {
            i++;
        } while (arr[i] < pivot);
        do
        {
            j--;
        } while (arr[j] > pivot);
        if (i < j)
            swap(&arr[i], &arr[j]);
        else return j;
    }
}
void Quick_Sort(int arr[], int low, int high)
{
    if (low < high)
    {
        int pivot = partition(arr, low, high);
        Quick_Sort(arr, low, pivot - 1);
        Quick_Sort(arr, pivot + 1, high);
    }
}
void printArr(int a[], int n)
{
    for (int i = 0; i < n; i++)
        printf("%d ", a[i]);
}