"""프로필 프로젝트 카드 SVG 생성. 실행: uv run --no-project tools/build_cards.py (tools/src/*.png를 base64로 내장)
- hero: EMS·CBT 전폭 카드 (1200×520)
- card: 조달핏·DAEASY 2단 카드 (1200×750)
"""
import base64, io, pathlib

SRC = pathlib.Path(__file__).parent / "src"
OUT = pathlib.Path(__file__).parent.parent / "assets" / "cards"
OUT.mkdir(parents=True, exist_ok=True)

FONT = "Pretendard, 'Apple SD Gothic Neo', 'Noto Sans KR', 'Malgun Gothic', system-ui, sans-serif"
MONO = "'JetBrains Mono', Consolas, monospace"
ACCENT = "#2dd4bf"          # 청록 하나
STATUS = {"운영 중": "#34d399", "개발 중": "#38bdf8", "개인": "#94a3b8"}
MUTED, TEXT, INK = "#94a3b8", "#e2e8f0", "#0b1220"


def b64(name: str) -> str:
    return base64.b64encode((SRC / f"{name}.png").read_bytes()).decode()


def defs() -> str:
    return f'''
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1220"/><stop offset="1" stop-color="#111c33"/></linearGradient>
  </defs>'''


def window(x, y, w, h, img_name, zoom=1.0, cid="win"):
    """브라우저 창 프레임 + 스크린샷(상단 기준, zoom배 확대)."""
    iw = w * zoom
    ih = iw * 675 / 1080
    return f'''
  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#0f172a" stroke="#ffffff" stroke-opacity="0.14"/>
  <rect x="{x}" y="{y}" width="{w}" height="34" rx="14" fill="#1e293b"/>
  <rect x="{x}" y="{y+20}" width="{w}" height="14" fill="#1e293b"/>
  <circle cx="{x+22}" cy="{y+17}" r="5" fill="#f87171"/><circle cx="{x+40}" cy="{y+17}" r="5" fill="#fbbf24"/><circle cx="{x+58}" cy="{y+17}" r="5" fill="#34d399"/>
  <clipPath id="{cid}"><rect x="{x}" y="{y+34}" width="{w}" height="{h-34}"/></clipPath>
  <image clip-path="url(#{cid})" x="{x}" y="{y+34}" width="{iw:.0f}" height="{ih:.0f}" preserveAspectRatio="xMinYMin meet" href="data:image/png;base64,{b64(img_name)}"/>
  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="none" stroke="{ACCENT}" stroke-opacity="0.35"/>'''


def status_chip(x, y, label):
    c = STATUS[label]
    w = 24 + len(label) * 22
    return f'''
  <rect x="{x-w}" y="{y-30}" width="{w}" height="40" rx="20" fill="{c}" fill-opacity="0.15" stroke="{c}" stroke-opacity="0.6"/>
  <circle cx="{x-w+20}" cy="{y-10}" r="5" fill="{c}"/>
  <text x="{x-w+34}" y="{y-3}" font-size="19" fill="#f8fafc">{label}</text>'''


# ── 전폭 히어로 카드 (EMS · CBT) ─────────────────────────────
def hero(name, title, subtitle, status, client, period, role, stats, note):
    """subtitle, note: 줄 리스트. stats: [(숫자, 라벨)]"""
    W, H = 1200, 540
    TX = 620   # 텍스트 시작 x (글 영역 532px)
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{title} — {' '.join(subtitle)}">{defs()}
  <rect width="{W}" height="{H}" rx="24" fill="url(#bg)"/>
  <rect x="0" y="0" width="{W}" height="6" fill="{ACCENT}"/>
  {window(48, 48, 532, 444, name, zoom=1.35, cid="w_"+name)}
  <g font-family="{FONT}">
    <text x="{TX}" y="98" font-size="44" font-weight="700" fill="#f8fafc">{title}</text>
    {status_chip(W-48, 98, status)}
    <text x="{TX}" y="138" font-size="21" fill="{TEXT}">{subtitle[0]}</text>
    <text x="{TX}" y="166" font-size="21" fill="{TEXT}">{subtitle[1] if len(subtitle) > 1 else ''}</text>
    <line x1="{TX}" y1="190" x2="{W-48}" y2="190" stroke="#ffffff" stroke-opacity="0.12"/>
    <text x="{TX}" y="226" font-size="18"><tspan fill="{ACCENT}" font-family="{MONO}" font-size="13" letter-spacing="2">발주처</tspan><tspan dx="14" fill="{TEXT}">{client}</tspan></text>
    <text x="{TX}" y="260" font-size="18"><tspan fill="{ACCENT}" font-family="{MONO}" font-size="13" letter-spacing="2">기간  </tspan><tspan dx="14" fill="{TEXT}">{period}</tspan></text>
    <text x="{TX}" y="294" font-size="18"><tspan fill="{ACCENT}" font-family="{MONO}" font-size="13" letter-spacing="2">역할  </tspan><tspan dx="14" fill="{TEXT}">{role}</tspan></text>
'''
    x = TX
    for num, label in stats:
        s += f'''
    <text x="{x}" y="384" font-size="46" font-weight="700" fill="{ACCENT}" font-family="{MONO}">{num}</text>
    <text x="{x}" y="414" font-size="17" fill="{MUTED}">{label}</text>'''
        x += 178
    for i, line in enumerate(note):
        s += f'''
    <text x="{TX}" y="{458 + i*24}" font-size="15" fill="{MUTED}">{line}</text>'''
    s += '''
  </g>
</svg>
'''
    return s


# ── 2단 카드 (조달핏 · DAEASY) ─────────────────────────────
def card(name, title, subtitle, status, tag, stat, stat_label, note):
    W, H = 1200, 750
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{title} — {subtitle}">{defs()}
  <rect width="{W}" height="{H}" rx="24" fill="url(#bg)"/>
  <rect x="0" y="0" width="{W}" height="6" fill="{ACCENT}"/>
  <g font-family="{FONT}">
    <text x="60" y="84" font-size="46" font-weight="700" fill="#f8fafc">{title}</text>
    {status_chip(W-60, 84, status)}
    <text x="60" y="124" font-size="24" fill="{TEXT}">{subtitle}</text>
  </g>
  {window(60, 150, 1080, 470, name, zoom=1.0, cid="w_"+name)}
  <g font-family="{FONT}">
    <text x="60" y="690"><tspan font-size="50" font-weight="700" fill="{ACCENT}" font-family="{MONO}">{stat}</tspan><tspan dx="18" font-size="24" fill="{MUTED}">{stat_label}</tspan></text>
    <text x="{W-60}" y="688" font-size="20" fill="{MUTED}" text-anchor="end" font-family="{MONO}">{tag}</text>
    <text x="60" y="724" font-size="17" fill="{MUTED}">{note}</text>
  </g>
</svg>
'''


OUTS = {
    "kbrain-ems": hero(
        "kbrain-ems", "kbrain-ems", ["모집부터 수료·결과보고까지", "교육 운영 데이터를 한 시스템에서 관리"],
        "운영 중", "행안부 · NIA AI 챔피언 사업", "2026.04 ~ 현재 · 개발 후 운영 병행", "요구분석 · 설계 · 개발 · 운영",
        [("41", "기수"), ("8,180", "지원 건수"), ("1,449", "수료 인원")],
        ["2026년 시스템 도입 후 집계 · 이전 엑셀·구글폼 데이터 이관 없음", "운영 담당자 10명 이상 사용"]),
    "kbrain-cert": hero(
        "kbrain-cert", "kbrain-cert", ["문항 관리 · 시험 진행 · 실시간 감독 · 결과 내보내기를", "통합한 사내 CBT"],
        "운영 중", "AI 챔피언 인증평가 (행안부 · NIA)", "2026.07 ~ 현재 · 개발 후 운영 병행", "요구분석 · 설계 · 개발 · 운영",
        [("108", "최대 동시 응시"), ("1,466", "누적 응시"), ("1,376", "고유 응시자")],
        ["실시험 운영 집계 (부하테스트 아님)", "동시 응시 설계 기준은 100명"]),
    "jodalfit": card(
        "jodalfit", "조달핏", "회사명 하나로 검토할 만한 나라장터 공고 TOP 5를 추천하는 공개 서비스",
        "운영 중", "jodalfit.co.kr", "11,000+", "공고 수집 · 색인 (매일 갱신)",
        "사내 수주 영업 지원 · 2026.05 ~ · 설계 · 개발 · 데이터 파이프라인"),
    "daeasy": card(
        "daeasy", "DAEASY", "회사 사이트와 인사이트 자동 발행 파이프라인",
        "운영 중", "daeasy.co.kr", "4.0/5", "자동 발행 합격선 · 평가 기준 7항목은 저장소 README",
        "케이브레인컴퍼니 회사 사이트 · 2026.05 ~ · 설계 · 개발 · 운영"),
}

for name, svg in OUTS.items():
    p = OUT / f"{name}.svg"
    io.open(p, "w", encoding="utf-8", newline="\n").write(svg)
    print(f"{p.name}: {p.stat().st_size // 1024} KB")

for old in ("agent-pipeline.svg", "nolai.svg"):
    q = OUT / old
    if q.exists():
        q.unlink(); print(f"removed {old}")
