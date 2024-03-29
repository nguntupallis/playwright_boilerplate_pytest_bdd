# Playwright Pytest BDD Boilerplate

This is a boilerplate project for setting up and running end-to-end tests using Playwright, Pytest, and the Behavior-Driven Development (BDD) approach. It utilizes the dependency injection design pattern to provide a flexible and modular testing framework.

## Features

- **Playwright**: A Python library for automating browsers based on the powerful Playwright toolset.
- **Pytest**: A testing framework that makes it easy to write simple and scalable tests.
- **Behavior-Driven Development (BDD)**: A methodology for writing tests in simple, natural language constructs, making them more accessible to non-technical stakeholders.
- **Dependency Injection**: The project leverages the dependency injection design pattern to manage dependencies and promote code reusability and testability.

## Getting Started

### Prerequisites

- Python installed on your machine
- Pip package manager

### Installation

1. Clone this repository:

  ```bash
  git clone https://github.com/nguntupallis/playwright_pytest_bdd_boilerplate.git
  ```
2. Navigate to the project directory:

  ```bash
  cd playwright_pytest_bdd_boilerplate
  ```

3. Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```
## Docker

### Build Docker Image

Build the Docker image using the following command:

```bash
docker build -t your_docker_image_name -f Docker/tests.dockerfile .
```
### Run Docker Container

Run the Docker container using the following command:

```bash
docker run -it -p 5050:5050 \
  -e PASSWORD=$env:PASSWORD \
  -e HEADLESS_MODE="true" \
  -e TEST_ENVIRONMENT="qa" \
  -e BROWSER="mobile" \
  -e DEVICE="android" \
  your_docker_image_name
```
Replace your_docker_image_name with the desired name for your Docker image. This command will run the Docker container with the specified environment variables, including the password, headless mode, test environment, browser, and device configuration.

### Usage

1. Write your feature files using Gherkin syntax in the `features` directory.
2. Implement your step definitions in the `steps` directory using Python.
3. Obtain the password from [https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login) and replace `YourPasswordHere` with it in the setting variables command below.
4. Run the tests using the following command:

    ```bash
    # For Windows
    scoop install allure

    # For Linux
    apt-get update && apt-get install -y allure

    # Set the password, headless mode, test environment, and browser variables and run the tests 
    $env:PASSWORD = "YourPasswordHere"; $env:HEADLESS_MODE = "false"; $env:TEST_ENVIRONMENT= "qa"; $env:BROWSER= "chrome" tox
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

### Test Run Report

The latest test run report can be found [[here](https://stellar-cobbler-6334cd.netlify.app/)]
## Contributing

Contributions are welcome! If you have suggestions, improvements, or new features to add, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
   

