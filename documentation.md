# .\main.py

This is the main entry point script for a code documentation tool. Here's a detailed breakdown of its components and functionality:

## Imports
- Uses the `Documenter` class from `src.document`
- Utilizes Python's built-in `argparse` for command-line argument parsing

## Constants
`CODE_EXTENSIONS`: A comprehensive set of file extensions covering numerous programming languages and file types, including:
- C/C++ family files
- Java-related files
- Web development files (JavaScript, HTML, CSS)
- Scripting languages (Python, Ruby, Perl)
- Shell scripts
- Data formats (JSON, XML, YAML)
- And many other programming language file extensions

## Main Function
The `main()` function sets up and handles command-line arguments:

### Arguments
- `file`: Required argument for the file to process
- `--hidden`: Optional flag to include hidden files
- `--all`: Optional flag to include all files
- `--langs`: Optional argument to specify specific file extensions to process

### Processing
1. Parses command-line arguments
2. Processes language specifications if provided
3. Creates a Documenter instance
4. Initiates documentation generation

## Script Execution
Contains standard Python idiom for script execution:
```python
if __name__ == "__main__":
   main()
```

## Usage
The script can be run from the command line with various combinations of arguments to control documentation generation for different file types and scenarios.

# ./src/document.py

This file contains the `Documenter` class which handles generating markdown documentation for code files using Claude AI.

## Dependencies
- typing
- anthropic
- datetime
- os
- json
- re
- subprocess
- src.utils (should_print)

## Class: Documenter

The main class for handling code documentation generation.

### Class Variables
- `SYSTEM_PROMPT`: Instructions for Claude AI to generate markdown documentation

### Methods

#### `__init__()`
Initializes a new Documenter instance with empty markdown and counter.

#### `_read_file(filename)`
Private method that reads contents of a file.
- **Args**: filename (str) - Path to file to read
- **Returns**: str - Contents of file

#### `_document_file(filename)` 
Private method that generates markdown documentation for a single file using Claude AI.
- **Args**: filename (str) - Path to file to document
- **Effect**: Writes output to temporary file and appends to markdown

#### `document(path, tabs, hidden=False, all_=True, extensions=None)`
Recursively documents files in a directory structure.
- **Args**:
  - path (str): Directory path to document
  - tabs (int): Indentation level
  - hidden (bool): Whether to include hidden files
  - all_ (bool): Whether to document all files
  - extensions (list): File extensions to include
- **Effect**: Processes files and generates documentation

#### `write_md(md)`
Writes markdown content to documentation file.
- **Args**: md (str) - Markdown content to write
- **Returns**: dict indicating success/failure
- **Effect**: Appends content to documentation.md file

## Usage
The Documenter class is used to generate documentation by:
1. Instantiating a Documenter object
2. Calling document() with a path to generate docs
3. Documentation is accumulated in documentation.md




# ./src/utils.py

This utility module provides functionality for file system operations and code file identification.

## Constants

### CODE_EXTENSIONS
A set containing file extensions for various programming languages and related file types, including:
- C/C++ family files
- Java related files
- Python files
- Web development files (JavaScript, HTML, CSS)
- Various other programming language extensions

## Functions

### find_files(path, tabs, hidden=False, all_=True, extensions=None)
Recursively lists files and directories in a given path with indentation.

Parameters:
- `path`: String path to directory to search
- `tabs`: Integer number of tabs for indentation
- `hidden`: Boolean to include hidden files
- `all_`: Boolean to include all files vs only code files
- `extensions`: Set of file extensions to filter by

Prints files/directories with the following format:
- Directories prefixed with "d: "
- Files prefixed with "f: "
- Indentation based on directory depth

### is_code_file(filename, extensions)
Checks if a file is a code file based on its extension.

Parameters:
- `filename`: String name of file to check
- `extensions`: Set of extensions to check against

Returns:
- Boolean indicating if file has a code extension

### should_print(filename, hidden, all_, is_dir, extensions)
Determines if a file/directory should be included in output based on filters.

Parameters:
- `filename`: String name of file/directory
- `hidden`: Boolean to include hidden files
- `all_`: Boolean to include all files vs only code files  
- `is_dir`: Boolean indicating if path is directory
- `extensions`: Set of extensions to filter by

Returns:
- Boolean indicating if file/directory should be printed
# CalorieCounter/addcustom.php

## Overview
This file provides a web interface for users to add custom food items to their calorie tracking database. It consists of an HTML form for input and PHP code for database operations.

## HTML Structure
- Main heading "Calorie Count!"
- Form for custom food entry with the following fields:
  - Food Name (text input)
  - Calories Per OZ (number input)
  - Serving Size (number input)
  - Submit button labeled "Create"

## PHP Components

### Database Configuration
- Uses `parse_ini_file()` to read database credentials from a config.ini file
- Establishes MySQL database connection using the following parameters:
  - host
  - user
  - password
  - database

### Form Processing
- Checks for GET request containing 'food' parameter
- When food parameter exists:
  1. Calls `add()` function with form data
  2. Closes database connection
  3. Redirects to home.php

### Add Function
```php
function add($food, $cal, $size, $cn)
```
- Purpose: Inserts custom food information into CustomFood table
- Parameters:
  - $food: Food name
  - $cal: Calories per ounce
  - $size: Serving size
  - $cn: Database connection object
- Uses prepared statements for secure database insertion
- Retrieves user information from cookies
- Table Structure: CustomFood(user, food_name, calories, serving_size)

## Security Features
- Uses prepared statements to prevent SQL injection
- Database credentials stored in external configuration file

## Dependencies
- Requires config.ini file with database credentials
- Requires active MySQL/MariaDB database
- Requires user to be logged in (uses cookie 'user')

## Redirect
- Upon successful addition, redirects to home.php# CalorieCounter/addmeal.php

This PHP file manages the meal creation interface of a calorie counting application. Here's a breakdown of its functionality:

## Page Structure
- Displays a header with "Calorie Count!"
- Shows the current date from a cookie
- Contains multiple forms and tables for food selection and meal creation

## Main Features

### Search Form
- Allows users to search for foods by name
- Implements a simple search interface with a text input and submit button

### Database Connection
- Establishes connection using credentials from a config.ini file
- Uses mysqli for database operations

### Food Search Functionality
- Function `search($food, &$namearr, &$per_ozarr, &$select_txt, $cn)`
- Searches food database for items matching user input
- Limits results to 10 items
- Displays results in a table showing:
  - Food name
  - Calories per ounce
  - Serving size

### Meal Building
- Function `addtomeal($name, $food_oz, $per_oz, &$chosen_names, &$chosen_cals, &$chosen_oz)`
- Allows users to select foods and specify portions
- Maintains running list of selected foods
- Stores selections in cookies for persistence

### Meal Submission
- Function `makemeal($mealname, $chosen_cals, $chosen_names, $chosen_oz, $cn)`
- Saves completed meal to database
- Inserts records into both Meal and MealFoods tables
- Calculates total calories for the meal

## Cookie Management
- Tracks selected foods
- Stores meal information temporarily
- Manages user session data

## Tables
1. Food Selection Table
   - Shows search results
   - Displays food details and selection options

2. Current Meal Table
   - Shows foods added to current meal
   - Displays portions and calorie information

## Forms
1. Search Form
   - For finding foods in database

2. Food Addition Form
   - For adding selected foods to meal

3. Meal Submission Form
   - For naming and saving the complete meal# CalorieCounter/analytics.php

This PHP script provides analytics functionality for a calorie counting application. The file consists of both PHP code and HTML elements to display various statistics about a user's food consumption.

## Main Components

### User Authentication
- Retrieves the current user from cookies
- Displays the user's name at the top of the analytics page

### Database Connection
- Reads database configuration from a config.ini file
- Establishes connection to MySQL database using mysqli

### Analytics Queries

1. **Maximum Calorie Days**
   - Finds the day(s) when the user consumed the most calories
   - Displays dates and calorie counts in a list format

2. **Minimum Calorie Days**
   - Identifies the day(s) with lowest calorie intake
   - Shows dates and calorie counts in a list format

3. **Average Daily Calories**
   - Calculates the average calories consumed per day across all entries
   - Rounds the result to 2 decimal places

4. **Popular Foods**
   - Lists the top 5 most frequently consumed foods
   - Shows rank, food name, and number of times eaten

### Date Range Analysis Form
- HTML form that allows users to input a date range
- Contains fields for start date and end date
- Submits via GET method

### Date Range Statistics
When date range is submitted, displays:
- Total calories consumed in the period
- Average daily calories during the period
- Comparison with user's calorie goal
- Shows whether user is over or under their goal

## Technical Details
- Uses prepared statements for SQL queries
- Implements proper statement closure
- Includes input parameter binding for security
- Formats output with HTML for better presentation

## Notes
- Database credentials are stored in config.ini (should be secured)
- All queries are specific to the logged-in user
- Includes basic error handling
# CalorieCounter/database_init.sql

This SQL script initializes the database schema for a Calorie Counter application. It creates several interconnected tables to manage users, foods, meals, and logging functionality.

## Table Structure

### User Table
- Stores basic user information
- Fields:
  - `username` (VARCHAR[20]) - Primary Key
  - `goal` (INTEGER) - User's calorie goal

### Food Table
- Stores standard food items
- Fields:
  - `f_name` (VARCHAR[20]) - Primary Key
  - `cal_per_oz` (INTEGER) - Calories per ounce
  - `oz_per_serving` (INTEGER) - Ounces per serving

### CustomFood Table
- Stores user-defined food items
- Fields:
  - `username` (VARCHAR[20]) - Foreign Key to User
  - `f_name` (VARCHAR[20]) 
  - `cal_per_oz` (INTEGER)
  - `oz_per_serving` (INTEGER)
- Composite Primary Key: (f_name, username)

### FoodLog Table
- Tracks individual food consumption
- Fields:
  - `user` (VARCHAR[20]) - Foreign Key to User
  - `f_name` (VARCHAR[20]) - Foreign Key to Food
  - `calories` (INTEGER)
  - `log_date` (DATETIME)
- Composite Primary Key: (user, f_name, log_date)

### Meal Table
- Defines meal combinations
- Fields:
  - `m_name` (VARCHAR[20])
  - `username` (VARCHAR[20]) - Foreign Key to User
  - `calories` (INTEGER)
- Composite Primary Key: (m_name, username)

### MealFoods Table
- Links meals to their constituent foods
- Fields:
  - `m_name` (VARCHAR[20]) - Foreign Key to Meal
  - `f_name` (VARCHAR[20]) - Foreign Key to Food
  - `user` (VARCHAR[20]) - Foreign Key to User
  - `f_oz` (INTEGER) - Amount of food in ounces
- Composite Primary Key: (m_name, f_name, user)

### MealLog Table
- Tracks meal consumption
- Fields:
  - `m_name` (VARCHAR[20]) - Foreign Key to Meal
  - `user` (VARCHAR[20]) - Foreign Key to User
  - `log_date` (DATETIME)
- Composite Primary Key: (m_name, user, log_date)

### CustomLog Table
- Tracks custom food consumption
- Fields:
  - `f_name` (VARCHAR[20]) - Foreign Key to CustomFood
  - `user` (VARCHAR[20]) - Foreign Key to User
  - `calories` (INTEGER)
  - `log_date` (DATETIME)
- Composite Primary Key: (f_name, user, log_date)

## Notes
- The script begins by dropping any existing tables to ensure a clean initialization
- Tables are created with appropriate foreign key constraints to maintain data integrity
- All string fields are limited to 20 characters# CalorieCounter/home.php

This file serves as the main dashboard for the Calorie Counter application. It provides a user interface for managing daily food intake and calorie tracking.

## Page Structure

### Navigation Buttons
- Log Food
- Log Meal
- Log Custom Food
- Analytics
- Create Meal
- Create Custom Food

### Date Selection
- Form allows users to select a specific date for viewing food logs
- Defaults to current date if none selected

### Main Features

1. **User Welcome Section**
   - Displays username
   - Shows selected date
   - Displays daily calorie goal

2. **Food Log Tables**
   - Regular Food Log (shows number, food name, calories)
   - Meal Log (shows meal name and calories)
   - Custom Food Log (shows food name and calories)

3. **Summary Statistics**
   - Shows total calories consumed
   - Displays percentage of daily goal reached

4. **Food Entry Management**
   - Remove Food feature
   - Edit Calories feature

## Technical Implementation

### Database Connection
- Utilizes config.ini file for database credentials
- Establishes MySQL connection

### Cookie Management
- Manages cookies for:
  - User session
  - Date selection
  - Meal tracking

### SQL Queries
1. User goal retrieval
2. Food log entries
3. Meal log entries
4. Custom food entries

### Functions
- `remove()`: Removes food entries from the log
- Edit functionality: Updates calorie values for existing entries

### Security Features
- Uses prepared statements for SQL queries
- Parameter binding for user inputs

## Display Components
- HTML tables for food logs
- Dropdown menus for food selection
- Forms for data modification
- Dynamic content generation through PHP

# CalorieCounter\index.php

This file serves as the landing page for the Calorie Counter application. It contains a simple HTML structure with navigation buttons.

## Structure

- Basic HTML document
- Main heading "Calorie Count!"
- Two navigation buttons:
  1. "Log In" button that links to `login.php`
  2. "Sign Up" button that links to `signup.html`

## Elements

- `<h1>`: Displays the application title
- Two `<button>` elements wrapped in `<a>` tags for navigation
- `<br>` tag for spacing between buttons

## Navigation

- The "Log In" button redirects users to the login page (login.php)
- The "Sign Up" button redirects new users to the registration page (signup.html)
# CalorieCounter/logcustom.php

This file manages the logging of custom food entries in a calorie counting application.

## Overview
The script provides functionality for users to log custom food items with their caloric intake. It includes a form interface and database interactions for storing food consumption records.

## Key Components

### Database Connection
- Utilizes a configuration file (`config.ini`) for database credentials
- Establishes connection to MySQL database using mysqli

### Custom Food Retrieval
- Queries the `CustomFood` table for foods associated with the current user
- Stores food details in arrays:
  - `$per_ozarr`: Calories per ounce
  - `$foodname_arr`: Food names
  - `$select_text`: HTML options for dropdown menu

### Form Interface
- Displays a form with:
  - Dropdown menu of custom foods
  - Input field for ounces consumed
  - Submit button for logging

### Logging Function
`logfood()` function handles:
- Takes parameters:
  - `$num`: Selected food index
  - `$ozs`: Amount consumed
  - `$foodnamearr`: Array of food names
  - `$per_ozarr`: Array of calorie values
  - `$cn`: Database connection
- Calculates total calories
- Inserts record into `CustomLog` table with:
  - Food name
  - Username
  - Calculated calories
  - Date

### Security Features
- Uses prepared statements for database queries
- Parameter binding for SQL injection prevention

### Navigation
- Redirects to `home.php` after successful food logging

## Dependencies
- Requires active database connection
- Needs `config.ini` file with database credentials
- Relies on user cookies for:
  - Username (`user`)
  - Date (`date`)