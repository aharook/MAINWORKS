#include <iostream>

class Vehicle //загальний класс
{
public:
    Vehicle( double fuel, double distance) //загальний конструктор з параметрами
    {
        m_fuel = fuel;
        m_distance = distance;
    }
    double  GetFuel(){return m_fuel;}
    double  Getdistance(){return m_distance;}

    void SetFuel(double fuel){m_fuel = fuel;}
    void Setdistance(double distance){m_distance = distance;}

    virtual double fuel_consumption_calc() = 0; //абстрактний метод(без реалізації)

    virtual void info() // віртуальний метод(з реалізацією, яку можна змінити)
    {
        std::cout <<"total fuel content" << m_fuel << std::endl; 
    }

    ~ Vehicle() // деструктор
    {
        std::cout <<"Destructor called" << std::endl;
    }
    
protected:
    double m_fuel;
    double m_distance;
};

class Bus: public Vehicle // класс наслідник №1
{
public:
    Bus(double fuel, double distance) : Vehicle( fuel, distance ) {} // заміна base()

    double fuel_consumption_calc() override //override абстрактного методу
    {
       return m_fuel * m_distance / 100;
    };
    
    void info() override
    {
        std::cout <<"Bus for passengers" << std::endl;
    }
};

class Truck: public Vehicle //класс наслідник №2
{
public:
    Truck(double fuel, double distance) : Vehicle( fuel, distance ) {} //заміна base()

    double fuel_consumption_calc() override   //override абстрактного методу
    {
       return m_fuel * m_distance / 100;
    };
    
    void info() override 
    {
        std::cout <<"Truck is working" << std::endl;
    }
       
};

int main()
{
    Bus bus(20, 40);
    std::cout << "fuel consumption: on distantion "<< bus.Getdistance() <<" km is: " << bus.fuel_consumption_calc() <<" liters" << std::endl;
    bus.info();
    std::cout << std::endl;

    Truck truck(120, 300);
    std::cout << "fuel consumption on distantion "<< truck.Getdistance() <<" km is: " << truck.fuel_consumption_calc() << " liters" << std::endl;
    truck.info();
    std::cout << std::endl;

    Vehicle* vehicles[] = {&bus, &truck};

    for(int i = 0; i<2; i++)
    {
         std::cout << "fuel consumption on distantion "<< vehicles[i]->Getdistance() <<" km is: " << vehicles[i]->fuel_consumption_calc() << " liters" << std::endl;
         vehicles[i]->info();
    }

}
