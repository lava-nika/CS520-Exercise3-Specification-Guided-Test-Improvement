# Exercise 3: Specification-Guided Test Improvement

**Student**: Lavanika Srinivasaraghavan  
**Course**: CS 520 - Fall 2025  
**Repository for Exercise 3**: https://github.com/lava-nika/CS520-Exercise3-Specification-Guided-Test-Improvement 

**Reference repository (Exercise 2)**: https://github.com/lava-nika/CS520-Exercise2-Automated-Testing-and-Coverage

---


## Quick Start

### Setup
- **Install dependencies**: `pip install -r requirements.txt`

This installs:

* pytest - Testing framework
* pytest-cov - Coverage plugin for pytest
* coverage - Core coverage measurement tool

---

## Instructions to run

### Prerequisites

Install required packages:
```bash
pip install pytest pytest-cov
```

### Run coverage analysis

```bash
python run_ex3_coverage.py
```

This script will:
1. Run baseline HumanEval tests for both problems
2. Run spec-guided tests for both problems
3. Display coverage comparison (statement and branch coverage)

**Expected Output:**
- Baseline coverage for is_prime: **100% statement, 100% branch**
- Spec-guided coverage for is_prime: **100% statement, 100% branch**
- Baseline coverage for make_palindrome: **100% statement, 100% branch**
- Spec-guided coverage for make_palindrome: **100% statement, 100% branch**

### Run individual test files

```bash
# Test is_prime spec-guided tests
cd Ex2_with_spec_guided_tests/problem4
pytest spec_guided_tests.py -v

# Test make_palindrome spec-guided tests
cd Ex2_with_spec_guided_tests/problem10
pytest spec_guided_tests.py -v
```

### To optionally generate HTML coverage reports 

```bash
# For is_prime
cd Ex2_with_spec_guided_tests/problem4
pytest spec_guided_tests.py --cov=spec_guided_tests --cov-report=html --cov-branch -v
# HTML report will be in: htmlcov/index.html
open htmlcov/index.html  # macOS
# Or: xdg-open htmlcov/index.html  # Linux
# Or: start htmlcov/index.html  # Windows

# For make_palindrome
cd ../problem10
pytest spec_guided_tests.py --cov=spec_guided_tests --cov-report=html --cov-branch
# HTML report will be in: htmlcov/index.html
open htmlcov/index.html
```
### Sample HTML reports
From Ex3 directory run:
```
open htmlcov/problem4_is_prime/index.html
open htmlcov/problem10_make_palindrome/index.html
```

---

## Submission contents

### Documentation

#### `Exercise3_Final_Report_Lavanika.md` or `Exercise3_Final_Report_Lavanika.pdf`: Final report

#### `Ex3_Part2_Prompts.md`
LLM prompts used to generate test cases from corrected specifications:
- Prompt 1: Generate tests for is_prime
- Prompt 2: Generate tests for make_palindrome

### Code Files

#### `run_ex3_coverage.py`
Script that does the following:
- Loads baseline HumanEval tests from `selected_humaneval_problems.json`
- Creates temporary test files for baseline tests
- Runs spec-guided tests from `Ex2_with_spec_guided_tests/`
- Measures and reports statement and branch coverage
- Compares baseline vs spec-guided coverage

#### `Ex2_with_spec_guided_tests/problem4/spec_guided_tests.py`
6 test functions for is_prime based on corrected specifications:
- `test_spec_1_numbers_less_than_two`
- `test_spec_2_two_is_prime`
- `test_spec_3_even_numbers_greater_than_two`
- `test_spec_4_prime_numbers_have_no_divisors`
- `test_spec_5_composite_numbers_have_divisors`
- `test_spec_edge_negative_and_large_values`

#### `Ex2_with_spec_guided_tests/problem10/spec_guided_tests.py`
6 test functions for make_palindrome based on corrected specifications:
- `test_spec_1_empty_string`
- `test_spec_2_result_is_palindrome_for_various_inputs`
- `test_spec_3_result_starts_with_input`
- `test_spec_4_length_constraints`
- `test_spec_5_minimality_property`
- `test_spec_edge_cases_various_strings`

---