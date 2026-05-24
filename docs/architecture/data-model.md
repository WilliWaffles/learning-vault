# Model for MVP v0.1

The visual ERD is defined in `learning-vault.dbml`.

```text
Language
 └── Category
      └── Topic
           ├── Theory Sections
           ├── Questions
           │    └── Question Attempts
           └── Exercises
                └── Exercise Attempts
```

# Language

Represents a programming language available in the application.

Examples:
- Python
- SQL
- TypeScript
- C#

Attributes:
- id
    - Unique identifier
- name
    - Visible name: Python, SQL, TypeScript, C#
- description
    - Brief description of the language
- created_at
    - Timestamp indicating when the record was created
- updated_at
    - Timestamp indicating when the record was updated

# Category

Represents a group of related topics inside a programming language.

Examples:
- Fundamentals
- Data Types
- Data Structures
- Object-Oriented Programming

One Language can have many Categories.
One Category belongs to one Language.

Attributes:
- id
    - Unique identifier
- language_id
    - Language unique identifier (Language entity)
- name
    - Visible name: Data Structures, OOP, Data Types, etc.
- description
    - Brief description of the category
- created_at
    - Timestamp indicating when the record was created
- updated_at
    - Timestamp indicating when the record was updated

# Topic

Represents a learning topic inside a category.

Examples:
- Functions
- Loops
- Dictionaries
- Exceptions

One Category can have many Topics.
One Topic belongs to one Category.

Future idea:
Topics could become global concepts shared between languages.

Attributes:
- id
    - Unique identifier
- category_id
    - Category unique identifier (Category entity)
- name
    - Visible name: For loops, conditionals, dictionaries, etc.
- description
    - Brief description of the topic
- created_at
    - Timestamp indicating when the record was created
- updated_at
    - Timestamp indicating when the record was updated

# Theory Section

Represents theory or notes related to a topic.

Examples:
- What is a list?
- List indexing
- List slicing
- Common list methods

One Topic can have many Theory Sections.
One Theory Section belongs to one Topic.

Attributes:
- id
    - Unique identifier
- topic_id
    - Topic unique identifier (Topic entity)
- title
    - Visible section title
- content
    - Theory or notes content for the section
- display_order
    - Helps organize sections inside a topic
- created_at
    - Timestamp indicating when the record was created
- updated_at
    - Timestamp indicating when the record was updated

# Question

Represents an open-ended review question related to a topic.

Examples:
- What is the difference between a list and a tuple?
- Why are strings immutable in Python?
- When would you use a dictionary instead of a list?

One Topic can have many Questions.
One Question belongs to one Topic.

Attributes:
- id
    - Unique identifier
- topic_id
    - Topic unique identifier (Topic entity)
- prompt
    - Question to be answered by the user
- expected_answer
    - Reference answer used for review and comparison
- created_at
    - Timestamp indicating when the record was created
- updated_at
    - Timestamp indicating when the record was updated

# Question Attempt

Represents a user response attempt for a question.

One Question can have many Question Attempts.
One Question Attempt belongs to one Question.

Attributes:
- id
    - Unique identifier
- question_id
    - Question unique identifier (Question entity)
- user_answer
    - User response for the question
- created_at
    - Timestamp indicating when the attempt was created

Future idea:
Question Attempts could later include AI feedback, score, reviewed_at, or self-assessment.

# Exercise

Represents a practical coding exercise related to a topic.

Examples:
- Coding challenges
- Input/output exercises
- Logic problems

One Topic can have many Exercises.
One Exercise belongs to one Topic.

Attributes:
- id
    - Unique identifier
- topic_id
    - Topic unique identifier (Topic entity)
- title
    - Visible exercise title
- description
    - Exercise instructions or problem statement
- difficulty
    - Exercise difficulty level: easy, medium, hard
- expected_input
    - Example input data for the exercise
- expected_output
    - Expected output result for the exercise
- test_script
    - Optional script the user can copy and run in an external IDE
- created_at
    - Timestamp indicating when the record was created
- updated_at
    - Timestamp indicating when the record was updated

# Exercise Attempt

Represents a user progress attempt for an exercise.

One Exercise can have many Exercise Attempts.
One Exercise Attempt belongs to one Exercise.

Attributes:
- id
    - Unique identifier
- exercise_id
    - Exercise unique identifier (Exercise entity)
- status
    - Current exercise progress status: not_started, in_progress, completed
- notes
    - Optional user notes about the exercise
- created_at
    - Timestamp indicating when the attempt was created
- updated_at
    - Timestamp indicating when the attempt was last modified

Future idea:
Exercise Attempts could later include submitted code path, self-rating, AI review, or completion time.

# Relations

Language 1 ────< Categories

Category 1 ────< Topics

Topic 1 ────< Theory Sections

Topic 1 ────< Questions

Question 1 ────< Question Attempts

Topic 1 ────< Exercises

Exercise 1 ────< Exercise Attempts