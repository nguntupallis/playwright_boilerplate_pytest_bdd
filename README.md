## Getting Started

### Prerequisites

- Python installed on your machine
- Pip package manager

### Installation

1. Clone this repository:

  ```bash
  git clone [https://github.com/nguntupallis/playwright_pytest_bdd_boilerplate.git](https://github.com/nguntupallis/playwright_pytest_bdd_boilerplate.git)
  ```
2. Navigate to the project directory:

  ```bash
  cd playwright_pytest_bdd_boilerplate
  ```

3. Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```
### Usage

1. Write your feature files using Gherkin syntax in the `features` directory.
2. Implement your step definitions in the `steps` directory using Python.
3. Provide the correct password in .env file
4. Run the tests using the following command:

    ```bash
    scoop install allure (for windows)
    apt-get update && apt-get install -y allure (for linux)
    tox
    ```

### Configuration

- Modify the `pytest.ini` file to configure Pytest options and plugins.
- Update the `tox.ini` file to define the test environments and configurations.

### Folder Structure
- features
- steps
- pages
- helpers
- pages
- Docker

## Contributing

Contributions are welcome! If you have suggestions, improvements, or new features to add, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
   

