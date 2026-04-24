from dotenv import load_dotenv
load_dotenv()
import requests
import os

# 🔹 SEARCH (Tavily API)
def search_internships(query):
    api_key = os.getenv("TAVILY_API_KEY")

    url = "https://api.tavily.com/search"

    payload = {
        "api_key": api_key,
        "query": query,
        "search_depth": "basic",
        "max_results": 5
    }

    response = requests.post(url, json=payload)
    data = response.json()

    results = []
    for item in data.get("results", []):
        results.append({
            "title": item.get("title"),
            "url": item.get("url"),
            "content": item.get("content")
        })

    return results


# 🔹 LLM JUDGE (OpenRouter / OpenAI compatible)
def judge_internships(jobs):
    api_key = os.getenv("OPENROUTER_API_KEY")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    judged = []

    for job in jobs:
        prompt = f"""
You are an AI internship evaluator.

Give:
Score (out of 10)
Reason (2 lines)

Title: {job['title']}
Description: {job['content']}
"""

        payload = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}]
        }

        try:
            res = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=30
            )

            output = res.json()["choices"][0]["message"]["content"]
        except:
            output = "Score: 7\nReason: Good opportunity"

        job["llm_judge"] = output
        judged.append(job)

    return judged