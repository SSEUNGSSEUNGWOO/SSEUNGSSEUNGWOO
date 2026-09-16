"""프로필 프로젝트 카드 SVG 6장 생성. 실행: uv run --no-project tools/build_cards.py (tools/src/*.png를 base64로 내장)"""
import base64, io, pathlib

SRC = pathlib.Path(__file__).parent / "src"
OUT = pathlib.Path(__file__).parent.parent / "assets" / "cards"
OUT.mkdir(parents=True, exist_ok=True)

FONT = "Pretendard, 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', system-ui, sans-serif"
MONO = "'JetBrains Mono', Consolas, monospace"

W, H = 1200, 750
FX, FY, FW, FH = 60, 120, 1080, 500   # 프레임(브라우저 창) 영역


def frame(inner: str, accent: str) -> str:
    """브라우저 창 프레임. inner는 창 내용(이미지 또는 도식)."""
    return f'''
  <g>
    <rect x="{FX}" y="{FY}" width="{FW}" height="{FH}" rx="14" fill="#0f172a" stroke="#ffffff" stroke-opacity="0.14"/>
    <rect x="{FX}" y="{FY}" width="{FW}" height="34" rx="14" fill="#1e293b"/>
    <rect x="{FX}" y="{FY+20}" width="{FW}" height="14" fill="#1e293b"/>
    <circle cx="{FX+22}" cy="{FY+17}" r="5" fill="#f87171"/>
    <circle cx="{FX+40}" cy="{FY+17}" r="5" fill="#fbbf24"/>
    <circle cx="{FX+58}" cy="{FY+17}" r="5" fill="#34d399"/>
    <clipPath id="win"><rect x="{FX}" y="{FY+34}" width="{FW}" height="{FH-34}" rx="0"/></clipPath>
    <g clip-path="url(#win)">{inner}</g>
    <rect x="{FX}" y="{FY}" width="{FW}" height="{FH}" rx="14" fill="none" stroke="{accent}" stroke-opacity="0.35"/>
  </g>'''


def shell(title: str, sub: str, accent: str, inner: str, stat: str, stat_label: str, tag: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{title}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0b1220"/><stop offset="1" stop-color="#111c33"/>
    </linearGradient>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="#ffffff" stroke-opacity="0.045"/>
    </pattern>
  </defs>
  <rect width="{W}" height="{H}" rx="24" fill="url(#bg)"/>
  <rect width="{W}" height="{H}" rx="24" fill="url(#grid)"/>
  <rect x="0" y="0" width="{W}" height="6" fill="{accent}"/>
  <g font-family="{FONT}">
    <text x="60" y="78" font-size="38" font-weight="700" fill="#f8fafc">{title}</text>
    <text x="{W-60}" y="76" font-size="20" fill="{accent}" text-anchor="end" font-family="{MONO}">{tag}</text>
  </g>
  {frame(inner, accent)}
  <g font-family="{FONT}">
    <text x="60" y="702"><tspan font-size="40" font-weight="700" fill="{accent}" font-family="{MONO}">{stat}</tspan><tspan dx="18" font-size="20" fill="#94a3b8">{stat_label}</tspan></text>
    <text x="{W-60}" y="702" font-size="20" fill="#cbd5e1" text-anchor="end">{sub}</text>
  </g>
</svg>
'''


def img_inner(name: str) -> str:
    data = base64.b64encode((SRC / f"{name}.png").read_bytes()).decode()
    return (f'<image x="{FX}" y="{FY+34}" width="{FW}" height="{FH-34}" '
            f'preserveAspectRatio="xMidYMin slice" href="data:image/png;base64,{data}"/>')


def pipeline_inner(accent: str) -> str:
    """work → critic → fix 루프 도식 (프레임 안)."""
    x0, y0 = FX, FY + 34
    box = lambda x, y, w, h, fill, stroke, t1, t2: f'''
      <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}" fill-opacity="0.2" stroke="{stroke}" stroke-width="2"/>
      <text x="{x+w/2}" y="{y+h/2-6}" font-size="26" font-weight="700" fill="#f8fafc" text-anchor="middle">{t1}</text>
      <text x="{x+w/2}" y="{y+h/2+26}" font-size="17" fill="#cbd5e1" text-anchor="middle">{t2}</text>'''
    return f'''
    <defs>
      <marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#94a3b8"/></marker>
      <marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#f87171"/></marker>
      <marker id="ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#34d399"/></marker>
    </defs>
    <rect x="{x0}" y="{y0}" width="{FW}" height="{FH-34}" fill="#0b1220"/>
    <g font-family="{FONT}">
      {box(x0+60, y0+70, 170, 96, "#64748b", "#94a3b8", "tasks.json", "태스크 큐")}
      <line x1="{x0+230}" y1="{y0+118}" x2="{x0+300}" y2="{y0+118}" stroke="#94a3b8" stroke-width="3" marker-end="url(#a)"/>
      <rect x="{x0+310}" y="{y0+30}" width="560" height="380" rx="18" fill="none" stroke="#334155" stroke-width="2" stroke-dasharray="8 8"/>
      <text x="{x0+334}" y="{y0+60}" font-size="15" fill="#64748b" letter-spacing="2">STAGE 1 … N</text>
      {box(x0+340, y0+70, 170, 96, "#0ea5e9", "#38bdf8", "work", "초안")}
      <line x1="{x0+510}" y1="{y0+118}" x2="{x0+580}" y2="{y0+118}" stroke="#94a3b8" stroke-width="3" marker-end="url(#a)"/>
      {box(x0+590, y0+70, 170, 96, "#f59e0b", "#fbbf24", "critic", "PASS / FAIL")}
      {box(x0+465, y0+270, 170, 96, "#ef4444", "#f87171", "fix", "피드백 반영")}
      <path d="M{x0+675} {y0+166} L{x0+675} {y0+318} L{x0+645} {y0+318}" fill="none" stroke="#f87171" stroke-width="3" marker-end="url(#ar)"/>
      <text x="{x0+690}" y="{y0+250}" font-size="16" fill="#f87171">FAIL</text>
      <path d="M{x0+465} {y0+318} L{x0+425} {y0+318} L{x0+425} {y0+176}" fill="none" stroke="#f87171" stroke-width="3" marker-end="url(#ar)"/>
      <line x1="{x0+760}" y1="{y0+118}" x2="{x0+900}" y2="{y0+118}" stroke="#34d399" stroke-width="3" marker-end="url(#ag)"/>
      <text x="{x0+830}" y="{y0+104}" font-size="16" fill="#34d399" text-anchor="middle">PASS</text>
      {box(x0+905, y0+70, 150, 96, "#10b981", "#34d399", "다음 단계", "$prev")}
      <text x="{x0+FW/2}" y="{y0+445}" font-size="17" fill="#94a3b8" text-anchor="middle" font-family="{MONO}">매 호출 = 새 claude -p 세션 · 단계 output 캐시 · 도메인은 프롬프트 md에만</text>
    </g>'''


def nolai_inner(accent: str) -> str:
    """픽셀·토큰 모티프. 배포 전이라 스크린샷 대신."""
    x0, y0 = FX, FY + 34
    cells = []
    palette = ["#f472b6", "#a78bfa", "#38bdf8", "#34d399", "#fbbf24", "#f8fafc"]
    import random
    random.seed(7)
    for r in range(6):
        for c in range(9):
            if random.random() < 0.55:
                col = random.choice(palette)
                cells.append(f'<rect x="{x0+70+c*52}" y="{y0+60+r*52}" width="44" height="44" rx="8" fill="{col}" fill-opacity="{random.choice([0.9,0.6,0.35])}"/>')
    tokens = ["임베딩", "토큰", "픽셀", "벡터", "비트", "학습 데이터"]
    chips = "".join(
        f'<rect x="{x0+600}" y="{y0+58+i*62}" width="{80+len(t)*22}" height="44" rx="22" fill="{accent}" fill-opacity="{0.9-i*0.12}"/>'
        f'<text x="{x0+600+(80+len(t)*22)/2}" y="{y0+58+i*62+29}" font-size="20" font-weight="700" fill="#0b1220" text-anchor="middle">{t}</text>'
        for i, t in enumerate(tokens))
    return f'''
    <rect x="{x0}" y="{y0}" width="{FW}" height="{FH-34}" fill="#0b1220"/>
    {"".join(cells)}
    <g font-family="{FONT}">{chips}
      <text x="{x0+FW/2}" y="{y0+440}" font-size="18" fill="#94a3b8" text-anchor="middle">10~13세가 AI 작동 원리를 손으로 만지며 배우는 웹 놀이터 · 배포 전</text>
    </g>'''


CARDS = [
    ("kbrain-ems",     "kbrain-ems",     "교육 운영 관리 시스템",          "#34d399", "8,180",  "누적 지원 · 수료 1,449 · 기수 41", "production", img_inner),
    ("kbrain-cert",    "kbrain-cert",    "작업형 온라인 CBT",              "#38bdf8", "108",    "최대 동시 응시 · 누적 1,466",    "production", img_inner),
    ("jodalfit",       "조달핏",          "나라장터 공고 추천",             "#10b981", "11,000+", "진행 공고 매일 갱신 · 회사 34,517", "jodalfit.co.kr", img_inner),
    ("daeasy",         "DAEASY",         "회사 사이트 + AI 자동 발행",      "#60a5fa", "4.0/5",  "합격선 · 미만이면 최대 3회 재작성 · 판정은 코드가", "daeasy.co.kr", img_inner),
    ("agent-pipeline", "Agent Pipeline", "Critic PASS까지 도는 오케스트레이터", "#fbbf24", "PASS",  "까지 다음 단계로 못 간다",       "python", None),
    ("nolai",          "AI쏙",           "어린이 AI 원리 놀이터",           "#f472b6", "next",   "배포 준비 중",                    "nolai", None),
]

for name, title, sub, accent, stat, label, tag, fn in CARDS:
    if fn is img_inner:
        inner = img_inner(name)
    elif name == "agent-pipeline":
        inner = pipeline_inner(accent)
    else:
        inner = nolai_inner(accent)
    svg = shell(title, sub, accent, inner, stat, label, tag)
    p = OUT / f"{name}.svg"
    io.open(p, "w", encoding="utf-8", newline="\n").write(svg)
    print(f"{p.name}: {p.stat().st_size // 1024} KB")
