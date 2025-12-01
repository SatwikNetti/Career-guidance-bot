from flask import Flask, request, render_template
import google.generativeai as genai
import os
import json

app = Flask(__name__)


genai.configure(api_key="include api key here")


model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def get_gemini_structured_response(prompt):
    try:
        
        generation_config = {
            "response_mime_type": "application/json",
            "response_schema": {
                "type": "ARRAY",
                "items": {
                    "type": "OBJECT",
                    "properties": {
                        "jobTitle": { "type": "STRING" },
                        "description": { "type": "STRING" }
                    }
                }
            }
        }
        
        response = model.generate_content(prompt, generation_config=generation_config)
        raw_response_text = response.text.strip()

        # Validate if the response is empty
        if not raw_response_text:
            return json.dumps({"error": "Gemini API returned an empty response. Please try again."})

        
        try:
            json.loads(raw_response_text)
            return raw_response_text
        except json.JSONDecodeError:
            print(f"Gemini API returned malformed JSON: {raw_response_text}")
            return json.dumps({"error": "Gemini API returned malformed data. Please try again."})

    except Exception as e:
        print(f"Error occurred while calling Gemini API: {e}")
        
        return json.dumps({"error": f"An error occurred while generating guidance: {e}"})

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-guidance', methods=['POST'])
def get_guidance():
    skills = request.form.get('skills', '')
    strengths = request.form.get('strengths', '')
    interests = request.form.get('interests', '')

    prompt = (
        f"Based on the following details, suggest 3-5 suitable career paths. "
        f"For each path, provide a concise job title and a brief job description (2-3 sentences). "
        f"Ensure the output is a JSON array of objects, where each object has 'jobTitle' and 'description' keys.\n"
        f"Skills: {skills}\nStrengths: {strengths}\nInterests: {interests}\n"
    )

    guidance_json_string = get_gemini_structured_response(prompt)

    try:
        
        guidance_data = json.loads(guidance_json_string)
    except json.JSONDecodeError:
        guidance_data = [{"jobTitle": "Error", "description": "Invalid response from Gemini API."}]

    return render_template('result.html', response_data=guidance_data)

if __name__ == '__main__':
    # Run the Flask app
    
    app.run(debug=True)
