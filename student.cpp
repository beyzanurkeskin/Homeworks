/* @Author
 * Student Name:Beyza Nur Keskin
 * Student ID : 150200320
 */

#include <string>
#include <iostream>
#include "student.h"




Student::Student(std::string _name, double _gpa, double _gre, double _toefl, double _app_num) {
    
    name=_name; 
    gpa=_gpa;
    gre=_gre;
    toefl=_toefl;
    app_num=_app_num;
            
    std::cout << name << " logged in to the system." << std::endl;
}

    // i write my getter functions because my variables are private 
    // and i will use them in the university class as well.
    
    std::string Student::get_name() const {
        
        return name; 
    }
    
    double Student::get_gpa() const {
        
        return gpa; 
    }
    
    double Student::get_gre() const { 
        
        return gre; 
    }
    
    double Student::get_toefl() const { 
        
        return toefl; 
    }
    
    double Student::get_app_num() const { 
        
        return app_num; 
    }

    // i write my getter functions, i will use them too
    
    void Student::set_name(std::string name) { 
        
        //here, before i change the name of Lily which is the object i created
        //from michael, i am writing him an introductory sentence once more, since micheal is first formed
        
        std::cout << get_name() << " logged in to the system." << std::endl;
        this->name = name;
        
    }
    
    
    void Student::set_app_num(double app_num){ 
        
        this->app_num = app_num;
    }

   
    Student::~Student(){
        std::cout << name << " logged out of the system with " << app_num << " application(s)." << std::endl;
    }