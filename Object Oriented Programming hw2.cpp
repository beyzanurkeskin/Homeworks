//--- 2022-2023 Fall YZV201E Assignment 1 ---//
//--------------------------//
//---Name & Surname:Beyza Nur KESKİN
//---Student Number: 150200320
//--------------------------//

//-------------Do Not Add New Libraries-------------//
//-------------All Libraries Needed Were Given-------------//

#include <iostream>  // For input/output operations
#include <WordList.h>


//-------------Word Methods-------------//

Word::Word() {
  word_ = "";
  edit_dist_ = 999;  // An arbitrary number to set the distance as infinite
  next_ = NULL;
}

Word::Word(std::string vocab_word) {
  word_ = vocab_word;
  edit_dist_ = 999;  // An arbitrary number to set the distance as infinite
  next_ = NULL;
}


//-------------WordList Methods-------------//

WordList::WordList() {
  this -> head_ = NULL;
}

// Add all words to the list
WordList::~WordList() {
  Word* traverse = head_;

  // To make sure that we clear the memory when the program ends.
  while (traverse != NULL) {
    Word* temp = traverse;
    traverse = traverse -> next_;
    delete temp;
  }
}

void WordList::AddWord(std::string st){
  Word *newptr = new Word(st);


  if (head_ == NULL){

    head_ = newptr;
    tail_ = newptr;
    
  
  }

  else if(head_-> next_ == NULL){

    head_ -> next_ == newptr;
    

  }
  Word *temp = head_;

  while(temp-> next_ != NULL){
     
    temp = temp -> next_;
    return;
  }
  
  temp -> next_ = newptr;
  tail_ = newptr;

}

// Print first "n" words from the list
void WordList::PrintWords(int n){

  Word *printptr = head_;

  for(int i = 0; i <= n; i++){

      std::cout << printptr -> word_;
      printptr = printptr -> next_;
      return;


  }

}

  // Calculate edit distances for all words in the list
void WordList::CalcEditDists(std::string st){


}


  // Print first "n" words' edit distance from the list
void WordList::PrintEditDists(int n){


}

  // Print "n" words that has the lowest edit distance
void WordList::SuggestWords(int n){


}
