from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def botler():
    return render_template('botler.html')

@app.route('/settings', methods=["POST"])
def settings():
    css_file = 'botler_settings.css'
    if request.form.get("settings"):
        return render_template('botler_settings.html', css_file=css_file)
    
@app.route('/save', methods=['POST'])
def save():
    name = request.form.get('name')
    academic_history = request.form.get('academic-history')
    experience = request.form.get('experience')
    interests = request.form.get('interests')
    facts_to_consider = request.form.get('facts-to-consider')

    # Save the data to the user's computer
    with open("user_data.txt", "w") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Academic History: {academic_history}\n")
        f.write(f"Experience: {experience}\n")
        f.write(f"Interests: {interests}\n")
        f.write(f"Facts to Consider: {facts_to_consider}\n")
    return "Data saved successfully!"
    
if __name__ == '__main__':
    app.run(debug=True)
