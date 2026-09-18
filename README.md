<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner.svg">
  <img src="assets/banner-light.svg" width="100%" alt="Seungwoo Jang — 교육 운영의 요구사항을 분석하고, 업무 시스템을 개발·운영합니다. 공공 AI 교육 기획·운영 · 업무 시스템 4개 개발·운영 · 컴퓨터과학 전공. 2026년 운영 집계: 기수 41, 지원 8,180, 수료 1,449, 동시 응시 108.">
</picture>

<img src="assets/sections/roles.svg" width="100%" alt="기획·운영 × 개발. 선발·교육·인증평가 운영, 현업 요구사항 정리·업무 절차 설계, 운영 담당자 10명 이상이 사용하는 시스템. 업무 시스템 4개 개발·운영, 웹·API·DB 구현 및 배포, 컴퓨터과학 전공(강원대학교).">

<img src="assets/sections/projects-header.svg" width="100%" alt="01 Projects — 사례 문서 3(회사 시스템, 소스 비공개), 소스 공개 3">

<table width="100%">
  <tr>
    <td>
      <a href="https://github.com/SSEUNGSSEUNGWOO/kbrain-ems-casestudy"><img src="assets/cards/kbrain-ems.svg" width="100%" alt="kbrain-ems — 모집부터 수료·결과보고까지 교육 운영 데이터를 한 시스템에서 관리. 운영 중. 발주처 행안부·NIA AI 챔피언 사업, 2026.04 ~ 현재, 요구분석·설계·개발·운영. 기수 41, 지원 8,180, 수료 1,449 (2026년 도입 후 집계, 이관 없음)."></a>
      <b><a href="https://github.com/SSEUNGSSEUNGWOO/kbrain-ems-casestudy">kbrain-ems</a></b> — 엑셀·구글폼으로 운영하던 교육 사업이 기수·운영자 모두 늘면서 한 시스템으로 옮겼다. 소스는 회사 자산이라 비공개이고, 결정 근거는 <a href="https://github.com/SSEUNGSSEUNGWOO/kbrain-ems-casestudy/blob/main/docs/decisions.md">설계 결정 기록</a>.
    </td>
  </tr>
</table>

<table width="100%">
  <tr>
    <td>
      <a href="https://github.com/SSEUNGSSEUNGWOO/kbrain-cert-casestudy"><img src="assets/cards/kbrain-cert.svg" width="100%" alt="kbrain-cert — 문항 관리·시험 진행·실시간 감독·결과 내보내기를 통합한 사내 CBT. 운영 중. AI 챔피언 인증평가, 2026.07 ~ 현재, 요구분석·설계·개발·운영. 최대 동시 응시 108, 누적 응시 1,466 (실시험 운영 집계)."></a>
      <b><a href="https://github.com/SSEUNGSSEUNGWOO/kbrain-cert-casestudy">kbrain-cert</a></b> — 외부 코드로 운영하던 인증평가에서 반복된 문제(감독 오탐, 정답 노출, 점수 표기, 타이머)를 설계 단계에서 다르게 풀었다. 결정 근거는 <a href="https://github.com/SSEUNGSSEUNGWOO/kbrain-cert-casestudy/blob/main/docs/decisions.md">설계 결정 기록</a>.
    </td>
  </tr>
</table>

<table width="100%">
  <tr valign="top">
    <td width="50%">
      <a href="https://jodalfit.co.kr"><img src="assets/cards/jodalfit.svg" width="100%" alt="조달핏 — 수주 영업의 공고 탐색을 대신한다. 매일 나라장터를 뒤지는 일을 회사명 입력 한 번으로. 진행 공고 11,000건 이상을 매일 수집해 자격 필터와 임베딩 매칭으로 회사별 TOP 5. 운영 중."></a>
      <b><a href="https://github.com/SSEUNGSSEUNGWOO/jodalfit">조달핏</a></b> · <a href="https://jodalfit.co.kr">jodalfit.co.kr</a> — 수주 영업 담당자가 매일 나라장터를 뒤져 "우리가 들어갈 수 있는 공고"를 골라내던 일을 대신한다. 키워드 알림(<a href="https://github.com/SSEUNGSSEUNGWOO/g2b-monitor">g2b-monitor</a>)으로 시작해 등록업종·공급물품·수주이력 임베딩 매칭으로 바꿨고, 자격(면허·지역·마감) 필터가 먼저다. 수주이력 중심 설계는 실데이터 매칭 1.1%로 확인 후 업종 중심으로 조정. 근거는 <a href="https://github.com/SSEUNGSSEUNGWOO/jodalfit#2-핵심-알고리즘-2026-05-25-pivot--업종-메인--동적-가중치">README 2장</a>.
    </td>
    <td width="50%">
      <a href="https://daeasy.co.kr"><img src="assets/cards/daeasy.svg" width="100%" alt="DAEASY — 기업·공공기관 교육 문의를 받는 B2B 영업 채널. 과정·사례·인사이트·AI 체험관의 모든 동선이 교육 문의로 모인다. 고객 회원, 역할 기반 어드민, 콘텐츠 자동 발행 2종. 운영 중."></a>
      <b><a href="https://github.com/SSEUNGSSEUNGWOO/daeasy-casestudy">DAEASY</a></b> · <a href="https://daeasy.co.kr">daeasy.co.kr</a> — 커리큘럼·일정·견적 문의가 목적인 사이트. 과정 소개·교육 사례·인사이트·AI 체험관(체험 뒤 과정 추천 → 문의)이 전부 문의로 이어지고, 캡차·이메일 인증 고객 회원, admin/editor 어드민, 인사이트·홍보자료 자동 발행까지 한 저장소. 자동 발행은 작성(claude)과 평가(codex)를 다른 모델에 맡기고 합격 판정은 코드가 한다. 결정 근거는 <a href="https://github.com/SSEUNGSSEUNGWOO/daeasy-casestudy/blob/main/docs/decisions.md">설계 결정 기록</a>.
    </td>
  </tr>
</table>

<table width="100%">
  <tr valign="top">
    <td width="50%">
      <a href="https://github.com/SSEUNGSSEUNGWOO/agent-pipeline"><img src="assets/cards/agent-pipeline.svg" width="100%" alt="Agent Pipeline — 검토자가 통과시킬 때까지 작업 → 검토 → 수정을 반복하는 오케스트레이터. 개인 프로젝트, 2026.03 ~."></a>
      <b><a href="https://github.com/SSEUNGSSEUNGWOO/agent-pipeline">Agent Pipeline</a></b> — 단계를 선언하면 Critic이 PASS를 낼 때까지 루프를 돌린다. 도메인은 프롬프트 md에만, 매 호출 새 세션. <a href="https://github.com/SSEUNGSSEUNGWOO/AX-team">AX Team</a>의 한계 분석에서 출발.
    </td>
    <td width="50%">
      <a href="https://nolai.vercel.app"><img src="assets/cards/nolai.svg" width="100%" alt="AI쏙 — 초등학생이 임베딩·벡터검색·토큰을 손으로 익히는 웹 놀이터. nolai.vercel.app, 개인 프로젝트, 2026.08 ~."></a>
      <b><a href="https://github.com/SSEUNGSSEUNGWOO/nolai">AI쏙</a></b> · <a href="https://nolai.vercel.app">nolai.vercel.app</a> — 10~13세 대상, 무료·회원가입 없음. 첫 레슨은 단어를 지도에 놓아 보는 임베딩 체험.
    </td>
  </tr>
</table>

<img src="assets/sections/think.svg" width="100%" alt="How I work. 01 현업 요구사항을 정리하고, 구현 후 운영 담당자와 업무 흐름을 검증한다. 02 주요 설계 결정과 운영 절차를 문서화하고 변경 시 갱신한다. 03 실데이터로 가설을 검증하고 결과에 따라 기능 범위와 설계를 조정한다. 04 운영 중 확인된 오류를 회귀 테스트에 반영한다. 테스트 자동화·RLS 정책은 2026 하반기 보강 중.">

<img src="assets/sections/stack.svg" width="100%" alt="Stack. 업무 서비스에서 사용: TypeScript, Next.js, React, Python, FastAPI, PostgreSQL·Supabase, pgvector, Vercel, Agora. 개인 프로젝트·실험: Claude API, Claude Code CLI, RAG, Multi-agent.">

<a href="mailto:jansseung@gmail.com"><img src="assets/sections/where.svg" width="100%" alt="Where. 케이브레인컴퍼니 공공AI센터 HRD사업실 주임. 강원대학교 컴퓨터과학전공. jansseung@gmail.com"></a>
