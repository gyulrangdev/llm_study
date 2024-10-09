import openai
import os

# OpenAI API 키 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_seo_blog_post(topic, keywords):
    prompt = f"다음 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요: {topic}\n\n키워드: {', '.join(keywords)}\n\n글:"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "당신은 SEO에 최적화된 블로그 글을 작성하는 전문 작가입니다."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].message['content'].strip()

# 사용 예시
topic = "인공지능의 미래"
keywords = ["머신러닝", "딥러닝", "자연어 처리", "컴퓨터 비전"]

blog_post = generate_seo_blog_post(topic, keywords)
print(blog_post)
