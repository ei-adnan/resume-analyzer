# 📄 Adnan's Resume Analyzer

An AI-powered resume analysis tool that scores ATS compliance, matches your skills against a job description, and gives actionable recommendations to improve your chances of getting hired.

🔗 **[Try it live →](https://resume-analyzer-adnan.streamlit.app)**

---

## What it does

Paste your resume and a job description and get back:

- **ATS Compliance Score** — how well your resume is formatted and keyword-optimized for applicant tracking systems
- **Job Match Percentage** — how closely your skills align with the job requirements
- **Skill Gap Analysis** — what's missing and why it matters
- **Recommendations** — specific, actionable suggestions to improve your resume for that role

## Example Output

```
Candidate: Adrian Keller
ATS Score: 85/100 | Job Match: 75%

Matching Skills: Python, SQL, Power BI, Data Cleaning
Missing Keywords: R, CRM, Azure, Databricks

Recommendations:
- Consider taking a course in R to enhance programming skills
- Gain experience with CRM tools through projects or internships
- Explore Azure and Databricks through online resources or certifications
```

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | Streamlit |
| AI Model | OpenAI GPT-4o-mini |
| Language | Python |
| Deployment | Streamlit Cloud |
| Containerization | Docker |

## How to run locally

**1. Clone the repo**
```bash
git clone https://github.com/ei-adnan/resume-analyzer.git
cd resume-analyzer
```

**2. Create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your OpenAI API key**
```bash
echo "OPENAI_API_KEY=your_key_here" > .env
```

**5. Run the app**
```bash
python -m streamlit run app.py
```

## How to run with Docker

```bash
docker build -t resume-analyzer .
docker run --env-file .env -p 8501:8501 resume-analyzer
```

Then open `http://localhost:8501` in your browser.

---

*Part of my Applied AI Engineering portfolio. Built during P3 of my roadmap.*
