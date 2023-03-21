#include <stdio.h>
#include <stdlib.h>
#include <time.h>


//////////////////////////////////////////////////////////
void bubbleSort(int array[], int len){
  for (int step = 0; step < len - 1; step++){  //number of swaps
    for (int i = 0; i < len - step - 1; i++){  //length of considered elements of array
      if (array[i] > array[i + 1]){  //swap itself
        int temp;
        temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
      }
    }
  }
}


//////////////////////////////////////////////////////////
  void hpf(int array[], int len, int i){
    int maxim = i, temp;  //i - index of currently last node to hpf down with
    int right = 2 * i + 2;
    int left = 2 * i + 1;

    //creating max heap
    if (right < len && array[right] > array[maxim]){
      maxim = right;
    }
    if (left < len && array[left] > array[maxim]){
      maxim = left;
    }
    if (maxim != i){
      temp = array[i];
      array[i] = array[maxim];
      array[maxim] = temp;
      hpf(array, len, maxim);
    }
  }

  void heapSort(int array[], int len){
    for (int i = len / 2 - 1; i >= 0; i--){  //dividing
      hpf(array, len, i);
    }
    int temp;
    for (int i = len - 1; i >= 0; i--){  //swap
      temp = array[i];
      array[i] = array[0];
      array[0] = temp;
      hpf(array, i, 0);  //creates max heap + reduces array
    }
  }


//////////////////////////////////////////////////////////
 void countingSort(int array[], int len){
    int maxim = -1;

    for(int i = 0; i < len; i++){  //searching for max value of array
        if(maxim < array[i]){
            maxim = array[i];
        }
    }
    //int count[maxim + 1];  //array of 0s for counting repeatitions of each value in array
    int *count = malloc((maxim + 1) * sizeof(*count));
    for(int i = 0; i <= maxim; i++){
        count[i] = 0;
    }

    for(int i = 0; i < len; i++){  //adding amount of repeatitions of each value in array
        count[array[i]]++;
    }
    for(int i = 1; i <= maxim; i++){  //adding values of previous elements to each element
        count[i] += count[i - 1];
    }
   // int sorted_array[len];
    int *sorted_array = malloc(len * sizeof(*sorted_array));

    for(int i = 0; i < len; i++){  //start of sorting merging data from count[] and array[]
        sorted_array[count[array[i]] - 1] = array[i];
	/*
	element of array[] goes to element of count[] with index = value of element of array[]
	and adds (this value - 1) to the sorted list of index = value of count[] element)
	*/
        count[array[i]]--;
    }
    for (int i = 0; i < len; i++) {
    	array[i] = sorted_array[i];}

    free(count);
    free(sorted_array);
}


//////////////////////////////////////////////////////////
void shellSort(int array[], int len){
    for (int i = len / 2; i > 0; i /= 2){  //for each gap in gaps (we reduces our gap by 2 each time)
        for (int j = i; j < len; j++){  //adding one more element to sort
            for(int k = j - i; k >= 0; k -= i){  //searching for correct location
                if (array[k + i] >= array[k]){  //gap = 0 -> stop algorithm
                    break;
                }
                else{  //putting an element to the correct location in the initial array
		    int temp;
                    temp = array[k];
                    array[k] = array[k + i];
                    array[k + i] = temp;
                }
            }
        }
    }
}


////////////////////////////////////////////////////////////
int quickSort(int arr[],int low,int high)
{
    if(low>=high)
        return 0;

    int mid=(low+high)/2;
    int pivot=arr[mid];
    int i=low,j=high;
    int temp;
    while(i<j)
    {
        if(arr[i]>=pivot && arr[j]<=pivot)
        {
            temp=arr[j];
            arr[j]=arr[i];
            arr[i]=temp;
            i++;
            j--;
        }
        else
        {
            i++;
        }
    }
    quickSort(arr,low,mid);
    quickSort(arr,mid+1,high);
}
//////////////////////////////////////////////////////////

void merge(int a[],int i1,int j1,int i2,int j2)
{
  //int temp[j2 + 1];  //array used for merging
  int *temp = malloc((j2 + 1) * sizeof(*temp));
  int i,j,k;
  i=i1;  //beginning of the first list
  j=i2;  //beginning of the second list
  k=0;

  while(i<=j1 && j<=j2)  //while elements in both lists
  {
    if(a[i]<a[j])
      temp[k++]=a[i++];
    else
      temp[k++]=a[j++];
  }

  while(i<=j1)  //copy remaining elements of the first list
    temp[k++]=a[i++];

  while(j<=j2)  //copy remaining elements of the second list
    temp[k++]=a[j++];

  //Transfer elements from temp[] back to a[]
  for(i=i1,j=0;i<=j2;i++,j++)
    a[i]=temp[j];

  free(temp);
}


void mergeSort(int a[],int i,int j)
{
  int mid;

  if(i<j)
  {
    mid=(i+j)/2;
    mergeSort(a,i,mid);    //left recursion
    mergeSort(a,mid+1,j);  //right recursion
    merge(a,i,mid,mid+1,j);  //merging of two sorted sub-arrays
  }
}

//////////////////////////////////////////////////////////
int main(){
   int N[3] = {99998, 99999, 100000};
   for (int j=0; j < 3; j++)  {
	int len = N[j];
	//scanf("%d", &len);
	int *array = malloc(len * sizeof(*array));
	/*for(int i = 0; i < len; i++){
        	array[i] = rand()%(len*10);
        	//printf("%d ", array[i]);
 	}*/

       int mid = len / 2;
       int odd = len ;
       for(int i = 0; i <= mid; i++){
         array[i] = odd;
         odd -= 2;
       }

       int even = 0;
       for(int i = mid + 1; i <= len; i++){
         array[i] = even;
         even += 2;
       }


	clock_t tic = clock();
	quickSort(array, 0, len);
	clock_t toc = clock();
	/*for(int i = 0; i < len; i++){
        	printf("%d ", array[i]);
 	}*/

	double time;
	time = (double)(toc - tic) / CLOCKS_PER_SEC;
	//printf("%f\n", (double)(toc - tic) / CLOCKS_PER_SEC);
	printf("%f\n", time);

	//FILE *f = fopen("/home/vovapain/ADS/pososi.txt", "a");
//	fprintf(f, "%f\n", time);
	//fclose (f);

	//for(int i = 0; i < len; i++)
    		//printf("%d ", array[i]);

	free(array);    }
	return 0;
}