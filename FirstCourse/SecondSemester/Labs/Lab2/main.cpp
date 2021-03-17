// 207
#include <iostream>
#include <fstream>

const char first_out = '0';
const char second_out = '5';
const std::string input_path = "input.txt";
const std::string output_path = "output.txt";
std::string input_way = "";

bool valid_input(std::string& input)
{
    size_t amount_of_digits = 0;
    for(auto& c : input)
        if (isdigit(c))
            ++amount_of_digits;

    return amount_of_digits == input.size();
}

void file_reader(std::string path, std::string& read_to)
{
    std::ifstream file(path);
    getline(file, read_to);
    file.close();
}

void file_writer(std::string path, std::string& to_write)
{
    std::ofstream file(path);
    file << to_write + "\n";
    file.close();
}

int input_menu()
{
    int key = 0;
    std::cout << "Доступные команды: \n" <<
        "0 - Ввод данных из консоли\n"  <<
        "1 - Ввод данных из файла 'input.txt'\n" <<
        "Ваш выбор: ";
    std::cin >> key;

    return key;
}

int output_menu()
{
    int key = 0;
    std::cout << "Доступные команды: \n" <<
        "0 - Вывод результата в консоль\n"  <<
        "1 - Вывод результата в файл 'output.txt'\n" <<
        "Ваш выбор: ";
    std::cin >> key;

    return key;
}

std::string symbol_remover(std::string& input)
{
    std::string out;
    for (size_t i = 0; i < input.size(); i++)
    {
        if ((input[i] != first_out) and (input[i] != second_out))
            out += input[i];
    }
    
    return out;
}

int main()
{
    bool is_working = true;
    int key;
    int inner_key;
    std::string input = "wrong input";
    while(is_working)
    {
        if(input_way == "")
        {
            key = input_menu();
            switch (key)
            {
                case 0:
                {
                    input_way = "console";
                    std::cout << "Введите число для редактирования: ";
                    std::cin >> input;
                    while(!valid_input(input))
                    {
                        std::cout << "К сожалению это не число! Повторите ваш ввод!\n";
                        std::cout << "Введите число для редактирования: ";
                        std::cin >> input;
                    }
                    break;
                }
                case 1:
                {
                    input_way = "file";
                    file_reader(input_path, input);
                    while(!valid_input(input))
                    {
                        std::cout << "К сожалению это не число! Измените запись в файле и перезапустите программу!\n";
                        is_working = false;
                        break;
                    }
                    break;
                }
                default:
                {
                    std::cout << "Такая команда отсутствует! Повторите попытку!\n";
                    break;
                }
            }
        }
        else
        {
            key = output_menu();
            switch (key)
            {
                case 0:
                {
                    std::cout << "Результат: " + symbol_remover(input) << "\n";
                    if(input_way == "file")
                    {
                        is_working = false;
                    }
                    else
                    {
                        std::cout << "Хотите продолжить? 1 - Да; 0 - Нет\nВаш выбор: ";
                        std::cin >> inner_key;
                        switch (inner_key)
                        {
                            case 1:
                            {
                                input_way = "";
                                std::cout << "Отлично!\n";
                                break;
                            }
                            case 0:
                            {
                                is_working = false;
                                break;
                            }
                            default:
                            {
                                std::cout << "Такая команда отсутствует! Повторите попытку!\n";
                                break;
                            }
                        }
                    }
                    break;
                }
                case 1:
                {
                    auto result = symbol_remover(input);
                    file_writer(output_path, result);
                    if(input_way == "file")
                    {
                        is_working = false;
                    }
                    else
                    {
                        std::cout << "Хотите продолжить? 1 - Да; 0 - Нет\nВаш выбор: ";
                        std::cin >> inner_key;
                        switch (inner_key)
                        {
                            case 1:
                            {
                                std::cout << "Отлично!\n";
                                input_way = "";
                                break;
                            }
                            case 0:
                            {
                                is_working = false;
                                break;
                            }
                            default:
                            {
                                std::cout << "Такая команда отсутствует! Повторите попытку!\n";
                                break;
                            }
                        }
                    }
                    break;
                }
                default:
                {
                    std::cout << "Такая команда отсутствует! Повторите попытку!\n";
                    break;
                }
            }
        } 
    }
    std::cout << "Хорошего дня!\n";
    return 0;
}