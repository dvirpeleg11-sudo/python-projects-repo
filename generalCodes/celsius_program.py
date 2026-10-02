def main():
    celsius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]
    fahrenheit_temps = map(lambda c_temp: c_temp * 9/5 + 32, celsius_temps)

    print(celsius_temps)
    print(list(fahrenheit_temps))

if __name__ == "__main__":
    main()