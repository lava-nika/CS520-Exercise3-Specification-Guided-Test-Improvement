#!/usr/bin/env python3
"""
Script for comparing coverage for baseline (HumanEval) tests with spec-guided tests for both problems.
"""

import subprocess
import sys
import json
from pathlib import Path

def extract_function_from_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    in_function = False
    function_lines = []
    for line in lines:
        if line.strip().startswith('def is_prime') or line.strip().startswith('def make_palindrome') or line.strip().startswith('def is_palindrome'):
            in_function = True
        if in_function:
            function_lines.append(line)
            if line.strip().startswith('def test_') or line.strip().startswith('class '):
                function_lines.pop() 
                break
    
    return ''.join(function_lines)

def run_baseline_test(problem_id, problem_data):
    print(f"BASELINE TESTS - {problem_id}")
    
    func_code = problem_data['prompt'] + problem_data['canonical_solution']
    
    test_code = problem_data['test']
    
    temp_file = f"temp_baseline_{problem_id}.py"
    with open(temp_file, 'w') as f:
        f.write(func_code)
        f.write('\n\n')
        
        f.write(test_code)
        f.write('\n\n')
        
        f.write('def test_baseline():\n')
        f.write(f'    check({problem_data["entry_point"]})\n')
    
    cmd = [
        'pytest',
        temp_file,
        f'--cov={temp_file.replace(".py", "")}',
        '--cov-report=term-missing',
        '--cov-branch',
        '-v',
        '--tb=short'
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    
    Path(temp_file).unlink(missing_ok=True)
    Path('.coverage').unlink(missing_ok=True)
    
    return result.returncode

def run_spec_guided_test(problem_folder, label, function_name):
    print(f"SPEC-GUIDED TESTS - {label}")
    
    test_dir = f"Ex2_with_spec_guided_tests/{problem_folder}"
    test_file = "spec_guided_tests.py"
    
    if not Path(f"{test_dir}/{test_file}").exists():
        print(f"ERROR: {test_dir}/{test_file} not found!")
        return 1
    
    cmd = [
        'python', '-m', 'pytest',
        test_file,
        f'--cov=spec_guided_tests',
        '--cov-report=term-missing',
        '--cov-branch',
        '-v',
        '--tb=short'
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=test_dir)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    
    Path(f"{test_dir}/.coverage").unlink(missing_ok=True)
    
    return result.returncode

def main():
    print("EXERCISE 3 PART 2 - Coverage Comparison")
    
    problems_file = 'selected_humaneval_problems.json'
    with open(problems_file, 'r') as f:
        all_problems = json.load(f)
    
    print("# PROBLEM 4: is_prime (HumanEval/31)")
    
    is_prime_data = all_problems['HumanEval/31']
    run_baseline_test('is_prime', is_prime_data)
    run_spec_guided_test('problem4', 'is_prime', 'is_prime')
    
    print("# PROBLEM 10: make_palindrome (HumanEval/10)")
    
    make_palindrome_data = all_problems['HumanEval/10']
    run_baseline_test('make_palindrome', make_palindrome_data)
    run_spec_guided_test('problem10', 'make_palindrome', 'make_palindrome')

if __name__ == '__main__':
    main()
