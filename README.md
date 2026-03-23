# 👋 Hi, I'm Seungwoo Jang

💡 **NLP / Computer Vision / AI 서비스 개발**

NLP와 Computer Vision 모델을 직접 학습시키고 서비스로 배포하는 것에 관심이 많습니다.
모델 성능 개선부터 실제 운영까지 end-to-end로 구현하는 것을 목표로 합니다.

모델 선택부터 설계 결정까지, 단순히 작동하는 것에 그치지 않고 "왜 이 선택인가"에 대한 근거를 먼저 생각하는 개발자입니다.

---

# 🎓 Education

**강원대학교 (Kangwon National University)**
컴퓨터공학과 학사

---

# 🏆 Activities

* 한국장학재단 홍보대사 강원권역리더
* 강원대학교 총학생회 정책차장
* 강연자 — 강원대학교 교수학습개발원 주관 신입생 워크숍 (400명 대상, 2018)

---

# 🚀 Featured Projects

### 🐶 Dog AI Agent — 강아지 품종 판별 · 맞춤 레시피 추천 서비스 (팀 프로젝트)

강아지 이미지를 업로드하면 품종을 판별하고, 해당 품종의 유전병 정보를 바탕으로 맞춤 식재료와 레시피를 추천해주는 AI 서비스.

**담당한 부분**
- 강아지 여부 판별 Object Detection 구현 (MobileNetV2 ImageNet, COCO 클래스 범위로 탐지)
- **백본 비교 실험 → EfficientNetB0 선정 후 단계적 성능 개선** (120종 견종 분류)

| Phase | 내용 | Top-1 Acc | Top-5 Acc |
|-------|------|-----------|-----------|
| Phase 1 | 백본 비교 — MobileNetV2 베이스라인 | 77.90% | 96.72% |
| Phase 1 | 백본 비교 — MobileNetV3Large | 78.18% | 96.78% |
| Phase 1 | 백본 비교 — EfficientNetB0 선정 | 85.52% | 98.67% |
| Phase 2 | **Validation set 구축** + epoch 30으로 확장 | 86.99% | 98.96% |
| Phase 3 | EarlyStopping 적용 (17 epoch 자동 종료) | 86.96% | 98.92% |
- Grad-CAM으로 모델이 어떤 특징을 보고 판단하는지 시각화 (Top-3 품종 히트맵)

> 베이스라인 모델 구조 참고: [aribiswas/stanford-dogs-classifier](https://github.com/aribiswas/stanford-dogs-classifier)

**Tech Stack**
Python · TensorFlow · Keras · EfficientNetB0 · MobileNetV2 · Grad-CAM

🔗 Service Repository
[https://github.com/Dog-AI-Agent/dog-ai-agent_mvp](https://github.com/Dog-AI-Agent/dog-ai-agent_mvp)

🔗 Model Experiments
[https://github.com/Dog-AI-Agent/dog-classifier-models](https://github.com/Dog-AI-Agent/dog-classifier-models)

---

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
