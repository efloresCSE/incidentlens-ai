# IncidentLens AI

An independent Python-based AI system for detecting,
analyzing, and investigating application incidents.

## Goals

- Process application and infrastructure logs.
- Train ML models for anomaly detection.
- Build an AI-powered incident analysis service.
- Expose functionality through a REST API.
- Develop with automated tests and CI/CD.
- Integrate with other applications.

## Tech Stack

- Python
- pytest
- scikit-learn (planned)
- FastAPI (planned)
- Docker and GitHub Actions (planned)

## Local Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## Run Tests

```bash
python -m pytest -v
```

## Status

Phase 1: Python foundations, testing, and CI/CD.
