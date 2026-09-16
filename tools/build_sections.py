"""프로필 섹션 패널 SVG 생성 (카드와 같은 디자인 언어). 실행: uv run --no-project tools/build_sections.py"""
import io, pathlib

OUT = pathlib.Path(__file__).parent.parent / "assets" / "sections"
OUT.mkdir(parents=True, exist_ok=True)

FONT = "Pretendard, 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', system-ui, sans-serif"
MONO = "'JetBrains Mono', Consolas, monospace"
W = 1200
EMERALD, SKY, AMBER, PINK, INK, MUTED, TEXT = "#34d399", "#38bdf8", "#fbbf24", "#f472b6", "#0b1220", "#94a3b8", "#e2e8f0"


def panel(h: int, body: str, label: str = "") -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-label="{label}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1220"/><stop offset="1" stop-color="#111c33"/></linearGradient>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#ffffff" stroke-opacity="0.045"/></pattern>
  </defs>
  <rect width="{W}" height="{h}" rx="24" fill="url(#bg)"/>
  <rect width="{W}" height="{h}" rx="24" fill="url(#grid)"/>
  <g font-family="{FONT}">{body}</g>
</svg>
'''


def header(num: str, title: str, accent: str) -> str:
    return f'''
  <text x="48" y="58" font-size="16" fill="{accent}" font-family="{MONO}" letter-spacing="3">{num}</text>
  <text x="112" y="60" font-size="30" font-weight="700" fill="#f8fafc">{title}</text>
  <line x1="48" y1="84" x2="{W-48}" y2="84" stroke="#ffffff" stroke-opacity="0.12"/>'''


def tw(s: str, size: int) -> float:
    """대략적 텍스트 폭 (모노스페이스 기준)."""
    return sum(size * (1.0 if ord(c) > 0x2E7F else 0.62) for c in s)


# ── 00 · Roles: 기획·운영 × 개발 ─────────────────────────────
def roles() -> str:
    def col(x, accent, kicker, lines):
        out = f'''
  <rect x="{x}" y="48" width="528" height="184" rx="18" fill="#ffffff" fill-opacity="0.035" stroke="#ffffff" stroke-opacity="0.1"/>
  <rect x="{x}" y="48" width="6" height="184" rx="3" fill="{accent}"/>
  <text x="{x+32}" y="90" font-size="15" fill="{accent}" font-family="{MONO}" letter-spacing="3">{kicker}</text>'''
        for i, (b, rest) in enumerate(lines):
            out += f'<text x="{x+32}" y="{130+i*38}" font-size="21" fill="{TEXT}"><tspan font-weight="700" fill="#f8fafc">{b}</tspan>{rest}</text>'
        return out
    body = col(48, EMERALD, "PLANNING · OPERATIONS", [
        ("행안부 · NIA AI 챔피언 사업", " 기획·운영"),
        ("선발 · 교육 · 인증평가", " 전 주기 담당"),
        ("운영자 10명+", " · 누적 기수 41개"),
    ]) + col(624, SKY, "FULL-STACK", [
        ("운영하면서 발견한 문제", "를 직접 시스템으로"),
        ("Next.js 16 · Supabase · FastAPI", " · pgvector"),
        ("1인", " 설계 · 구현 · 배포"),
    ])
    body += f'''
  <circle cx="600" cy="140" r="22" fill="{INK}" stroke="#ffffff" stroke-opacity="0.2"/>
  <text x="600" y="149" font-size="24" font-weight="700" fill="#f8fafc" text-anchor="middle">×</text>'''
    return panel(280, body, "기획·운영 × 풀스택 개발")


# ── 02 · What I think ───────────────────────────────────────
def think() -> str:
    items = [
        ("운영자로서 발견한 문제만 진짜 문제다.", "운영도 코드도 한 사람이 하면 잘못 푸는 일이 줄어든다."),
        ("도메인 깊이가 없으면", "AI는 가짜 문제만 푼다."),
        ("평가 없는 PoC는 데모일 뿐.", "backtest 1번이 도입 결정의 무기."),
        ("가장 비싼 사람은 기획·운영 + 코드 + 도메인 hybrid.", "AI 코딩 시대의 셈법."),
    ]
    body = header("02", "What I think", AMBER)
    for i, (b, rest) in enumerate(items):
        y = 140 + i * 66
        body += f'''
  <text x="48" y="{y}" font-size="15" fill="{AMBER}" font-family="{MONO}">0{i+1}</text>
  <text x="96" y="{y}" font-size="22"><tspan font-weight="700" fill="#f8fafc">{b}</tspan><tspan dx="12" fill="{MUTED}">{rest}</tspan></text>'''
    return panel(420, body, "What I think")


# ── 03 · Stack ──────────────────────────────────────────────
def stack() -> str:
    rows = [
        ("LANG · FRAMEWORK", EMERALD, ["Python", "TypeScript", "Next.js 16", "React 19", "FastAPI", "Tailwind"]),
        ("DATA · DEPLOY", SKY, ["Supabase", "Postgres", "pgvector", "Vercel", "GitHub Actions", "Bun · uv"]),
        ("AI", PINK, ["Claude API", "Claude Code CLI", "RAG", "GraphRAG", "Multi-agent orchestration"]),
    ]
    body = header("03", "Stack", EMERALD)
    for r, (label, accent, chips) in enumerate(rows):
        y = 140 + r * 74
        body += f'<text x="48" y="{y+6}" font-size="13" fill="{accent}" font-family="{MONO}" letter-spacing="2">{label}</text>'
        x = 270
        for c in chips:
            w = tw(c, 17) + 30
            body += f'''
  <rect x="{x}" y="{y-24}" width="{w:.0f}" height="42" rx="21" fill="{accent}" fill-opacity="0.12" stroke="{accent}" stroke-opacity="0.5"/>
  <text x="{x + w/2:.0f}" y="{y+3}" font-size="17" fill="#f8fafc" text-anchor="middle" font-family="{MONO}">{c}</text>'''
            x += w + 12
    return panel(370, body, "Stack")


# ── 04 · Where ──────────────────────────────────────────────
def where() -> str:
    body = header("04", "Where", SKY) + f'''
  <text x="48" y="146" font-size="24" font-weight="700" fill="#f8fafc">케이브레인컴퍼니</text>
  <text x="270" y="146" font-size="20" fill="{MUTED}">공공AI센터 · HRD사업실</text>
  <rect x="{W-48-330}" y="116" width="330" height="44" rx="22" fill="{SKY}" fill-opacity="0.12" stroke="{SKY}" stroke-opacity="0.5"/>
  <text x="{W-48-165}" y="145" font-size="18" fill="#f8fafc" text-anchor="middle" font-family="{MONO}">jansseung@gmail.com</text>'''
    return panel(200, body, "Where")


# ── 01 · Projects header ────────────────────────────────────
def projects_header() -> str:
    body = header("01", "Projects", EMERALD) + f'''
  <text x="{W-48}" y="60" font-size="15" fill="{MUTED}" text-anchor="end" font-family="{MONO}">5 pinned · 1 next</text>'''
    return panel(100, body, "Projects")


for name, fn in [("roles", roles), ("projects-header", projects_header), ("think", think), ("stack", stack), ("where", where)]:
    p = OUT / f"{name}.svg"
    io.open(p, "w", encoding="utf-8", newline="\n").write(fn())
    print(f"{p.name}: {p.stat().st_size // 1024} KB")
