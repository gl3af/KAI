#include <iostream>
#include <cmath>

int main()
{
    double x1, x2;
    int roots = 0;
    int a,b,c;
    std::cout << "Введите a: ";
    std::cin >> a;
    std::cout << "Введите b: ";
    std::cin >> b;
    std::cout << "Введите c: ";
    std::cin >> c;
    // x + 2 >= 0
    double D = sqrt(pow(a - c, 2) + 4 * (a * c - b));
    if (D == 0)
    {
        x1 = (c - a) / 2.0;
        if (x1 >= -1 * a)
        {
            ++roots;
            std::cout << "Корень уравнения: " << x1 << "\n";
        }
    }
    else if(D > 0)
    {
        x1 = (c - a + D) / 2.0;
        x2 = (c - a - D) / 2.0;
        if (x1 >= -1 * a)
        {
            ++roots;
            std::cout << "Корень уравнения: " << x1 << "\n";
        }
        if (x2 >= -1 * a)
        {
            ++roots;
            std::cout << "Корень уравнения: " << x2 << "\n";
        }
    }
    // x + 2 < 0
    D = sqrt(pow(a - c, 2) + 4 * (a * c + b));
    if (D == 0)
    {
        x1 = (c - a) / 2.0;
        if (x1 < -1 * a)
        {
            ++roots;
            std::cout << "Корень уравнения: " << x1 << "\n";
        }
    }
    else if(D > 0)
    {
        x1 = (c - a + D) / 2.0;
        x2 = (c - a - D) / 2.0;
        if (x1 < -1 * a)
        {
            ++roots;
            std::cout << "Корень уравнения: " << x1 << "\n";
        }
        if (x2 < -1 * a)
        {
            ++roots;
            std::cout << "Корень уравнения: " << x2 << "\n";
        }
    }
    if(roots == 0)
    {
        std::cout << "Корней нет :(\n";
    }
    return 0;
}