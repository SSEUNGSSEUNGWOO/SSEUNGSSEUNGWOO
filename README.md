# 👋 Hi, I'm Seungwoo Jang

💡 **AI 에이전트 · NLP · Computer Vision · AI 서비스 개발**

매일 쏟아지는 새로운 AI 기술을 빠르게 파악하고, 직접 구현해서 서비스로 만드는 것에 관심이 많습니다.
멀티 에이전트 오케스트레이션, NLP, Computer Vision까지 — "왜 이 설계인가"를 먼저 생각하는 개발자입니다.

📬 jsw7980@gmail.com

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

### 🏭 Agent Pipeline — 자율 에이전트 빌드 팩토리

태스크를 입력하면 AI 에이전트 팀이 **계획 → 구현 → 검토 → 저장** 파이프라인을 자동으로 실행해 완성된 Python 프로젝트를 만들어낸다. 태스크가 소진되면 Claude가 새 아이디어를 생성해 무한히 계속된다.

**왜 이렇게 설계했나?**

- **역할을 5개로 분리한 이유** — Planner가 코드까지 쓰면 설계 단계에서 구현 디테일에 끌려간다. 계획·구현·검토·수정·저장을 완전히 분리해서 각 에이전트가 자기 역할에만 집중하게 만들었다.

- **Critic 루프를 무한으로 둔 이유** — max_retries를 두면 기준을 낮춰서라도 통과시키는 상황이 생긴다. Critic이 PASS를 줄 때까지 반복하는 구조로, 품질 기준을 타협하지 않는다.

- **`claude -p` subprocess로 호출한 이유** — 에이전트마다 독립된 컨텍스트가 필요하다. 하나의 대화 안에서 역할을 바꾸면 이전 역할의 편향이 남는다. 매 호출마다 새 세션을 띄워서 완전히 분리했다.

- **`run.sh` 래퍼를 별도로 만든 이유** — 맥북 슬립, 네트워크 타임아웃으로 프로세스가 죽어도 `tasks.json` 상태가 남아 있다. 래퍼가 비정상 종료를 감지하고 재시작하면 완료된 태스크는 스킵하고 이어서 진행된다.

- **태스크 소진 후 자동 생성하는 이유** — 정해진 목록이 끝나면 멈추는 시스템은 사람이 계속 개입해야 한다. 기존 태스크 전체를 컨텍스트로 넘겨서 중복 없는 새 아이디어를 생성하고 `tasks.json`에 추가해 루프를 유지한다.

**핵심 구현**
멀티 에이전트 파이프라인 · Critic 품질 루프 · 자율 태스크 생성 · 자동 재시작 복구

**Tech Stack**
Python · Claude Code CLI · subprocess

🔗 Repository
[https://github.com/SSEUNGSSEUNGWOO/agent-pipeline](https://github.com/SSEUNGSSEUNGWOO/agent-pipeline)

---

### 🛠️ OpsAgent — 도메인 적응형 내부 AI 코파일럿 플랫폼

문서·CSV·지식 그래프를 결합해 운영 의사결정을 지원하는 AI 시스템. 어떤 업종이든 파일을 올리면 즉시 작동한다.

**왜 이렇게 설계했나?**

- **단순 RAG 챗봇을 넘어선 이유** — 문서 검색만으로는 "재고 위험 상품이 뭔지, 회의에서 어떤 결정을 했는지, 다음에 뭘 해야 하는지"를 한 번에 답할 수 없다. 문서(RAG) + 정형 데이터(CSV) + 지식 그래프(NetworkX)를 결합해서 실무 의사결정 흐름을 직접 보조하도록 설계했다.

- **도메인을 무관하게 만든 이유** — 업종마다 entity 타입과 용어가 다르다. 7개 업종 프리셋 + Claude 동적 분석으로 도메인 설정을 자동화하고, 모든 프롬프트에 `{domain_context}`를 주입해서 어떤 업종이든 즉시 적응하게 만들었다.

- **지식 그래프 빌드 경로를 4가지로 분리한 이유** — 파일 타입마다 관계 추출 방식이 다르다. 일반 문서는 Claude로 entity/relation을 JSON 추출하고, CSV는 스키마 기반 2-pass, Python은 AST 분석으로 각각 최적 경로를 탄다.

- **RAG 컬렉션을 도메인별로 분리한 이유** — 단일 컬렉션에 쌓으면 제조업 문서가 금융 질의에 검색돼서 노이즈가 생긴다. `collection_name` 프로퍼티로 도메인마다 독립된 ChromaDB 컬렉션을 사용한다.

**핵심 구현**
RAG + Knowledge Graph 결합 · 도메인 적응형 프롬프트 · 4가지 KG 빌드 경로 · 3-Layer 채팅 라우터 (data / doc / combined)

**Tech Stack**
Python · Streamlit · Claude API · ChromaDB · NetworkX · pyvis

🔗 Repository
[https://github.com/SSEUNGSSEUNGWOO/OpsAgent](https://github.com/SSEUNGSSEUNGWOO/OpsAgent)

🌐 Live
[https://sseungsseungwoo-opsagent.streamlit.app](https://sseungsseungwoo-opsagent.streamlit.app)

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

### 📈 Alpha Agents — 암호화폐 자동매매 ML 시스템

5개 코인(BTC·ETH·SOL·BNB·XRP)을 대상으로 XGBoost가 SELL/HOLD/BUY를 분류하고, 단일 포트폴리오 풀에서 동적으로 자금을 배분하는 자동매매 시스템. Railway에 실배포, 15분마다 신호를 생성한다.

**왜 이렇게 설계했나?**

- **XGBoost를 선택한 이유** — 금융 시계열은 비선형 관계가 강하고 피처 수가 많다. 딥러닝보다 과적합에 강하고, 피처 중요도를 직접 확인해서 모델이 어떤 지표를 보고 판단하는지 해석할 수 있다.

- **look-ahead bias를 방지한 이유** — 미래 데이터가 학습에 섞이면 백테스트 성능은 높아 보이지만 실제 배포에서 무너진다. shuffle=False, 시간 순서 기준 70/15/15 split으로 Test 셋을 완전한 unseen 데이터로 유지했다.

- **시간 감쇠 가중치를 쓴 이유** — 3년 전 시장 패턴과 최근 패턴은 다르다. `weight = exp(-ln(2) × days_old / 180)`으로 최근 데이터에 더 높은 가중치를 줘서 현재 시장에 더 잘 맞는 모델을 만들었다.

- **모델을 파일 대신 PostgreSQL에 저장한 이유** — Railway는 재배포 시 파일 시스템이 초기화된다. pickle을 BYTEA로 DB에 저장하고, 주간 재학습 후 F1이 개선됐을 때만 핫스왑하는 방식으로 모델 영속성을 확보했다.

- **단일 포트폴리오 풀로 전환한 이유** — 코인별로 자금을 고정 배분하면 한 코인에 기회가 몰려도 다른 코인의 자금을 활용할 수 없다. 전체 잔액을 하나의 풀로 관리하고 신호 강도에 따라 동적으로 배분한다.

**Tech Stack**
Python · XGBoost · TA-Lib · PostgreSQL · FastAPI · Railway · GitHub Actions

🔗 Repository
[https://github.com/SSEUNGSSEUNGWOO/alpha-agents](https://github.com/SSEUNGSSEUNGWOO/alpha-agents)

🌐 Live
[https://alpha-agents-production.up.railway.app](https://alpha-agents-production.up.railway.app)

---

### 🐶 Dog AI Agent — 강아지 품종 판별 · 맞춤 레시피 추천 서비스 (팀 프로젝트)

강아지 이미지를 업로드하면 품종을 판별하고, 해당 품종의 유전병 정보를 바탕으로 맞춤 식재료와 레시피를 추천해주는 AI 서비스.

**담당한 부분**
- 강아지 여부 판별 Object Detection 구현 (MobileNetV2 ImageNet, COCO 클래스 범위로 탐지)
- **백본 비교 실험 → EfficientNetB0 선정 후 단계적 성능 개선** (120종 견종 분류)
- 레시피 프롬프트 기반 DALL-E 3 음식 이미지 자동 생성 — 조리 단계 키워드를 파싱해 최종 플레이팅 묘사로 변환

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

### 🍎 Diabetes Food Risk Detection

HuggingFace DETR 모델을 활용해 **Object Detection 파이프라인을 end-to-end로 직접 구현**한 프로젝트.
모델 로딩부터 bounding box 시각화까지 전체 흐름을 직접 구현했습니다.

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
XGBoost · 시계열 피처 엔지니어링 · TA-Lib
멀티 에이전트 오케스트레이션 · RAG · ReAct · Knowledge Graph

### Backend / Infra
FastAPI · Flask · SSE · Streamlit · Supabase · ChromaDB · NetworkX · Railway · GitHub Actions

### Frontend
React

### Tools
Git · Jupyter Notebook · Vercel

---

# 📊 GitHub Stats

![GitHub stats](https://github-readme-stats.vercel.app/api?username=SSEUNGSSEUNGWOO\&show_icons=true)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=SSEUNGSSEUNGWOO\&layout=compact)
