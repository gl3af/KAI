// 141
#include <iostream>
#include <fstream>
#include <cmath>

const double pi = 3.14;

void menu()
{
    std::cout << "Доступные команды:\n" <<
    "0 - Вывод результата в файл\n" <<
    "1 - Вывод результата в консоль\n" <<
    "Ваш выбор: ";
}

void console_writer(double v)
{
    for (double h = 0.5; h <= 5.0; h += 0.5)
    {
        double r = sqrt(v / (pi * h));
        std::cout << "Радиус цилиндра с объемом 1 при высоте h = " << h << " равен " << r << "\n";
    }
}

void file_writer(double v)
{
    std::ofstream file;
    file.open("rez.txt");
    if (file.is_open())
        for (double h = 0.5; h <= 5.0; h += 0.5)
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
    int key = 0, inner_key = 0;
    bool is_active = true;
    while(is_active)
    {
        menu();
        std::cin >> key;
        switch(key)
        {
            case 0:
            {
                file_writer(v);
                bool wrong_input = true;
                while(wrong_input)
                {
                    std::cout << "Хотите продолжить? 1 - Да, 0 - Нет\n" << "Ваш выбор: ";
                    std::cin >> inner_key;
                    switch(inner_key)
                    {
                        case 1:
                        {
                            wrong_input = false;
                            break;
                        }
                        case 0:
                        {
                            wrong_input = false;
                            is_active = false;
                            break;
                        }
                        default:
                        {
                            std::cout << "Неверный ввод! Повторите снова\n";
                            break;
                        }
                    }
                }
                break;
            }
            case 1:
            {
                console_writer(v);
                bool wrong_input = true;
                while(wrong_input)
                {
                    std::cout << "Хотите продолжить? 1 - Да, 0 - Нет\n" << "Ваш выбор: ";
                    std::cin >> inner_key;
                    switch(inner_key)
                    {
                        case 1:
                        {
                            wrong_input = false;
                            break;
                        }
                        case 0:
                        {
                            wrong_input = false;
                            is_active = false;
                            break;
                        }
                        default:
                        {
                            std::cout << "Неверный ввод! Повторите снова\n";
                            break;
                        }
                    }
                }
                break;
            }
            default:
            {
                std::cout << "Такая команда отсутствует, введите еще раз\n";
                break;
            }
        }
    }
    std::cout << "Хорошего дня!\n";
    return 0;
}