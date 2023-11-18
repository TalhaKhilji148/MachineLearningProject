from flask import Flask, request, jsonify, render_template
import util_home
import util_flat
import util_rent
from http.client import HTTPConnection
# from chat import get_response
app = Flask(__name__)

# @app.route('/hello')
# def hello():
#     return "Hi"

##the way we expose http endpoint is
#util have the all core routines
@app.route('/get_location_names_for_houses')
def get_location_names():
    response = jsonify({
        'House_location': util_home.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    #The Access-Control-Allow-Origin header is included in the response from one website to a
    # request originating from another website, and identifies the permitted origin of the request.
    HTTPConnection._http_vsn_str = "HTTP/1.0"
    return response

@app.route('/predict_houses_price', methods=['POST'])
def predict_home_price():
    print(request.form)
    total_sqft = float(request.form['total_sqft'])
    House_location = request.form['House_location']
    beds = int(request.form['beds'])
    baths = int(request.form['baths'])
    kitchens=int(request.form['kitchens'])
    tv_lounge=int(request.form['tv_lounge'])
    store=int(request.form['store'])

    response = jsonify({
        'estimated_price': util_home.get_estimated_price(House_location, total_sqft, beds, baths, kitchens, tv_lounge, store)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')


    return response


@app.route('/get_location_names_for_flats')
def get_flat_location_names():
    response = jsonify({
        'House_location': util_flat.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    #The Access-Control-Allow-Origin header is included in the response from one website to a
    # request originating from another website, and identifies the permitted origin of the request.
    return response

@app.route('/predict_flats_price', methods=['POST'])
def predict_flat_price():
    total_sqft = float(request.form['total_sqft'])
    House_location = request.form['House_location']
    beds = int(request.form['beds'])
    baths = int(request.form['baths'])


    response = jsonify({
        'estimated_price': util_flat.get_estimated_price(House_location, total_sqft, beds, baths, )
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_location_names_for_rent_a_house')
def get_rent_location_names():
    response = jsonify({
        'House_location': util_rent.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    #The Access-Control-Allow-Origin header is included in the response from one website to a
    # request originating from another website, and identifies the permitted origin of the request.
    return response

@app.route('/predict_rent_a_house_price', methods=['GET', 'POST'])
def predict_rent_home_price():
    total_sqft = float(request.form['total_sqft'])
    House_location = request.form['House_location']
    beds = int(request.form['beds'])
    baths = int(request.form['baths'])
    portion=int(request.form['portion'])
    garage=int(request.form['garage'])


    response = jsonify({
        'estimated_price': util_rent.get_estimated_price(House_location,total_sqft,baths,beds,portion,garage)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response



@app.route("/", methods=["GET"])
def index_get():
    return render_template("base.html")

@app.route('/predict', methods=["POST"])
def predict():
    # print()
    text=request.get_json().get("message")
    text = request.args.get('message')
    # response=get_response(text)
    # message ={"answer":response}
    return jsonify(message)



if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util_home.load_saved_artifacts()
    util_flat.load_saved_artifacts()
    util_rent.load_saved_artifacts()
    app.run()