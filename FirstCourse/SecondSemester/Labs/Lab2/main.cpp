// 207
#include <iostream>
#include <algorithm>
#include <fstream>

const char first_out = '0';
const char second_out = '5';
const std::string path = "input.txt";

// ready
bool valid_input(std::string& input)
{
    size_t amount_of_digits = 0;
    for(auto& c : input)
        if (isdigit(c))
            ++amount_of_digits;

    return amount_of_digits == input.size();
}

// ready
std::string file_reader(std::string path)
{
    std::ifstream file(path);
    std::string input;
    char c;
    getline(file, input);
    file.close();
    return input;
}

void menu()
{
    std::cout << "Доступные команды:\n" <<
    "0 - Вывод результата в файл\n" <<
    "1 - Вывод результата в консоль\n" <<
    "2 - Выход\n" <<
    "Ваш выбор: ";
}

//ready
std::string symbol_remover(std::string& input)
{
    std::string out;
    int curr_pos = 0;
    for (size_t i = 0; i < input.size(); i++)
    {
        if ((input[i] != first_out) and (input[i] != second_out))
            out.insert(curr_pos++, 1, input[i]);
    }
    
    return out;
}

int main()
{
    std::string input_way;
    bool is_working = true;
    std::cout << file_reader(path);
    return 0;
}