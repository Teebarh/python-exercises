def make_car(manufacturer, model_name, **car_info):
    """This function creates a dictionary that accepts info on a car profile."""
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info

