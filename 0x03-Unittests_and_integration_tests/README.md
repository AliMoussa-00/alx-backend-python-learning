# Unittests and Integration Tests

[tasks](https://drive.google.com/file/d/1xYo77Mn30PWihkAWSFqj-DRFNfUykU9P/view?usp=drive_link)

[unittest]([unittest — Unit testing framework — Python 3.12.3 documentation](https://docs.python.org/3/library/unittest.html))

---

## Introduction

Testing is an essential aspect of software development that ensures the reliability, correctness, and robustness of your codebase. Python offers several testing frameworks and techniques to facilitate the testing process.

## 1. Unit Tests

- **Definition**: Unit tests are designed to verify the correctness of individual units or components of code in isolation.
- **Purpose**: Ensure that each unit of code behaves as expected under various conditions.
- **Characteristics**:
  - Fine-grained and focus on small pieces of functionality.
  - Independent of external dependencies such as databases or network connections.
  - Execute quickly and frequently during development.
- **Example**:
  
  ```python
  # Example of a unit test
  def test_add():
      assert add(1, 2) == 3
      assert add(0, 0) == 0
      assert add(-1, 1) == 0
  ```
  

## 2. Integration Tests

- **Definition**: Integration tests verify interactions between different components or modules of a system.
- **Purpose**: Ensure that different parts of the system work together correctly.
- **Characteristics**:
  - Coarser-grained compared to unit tests.
  - Involve testing interactions with external dependencies such as databases or APIs.
  - Take longer to execute due to setup complexity.
- **Example**:
  
  ```python
  # Example of an integration test
  def test_get_user_integration():
      user = get_user('testuser')
      assert user is not None
      assert user[0] == 'testuser'
  ```
  

## 3. Mocking

- **Definition**: Mocking involves replacing real objects or dependencies with simulated objects during testing.
  
- **Purpose**: Isolate code under test and control the behavior of dependencies.
  
- **Use Cases**:
  
  - Simulating database interactions or HTTP requests.
  - Testing code that relies on external services without invoking them.
- **Example**:
  
  ```python
  from unittest.mock import Mock
  
  # Create a mock object
  mock_obj = Mock()
  ```
  

## 4. Parametrization

- **Definition**: Parametrization allows running the same test function with different sets of parameters.
  
- **Purpose**: Test a function or method with various inputs or conditions without duplicating test code.
  
- **Example**:
  
  ```python
  import pytest
  
  @pytest.mark.parametrize("input, expected", [
      (1, 2),
      (2, 4),
      (3, 6)
  ])
  def test_double(input, expected):
      assert input * 2 == expected
  ```
  

## 5. Fixtures

- **Definition**: Fixtures are functions that provide data or set up the environment for tests.
  
- **Purpose**: Share setup and teardown logic across multiple test functions or modules.
  
- **Example**:
  
  ```python
  import pytest
  
  @pytest.fixture
  def input_data():
      return [1, 2, 3, 4, 5]
  
  def test_sum(input_data):
      assert sum(input_data) == 15
  ```
  

## Conclusion

Testing is a crucial part of the software development process, and Python offers powerful tools and frameworks to facilitate testing. By understanding and applying unit tests, integration tests, mocking, parametrization, and fixtures, you can ensure the quality and reliability of your Python applications.

---

## Example of Mock

Scenario: You have a function `fetch_data_from_api()` that makes a request to an external API to fetch some data. You want to test this function without actually hitting the real API.

```python
import requests

def fetch_data_from_api():
    response = requests.get('https://api.example.com/data')
    if response.status_code == 200:
        return response.json()
    else:
        return None
```

Now, let's write a test for this function using a mock object to simulate the API response:

```python
import unittest
from unittest.mock import patch
from my_module import fetch_data_from_api

class TestFetchDataFromAPI(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_data_from_api_success(self, mock_get):
        # Configure mock response for success
        mock_response = {'key': 'value'}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Call the function under test
        result = fetch_data_from_api()

        # Verify the result
        self.assertEqual(result, mock_response)

    @patch('requests.get')
    def test_fetch_data_from_api_failure(self, mock_get):
        # Configure mock response for failure
        mock_get.return_value.status_code = 404

        # Call the function under test
        result = fetch_data_from_api()

        # Verify the result
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
```

Explanation:

1. We use the `@patch` decorator from the `unittest.mock` module to patch the `requests.get` function, which is called by `fetch_data_from_api()`. This effectively replaces the real `requests.get` function with a mock version during the test.
  
2. In each test method (`test_fetch_data_from_api_success` and `test_fetch_data_from_api_failure`), we configure the mock response returned by `requests.get`. We set the `status_code` attribute to simulate both success (status code 200) and failure (status code 404) scenarios.
  
3. We call the `fetch_data_from_api()` function under test, which internally makes a request using the patched `requests.get`. Depending on the configured mock response, we expect the function to return the appropriate result.
  
4. Finally, we verify the returned result to ensure that the function behaves correctly under different conditions.
  

In the example provided, `mock_get` is a mock object created to replace the `requests.get` function during the test. Let's break down its role and how it's used:

1. **Purpose**:
  
  - `mock_get` serves as a substitute for the `requests.get` function within the context of the test. By creating a mock object for `requests.get`, we can control its behavior and simulate different responses without actually making HTTP requests to the external API.
2. **Creation**:
  
  - The `mock_get` object is created **dynamically** by the `@patch` decorator from the `unittest.mock` module. It is passed as an argument to the test function (`test_fetch_data_from_api_success` and `test_fetch_data_from_api_failure`) to replace the original `requests.get` function.
3. **Configuration**:
  
  - Within each test method, we configure the behavior of `mock_get` to simulate different scenarios. For example, in `test_fetch_data_from_api_success`, we configure `mock_get` to return a mock response with status code 200 and a JSON payload. In `test_fetch_data_from_api_failure`, we configure it to return a mock response with status code 404.
4. **Usage**:
  
  - Once configured, `mock_get` is used implicitly by the function under test (`fetch_data_from_api`) when it calls `requests.get`. The function interacts with `mock_get` as if it were the real `requests.get` function, unaware that it's actually dealing with a mock object. This allows us to test the behavior of `fetch_data_from_api` in different scenarios without relying on the actual external API.
5. **Assertion**:
  
  - After calling the function under test (`fetch_data_from_api`), we verify the result based on the configured behavior of `mock_get`. For example, in `test_fetch_data_from_api_success`, we expect the function to return the mock response provided by `mock_get`. In `test_fetch_data_from_api_failure`, we expect the function to return `None` due to the simulated failure response.

In summary, `mock_get` is a mock object created to simulate the behavior of the `requests.get` function during testing. It allows us to control the responses returned by `requests.get` and test the behavior of our code under different conditions without relying on the actual external API.
