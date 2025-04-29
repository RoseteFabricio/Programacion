#include <iostream>
int main(){
int base,altura,area;
std::cout << ("ingresa el valor de la base");	
std::cin >> base;	
std::cout << ("ingresa el valor de la altura");	
std::cin >> altura;

area=base*altura/2;

std::cout << ("el area del triangulo es:") << area << std::endl;
return 0;
}
