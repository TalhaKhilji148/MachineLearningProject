import os
import warnings
warnings.simplefilter("ignore", UserWarning)
import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_location_names():
    return __locations

def get_estimated_price(House_location, total_sqft, beds, baths, kitchens, tv_lounge, store):
    try:
        loc_index = __data_columns.index(House_location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = baths
    x[1] = beds
    x[2] = total_sqft
    x[3] = kitchens
    x[4] = tv_lounge
    x[5] = store

    if loc_index >= 0:
        x[loc_index] = 1
        if x[0] >= 1:
            if x[1] >= 1:
                if 0 < x[2] < 30000:
                    # rounding of the float number to two decimal places
                    return round(__model.predict([x])[0], 0)
                else:
                    print("Invalid Input for Square foot. It must be greater than 0 and less than 30000")
            else:
                print("Invalid Input for bedroom")
        else:
            print("Invalid Input for bath")
    else:
        print("Your Typed Location doesn't Exist")

def load_saved_artifacts():
    print("Current Working Directory:", os.getcwd())  # Print current working directory
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    # Use os.path.join to create the correct file path
    columns_file_path = os.path.join("artifacts", "columns_home.json")
    with open(columns_file_path, "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[6:]  # first 6 columns are square foot, bedrooms, baths, kitchen, other

    global __model
    if __model is None:
        model_file_path = os.path.join("artifacts", "islamabad_houses_prices_model.pickle")
        with open(model_file_path, 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")
