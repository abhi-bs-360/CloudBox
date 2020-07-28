#include<stdio.h>
#include<string.h>
#include<unistd.h>
#include<stdlib.h>
#include<time.h>


// Useful Global variables
int offcount = 1;
int items = 4;
int iMenu = 0;


// Unique index tracker
union Index {
    int Id;
} User;



// SearchDeck using unique index
struct SearchDeck {
    char store[200][50];
} deck;



// Stores most of var's related to Customers
struct Customers {
	
    char name[50], gender[15], email[100];
	
    long int mobile;
    int age;
    float damount;
    
    int offerCheck;

    char qZoneNumber[50], *password;
    char final_order[50][50];
    
    int count_arr[100];
    float cost_arr[100];

} user[100];



struct Officials {
	
    char official_id[20];
	char official_password[50];
	char official_status[20];

} emp;



typedef struct menu {
    
    char food[50];    
    float cost;
    int foodno, mark, count;

} sm;
sm x[100];


typedef struct offer {
    int code, discount, serialno;
} so;
so off[100];
