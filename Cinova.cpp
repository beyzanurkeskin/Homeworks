/* * * * * * * * * * * * * * * * * * * * * * * * *
* PLEASE DO NOT CHANGE ANYTHING UNLESS REQUESTED *
* * * * * * * * * * * * * * * * * * * * * * * * * */
/* Gülşen Eryiğit
 * Student Name:  Beyza Nur Keskin
 * Student ID : 150200320
 */



#include <iostream>
#include <stdlib.h>
#include <iomanip>
#include "Course.h" // burada bazen sıkıntı çıkarıyor C:\\User... şeklinde de eklemeyi denedim ama düzelmedi



using namespace std;



Course data_structure;

/* Function declarations */
void print_menu();
bool perform_operation(char);
void search_record();
void add_record();
void delete_record();
void update_record();
void avg();




int main(){	

	data_structure.create();	
	bool end = false; 
	char choice;

	/* Main program menu flow */

	while (!end) { 
		print_menu(); 
		cin >> choice;
		end = perform_operation(choice); 
		} 	
	data_structure.close();

	return EXIT_SUCCESS;
}





void print_menu(){
	cout << endl << endl;
	cout << "Cinova Lecture Management Application" << endl;
	cout << "1: Add a student" << endl;
	cout << "2: Remove a student" << endl;
	cout << "3: Update a student" << endl;
	cout << "4: List students" << endl;
	cout << "5: Get average of a student" << endl;
	cout << "0: Exit" << endl;	
	cout << endl;
	cout << "Please enter a choice: ";	
}

bool perform_operation(char choice){
	char id[ID_LENGTH];
	bool terminate=false;
	switch (choice) { 
//gerekli fonksiyonları yazdım 

		case '1':
			add_record();
			break;


		case '2':
			delete_record();
			break;


		case '3':
			update_record();
			break;


		case '4':
            data_structure.list();
			break;


		case '5':
			avg();
			break;


		case '0':

			cout << "Do you want to exit the program? (Y/N):";
			cin >> choice;
			if(choice=='Y' || choice=='y')
				terminate=true;
			break; 


		default:

			cout << "You have entered an invalid choice" << endl; 
			cout << "Please try again {1,2,3,4,5,0} :" ;
			cin >> choice;
			terminate = perform_operation(choice);
			break; 
	}

	return terminate;
}



void add_record(){

	Student* newStudent; //classtan bir öğrenci oluşturdum

	cout << "Please enter student information you want to add" << endl;
	cout << "Name: " << endl;
	cin.getline(newStudent->name,NAME_LENGTH);      //ismini aldım - getline olmasaydı beyza keskin yazınca sadece beyzayı alırdı
	

	cout << "Please enter student information you want to add" << endl;
	cout << "Id: " << endl;
	cin >> newStudent->id;        //idsini aldım


	cout << "Please enter student information you want to add" << endl;
	cout << "Grades: " << endl;

	for(int i = 0; i < GRADES_LENGTH; i++){

		cin >> newStudent->grades[GRADES_LENGTH];     // üç puan girileceği için for döngüsü oluşturdum

	}

	data_structure.add(newStudent);
	

	cout << "Record added" << endl;


	
}



void delete_record(){

	char id[ID_LENGTH];  

	cout << "Please enter student id you want to delete" << endl;

	cin >> id; //silinecek öğrencini idsini aldım
	
	data_structure.remove(id);

	cout << "Record removed" << endl;

}



void update_record(){

	/*   Burayı da yapamadım malesef ama bir şeyler denemeye çalıştım.

	
	Student newStu;  //classtan bir öğrenci oluşturdum

	cout << "Please enter student information you want to add" << endl;
	cout << "Name: " << endl;
	cin.getline(newStu.name,NAME_LENGTH);      // ismini aldım - getline olmasaydı beyza keskin yazınca sadece beyzayı alırdı
	

	cout << "Please enter student information you want to add" << endl;
	cout << "Id: " << endl;
	cin >> newStu.id;        //idsini aldım


	cout << "Please enter student information you want to add" << endl;
	cout << "Grades: " << endl;

	for(int i = 0; i < GRADES_LENGTH; i++){

		cin >> newStu.grades[GRADES_LENGTH];     // üç puan girileceği için for döngüsü oluşturdum

	}

	data_structure.update(newStu);
	

	cout << "Record updated" << endl;	

	*/

}

void avg(){


	char id[ID_LENGTH]; //burayı yapamadım

	cout << "Please enter student id you want to get average" << endl;

	



}

























