# Quiz Python Module Documentation

The `quiz` module provides two methods for interacting with users to obtain their responses to questions or multiple-choice questions.

## Installing and using the Module

Install the module by using:
```
pip install quiz


To use the `quiz` module, you first need to import it using the following statement:

```python
import quiz
```

## Methods

The `quiz` module provides the following methods:

### • ask.question()

This method takes a single argument `question` which is a string that represents the question you want to ask the user. The method will print the question to the console and wait for the user to input their response. The user's response will be returned as a string.

Example usage:
```python
response = quiz.ask.question("What is your name?")
print(response)
```

Output:
```
What is your name?

> John

John
```

### • ask.choice()

This method takes three arguments:

- `question`: a string that represents the question you want to ask the user.
- `options`: a list of strings that represents the options the user can choose from.
- `default_choice`: an optional integer that represents the default choice the user will see highlighted. If not specified, the first option will be selected by default.

The method will print the question and the list of options to the console, and prompt the user to select an option using arrow keys. The user's selection will be returned as a tuple containing the selected option and its index.

Example usage:
```python
options = ['Option 1', 'Option 2', 'Option 3']
selected_option, index = quiz.ask.choice("Select an option:", options, default_choice=2)
print(selected_option)
```

Output:
```
Select an option:

    Option 1
  > Option 2
    Option 3

Option 3
```

## Dependencies

The `quiz` module requires the following dependencies to be installed:

- `pick`: a Python library for creating interactive command-line interfaces.
- `os`: a Python library for interacting with the operating system.
