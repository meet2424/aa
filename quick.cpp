#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
void swap(int *a, int *b)
{
  int t = *a;
  *a = *b;
  *b = t;
}

int partition(int arr[], int low, int high, int &comparisons)
{
  int pivot = arr[high];
  int i = (low - 1);
  for (int j = low; j <= high - 1; j++)
  {

    if (arr[j] <= pivot)
    {
      comparisons++;
      i++;
      swap(&arr[i], &arr[j]);
    }
  }
  swap(&arr[i + 1], &arr[high]);
  return (i + 1);
}

void randomized_quicksort(int arr[], int low, int high, int &comparisons)
{
  if (low < high)
  {

    srand(time(NULL));
    int random = low + rand() % (high - low);
    swap(&arr[random], &arr[high]);
    int pi = partition(arr, low, high, comparisons);
    randomized_quicksort(arr, low, pi - 1, comparisons);
    randomized_quicksort(arr, pi + 1, high, comparisons);
  }
}

void quickSort(int arr[], int low, int high, int &qcomp)
{
  if (low < high)
  {

    int pi = partition(arr, low, high, qcomp);

    quickSort(arr, low, pi - 1, qcomp);
    quickSort(arr, pi + 1, high, qcomp);
  }
}

void printArray(int arr[], int n)
{
  for (int i = 0; i < n; i++)
  {
    cout << arr[i] << " ";
  }
  cout << endl;
}

int main()
{
  int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  int n = sizeof(arr) / sizeof(arr[0]);
  int m = sizeof(a) / sizeof(a[0]);
  cout << "Original array: ";
  printArray(arr, n);
  int comparisons = 0;
  int qcomp = 0;
  randomized_quicksort(arr, 0, n - 1, comparisons);
  cout << "Sorted array: ";
  printArray(arr, n);
  cout << "Number of comparisons in randomized: " << comparisons << endl;
  quickSort(a, 0, m - 1, qcomp);
  cout << "Sorted array: ";
  printArray(a, n);
  cout << "Number of comparisons in quickSort: " << qcomp << endl;
  return 0;
}
