import streamlit as st
import openai
import json
import os
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT, get_analysis_prompt

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Adnan's Resume Analyzer", page_icon="📄")
st.title("📄 Adnan's Resume Analyzer")
st.write("Paste your resume and job description to get instant feedback.")

resume_text = st.text_area("Your Resume", height=300, placeholder="Paste your resume text here...")
job_description = st.text_area("Job Description", height=300, placeholder="Paste the job description here...")

if st.button("Analyze"):
    if not resume_text or not job_description:
        st.warning("Please fill in both fields.")
    else:
        with st.spinner("Analyzing..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                temperature=0.3,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": get_analysis_prompt(resume_text, job_description)}
                ]
            )

            result = json.loads(response.choices[0].message.content)

        st.success("Analysis Complete!")

        st.subheader(f"Candidate: {result['candidate_name']}")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("ATS Score", f"{result['ats_compliance']['score']}/100")
        with col2:
            st.metric("Job Match", f"{result['job_match']['match_percentage']}%")

        st.subheader("ATS Compliance")
        st.write(f"**Keyword Detection:** {result['ats_compliance']['keyword_detection']}")
        st.write(f"**Section Formatting:** {result['ats_compliance']['section_formatting']}")
        st.write(f"**Layout Compatibility:** {result['ats_compliance']['layout_compatibility']}")

        st.subheader("Job Match")
        st.write(f"**Skill Gap Analysis:** {result['job_match']['skill_gap_analysis']}")

        col1, col2 = st.columns(2)
        with col1:
            st.write("**Matching Skills:**")
            for skill in result['job_match']['matching_skills']:
                st.write(f"✅ {skill}")
        with col2:
            st.write("**Missing Keywords:**")
            for keyword in result['job_match']['missing_keywords']:
                st.write(f"❌ {keyword}")

        st.subheader("Recommendations")
        st.write("**Gaps:**")
        for gap in result['recommendations']['gaps']:
            st.write(f"• {gap}")
        st.write("**Suggestions:**")
        for suggestion in result['recommendations']['suggestions']:
            st.write(f"💡 {suggestion}")