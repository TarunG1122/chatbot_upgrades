from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

button_logic_to_col_names = {
    'Precon - NTP': [
        "How many Sites are waiting for NTP ?",
        "One Quote submission pending for how",
        "How many site Installation started but N"
    ],
    'Installation': [
        "Which market has most number of sites",
        "How many sites are Cx WIP now ?",
        "MS1555 done but MS15550 not done"
    ],
    'SCOP': [
        "How many sites are pending for SCOP Su",
        "Which market has highest rollout in past",
        "Which market has the highest no. of site",
        "Which market has the most SCOP Reject",
        "Which market has the more SCOP Resub",
        "Which market has the highest ageing for",
        "Which market has more SCOP Acceptanc",
        "What is Rank of Portland in SCOP rejecti",
        "Which region is having least SCOP reject",
        "How many site are SCOP submission pen",
        "How many sites are stuck in between 95"
    ],
    'E2E': [
        "Which market has highest rollout in past",
        "Which market taking lowest cycle time ?",
        "Which market has the highest cycle time",
        "Which Market has Highest Rev Rec base",
        "Which market has more Rev Rec Contrib",
        "How many sites construction completed E2E"
    ],
    'Cycle time / E2E': [
        "Which market taking lowest cycle time ?",
        "Which market has the highest cycle time"
    ],
    'Rev. Rec': [
        "Which market has most number of sites"
    ],

}



@app.route('/')
def index():
    return render_template('TMO-logic-check-1.html')  # make sure 'index.html' is the name of your HTML file

@app.route('/get-button-logic', methods=['GET'])
def get_button_logic():
    # Return all the unique Button_logic values
    return jsonify(list(button_logic_to_col_names.keys()))

@app.route('/get-col-names', methods=['POST'])
def get_col_names():
    button_logic = request.json['button_logic']
    col_names = button_logic_to_col_names.get(button_logic, [])
    return jsonify(col_names)



if __name__ == '__main__':
    app.run(debug=True)
