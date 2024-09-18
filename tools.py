import PyPDF2
import os
from openai import OpenAI
from pydantic import BaseModel
from dotenv import load_dotenv

# Create a .env file in the root directory of the project and add the OPENAI_API_KEY variable
# or you can set openai_api_key directly
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)

# Pick the openai model you want to use

model = 'gpt-4o-2024-08-06'

def read_pdf(file_path):
    # Open the PDF file in binary mode
    with open(file_path, 'rb') as pdf_file:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(pdf_file)
        all_text = ''
        
        # Iterate through all the pages in the PDF
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            all_text += page.extract_text()  # Extract text from each page
            
    return all_text

def format_resume_txt(resume_file_path, file_path='prompts/prompt_convert_resume.txt', save=False):
    # Check if the formatted resume already exists
    formatted_resume_file = 'inputs/formated_resume.txt'
    
    if os.path.exists(formatted_resume_file):
        with open(formatted_resume_file, 'r') as file:
            formated_resume = file.read()
        return formated_resume

    # Read the raw resume from the PDF
    raw_resume = read_pdf(resume_file_path)

    # Read the prompt for converting the resume
    with open(file_path, 'r') as file:
        prompt_convert_resume = file.read()

    # Generate the formatted resume
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": prompt_convert_resume},
            {"role": "user", "content": raw_resume}
        ]
    )
    
    formated_resume = completion.choices[0].message.content

    # Save the formatted resume if save is True
    if save:
        with open(formatted_resume_file, 'w', encoding='utf-8') as text_file:
            text_file.write(formated_resume)

    return formated_resume


class JobInfo(BaseModel):
    job_title: str
    job_summary: str
    company_name: str
    company_summary: str
    company_vibe: str
    required_skills: list[str]
    preferred_skills: list[str]
    

def get_job_info(job_description_file = 'inputs/job_description.txt'):

    with open(job_description_file, 'r') as file:
        job_description = file.read()

    with open('prompts/prompt_job_info_extraction.txt', 'r') as file:
        prompt_job_summary = file.read()

    completion = client.beta.chat.completions.parse(
        model=model,
        messages=[
            {"role": "system", "content": prompt_job_summary},
            {"role": "user", "content": job_description},
        ],
        response_format=JobInfo,
    )

    job_info = completion.choices[0].message.parsed

    return job_info 


def build_cover_letter_generation_prompt(job_title, job_description, company_name, company_summary,company_vibe, candidate_resume, required_skills,preferred_skills,tone = 3, prompt_file = 'prompts/prompt_cover_letter_generation.txt'):
    # Read the template from the file
    with open(prompt_file, 'r') as file:
        prompt = file.read()

    # Replace placeholders with user input
    prompt = prompt.replace("{job_title}", job_title)
    prompt = prompt.replace("{job_description}", job_description)
    prompt = prompt.replace("{company_name}", company_name)
    prompt = prompt.replace("{company_summary}", company_summary)
    prompt = prompt.replace("{company_vibe}", company_vibe)
    prompt = prompt.replace("{candidate_info}", candidate_resume)
    prompt = prompt.replace("{required_skills}", ', '.join(required_skills))
    prompt = prompt.replace("{preferred_skills}", ', '.join(preferred_skills))
    prompt = prompt.replace("{tone}", str(tone))
    return prompt


def generate_cover_letter(job_title, job_description, company_name, company_summary,company_vibe, candidate_resume, required_skills,preferred_skills, tone = 3):
    prompt_cover_letter = build_cover_letter_generation_prompt(job_title, job_description, company_name, company_summary, company_vibe, candidate_resume, required_skills,preferred_skills, tone)

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": prompt_cover_letter}
        ]
    )

    cover_letter = completion.choices[0].message.content

    return cover_letter


