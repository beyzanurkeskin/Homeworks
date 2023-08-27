/* @Author
 * Student Name:Beyza Nur Keskin
 * Student ID : 150200320
 */


#include <string>
#include <iostream>
#include "university.h"




//here i wrote a constructor function for my university class

    University::University(std::string nname, double gpa_weight,
        double gre_weight, double toefl_weight, double bias,std::string ccountry){
        
        name_=nname;
        w_gpa_=gpa_weight;
        w_gre_=gre_weight;
        w_toefl_=toefl_weight;;
        bias_=bias;
        country_=ccountry;
            
        }

    // i wrote the evaluate function here
    void University::evaluate_student(const Student& student) const {
        
        
        // i calculate a z-value by including the braces and bias as given in the assignment pdf
        student.app_num ++;
        double activation = student.get_gpa() * w_gpa_ +
            student.get_gre() * w_gre_ +
            student.get_toefl() * w_toefl_ + bias_;
        
        if (activation >= 0.0) {
            
            //If the z value is greater than 0, she/he is accepted to the university.
            std::cout << student.get_name() << " is admitted to " << name_ << std::endl;
        }
        
        else {
            
            //if not she/he does not
            std::cout << student.get_name() << " is rejected from " << name_ << std::endl;
        }
    }
    void University::evaluate_student(Student& student) const {
        
        
        // i calculate a z-value by including the braces and bias as given in the assignment pdf
        student.app_num++;
        double activation = student.get_gpa() * w_gpa_ +
            student.get_gre() * w_gre_ +
            student.get_toefl() * w_toefl_ + bias_;
        
        if (activation >= 0.0) {
            
            //If the z value is greater than 0, she/he is accepted to the university.
            std::cout << student.get_name() << " is admitted to " << name_ << std::endl;
        }
        
        else {
            
            //if not she/he does not
            std::cout << student.get_name() << " is rejected from " << name_ << std::endl;
        }
    }

    