#include <iostream>
#include <fstream>
#include <cmath>

const double pi = 3.14;

void ConsoleWriter(double v)
{
    for (double h = 0.5; h <= 5; h += 0.5)
    {
        double r = sqrt(v / (pi * h));
        std::cout << "Радиус цилиндра с объемом 1 при высоте h = " << h << " равен " << r << "\n";
    }
}

void FileWriter(double v)
{
    std::ofstream file;
    file.open("rez.txt");
    if (file.is_open())
        for (double h = 0.5; h <= 5; h += 0.5)
        {
            double r = sqrt(v / (pi * h));
            file << "Радиус цилиндра с объемом 1 при высоте h = " << h << " равен " << r << "\n";
        }
    else
        std::cout << "Error!\n";
    file.close();
}

int main()
{
    double v = 1.0f;
    int key;
    while(true)
    {
        std::cout << "Добрый день! Пожалуйста, введите:\n" <<
        "0, чтобы получить результат в файл\n" <<
        "1, чтобы получить результат в консоль\n" <<
        "2, чтобы выйти.\n"
        "Ваш ввод: ";
        std::cin >> key;
        switch(key)
        {
            case 0:
            {
                FileWriter(v);
                break;
            }
            case 1:
            {
                ConsoleWriter(v);
                break;
            }
            case 2:
            {
                std::cout << "Хорошего дня!\n";
                return 0;
            }
            default:
            {
                std::cout << "Такая команда отсутствует, введите еще раз\n";
                break;
            }
        }
    }
    return 0;
}