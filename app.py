from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

app = Flask(__name__)
CORS(app)

criminals = [
    {
        "id": 1,
        "reward_text": "The FBI is offering a reward of up to $10,000 for information leading to the arrest of Christopher Gardner.",
        "aliases": "Chris Gardner",
        "warning_message": "SHOULD BE CONSIDERED AN INTERNATIONAL FLIGHT RISK.",
        "sex": "Male",
        "caution": "Christopher C. Gardner is wanted for his alleged participation in a wire fraud scheme and the transportation of a stolen motor vehicle in foreign commerce. It is alleged that in March 2001, Gardner burglarized a business in Milwaukee, Wisconsin, and stole a rare 1938 Talbot Lago T150C-SS “Teardrop” Coupe motor vehicle, chassis #90108. The vehicle is one of only approximately 16 such vehicles ever made. Gardner allegedly shipped the vehicle to Switzerland in 2006, had it restored in France, and in 2015 sold it to a buyer in the United States for $7.6 million. On May 29, 2019, Gardner was indicted on 4 counts of wire fraud and 1 count of transportation of stolen motor vehicle in foreign commerce in the United States District Court, Eastern District of Wisconsin, and a federal warrant was issued for his arrest. In June 2021, Gardner was arrested in Italy, placed on house arrest, and fled in November 2021. His whereabouts remain unknown.",
        "description": "Wire Fraud; Transportation of Stolen Motor Vehicle in Foreign Commerce"
    },
    {
        "id": 2,
        "reward_text": "The FBI is offering a reward of up to $10,000 to anyone with information leading to the location, arrest, and conviction of Darasy S. Chhim.",
        "aliases": "Darasy S. Chhim",
        "warning_message": "SHOULD BE CONSIDERED ARMED AND DANGEROUS",
        "sex": "Male",
        "caution": "The Federal Bureau of Investigation, Boston Division's Merrimack Valley Transnational Organized Crime Task Force, and the Lowell Police Department are asking for the public's assistance in locating Darasy S. Chhim, a member of the Lowell, Massachusetts-based gang One Family Clique (OFC), and the Bloods. Chhim is wanted for his alleged role in a large-scale and long-running drug trafficking conspiracy in which 15 alleged gang members and associates were charged. Chhim is the only remaining fugitive. A federal arrest warrant was issued for Chhim on June 9, 2021, in the United States District Court, District of Massachusetts, Boston, Massachusetts, after he was charged with Conspiracy to Distribute and to Possess with Intent to Distribute Heroin, 500 Grams or More of Cocaine, Cocaine Base, 40 Grams or More of Fentanyl, 500 Grams or More of Methamphetamine, and MDMA.",
        "description": "Conspiracy to Distribute and to Possess with Intent to Distribute Heroin, 500 Grams or More of Cocaine, Cocaine Base, 40 Grams or More of Fentanyl, 500 Grams or More of Methamphetamine, and MDMA"
    },
    {
        "id": 3,
        "reward_text": "The United States Government is offering a reward of up to $5,000,000 for information leading to the arrest and/or conviction of Semion Mogilevich.",
        "aliases": "Seva Moguilevich",
        "warning_message": "SHOULD BE CONSIDERED ARMED AND DANGEROUS",
        "sex": "Male",
        "description": "Fraud by Wire; RICO Conspiracy; Mail Fraud; Money Laundering Conspiracy; Money Laundering; Aiding and Abetting; Securities Fraud; Filing False Registration With the SEC; False Filings With the SEC; Falsification of Books and Records",
    }
]

@app.route('/')
def welcome():
    return render_template('welcome.html'), 200

@app.route('/criminals', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.form)
        new_criminal = request.form
        # print(new_criminal)
        # last_id = criminals[-1]['id']
        # new_criminal['id'] = last_id + 1
        criminals.insert(0, new_criminal)
        print(criminals)
        return render_template('index.html', result=criminals), 201
    elif request.method == "GET":
        return render_template('index.html', result=criminals), 200

@app.route('/criminals/<int:criminal_id>')
def show(criminal_id):
    criminal =  next(criminal for criminal in criminals if criminal['id'] == criminal_id)
    return render_template('criminal.html', result=criminal), 200

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


# @app.errorhandler(NotFound)
# def handle_404(err):
#     return jsonify({"message": f"Oops{err}"}), 404

# @app.errorhandler(InternalServerError)
# def handle_500(err):
#     return jsonify({"message": f"It's not you, it's us"})
#run app.py
if __name__ == "__main__":
    app.run()