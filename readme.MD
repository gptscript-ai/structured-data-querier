# structured-data-querier

## Overview
This tool supports querying CSV, XLSX (Excel), and JSON. It leverages DuckDB and the LLM to allow querying your data using natural language.

For optimal results with csv and xlsx, the first row should contain the column names.


## Examples

### Query an Excel File
```gptscript
tools: github.com/gptscript-ai/structured-data-querier

What is the email address of the person with the first name 'One' from the test.xlsx file?
```