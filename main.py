from flask import Flask, render_template, request, redirect
import datetime

import openai
openai.api_key = "YOUR_API_KEY"
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


'''
response = openai.Completion.create(
    prompt='Write a cover letter for a job in data science',
    model='text-davinci-002',
    temperature=0.5, #this is the creativity of the generated text, from 0 dry cardboard to 1 wedding cake
    max_tokens=3000, #this paramater is the length of the generated text
    top_p=1, #this paramer helps generate more coherent and meaninful text at the detriment of creativity 0 uncoherent very creative 1 not as creative but more coherent
    frequency_penalty=1, #this parameter penalizes tokens that are similar even if they have high penatly, 0 no penalty for repeats, 1 generate less frequent and rarer tokens

    presence_penalty=1  # 0 dont penalize for generating tokens present in input, 1 penalize for generating tokens present in input
)

generated_text = response.choices[0].text
'''
@app.route("/result", methods=["POST"])
def result():
    with open("user_data.txt") as f:
        user_data = f.read()
    
    user_data += request.form.get('text-box')
    text_box = request.form.get('text-box')
    selected_value = request.form.get('dropdown')
    if selected_value == "1":
        user_data += "selected option was 1"
    elif selected_value == "2":
        user_data += "selected option was 2"
    
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("generated_response.txt", "a") as f:
        f.write(f"[{current_time}]\n")
        f.write(f"[text_box] \n{text_box}\n\n")
        f.write(f"[user_data]\n {user_data}\n\n=============================================\n")
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
