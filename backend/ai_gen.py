from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def ask(prompt):
    res = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message["content"]

def generate_study_materials(text):

    summary_prompt = f"""
    Summarize the following lecture concisely with bullet points:
    {text}
    """

    guide_prompt = f"""
    Create a detailed study guide from the lecture. Use:
    - Headers
    - Bullet points
    - Definitions
    - Key concepts
    {text}
    """

    quiz_prompt = f"""
    Generate 10 multiple choice quiz questions with answer key at the end:
    {text}
    """

    summary = ask(summary_prompt)
    guide = ask(guide_prompt)
    quiz = ask(quiz_prompt)

    return guide, summary, quiz