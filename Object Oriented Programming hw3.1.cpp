/* @Author
* Student Name: Beyza Nur Keskin
* Student ID : 150200320
*/

#include <iostream>
#include <string>
#include <random>
#include "psychicPokemon.h"

//I assigned the functions of the functions I created in psychichpokemon.h

PsychicPokemon::PsychicPokemon(const std::string& name, int hp, int damage)
        : Pokemon(name, hp, damage, 0.3, 5) {
    }
