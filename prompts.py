SYSTEM_PROMPT = """You are a senior recruiter with over 20 years of experience in talent acquisition. 
Your job is to analyze resumes against job descriptions and provide detailed, actionable feedback.
Always respond with valid JSON only. No extra text, no markdown, no code blocks."""

def get_analysis_prompt(resume_text, job_description):
    return f"""Analyze the following resume against the job description and return a JSON with exactly these fields:

{{
    "candidate_name": "full name from resume",
    "ats_compliance": {{
        "score": 0-100,
        "keyword_detection": "brief assessment",
        "section_formatting": "brief assessment",
        "layout_compatibility": "brief assessment"
    }},
    "job_match": {{
        "match_percentage": 0-100,
        "matching_skills": ["skill1", "skill2"],
        "missing_keywords": ["keyword1", "keyword2"],
        "skill_gap_analysis": "brief paragraph"
    }},
    "recommendations": {{
        "gaps": ["gap1", "gap2"],
        "suggestions": ["suggestion1", "suggestion2"]
    }}
}}

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}"""