def pricing(VehicleType: str, VehicleCount: int, PricingMethod: str, PricingMethodUnits: float):
    # pricing method units is how many days hours or miles
    dictionary = {
        'Cha_Daily': 1000.00,
        'Cha_Hourly': 400.00,
        'Cha_Distance': 3.50,
        'Min_Daily': 925.00,
        'Min_Hourly': 360.00,
        'Min_Distance': 3.25,
        'Spr_Daily': 850.00,
        'Spr_Hourly': 320.00,
        'Spr_Distance': 3.00,
        'Par_Daily': 775.00,
        'Par_Hourly': 280.00,
        'Par_Distance': 2.75,
        'Sed_Daily': 700.00,
        'Sed_Hourly': 240.00,
        'Sed_Distance': 2.50,
        'SUV_Daily': 625.00,
        'SUV_Hourly': 200.00,
        'SUV_Distance': 2.25,
        'Lim_Daily': 550.00,
        'Lim_Hourly': 160.00,
        'Lim_Distance': 2.00,
        'Tro_Daily': 475.00,
        'Tro_Hourly': 120.00,
        'Tro_Distance': 1.75,
    }
    VehicleTypeRate = dictionary.get(VehicleType[0:3] + '_' + PricingMethod)
    price = VehicleCount * VehicleTypeRate * PricingMethodUnits
    return price


if __name__ == '__main__':
    price = pricing('Trolly', 2, 'Hourly', 3.0)
    # pricing('string of vehicle (spelling matters)', 'number of vehicles (integer)', 'Rate type (spelling matters)',
    # 'Float of number of days, hours, or miles')
    print(f'The cost of renting the vehicle is {price} dollars')