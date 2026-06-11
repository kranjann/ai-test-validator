from services.evaluator import Evaluator
from schemas.requirement import Requirement
from schemas.generated_test_case import GeneratedTestCase


def test_calculate_coverage_score_returns_100():

    evaluator = Evaluator()

    requirement = Requirement(
        requirement_id="REQ-001",
        requirement="Test Requirement",
        ground_truth=[
            "TC1",
            "TC2",
            "TC3",
            "TC4"
        ]
    )

    generated = GeneratedTestCase(
        requirement_id="REQ-001",
        test_cases=[
            "TC1",
            "TC2",
            "TC3",
            "TC4"
        ]
    )

    score = evaluator.calculate_coverage_score(
        requirement,
        generated
    )

    assert score == 100.0

def test_calculate_coverage_score_is_capped_at_100():

    evaluator = Evaluator()

    requirement = Requirement(
        requirement_id="REQ-001",
        requirement="Test Requirement",
        ground_truth=[
            "TC1",
            "TC2",
            "TC3",
            "TC4"
        ]
    )

    generated = GeneratedTestCase(
        requirement_id="REQ-001",
        test_cases=[
            "TC1",
            "TC2",
            "TC3",
            "TC4",
            "TC5"
        ]
    )

    score = evaluator.calculate_coverage_score(
        requirement,
        generated
    )

    assert score == 100.0

def test_calculate_overall_score_applies_hallucination_penalty():

    evaluator = Evaluator()

    score = evaluator.calculate_overall_score(
        coverage_score=100,
        similarity_score=80,
        hallucination_detected=True
    )

    assert score == 65.0

def test_calculate_overall_score_without_penalty():

    evaluator = Evaluator()

    score = evaluator.calculate_overall_score(
        coverage_score=100,
        similarity_score=80,
        hallucination_detected=False
    )

    assert score == 90.0

def test_generate_root_cause_for_missing_test_cases():

    evaluator = Evaluator()

    root_cause = evaluator.generate_root_cause(
        coverage_score=0,
        similarity_score=0,
        hallucination_detected=False
    )

    assert (
        root_cause ==
        "No test cases were generated for the requirement."
    )

def test_generate_root_cause_for_hallucination():

    evaluator = Evaluator()

    root_cause = evaluator.generate_root_cause(
        coverage_score=100,
        similarity_score=80,
        hallucination_detected=True
    )

    assert (
        root_cause ==
        "Generated output contains hallucinated test cases unrelated to the requirement."
    )