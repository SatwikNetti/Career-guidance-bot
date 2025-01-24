from flask import Flask, request, render_template
import openai
import os

app = Flask(__name__)

# Set the OpenAI API key
openai.api_key = "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"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-guidance', methods=['POST'])
def get_guidance():
    # Extract form data
    skills = request.form.get('skills', '')
    strengths = request.form.get('strengths', '')
    interests = request.form.get('interests', '')

    prompt = (f"I am a career guidance expert. Based on the following details, suggest suitable career paths:\n"
              f"Skills: {skills}\nStrengths: {strengths}\nInterests: {interests}\n"
              f"Provide a concise, clear response.")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Use the specified model
            messages=[
                {"role": "system", "content": "You are a helpful career guidance expert."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )

        guidance = response['choices'][0]['message']['content'].strip()
        return render_template('result.html', response=guidance)

    except Exception as e:
        print(f"Error occurred: {e}")
        return render_template('result.html', response="An error occurred while generating the guidance. Please try again.")

if __name__ == '__main__':
    app.run(debug=True)
