from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def botler():
    return render_template('botler.html')
'''
@app.route('/settings', methods=["POST"])
def settings():
    css_file = 'botler_settings.css'
    if request.form.get("settings"):
        return render_template('botler_settings.html', css_file=css_file)
 '''   
@app.route('/settings', methods=["POST"])
def settings():
    css_file = 'botler_settings.css'
    user_data = {}
    if request.form.get("settings"):
        with open("user_data.txt", "r") as f:
            for line in f:
                key, value = line.strip().split(":")
                user_data[key] = value
        return render_template('botler_settings.html', css_file=css_file, user_data=user_data)

@app.route("/result", methods=["POST"])
def result():
    with open("user_data.txt") as f:
        user_data = f.read()
    
    user_data += request.form.get('text-box')
    selected_value = request.form.get('dropdown')
    if selected_value == "1":
        user_data += "selected option was 1"
    elif selected_value == "2":
        user_data += "selected option was 2"
    
    return render_template('result.html',user_data = user_data)

@app.route('/ret', methods=['POST'])
def ret():
    return redirect('/')

@app.route('/save', methods=['POST'])
def save():
    name = request.form.get('name')
    academic_history = request.form.get('academic-history')
    experience = request.form.get('experience')
    interests = request.form.get('interests')
    facts_to_consider = request.form.get('facts-to-consider')

    # Save the data to the user's computer
    with open("user_data.txt", "w") as f:
        f.write(f"Name:{name}\n")
        f.write(f"Academic History:{academic_history}\n")
        f.write(f"Experience:{experience}\n")
        f.write(f"Interests:{interests}\n")
        f.write(f"Facts to Consider:{facts_to_consider}\n")
    return redirect('/')
    
if __name__ == '__main__':
    app.run(debug=True)
