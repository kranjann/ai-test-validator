# Project Context

## Overview

AI Test Validator is a learning project designed to simulate the evaluation workflows used in modern AI-powered systems.

The project focuses on generating and validating test cases from requirements while introducing concepts commonly used in AI Quality Assurance and LLM Evaluation.

---

## Problem Statement

Traditional software systems produce deterministic outputs.

Example:

Input:
User enters invalid password.

Output:
Login fails.

Expected output can be validated exactly.

AI systems are different.

Example:

Requirement:
Patient age must be between 18 and 60.

Generated Test Cases:

Output A:

* Verify age 18 is accepted
* Verify age 60 is accepted

Output B:

* Validate minimum age boundary
* Validate maximum age boundary

Both outputs may be correct.

Traditional equality-based validation becomes insufficient.

---

## Project Objectives

The project aims to answer:

1. How can AI-generated test cases be evaluated?
2. How can semantic similarity be measured?
3. How can hallucinated outputs be detected?
4. How can automated grading be implemented?
5. How can evaluation datasets be designed?

---

## Architecture

Current Architecture

```text
Ground Truth Dataset
        │
        ▼
Requirement Loader
        │
        ▼
Requirement Objects
        │
        ▼
Test Case Generator
```

Target Architecture

```text
Ground Truth Dataset
        │
        ▼
Requirement Loader
        │
        ▼
Test Case Generator
        │
        ▼
Generated Test Cases
        │
        ▼
Evaluation Engine
        │
        ├── Coverage Scoring
        ├── Similarity Scoring
        ├── Hallucination Detection
        └── Automated Grading
        │
        ▼
Evaluation Report
```

---

## Key Concepts

### Ground Truth

Human-validated expected test cases used as a benchmark.

### Coverage

Measures how many expected test cases are generated.

### Semantic Similarity

Measures meaning similarity rather than exact text matching.

### Hallucination

Generated test cases that are unrelated to the requirement.

### Automated Grading

Programmatic scoring of generated outputs.

---

## Development Approach

Development follows an incremental sprint-based workflow.

### Sprint 1

Ground Truth Dataset

Status: Completed

### Sprint 2

Requirement Loader

Status: Completed

### Sprint 3

Deterministic Test Case Generator

Status: Completed

### Sprint 4

Evaluation Engine

Status: Planned

### Sprint 5

Embedding-Based Similarity Engine

Status: Planned

### Sprint 6

Hallucination Detection

Status: Planned

### Sprint 7

LLM-Based Evaluation

Status: Planned

---

## Long-Term Vision

Transform the project into a complete AI Evaluation Framework capable of:

* Requirement Understanding
* Test Case Generation
* Semantic Evaluation
* Hallucination Detection
* Automated Scoring
* Evaluation Reporting

This mirrors the validation workflows used in modern AI and LLM-based systems.
