import warnings
warnings.simplefilter("ignore",UserWarning)
import pickle
import json

import numpy as np

__locations = None
__data_columns = None
__model = None


def get_location_names():
    return __locations


def get_estimated_price(House_location,total_sqft,baths,beds,portion,garage):
    try:
        loc_index = __data_columns.index(House_location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = baths
    x[1] = beds
    x[2] = total_sqft
    x[3] = portion
    x[4] = garage

    if loc_index >= 0:
        x[loc_index] = 1
        if x[0] >= 1:
            if x[1] >= 1:
                if (x[2] > 0) & (x[2] < 4500):
                    # rounding of float number to two decimal place
                    return round(__model.predict([x])[0], 0)
                else:
                    print("Invalid Input for Square foot. It must be greater then 0 and less then 4500")
            else:
                print("Invalid Input for bedroom")
        else:
            print("Invalid Input for bath")
    else:
        print("Your Typed Location doesn't Exist")


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    with open("./artifacts/columns_rent.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[5:]  # first 5 columns are square foot, bedrooms, baths, kitchen,other

    global __model
    if __model is None:
        with open('./artifacts/islamabad_rent_a_house_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('Ghauri Town',1000,2,3,0,1))
