/* * * * * * * * * * * * * * * * * * * * * * * * *
* PLEASE DO NOT CHANGE ANYTHING UNLESS REQUESTED *
* * * * * * * * * * * * * * * * * * * * * * * * * */
/* Gülşen Eryiğit
 * Student Name:  Beyza Nur Keskin
 * Student ID : 150200320
 */
#include "Course.h"
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string.h>
#include "Student.h"

using namespace std;

/* Add new student to the file */


void Course::add(Student *nrptr){

    course_stream.seekp(0,ios_base::end);                                       //dosyayı açıp baştan başlattım

    course_stream.write(reinterpret_cast<char *>(nrptr), sizeof(Student));      //burda tür dönüşümü yapıyoruz reinterpret cast kullanarak ve 
    //                                                                            Student classındaki belirlediğimiz kadar yer ayırıyor ve yazıyor
    

}


/* Create a new .txt file to store Student information */
void Course::create(){


    file = "StudentList.txt"; //dosyama isim verdim

    course_stream.open(file, ios::out | ios::in | ios::trunc); //dosyamı açtım ve içine ioslu ifadeleri koydum ki  
    //                                                                        ilerde yapacağım işlemleri uygulayabileyim

 

}

/* Close the file */
void Course::close(){

    course_stream.close();  //dosyamı kapadım

    
}

/* Print average of a student with the given id */
void Course::get_average(char *desired){}



/* Update the file with given information */
void Course::update(char* id){}


/* Remove a student from the file */
void Course::remove(char id){

Student emptyrecord={"",""};  //boşlukla doldurmayın dediniz ancak başka yol bulamadım
//                   '-->    bi de burda aslında daha fazla '' böyle boşluk yapacaktım name id ve grade için ama hata verince sildim

if(course_stream.seekp(sizeof(Student)))

        course_stream.write(reinterpret_cast<char *>(&emptyrecord), sizeof(Student));

}


void Course::list() {


  ifstream course_stream(file); // okumak için dosyamı oluşturdum

  string t;  // içindekileri okuması için bir string değişkeni tanımladım
  
  while (getline (course_stream,t)) //satır satır okuması için while döngüsü kullandım
    
    cout << t; // satırları yazdırdım
  }


