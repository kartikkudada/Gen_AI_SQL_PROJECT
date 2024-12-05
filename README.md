

# Project Overview 
# Gen_AI_SQL_PROJECT


This project leverages the capabilities of **Apache Spark**, **Langchain**, **MySQL Database**, and the **Google Gemini-1.5-flash model**. It enables interaction between a human and the system by interpreting natural language queries, generating SQL based on those queries, and executing them on a MySQL table to return accurate results.

## Key Technologies

- **Apache Spark**: Used to connect to the MySQL database and handle data processing tasks.
- **Langchain**: Utilized to enable natural language processing, understanding human queries, and generating SQL queries dynamically.
- **MySQL Database**: Serves as the primary data storage, with Spark interacting with tables to execute SQL queries.
- **Google Gemini-1.5-flash Model**: Powers the language understanding and generation capabilities for interpreting human questions.

## Project Workflow

1. **Spark and MySQL Connection**: Spark establishes a connection with the MySQL database and interacts with the specified table.
2. **Langchain Tools & Agent Toolkits**: Langchain processes human input, converts natural language queries into corresponding SQL statements, and prepares them for execution.
3. **Query Execution & Result Return**: The dynamically generated SQL query is run against the MySQL table, and the result is fetched and presented as an answer to the user.

## Usage

1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```

2. Install the required dependencies.

3. Set up the MySQL database and table structure.

4. Run the application to start interacting with it via natural language queries.

## Contributions

Feel free to submit pull requests or suggest improvements!

## License

[Your preferred license here]

---

Let me know if you'd like any changes or additions!
