# AWS Backend

Backend scaffold for the AWS-hosted website. This repository provides a lightweight Python starting point with configuration, local data, dependency tracking, and a branching model aligned with the frontend repository.

## File Structure

```text
aws-backend/
├── app.py
├── config.json
├── data.json
├── requirements.txt
└── README.md
```

## What Each File Does

- `app.py`: application entry point and starter API server.
- `config.json`: runtime configuration such as host, port, and debug mode.
- `data.json`: sample data returned by the starter endpoint.
- `requirements.txt`: Python dependencies.
- `README.md`: setup instructions, workflow, and branching rules.

## How To Progress

1. Start backend work from `dev`.
2. Expand `config.json` before hardcoding environment values.
3. Add or replace sample records in `data.json` as the API model becomes clearer.
4. Extend `app.py` with routes, validation, and service logic.
5. Freeze or update dependencies in `requirements.txt`.
6. Merge into `main` only after the feature is validated on `dev`.

## Branching Strategy

- `main`: stable branch for production-ready backend code.
- `dev`: default branch for active development and integration.

Recommended flow:

```bash
git checkout dev
git pull origin dev
git checkout -b feature/<short-name>
# make changes
git add .
git commit -m "Add <feature>"
git push origin feature/<short-name>
```

Then:

1. Open a pull request into `dev`.
2. Test the API behavior and config changes.
3. Merge `dev` into `main` during release preparation.

## Local Setup

1. Install Python 3.11 or later.
2. Create a virtual environment.
3. Run `pip install -r requirements.txt`.
4. Start the server with `python app.py`.
5. Open `http://localhost:5000/health` to verify the service.
