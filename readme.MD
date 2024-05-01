# DuckDB

## Overview
This tool supports querying CSV, XLSX (Excel), and JSON. It leverages DuckDB and the LLM to allow querying your data using natural language.

For optimal results with csv and xlsx, the first row should contain the column names.


## Examples
Here are a few examples of how you can query data using the GPTScript Tool with DuckDB:

### Query a CSV File
```gptscript
tools: github.com/gptscript-ai/duckdb

What is the email address of the person with the first name 'One' from the test.xlsx file?
```