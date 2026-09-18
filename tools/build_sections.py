"""프로필 섹션 패널 SVG 생성 (카드와 같은 디자인 언어). 실행: uv run --no-project tools/build_sections.py"""
import io, pathlib

OUT = pathlib.Path(__file__).parent.parent / "assets" / "sections"
OUT.mkdir(parents=True, exist_ok=True)

FONT = "Pretendard, 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', system-ui, sans-serif"
MONO = "'JetBrains Mono', Consolas, monospace"
W = 1200
ACCENT = "#2dd4bf"
MUTED, TEXT, INK = "#94a3b8", "#e2e8f0", "#0b1220"


def panel(h: int, body: str, label: str = "") -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-label="{label}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1220"/><stop offset="1" stop-color="#111c33"/></linearGradient>
  </defs>
  <rect width="{W}" height="{h}" rx="24" fill="url(#bg)"/>
  <g font-family="{FONT}">{body}</g>
</svg>
'''


def header(num: str, title: str) -> str:
    return f'''
  <text x="48" y="60" font-size="17" fill="{ACCENT}" font-family="{MONO}" letter-spacing="3">{num}</text>
  <text x="112" y="62" font-size="34" font-weight="700" fill="#f8fafc">{title}</text>
  <line x1="48" y1="88" x2="{W-48}" y2="88" stroke="#ffffff" stroke-opacity="0.12"/>'''


def tw(s: str, size: int) -> float:
    return sum(size * (1.0 if ord(c) > 0x2E7F else 0.62) for c in s)


# ── Roles ───────────────────────────────────────────────────
def roles() -> str:
    def col(x, kicker, lines):
        out = f'''
  <rect x="{x}" y="48" width="528" height="200" rx="18" fill="#ffffff" fill-opacity="0.035" stroke="#ffffff" stroke-opacity="0.1"/>
  <rect x="{x}" y="48" width="6" height="200" rx="3" fill="{ACCENT}"/>
  <text x="{x+32}" y="92" font-size="15" fill="{ACCENT}" font-family="{MONO}" letter-spacing="3">{kicker}</text>'''
        for i, (b, rest) in enumerate(lines):
            out += f'<text x="{x+32}" y="{136+i*42}" font-size="23" fill="{TEXT}"><tspan font-weight="700" fill="#f8fafc">{b}</tspan>{rest}</text>'
        return out
    body = col(48, "PLANNING · OPERATIONS", [
        ("선발 · 교육 · 인증평가", " 운영"),
        ("현업 요구사항 정리", " · 업무 절차 설계"),
        ("운영 담당자 10명 이상", "이 사용하는 시스템"),
    ]) + col(624, "DEVELOPMENT", [
        ("업무 시스템 4개", " 개발 · 운영"),
        ("웹 · API · DB", " 구현 및 배포"),
        ("컴퓨터과학 전공", " (강원대학교)"),
    ])
    body += f'''
  <circle cx="600" cy="148" r="22" fill="{INK}" stroke="#ffffff" stroke-opacity="0.2"/>
  <text x="600" y="157" font-size="24" font-weight="700" fill="#f8fafc" text-anchor="middle">×</text>'''
    return panel(296, body, "기획·운영 × 개발")


# ── How I work ──────────────────────────────────────────────
def think() -> str:
    items = [
        ("현업 요구사항을 정리하고,", "구현 후 운영 담당자와 업무 흐름을 검증한다."),
        ("주요 설계 결정과 운영 절차를 문서화하고,", "변경 시 갱신한다. 저장소마다 설계 문서와 운영 가이드."),
        ("실데이터로 가설을 검증하고,", "결과에 따라 기능 범위와 설계를 조정한다. 조달핏: 수주이력 매칭 1.1% → 업종 중심."),
        ("운영 중 확인된 오류를 회귀 테스트에 반영한다.", "테스트 자동화 · RLS 정책은 2026 하반기 보강 중."),
    ]
    body = header("02", "How I work")
    for i, (b, rest) in enumerate(items):
        y = 148 + i * 70
        body += f'''
  <text x="48" y="{y}" font-size="16" fill="{ACCENT}" font-family="{MONO}">0{i+1}</text>
  <text x="96" y="{y}" font-size="23"><tspan font-weight="700" fill="#f8fafc">{b}</tspan><tspan dx="10" fill="{MUTED}">{rest}</tspan></text>'''
    return panel(440, body, "How I work")


# ── Stack ───────────────────────────────────────────────────
def stack() -> str:
    rows = [
        ("업무 서비스에서 사용", ["TypeScript", "Next.js", "React", "Python", "FastAPI", "PostgreSQL · Supabase", "pgvector", "Vercel", "Agora"]),
        ("개인 프로젝트 · 실험", ["Claude API", "Claude Code CLI", "RAG", "Multi-agent"]),
    ]
    body = header("03", "Stack")
    y = 150
    for label, chips in rows:
        body += f'<text x="48" y="{y+7}" font-size="17" fill="{ACCENT}">{label}</text>'
        x = 250
        for c in chips:
            w = tw(c, 18) + 32
            if x + w > W - 48:          # 넘치면 다음 줄
                x = 250; y += 60
            body += f'''
  <rect x="{x}" y="{y-26}" width="{w:.0f}" height="46" rx="23" fill="{ACCENT}" fill-opacity="0.1" stroke="{ACCENT}" stroke-opacity="0.45"/>
  <text x="{x + w/2:.0f}" y="{y+4}" font-size="18" fill="#f8fafc" text-anchor="middle" font-family="{MONO}">{c}</text>'''
            x += w + 12
        y += 80
    return panel(y - 80 + 60, body, "Stack")


# ── Where ───────────────────────────────────────────────────
def where() -> str:
    body = header("04", "Where") + f'''
  <text x="48" y="150" font-size="26" font-weight="700" fill="#f8fafc">케이브레인컴퍼니</text>
  <text x="290" y="150" font-size="21" fill="{MUTED}">공공AI센터 · HRD사업실 · 주임</text>
  <text x="48" y="196" font-size="21" fill="{TEXT}">강원대학교 컴퓨터과학전공</text>
  <rect x="{W-48-330}" y="118" width="330" height="46" rx="23" fill="{ACCENT}" fill-opacity="0.1" stroke="{ACCENT}" stroke-opacity="0.45"/>
  <text x="{W-48-165}" y="148" font-size="19" fill="#f8fafc" text-anchor="middle" font-family="{MONO}">jansseung@gmail.com</text>'''
    return panel(236, body, "Where")


# ── Projects header ─────────────────────────────────────────
def projects_header() -> str:
    body = header("01", "Projects") + f'''
  <text x="{W-48}" y="62" font-size="17" fill="{MUTED}" text-anchor="end">업무 서비스 4 (소스 비공개 · 사례 문서) · 개인 프로젝트 2</text>'''
    return panel(104, body, "Projects")


for name, fn in [("roles", roles), ("projects-header", projects_header), ("think", think), ("stack", stack), ("where", where)]:
    p = OUT / f"{name}.svg"
    io.open(p, "w", encoding="utf-8", newline="\n").write(fn())
    print(f"{p.name}: {p.stat().st_size // 1024} KB")
