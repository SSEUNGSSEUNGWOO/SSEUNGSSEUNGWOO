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

### 🍎 Diabetes Food Risk Detection

HuggingFace DETR 모델을 활용해 **Object Detection 파이프라인을 end-to-end로 직접 구현**해본 학습용 프로젝트.
모델 로딩부터 bounding box 시각화까지 전체 흐름을 익히는 것을 목표로 했습니다.

**Tech Stack**
Python · PyTorch · HuggingFace Transformers · PIL

🔗 Repository
[https://github.com/SSEUNGSSEUNGWOO/diabetes-food-detection](https://github.com/SSEUNGSSEUNGWOO/diabetes-food-detection)

---

### 🐶 Dog AI Agent — 강아지 탐지 · 견종 분류 서비스 (팀 프로젝트)

이미지에서 강아지를 탐지하고 견종을 분류한 뒤, 견종별 유전병 정보 기반으로 레시피 이미지를 자동 생성하는 AI 서비스.

**담당한 부분**
- 강아지 여부 판별 Object Detection 구현 (MobileNetV2 ImageNet, COCO 클래스 범위로 탐지)
- **MobileNetV2 / MobileNetV3Large / EfficientNetB0 백본 비교 실험 → EfficientNetB0 선정** (val acc 85.52%, 2위 대비 +7.3%p)
- EfficientNetB0 fine-tuning으로 120종 견종 분류 모델 성능 개선
- Grad-CAM으로 모델이 어떤 특징을 보고 판단하는지 시각화 (Top-3 품종 히트맵)

**Tech Stack**
Python · TensorFlow · Keras · EfficientNetB0 · MobileNetV2 · Grad-CAM

🔗 서비스 레포
[https://github.com/Dog-AI-Agent/dog-ai-agent_mvp](https://github.com/Dog-AI-Agent/dog-ai-agent_mvp)

🔗 모델 실험 레포
[https://github.com/Dog-AI-Agent/dog-classifier-models](https://github.com/Dog-AI-Agent/dog-classifier-models)

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
