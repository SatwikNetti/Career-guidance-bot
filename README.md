# Career Guidance Project (Interview-ready bundle)

This project demonstrates the pieces you described for your interview:
- Python (Flask) web app (api.py included if uploaded). See `app.py` to run a lightweight runner.
- Rasa Core scaffold for dialogue management (under `rasa/`).
- PostgreSQL schema (db/schema.sql) and example `.env.example` for DATABASE_URL.
- REST API key storage design (db/schema.sql + example endpoints in app.py and api.py).
- Libraries used: NLTK, spaCy, scikit-learn, pandas — see `examples/nlp_example.py`.
- Instructions to run locally are in this README.

## Quick run (local dev)
1. Create a Python 3.9+ virtualenv and activate it.
2. Install requirements: `pip install -r requirements.txt`
3. (Optional) Initialize Postgres and run `db/schema.sql`.
4. Copy `.env.example` to `.env` and set values.
5. Run the app: `python app.py` (or `python api.py` to run your uploaded file directly).

## Notes for interview
- `api.py` was included (the version you uploaded). You can mention it integrates with Google Gemini structured responses.
- Rasa shows dialogue structure and a custom action stub for integrating with ML or DB.
- We use `.env` for API key management (do not commit secrets).
- The `examples/` folder demonstrates the language libraries you listed; mention that actual model downloads (spaCy models, NLTK data) are done in setup.
