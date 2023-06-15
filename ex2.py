from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)
about = {
    "version": "0.1",
    "name": "5G UDR Service"
}
subscriber_list = []


@app.route('/', methods=['GET'])
def default():
    return "This is a 5G UDR Service!"


@app.route('/about', methods=['GET'])
def about():
    return jsonify({'about': about})


def check_if_subscriber_exists(input_imsi):
    print("sub org list", subscriber_list)
    # Check is list is empty
    if not subscriber_list:
        print("List is empty")
    return False


    print("Checking if this imsi value already exists", input_imsi)
    # Loop through list and check if value exists in any "imsi" field
    for entry in subscriber_list:
        print(entry)
        for key, value in entry.items():
            if key == 'imsi':
                print("The key and value are ({}) = ({})".format(key, value))
                print("Compare value and input_imsi: ", value, input_imsi)
                if (value == input_imsi):
                    print("This imsi already exists", input_imsi)
                    return True
    return False


@app.route('/createSubscriber', methods=['POST'])
def createSubscriber():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.json
        if (check_if_subscriber_exists(data['imsi']) == False):
            print("New Subscriber added")
            subscriber_list.append(data)
            return (data)
        else:
            return "Subscriber already exists"
    else:
        return 'Content-Type not supported!'


@app.route('/listSubscriber', methods=['GET'])
def listSubscriber():
    return jsonify({'subscriber list': subscriber_list})


if __name__ == "__main__":
    app.run(debug=True)
