#include <iostream>
#include <string>

class Iengine {
    public:
    virtual void start() = 0;
    virtual void stop() = 0;
    virtual ~Iengine() = default;
};

class Itiers{
    public:
    virtual void health() = 0;
    virtual void badly() = 0;
    virtual ~Itiers() = default;
};

class Car : public Iengine, public Itiers {
    protected:
    std::string model;
    int year;
    int maxSpeed;

    public:
    Car(std::string m, int y, int ms) : model(m), year(y), maxSpeed(ms) {}

    std::string getModel() const {
        return model;
    }
    int getYear() const {
        return year;
    }
    int getMaxSpeed() const {
        return maxSpeed;
    }

    void start() override {
        std::cout << "Car " << model << " started." << std::endl;
    }

    void stop() override {
        std::cout << "Car " << model << " stopped." << std::endl;
    }

    void health() override {
        std::cout << "Tires are in good condition." << std::endl;
    }
    void badly() override {
        std::cout << "Tires need replacement!" << std::endl;
    }

};

class SportsCar : public Car
{
    private:
    int horsePower;

    public:
    SportsCar(std::string m, int y, int ms, int hp) : Car(m, y, ms), horsePower(hp) {}

    int getHorsePower() const {
        return horsePower;
    }

    void start() override {
        std::cout << "SportsCar " << model << " with " << horsePower << " HP started." << std::endl;
    }

    void stop() override {
        std::cout << "SportsCar " << model << " stopped." << std::endl;
    }

    void problems() {
        if (horsePower > 400) {
            std::cout << "Warning: High horsepower may lead to engine problems!" << std::endl;
        } else {
            std::cout << "Engine is running smoothly." << std::endl;
        }
    }

    

    void carInfo() {
        std::cout << "Model: " << model << ", Year: " << year << ", Max Speed: " << maxSpeed << " km/h, Horse Power: " << horsePower << " HP" << std::endl;

        health();
        problems();
        badly();

    };
};

int main() {
    std::string a;
    int b;
    int c;
    int d;
     std::cout << "Enter SportsCar model: ";
    std::cin >> a;
     std::cout << "Enter SportsCar year: ";
    std::cin >> b;
    std:: cout << "Enter SportsCar max speed: ";
    std::cin >> c;
    std:: cout << "Enter SportsCar horse power: ";
    std::cin >> d;


    SportsCar mySportsCar(a, b, c, d);

    std::cout << "Car Information:" << std::endl;
    mySportsCar.carInfo();

    std::cout << "do u wana start the car? (y/n): ";
    char choice;
    std::cin >> choice;
    if (choice == 'y' || choice == 'Y') {
        mySportsCar.start();
    } else {
        std::cout << "Car not started." << std::endl;
    }
    return 0;
};