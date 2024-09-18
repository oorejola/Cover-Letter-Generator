# Cover Letter Generator

This project automatically generates personalized cover letters based on your resume and a job description.

## File Structure

```
.
├── LICENSE
├── inputs/
│   ├── resume.pdf
│   └── job_description.txt
├── outputs/
├── prompts/
├── tools.py
├── generate_cover_letter.py
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.7+
- OpenAI API key

## Setup

1. Clone this repository.
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up your OpenAI API key:
   - Option 1: Create a `.env` file in the project root and add your API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```
   - Option 2: Hard-code your API key in the `tools.py` file (not recommended for security reasons).

## Usage

1. Replace the `resume.pdf` file in the `inputs/` directory with your own resume.
2. Replace the `job_description.txt` file in the `inputs/` directory with the job description you're applying for.
3. Run the script:
   ```
   python generate_cover_letter.py
   ```
4. Your generated cover letter will be saved in the `outputs/` directory.

## Prompt Engineering

This project utilizes advanced prompt engineering techniques to improve the quality and relevance of the generated cover letters. The `prompts/` folder contains three main prompts, each designed for a specific task in the cover letter generation process:

1. Resume Formatting Prompt:
   - Purpose: Converts various resume formats into a structured markdown format.
   - Key Features:
     * Uses markdown headers to organize sections (e.g., Experience, Education, Skills)
     * Formats contact information, experience, and education consistently
     * Preserves all original information while improving readability

2. Job Description Analysis Prompt:
   - Purpose: Extracts key information from the job description.
   - Key Features:
     * Identifies job title, company name, and summarizes main responsibilities
     * Extracts up to 5 required and 5 preferred skills/qualifications
     * Analyzes company vibe and culture based on the job description language

3. Cover Letter Generation Prompt:
   - Purpose: Creates a tailored cover letter based on the resume and job description analysis.
   - Key Features:
     * Adjusts tone based on a 1-5 scale (very formal to casual)
     * Structures the letter with an opening, skills alignment paragraphs, and closing
     * Emphasizes how the candidate's skills match the job requirements
     * Incorporates the company's vibe into the letter's style

These prompts work together to:
- Extract relevant information from your resume
- Analyze the job description for key requirements and company culture
- Structure the cover letter in a professional format
- Tailor the content to highlight your qualifications for the specific job

By using well-designed prompts, the system generates focused and effective cover letters. Users can modify these prompts in the `prompts/` folder to fine-tune the output according to their preferences or specific industry requirements.

## License

See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This tool is for assistance purposes only. Always review and personalize the generated cover letter before sending it to potential employers.