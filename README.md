# 👋 Hi, I'm Seungwoo Jang

💡 **AI 에이전트 · NLP · Computer Vision · AI 서비스 개발**

AI 분야는 매일 새로운 모델과 기법이 나옵니다. 새로 나온 것들을 빠르게 파악하고 직접 써보는 것에 관심이 많습니다.
멀티 에이전트 오케스트레이션부터 NLP, Computer Vision까지, 새로운 기술을 실제 서비스에 적용하며 end-to-end로 구현하는 것을 목표로 합니다.

모델 선택부터 설계 결정까지, 단순히 작동하는 것에 그치지 않고 "왜 이 선택인가"에 대한 근거를 먼저 생각하는 개발자입니다.

---

# 🎓 Education

**강원대학교 (Kangwon National University)**
컴퓨터공학과 학사

---

# 🏆 Activities

* 한국장학재단 홍보대사 강원지역 권역리더
* 강원대학교 총학생회 정책차장
* 강연자 — 강원대학교 교수학습개발원 주관 신입생 워크숍 (400명 대상, 2018)

---

# 🚀 Featured Projects

### 🤖 AX Team Office — AI 에이전트 6명이 자율 협업하는 프로젝트 시뮬레이터

태스크를 입력하면 성향이 다른 AI 에이전트 6명(속도파·품질파·혁신파·실용파·아키텍처파·사용자파)이
토론·합의·투표·생성 과정을 거쳐 문서와 코드를 실시간으로 만들어낸다.

**왜 이렇게 설계했나?**

- **역할 대신 성향으로 구분한 이유** — 마케팅담당·기획담당처럼 역할을 나누면 각자 담당 영역만 얘기하고 실제 충돌이 없다. 전원 개발자로 통일하고 성향만 다르게 해서 같은 주제에 진짜로 부딪히게 만들었다.

- **team_gate를 6명 전원 투표로 만든 이유** — 팀장 혼자 PASS/REVISE를 판단하면 한 관점만 반영된다. 6명이 각자 자기 요구사항이 결과물에 반영됐는지 직접 검증하고, 1명이라도 BLOCK이면 재작성한다.

- **classify_task()로 워크플로우를 분기한 이유** — 고정 파이프라인으로 모든 태스크를 처리하면 "피드백해줘"를 넣어도 코드를 만들어버린다. 태스크를 먼저 build/feedback/review/discuss/plan으로 분류해서 각각에 맞는 흐름을 탄다.

- **generator 패턴을 쓴 이유** — SSE로 에이전트 발언을 실시간 스트리밍하려면 결과를 모아서 한번에 반환하면 안 된다. 각 단계를 yield로 흘려보내고 백그라운드 스레드에서 큐로 받아 keepalive와 함께 전송한다.

실제로 돌려보면서 발견한 버그들(코드 잘림, import 불일치, rate limit, 설명 텍스트 혼입)을 분석해 시스템을 반복 개선했다.

**핵심 구현**
멀티 에이전트 오케스트레이션 · 에이전트 RAG (과거 유사 태스크 검색 → 프롬프트 주입) · ReAct 루프

**Tech Stack**
Python · Flask · SSE · Claude API (Haiku / Sonnet) · Supabase

🔗 Repository
[https://github.com/SSEUNGSSEUNGWOO/AX-team](https://github.com/SSEUNGSSEUNGWOO/AX-team)

---

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

→ 베이스라인 대비 최종 **+9%p 이상 성능 향상** (77.90% → 86.99%)

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
Python · SQL · TypeScript

### Machine Learning / AI
TensorFlow · Keras · PyTorch · HuggingFace Transformers
BERT fine-tuning · EfficientNetB0 · TF-IDF · Grad-CAM · t-SNE
멀티 에이전트 오케스트레이션 · RAG · ReAct

### Backend / Infra
FastAPI · Flask · SSE · Supabase · Railway · GitHub Actions

### Frontend
React

### Tools
Git · Jupyter Notebook · Vercel

---

# 📊 GitHub Stats

![GitHub stats](https://github-readme-stats.vercel.app/api?username=SSEUNGSSEUNGWOO\&show_icons=true)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=SSEUNGSSEUNGWOO\&layout=compact)
