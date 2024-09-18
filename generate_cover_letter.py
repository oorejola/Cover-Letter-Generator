from tools import get_job_info, format_resume_txt, generate_cover_letter

# Get job information
print('Getting job information... \n')
result = get_job_info('inputs/job_description.txt')

job_title = result.job_title
job_description = result.job_summary
company_vibe = result.company_vibe
company_name = result.company_name
company_summary = result.company_summary
required_skills = result.required_skills
preferred_skills = result.preferred_skills


# Get formatted resume
print('Reformatting resume... \n')
candidate_resume = format_resume_txt('inputs/resume.pdf',save=False)

# Generate cover letter
print('Generating cover letter... \n')
cover_letter = generate_cover_letter(job_title, job_description, company_name, company_summary,company_vibe, candidate_resume, required_skills,preferred_skills, tone = 4)

print(cover_letter)

cover_letter_file = 'outputs/coverletter.txt'
with open(cover_letter_file, 'w', encoding='utf-8') as text_file:
    text_file.write(cover_letter)

