# AI Test Validator

An AI-inspired Test Case Generation and Validation Framework designed to explore modern AI evaluation techniques such as semantic similarity, hallucination detection, automated grading, and ground-truth-based validation.

## Project Goal

This project simulates how AI-powered systems can generate and evaluate software test cases from business requirements.

The project is intentionally built in incremental phases:

1. Requirement Ingestion
2. Ground Truth Dataset Creation
3. Test Case Generation
4. Evaluation Engine
5. Semantic Similarity Scoring
6. Hallucination Detection
7. Automated Grading
8. Agentic Evaluation Workflows

## Current Features

### Requirement Dataset

Requirements are stored as structured JSON files.

Example:

```json
{
  "requirement_id": "REQ-001",
  "requirement": "Patient age must be between 18 and 60.",
  "ground_truth": [
    "Verify age 18 is accepted",
    "Verify age 60 is accepted",
    "Verify age below 18 is rejected",
    "Verify age above 60 is rejected"
  ]
}
```

### Requirement Loader

Loads all requirements and validates them using Pydantic schemas.

### Deterministic Test Case Generator

Generates baseline test cases using rule-based logic.

Example:

Input:

Patient age must be between 18 and 60.

Output:

* Verify value 18 is accepted
* Verify value 60 is accepted
* Verify value below 18 is rejected
* Verify value above 60 is rejected

## Project Structure

```text
ai-test-validator/

├── data/
│   └── requirements/

├── docs/

├── schemas/

├── services/

├── tests/

├── main.py

├── README.md

└── PROJECT_CONTEXT.md
```

## Tech Stack

* Python
* Pydantic
* PyTest
* JSON
* Pathlib

Future Additions:

* Sentence Transformers
* Cosine Similarity
* ChromaDB
* FastAPI
* Streamlit

## Learning Objectives

This project is designed to teach:

* AI Evaluation
* Ground Truth Dataset Design
* Data Validation
* Semantic Similarity
* Hallucination Detection
* Automated Grading
* Python Engineering
* Test Framework Design

## Status

Current Sprint:

Sprint 3 – Deterministic Test Case Generator

Upcoming Sprint:

Sprint 4 – Evaluation Engine
