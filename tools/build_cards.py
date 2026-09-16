"""프로필 프로젝트 카드 SVG 생성. 실행: uv run --no-project tools/build_cards.py (tools/src/*.png를 base64로 내장)
- hero: EMS·CBT 전폭 카드 (1200×540)
- card: 2단 카드 (1200×750) — 스크린샷 또는 도식
카드마다 accent 색이 다르고, 상태 칩 색은 공통(운영 중=초록, 사용 중=연두, 개발 중=파랑).
"""
import base64, io, pathlib, random

SRC = pathlib.Path(__file__).parent / "src"
OUT = pathlib.Path(__file__).parent.parent / "assets" / "cards"
OUT.mkdir(parents=True, exist_ok=True)

FONT = "Pretendard, 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', system-ui, sans-serif"
MONO = "'JetBrains Mono', Consolas, monospace"
STATUS = {"운영 중": "#34d399", "사용 중": "#a3e635", "개발 중": "#38bdf8"}
MUTED, TEXT, INK = "#94a3b8", "#e2e8f0", "#0b1220"


def b64(name: str) -> str:
    return base64.b64encode((SRC / f"{name}.png").read_bytes()).decode()


def defs() -> str:
    return '''
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1220"/><stop offset="1" stop-color="#111c33"/></linearGradient>
  </defs>'''


def window(x, y, w, h, accent, img_name=None, zoom=1.0, inner="", cid="win"):
    """브라우저 창 프레임. img_name이 있으면 스크린샷(상단 기준, zoom배), 없으면 inner 도식."""
    if img_name:
        iw = w * zoom
        ih = iw * 675 / 1080
        content = (f'<image clip-path="url(#{cid})" x="{x}" y="{y+34}" width="{iw:.0f}" height="{ih:.0f}" '
                   f'preserveAspectRatio="xMinYMin meet" href="data:image/png;base64,{b64(img_name)}"/>')
    else:
        content = f'<g clip-path="url(#{cid})">{inner}</g>'
    return f'''
  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#0f172a" stroke="#ffffff" stroke-opacity="0.14"/>
  <rect x="{x}" y="{y}" width="{w}" height="34" rx="14" fill="#1e293b"/>
  <rect x="{x}" y="{y+20}" width="{w}" height="14" fill="#1e293b"/>
  <circle cx="{x+22}" cy="{y+17}" r="5" fill="#f87171"/><circle cx="{x+40}" cy="{y+17}" r="5" fill="#fbbf24"/><circle cx="{x+58}" cy="{y+17}" r="5" fill="#34d399"/>
  <clipPath id="{cid}"><rect x="{x}" y="{y+34}" width="{w}" height="{h-34}"/></clipPath>
  {content}
  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="none" stroke="{accent}" stroke-opacity="0.4"/>'''


def tw(s, size):
    return sum(size * (1.0 if ord(ch) > 0x2E7F else 0.62) for ch in s)


def status_chip(x, y, label):
    c = STATUS[label]
    w = 34 + tw(label, 19) + 16          # 점(34) + 글자 + 오른쪽 여백
    return f'''
  <rect x="{x-w}" y="{y-30}" width="{w}" height="40" rx="20" fill="{c}" fill-opacity="0.15" stroke="{c}" stroke-opacity="0.6"/>
  <circle cx="{x-w+20}" cy="{y-10}" r="5" fill="{c}"/>
  <text x="{x-w+34}" y="{y-3}" font-size="19" fill="#f8fafc">{label}</text>'''


# ── 전폭 히어로 카드 (EMS · CBT) ─────────────────────────────
def hero(name, accent, title, subtitle, status, client, period, role, stats, note):
    W, H = 1200, 540
    TX = 620
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{title} — {' '.join(subtitle)}">{defs()}
  <rect width="{W}" height="{H}" rx="24" fill="url(#bg)"/>
  <rect x="0" y="0" width="{W}" height="6" fill="{accent}"/>
  {window(48, 48, 532, 444, accent, img_name=name, zoom=1.35, cid="w_"+name)}
  <g font-family="{FONT}">
    <text x="{TX}" y="98" font-size="44" font-weight="700" fill="#f8fafc">{title}</text>
    {status_chip(W-48, 98, status)}
    <text x="{TX}" y="138" font-size="21" fill="{TEXT}">{subtitle[0]}</text>
    <text x="{TX}" y="166" font-size="21" fill="{TEXT}">{subtitle[1] if len(subtitle) > 1 else ''}</text>
    <line x1="{TX}" y1="190" x2="{W-48}" y2="190" stroke="#ffffff" stroke-opacity="0.12"/>
    <text x="{TX}" y="226" font-size="18"><tspan fill="{accent}" font-family="{MONO}" font-size="13" letter-spacing="2">발주처</tspan><tspan dx="14" fill="{TEXT}">{client}</tspan></text>
    <text x="{TX}" y="260" font-size="18"><tspan fill="{accent}" font-family="{MONO}" font-size="13" letter-spacing="2">기간  </tspan><tspan dx="14" fill="{TEXT}">{period}</tspan></text>
    <text x="{TX}" y="294" font-size="18"><tspan fill="{accent}" font-family="{MONO}" font-size="13" letter-spacing="2">역할  </tspan><tspan dx="14" fill="{TEXT}">{role}</tspan></text>
'''
    x = TX
    for num, label in stats:
        s += f'''
    <text x="{x}" y="384" font-size="46" font-weight="700" fill="{accent}" font-family="{MONO}">{num}</text>
    <text x="{x}" y="414" font-size="17" fill="{MUTED}">{label}</text>'''
        x += 178
    for i, line in enumerate(note):
        s += f'''
    <text x="{TX}" y="{458 + i*24}" font-size="15" fill="{MUTED}">{line}</text>'''
    return s + '''
  </g>
</svg>
'''


# ── 2단 카드 ─────────────────────────────────────────────────
def card(name, accent, title, subtitle, status, tag, stat, stat_label, note, inner=None):
    W, H = 1200, 750
    win = window(60, 150, 1080, 470, accent, img_name=None if inner else name, inner=inner or "", cid="w_"+name)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{title} — {subtitle}">{defs()}
  <rect width="{W}" height="{H}" rx="24" fill="url(#bg)"/>
  <rect x="0" y="0" width="{W}" height="6" fill="{accent}"/>
  <g font-family="{FONT}">
    <text x="60" y="84" font-size="46" font-weight="700" fill="#f8fafc">{title}</text>
    {status_chip(W-60, 84, status)}
    <text x="60" y="124" font-size="24" fill="{TEXT}">{subtitle}</text>
  </g>
  {win}
  <g font-family="{FONT}">
    <text x="60" y="690"><tspan font-size="50" font-weight="700" fill="{accent}" font-family="{MONO}">{stat}</tspan><tspan dx="18" font-size="24" fill="{MUTED}">{stat_label}</tspan></text>
    <text x="{W-60}" y="688" font-size="20" fill="{MUTED}" text-anchor="end" font-family="{MONO}">{tag}</text>
    <text x="60" y="724" font-size="17" fill="{MUTED}">{note}</text>
  </g>
</svg>
'''


# ── 도식: Agent Pipeline 루프 ───────────────────────────────
def pipeline_inner(accent):
    x0, y0 = 60, 184                      # 창 내부 원점 (창 x=60, y=150+34)
    def box(x, y, w, h, fill, stroke, t1, t2):
        return f'''
      <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}" fill-opacity="0.2" stroke="{stroke}" stroke-width="2"/>
      <text x="{x+w/2}" y="{y+h/2-6}" font-size="27" font-weight="700" fill="#f8fafc" text-anchor="middle">{t1}</text>
      <text x="{x+w/2}" y="{y+h/2+27}" font-size="18" fill="#cbd5e1" text-anchor="middle">{t2}</text>'''
    return f'''
    <defs>
      <marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#94a3b8"/></marker>
      <marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#f87171"/></marker>
      <marker id="ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#34d399"/></marker>
    </defs>
    <rect x="{x0}" y="{y0}" width="1080" height="436" fill="#0b1220"/>
    <g font-family="{FONT}">
      {box(x0+60, y0+70, 170, 96, "#64748b", "#94a3b8", "tasks.json", "태스크 큐")}
      <line x1="{x0+230}" y1="{y0+118}" x2="{x0+300}" y2="{y0+118}" stroke="#94a3b8" stroke-width="3" marker-end="url(#a)"/>
      <rect x="{x0+310}" y="{y0+30}" width="560" height="380" rx="18" fill="none" stroke="#334155" stroke-width="2" stroke-dasharray="8 8"/>
      <text x="{x0+334}" y="{y0+60}" font-size="15" fill="#64748b" letter-spacing="2">STAGE 1 … N</text>
      {box(x0+340, y0+70, 170, 96, "#0ea5e9", "#38bdf8", "work", "초안")}
      <line x1="{x0+510}" y1="{y0+118}" x2="{x0+580}" y2="{y0+118}" stroke="#94a3b8" stroke-width="3" marker-end="url(#a)"/>
      {box(x0+590, y0+70, 170, 96, accent, accent, "critic", "PASS / FAIL")}
      {box(x0+465, y0+270, 170, 96, "#ef4444", "#f87171", "fix", "피드백 반영")}
      <path d="M{x0+675} {y0+166} L{x0+675} {y0+318} L{x0+645} {y0+318}" fill="none" stroke="#f87171" stroke-width="3" marker-end="url(#ar)"/>
      <text x="{x0+690}" y="{y0+250}" font-size="16" fill="#f87171">FAIL</text>
      <path d="M{x0+465} {y0+318} L{x0+425} {y0+318} L{x0+425} {y0+176}" fill="none" stroke="#f87171" stroke-width="3" marker-end="url(#ar)"/>
      <line x1="{x0+760}" y1="{y0+118}" x2="{x0+900}" y2="{y0+118}" stroke="#34d399" stroke-width="3" marker-end="url(#ag)"/>
      <text x="{x0+830}" y="{y0+104}" font-size="16" fill="#34d399" text-anchor="middle">PASS</text>
      {box(x0+905, y0+70, 150, 96, "#10b981", "#34d399", "다음 단계", "$prev")}
      <text x="{x0+540}" y="{y0+410}" font-size="17" fill="#94a3b8" text-anchor="middle" font-family="{MONO}">매 호출 = 새 claude -p 세션 · 단계 output 캐시 · 도메인은 프롬프트 md에만</text>
    </g>'''


# ── 도식: AI쏙 픽셀·토큰 모티프 ─────────────────────────────
def nolai_inner(accent):
    x0, y0 = 60, 184
    random.seed(7)
    palette = ["#f472b6", "#a78bfa", "#38bdf8", "#34d399", "#fbbf24", "#f8fafc"]
    cells = "".join(
        f'<rect x="{x0+70+c*52}" y="{y0+50+r*52}" width="44" height="44" rx="8" fill="{random.choice(palette)}" fill-opacity="{random.choice([0.9,0.6,0.35])}"/>'
        for r in range(6) for c in range(9) if random.random() < 0.55)
    tokens = ["임베딩", "토큰", "픽셀", "벡터", "비트", "학습 데이터"]
    chips = "".join(
        f'<rect x="{x0+600}" y="{y0+48+i*60}" width="{80+len(t)*22}" height="44" rx="22" fill="{accent}" fill-opacity="{0.9-i*0.12}"/>'
        f'<text x="{x0+600+(80+len(t)*22)/2}" y="{y0+48+i*60+29}" font-size="20" font-weight="700" fill="#0b1220" text-anchor="middle">{t}</text>'
        for i, t in enumerate(tokens))
    return f'''
    <rect x="{x0}" y="{y0}" width="1080" height="436" fill="#0b1220"/>
    {cells}
    <g font-family="{FONT}">{chips}
      <text x="{x0+540}" y="{y0+410}" font-size="18" fill="#94a3b8" text-anchor="middle">10~13세가 AI 작동 원리를 손으로 만지며 배우는 웹 놀이터 · 배포 전</text>
    </g>'''


OUTS = {
    "kbrain-ems": hero(
        "kbrain-ems", "#34d399", "kbrain-ems", ["모집부터 수료·결과보고까지", "교육 운영 데이터를 한 시스템에서 관리"],
        "운영 중", "행안부 · NIA AI 챔피언 사업", "2026.04 ~ 현재 · 개발 후 운영 병행", "요구분석 · 설계 · 개발 · 운영",
        [("41", "기수"), ("8,180", "지원 건수"), ("1,449", "수료 인원")],
        ["2026년 시스템 도입 후 집계 · 이전 엑셀·구글폼 데이터 이관 없음", "운영 담당자 10명 이상 사용"]),
    "kbrain-cert": hero(
        "kbrain-cert", "#38bdf8", "kbrain-cert", ["문항 관리 · 시험 진행 · 실시간 감독 · 결과 내보내기를", "통합한 사내 CBT"],
        "운영 중", "AI 챔피언 인증평가 (행안부 · NIA)", "2026.07 ~ 현재 · 개발 후 운영 병행", "요구분석 · 설계 · 개발 · 운영",
        [("108", "최대 동시 응시"), ("1,466", "누적 응시"), ("1,376", "고유 응시자")],
        ["실시험 운영 집계 (부하테스트 아님)", "동시 응시 설계 기준은 100명"]),
    "jodalfit": card(
        "jodalfit", "#2dd4bf", "조달핏", "회사명 하나로 검토할 만한 나라장터 공고 TOP 5를 추천하는 공개 서비스",
        "운영 중", "jodalfit.co.kr", "11,000+", "공고 수집 · 색인 (매일 갱신)",
        "사내 수주 영업 지원 · 2026.05 ~ · 설계 · 개발 · 데이터 파이프라인"),
    "daeasy": card(
        "daeasy", "#60a5fa", "DAEASY", "기업·공공기관 교육 문의를 받는 B2B 영업 채널 — 과정 · 사례 · 인사이트 · AI 체험관",
        "운영 중", "daeasy.co.kr", "1", "출구 · 모든 동선이 교육 문의로 모인다 · 고객 회원 · 어드민 · 자동 발행 2종",
        "케이브레인컴퍼니 · 2026.05 ~ 운영 중 · 요구분석 · 설계 · 개발 · 운영 · 캡차 · rate limit · RLS"),
    "agent-pipeline": card(
        "agent-pipeline", "#fbbf24", "Agent Pipeline", "검토자가 통과시킬 때까지 작업 → 검토 → 수정을 반복하는 오케스트레이터",
        "사용 중", "python", "PASS", "까지 다음 단계로 못 간다 · 자동 검토·수정 루프 구현",
        "개인 프로젝트 · 2026.03 ~ · AX Team(에이전트 6명 토론 시뮬레이터)의 한계 분석에서 출발", inner=pipeline_inner("#fbbf24")),
    "nolai": card(
        "nolai", "#f472b6", "AI쏙", "초등학생이 임베딩 · 벡터검색 · 토큰을 글이 아니라 손으로 익히는 웹 놀이터",
        "운영 중", "nolai.vercel.app", "10~13", "세 대상 · 무료 · 회원가입 없음",
        "개인 프로젝트 · 2026.08 ~ · 설계 · 개발 · 배포"),
}

for name, svg in OUTS.items():
    p = OUT / f"{name}.svg"
    io.open(p, "w", encoding="utf-8", newline="\n").write(svg)
    print(f"{p.name}: {p.stat().st_size // 1024} KB")
