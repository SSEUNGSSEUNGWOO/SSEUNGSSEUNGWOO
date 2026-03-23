# 👋 Hi, I'm Seungwoo Jang

💡 **Data Analysis / AI / Machine Learning**

Python 기반 데이터 분석과 AI 프로젝트를 공부하고 구현하고 있습니다.
데이터 분석, 머신러닝, NLP 프로젝트를 중심으로 다양한 문제를 해결하는 것을 목표로 합니다.

---

# 🎓 Education

**Kangwon National University**
B.S. in Computer Science

---

# 🏆 Activities

* Ambassador – Korea Student Aid Foundation
* Student Council – Kangwon National University

---

# 🚀 Featured Projects

### 📰 Newszips — 뉴스 자동 분류 · 요약 서비스

유튜브 뉴스 영상을 크롤링해서 **카테고리 분류 → 핵심어 추출 → AI 요약**까지 자동화하고, React 앱으로 서비스하는 풀스택 프로젝트.

**왜 이렇게 설계했나?**

- **BERT로 분류한 이유** — 키워드 매칭 방식은 "삼성 화재"를 사회 뉴스로 분류하는 등 문맥을 못 읽는 문제가 있었음. klue/bert-base를 fine-tuning해서 문맥 기반 분류로 해결 (6개 카테고리, 정확도 96%)

- **TF-IDF를 카테고리별로 따로 학습한 이유** — 전체 corpus 기준 IDF를 쓰면 "대통령"이 정치 기사와 스포츠 기사에서 같은 가중치를 가짐. 카테고리 내부 IDF로 계산해야 그 기사에서 실제로 특이한 단어가 핵심어로 올라옴

- **LLM에 본문을 그대로 안 넘긴 이유** — 본문을 직접 요약시키면 모델이 문체나 도입부에 끌려가서 같은 사건도 요약이 매번 달라짐. TF-IDF로 핵심어를 먼저 추출하고 프롬프트에 명시해서 LLM이 집중할 포인트를 유도함

- **t-SNE를 쓴 이유** — BERT 임베딩을 2D로 시각화해서 분류 결과가 실제로 의미적으로 클러스터링되는지 검증. 유사 기사 추천에도 유클리드 거리를 활용

**Tech Stack**
Python · BERT (klue/bert-base) · TF-IDF · OpenAI gpt-4o-mini · FastAPI · React · Supabase · t-SNE · GitHub Actions

🔗 Repository
[https://github.com/SSEUNGSSEUNGWOO/newszips](https://github.com/SSEUNGSSEUNGWOO/newszips)

🌐 Live
[https://newszips.vercel.app](https://newszips.vercel.app)

---

### 🍎 Diabetes Food Risk Analysis

Object Detection 기반 **음식 인식 및 당뇨 위험도 분석 AI 프로젝트**

**Tech Stack**
Python · PyTorch · Transformers · Computer Vision

🔗 Repository
[https://github.com/SSEUNGSSSEUNGWOO/diabetes-food-detection](https://github.com/SSEUNGSSEUNGWOO/diabetes-food-detection.git)

---

# 🧠 Skills

### Programming

Python · SQL

### Data Analysis

Pandas · NumPy · Data Visualization

### Machine Learning / AI

Machine Learning · NLP

### Tools

GitHub · Jupyter Notebook · FastAPI

---

# 📊 GitHub Stats

![GitHub stats](https://github-readme-stats.vercel.app/api?username=SSEUNGSSSEUNGWOO\&show_icons=true)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=SSEUNGSSSEUNGWOO\&layout=compact)
