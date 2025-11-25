# Part 2: Prompts for Test Generation from Specifications


## Prompt 1: Generate Tests for is_prime

```
I have the following corrected formal specifications for the is_prime function:

Function signature: def is_prime(n: int) -> bool

Corrected Specifications (as assertions where 'res' is the return value):

# Specification 1: Numbers less than 2 are not prime
assert (n >= 2) or (not res), "Numbers < 2 must not be classified as prime"

# Specification 2: Number 2 is prime
assert (n != 2) or res, "2 must be classified as prime"

# Specification 3: Even numbers > 2 are not prime
assert (n <= 2) or (n % 2 != 0) or (not res), "Even numbers greater than 2 are not prime"

# Specification 4: If res is True, n has no divisors in [2, n-1]
assert (not res) or all(n % d != 0 for d in range(2, n)), \
    "If res is True, n must not be divisible by any number between 2 and n-1"

# Specification 5: If res is False and n >= 2, then n has some divisor in [2, n-1]
assert res or (n < 2) or any(n % d == 0 for d in range(2, n)), \
    "If res is False and n >= 2, there must exist a divisor between 2 and n-1"

Please generate pytest test cases that validate these specifications. Each test should:
1. Call is_prime with specific input values
2. Check that the result satisfies the relevant specifications
3. Be clearly labeled as spec-guided tests
4. Cover edge cases and boundary conditions implied by the specifications

Generate about 5-7 test functions in pytest format. Include:
- Test for n < 2 (Spec 1)
- Test for n = 2 (Spec 2)
- Test for even numbers > 2 (Spec 3)
- Test for prime numbers (Spec 4)
- Test for composite numbers (Spec 5)
- Edge cases

Format:
def test_spec_<number>_<description>():
    # Test for Specification <number>
    <test code>
```

---

## Prompt 2: Generate Tests for make_palindrome

```
I have the following corrected formal specifications for the make_palindrome function:

Function signature: def make_palindrome(string: str) -> str

Corrected Specifications (as assertions where 'res' is the return value):

# Specification 1: Empty string handling
assert (string != "") or (res == ""), \
    "If the input string is empty, the result must also be an empty string"

# Specification 2: The result must be a palindrome
assert res == res[::-1], \
    "The result must be a palindrome (equal to its own reverse)"

# Specification 3: The result must start with the original string
assert res.startswith(string), \
    "The result must begin with the original input string"

# Specification 4: Length constraints relative to input
assert (string == "" and len(res) == 0) or \
       (string != "" and len(string) <= len(res) <= 2 * len(string)), \
    "Result length must be at least the input length and at most twice the input length"

# Specification 5: Minimality – no shorter prefix of res is a valid palindrome starting with string
assert all(
    not (prefix.startswith(string) and prefix == prefix[::-1])
    for prefix in (res[:k] for k in range(len(string), len(res)))
), \
    "There must be no shorter prefix of res that is itself a palindrome starting with the input string"

Please generate pytest test cases that validate these specifications. Each test should:
1. Call make_palindrome with specific input values
2. Check that the result satisfies the relevant specifications
3. Be clearly labeled as spec-guided tests
4. Cover edge cases and boundary conditions implied by the specifications

Generate about 5-7 test functions in pytest format. Include:
- Test for empty string (Spec 1)
- Test that result is palindrome (Spec 2)
- Test that result starts with input (Spec 3)
- Test length constraints (Spec 4)
- Test minimality (Spec 5)
- Edge cases

Format:
def test_spec_<number>_<description>():
    # Test for Specification <number>
    <test code>
```

---

Generated test code from ChatGPT 5.1 saved in `chatgpt5.1/is_prime.txt` and `chatgpt5.1/make_palindrome.txt`. 

---

