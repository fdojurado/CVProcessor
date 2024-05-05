# CVProcessor

CVProcessor is a Python library for processing CV (Curriculum Vitae) or resume documents. It provides a set of functions and utilities to extract information from CVs, such as personal details, education, work experience, skills, and more.

## Features

- Extract personal details from CVs, including name, contact information, and address.
- Parse education details, including degrees, institutions, and dates.
- Extract work experience information, including job titles, companies, and dates.
- Identify and extract skills mentioned in CVs.
- Support for various CV formats, including PDF, Word, and plain text.

## Installation

You can install CVProcessor using pip:

```bash
pip install cvprocessor
```

## Usage

Here's a simple example of how to use CVProcessor to extract personal details from a CV:

```python
from cvprocessor import CVProcessor

# Load a CV file
cv_file = "resume.pdf"
cv = CVProcessor(cv_file)

# Extract personal details
personal_details = cv.extract_personal_details()
print(personal_details)
```
