#include <iostream>
int main(){
int base,altura,area;
std::cout << ("ingresa el valor de la base");	
std::cin >> base;	
std::cout << ("ingresa el valor de la altura");	
std::cin >> altura;

area=base*altura;

std::cout << ("el area del rectangulo es:") << area << std::endl;
return 0;
}
