//Write a program in C to delete an element at a specified position in a given array containing n numbers.


#include <stdio.h>

int main(){
    int a[50],n,i,pos;
    printf("enter the range: ");
    scanf("%d",&n);
    printf("enter the elements: ");
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    printf("enter the pos from where you want to delete: ");
    scanf("%d",&pos);
    if(pos>n){
        printf("cannot delete");
    }
    else{
        for (i=pos-1;i<n-1;i++){
            a[i]=a[i+1];
        }
    }
    printf("the array: ");
    for(i=0;i<n-1;i++){
        printf("%d ",a[i]);
    }
    return 0;
}
