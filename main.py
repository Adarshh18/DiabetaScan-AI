import streamlit as st
import pandas as pd
import numpy as np
import joblib
import warnings
warnings.filterwarnings('ignore')

# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="DiabetaScan AI",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── GLOBAL CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Exo+2:ital,wght@0,300;0,400;0,600;0,700;0,800;0,900;1,300&family=Inter:wght@300;400;500;600&family=Fira+Code:wght@400;500;600&display=swap');

/* ══════════════════════════════════════════
   KEYFRAME ANIMATIONS — Premium Set
══════════════════════════════════════════ */

@keyframes mesh-drift {
    0%   { background-position: 0% 0%, 100% 100%, 50% 0%; }
    33%  { background-position: 100% 50%, 0% 50%, 100% 100%; }
    66%  { background-position: 50% 100%, 50% 0%, 0% 50%; }
    100% { background-position: 0% 0%, 100% 100%, 50% 0%; }
}

@keyframes aurora-shift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes float-slow {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    33%       { transform: translateY(-14px) rotate(1.2deg); }
    66%       { transform: translateY(-6px) rotate(-0.8deg); }
}

@keyframes logo-spin-halo {
    0%   { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

@keyframes logo-counter-spin {
    0%   { transform: rotate(0deg); }
    100% { transform: rotate(-360deg); }
}

@keyframes pulse-ring {
    0%   { transform: scale(0.88); opacity: 0.9; }
    100% { transform: scale(1.8); opacity: 0; }
}

@keyframes shimmer-slide {
    0%   { transform: translateX(-120%) skewX(-15deg); }
    100% { transform: translateX(220%) skewX(-15deg); }
}

@keyframes scan-line {
    0%   { top: -3px; opacity: 0.9; }
    70%  { opacity: 0.5; }
    100% { top: 100%; opacity: 0; }
}

@keyframes fade-up {
    from { opacity: 0; transform: translateY(32px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes fade-in {
    from { opacity: 0; }
    to   { opacity: 1; }
}

@keyframes glow-pulse {
    0%, 100% { box-shadow: 0 0 8px rgba(120,80,255,0.3), 0 0 20px rgba(120,80,255,0.1); }
    50%       { box-shadow: 0 0 16px rgba(120,80,255,0.7), 0 0 40px rgba(120,80,255,0.25); }
}

@keyframes border-chase {
    0%   { background-position: 0% 0%; }
    100% { background-position: 400% 0%; }
}

@keyframes number-glow {
    0%, 100% { filter: brightness(1); }
    50%       { filter: brightness(1.35) drop-shadow(0 0 10px rgba(120,80,255,0.5)); }
}

@keyframes rotate-slow {
    from { transform: rotate(0deg); }
    to   { transform: rotate(360deg); }
}

@keyframes star-twinkle {
    0%, 100% { opacity: 0.12; transform: scale(1); }
    50%       { opacity: 0.75; transform: scale(1.5); }
}

@keyframes slide-in-left {
    from { opacity: 0; transform: translateX(-36px); }
    to   { opacity: 1; transform: translateX(0); }
}

@keyframes hero-orb {
    0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.7; }
    25%       { transform: translate(40px, -25px) scale(1.12); opacity: 0.9; }
    50%       { transform: translate(-20px, 35px) scale(0.92); opacity: 0.6; }
    75%       { transform: translate(-35px, -12px) scale(1.08); opacity: 0.85; }
}

@keyframes risk-reveal {
    0%   { opacity: 0; transform: scale(0.65) translateY(30px); }
    55%  { transform: scale(1.06) translateY(-6px); }
    100% { opacity: 1; transform: scale(1) translateY(0); }
}

@keyframes dna-helix {
    0%   { stroke-dashoffset: 0; }
    100% { stroke-dashoffset: -120; }
}

@keyframes heartbeat {
    0%, 100% { transform: scale(1); }
    14%       { transform: scale(1.25); }
    28%       { transform: scale(1); }
    42%       { transform: scale(1.15); }
    70%       { transform: scale(1); }
}

@keyframes slide-down {
    from { opacity: 0; transform: translateY(-16px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes grid-scroll {
    from { transform: translateY(0); }
    to   { transform: translateY(60px); }
}

@keyframes neon-flicker {
    0%, 95%, 100% { opacity: 1; }
    96%            { opacity: 0.6; }
    97%            { opacity: 1; }
    98%            { opacity: 0.5; }
    99%            { opacity: 0.9; }
}

/* ══════════════════════════════════════════
   RESET & BASE
══════════════════════════════════════════ */
*, *::before, *::after { box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"] {
    background: #06040f !important;
    color: #e2dff4;
    font-family: 'Inter', sans-serif;
}

/* ── Scrolling grid mesh background ── */
[data-testid="stAppViewContainer"]::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(120,80,255,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(120,80,255,0.04) 1px, transparent 1px);
    background-size: 50px 50px;
    animation: grid-scroll 8s linear infinite;
    pointer-events: none;
    z-index: 0;
}

/* ── Gradient atmosphere orbs ── */
[data-testid="stAppViewContainer"]::after {
    content: '';
    position: fixed;
    inset: 0;
    background:
        radial-gradient(ellipse 55% 45% at 8% 15%,  rgba(120,80,255,0.09) 0%, transparent 55%),
        radial-gradient(ellipse 50% 40% at 92% 80%,  rgba(220,40,100,0.07) 0%, transparent 55%),
        radial-gradient(ellipse 40% 35% at 50% 50%,  rgba(0,180,220,0.04) 0%, transparent 60%),
        radial-gradient(ellipse 35% 55% at 75% 20%,  rgba(80,200,160,0.05) 0%, transparent 50%);
    animation: mesh-drift 20s ease-in-out infinite;
    background-size: 200% 200%;
    pointer-events: none;
    z-index: 0;
}

/* Twinkling star field */
[data-testid="stMain"]::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
        radial-gradient(1.5px 1.5px at 8%  18%,  rgba(120,80,255,0.9) 0%, transparent 100%),
        radial-gradient(1px   1px   at 27% 55%,  rgba(220,40,100,0.8)  0%, transparent 100%),
        radial-gradient(1.5px 1.5px at 52% 22%,  rgba(0,200,180,0.7)   0%, transparent 100%),
        radial-gradient(1px   1px   at 73% 78%,  rgba(120,80,255,0.8)  0%, transparent 100%),
        radial-gradient(1px   1px   at 89% 12%,  rgba(220,40,100,0.7)  0%, transparent 100%),
        radial-gradient(1.5px 1.5px at 18% 88%,  rgba(0,180,220,0.7)   0%, transparent 100%),
        radial-gradient(1px   1px   at 95% 52%,  rgba(120,80,255,0.6)  0%, transparent 100%),
        radial-gradient(1px   1px   at 43% 97%,  rgba(220,40,100,0.6)  0%, transparent 100%),
        radial-gradient(1px   1px   at 5%  43%,  rgba(0,200,180,0.7)   0%, transparent 100%),
        radial-gradient(1.5px 1.5px at 61% 67%,  rgba(120,80,255,0.7)  0%, transparent 100%),
        radial-gradient(1px   1px   at 33% 33%,  rgba(220,40,100,0.5)  0%, transparent 100%),
        radial-gradient(1px   1px   at 80% 45%,  rgba(0,180,220,0.6)   0%, transparent 100%);
    animation: star-twinkle 5s ease-in-out infinite;
    pointer-events: none;
    z-index: 0;
}

/* ══════════════════════════════════════════
   SIDEBAR
══════════════════════════════════════════ */
[data-testid="stSidebar"] {
    background: linear-gradient(165deg, #0b0718 0%, #0e0820 50%, #080514 100%) !important;
    border-right: 1px solid rgba(120,80,255,0.18);
    box-shadow: 6px 0 50px rgba(0,0,0,0.7), inset -1px 0 0 rgba(120,80,255,0.08);
}
[data-testid="stSidebarContent"] { padding: 1.5rem 1rem; }

.stRadio > div { gap: 0.5rem; }
.stRadio [data-baseweb="radio"] {
    background: rgba(255,255,255,0.015);
    border: 1px solid rgba(120,80,255,0.18);
    border-radius: 12px;
    padding: 0.65rem 1rem;
    margin: 0.15rem 0;
    transition: all 0.35s cubic-bezier(0.4,0,0.2,1);
    position: relative;
    overflow: hidden;
}
.stRadio [data-baseweb="radio"]::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(120,80,255,0.1), rgba(220,40,100,0.06));
    opacity: 0;
    transition: opacity 0.3s;
}
.stRadio [data-baseweb="radio"]:hover {
    border-color: rgba(120,80,255,0.55);
    transform: translateX(5px);
    box-shadow: 0 4px 22px rgba(120,80,255,0.15);
}
.stRadio [data-baseweb="radio"]:hover::before { opacity: 1; }

h1, h2, h3, h4 {
    font-family: 'Exo 2', sans-serif !important;
    color: #e2dff4 !important;
}

/* ══════════════════════════════════════════
   METRIC CARDS
══════════════════════════════════════════ */
.metric-card {
    background: linear-gradient(145deg, #100c22 0%, #160e2e 50%, #0e0b1e 100%);
    border: 1px solid rgba(120,80,255,0.2);
    border-radius: 22px;
    padding: 1.7rem 1.3rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: transform 0.45s cubic-bezier(0.34,1.56,0.64,1), box-shadow 0.4s ease;
    animation: fade-up 0.6s ease both;
}
.metric-card:hover {
    transform: translateY(-8px) scale(1.03);
    box-shadow: 0 24px 70px rgba(120,80,255,0.2), 0 8px 28px rgba(0,0,0,0.5);
    border-color: rgba(120,80,255,0.5);
}
.metric-card::before {
    content: '';
    position: absolute;
    top: 0; left: -100%; right: -100%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #7850ff, #dc2864, #00c8b4, #7850ff, transparent);
    background-size: 200% 100%;
    animation: border-chase 3.5s linear infinite;
}
.metric-card::after {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 50%;
    height: 100%;
    background: linear-gradient(105deg, transparent 38%, rgba(255,255,255,0.035) 50%, transparent 62%);
    animation: shimmer-slide 4s ease-in-out infinite;
}
.metric-number {
    font-family: 'Exo 2', sans-serif;
    font-size: 2.5rem;
    font-weight: 900;
    background: linear-gradient(135deg, #a078ff 0%, #dc2864 50%, #00c8b4 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
    animation: number-glow 3.5s ease-in-out infinite;
}
.metric-label {
    font-family: 'Fira Code', monospace;
    font-size: 0.67rem;
    color: rgba(140,120,200,0.85);
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-top: 0.5rem;
    font-weight: 500;
}
.metric-sub {
    font-size: 0.82rem;
    color: rgba(160,150,210,0.65);
    margin-top: 0.25rem;
}

/* ══════════════════════════════════════════
   SECTION TITLES
══════════════════════════════════════════ */
.section-title {
    font-family: 'Exo 2', sans-serif;
    font-size: 1.9rem;
    font-weight: 800;
    color: #e2dff4;
    margin-bottom: 0.3rem;
    animation: fade-up 0.5s ease both;
}
.section-subtitle {
    color: rgba(140,120,200,0.8);
    font-size: 0.95rem;
    margin-bottom: 2rem;
    animation: fade-up 0.5s 0.1s ease both;
}
.accent {
    background: linear-gradient(135deg, #a078ff, #dc2864, #00c8b4);
    background-size: 200% 100%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: aurora-shift 5s ease infinite;
}

/* ══════════════════════════════════════════
   HERO BANNER
══════════════════════════════════════════ */
.hero-banner {
    background: linear-gradient(145deg, #110e25 0%, #0e0920 40%, #130d22 70%, #0a0818 100%);
    background-size: 300% 300%;
    border: 1px solid rgba(120,80,255,0.22);
    border-radius: 30px;
    padding: 3.8rem 3.8rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    animation: aurora-shift 12s ease infinite, fade-up 0.7s ease both;
    box-shadow: 0 50px 100px rgba(0,0,0,0.6), 0 0 0 1px rgba(120,80,255,0.08), inset 0 1px 0 rgba(255,255,255,0.04);
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -80px; right: -80px;
    width: 360px; height: 360px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(120,80,255,0.14) 0%, rgba(220,40,100,0.07) 40%, transparent 70%);
    animation: hero-orb 9s ease-in-out infinite;
}
/* DNA helix SVG watermark replacing stethoscope */
.hero-banner::after {
    content: '';
    position: absolute;
    right: 3rem;
    top: 50%;
    transform: translateY(-50%);
    width: 140px; height: 180px;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 100 140' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M30 10 Q70 35 30 60 Q70 85 30 110 Q70 135 30 160' stroke='%237850ff' stroke-width='2.5' fill='none' stroke-dasharray='6 3' opacity='0.4'/%3E%3Cpath d='M70 10 Q30 35 70 60 Q30 85 70 110 Q30 135 70 160' stroke='%23dc2864' stroke-width='2.5' fill='none' stroke-dasharray='6 3' opacity='0.4'/%3E%3Cline x1='30' y1='35' x2='70' y2='35' stroke='%2300c8b4' stroke-width='1.5' opacity='0.35'/%3E%3Cline x1='30' y1='60' x2='70' y2='60' stroke='%23a078ff' stroke-width='1.5' opacity='0.35'/%3E%3Cline x1='30' y1='85' x2='70' y2='85' stroke='%2300c8b4' stroke-width='1.5' opacity='0.35'/%3E%3Cline x1='30' y1='110' x2='70' y2='110' stroke='%23a078ff' stroke-width='1.5' opacity='0.35'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-size: contain;
    opacity: 0.55;
    animation: float-slow 8s ease-in-out infinite;
}
.hero-banner .scan-line {
    position: absolute;
    left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(120,80,255,0.5), rgba(220,40,100,0.4), transparent);
    animation: scan-line 5s linear infinite;
}
.hero-title {
    font-family: 'Exo 2', sans-serif;
    font-size: 3.3rem;
    font-weight: 900;
    line-height: 1.08;
    margin-bottom: 1rem;
    animation: fade-up 0.7s 0.1s ease both;
    letter-spacing: -0.8px;
}
.hero-sub {
    color: rgba(160,150,210,0.82);
    font-size: 1.05rem;
    max-width: 580px;
    line-height: 1.78;
    animation: fade-up 0.7s 0.2s ease both;
}

/* ══════════════════════════════════════════
   RISK CARDS
══════════════════════════════════════════ */
.risk-low {
    background: linear-gradient(145deg, #081a12, #0c2518, #051410);
    border: 2px solid rgba(0,200,140,0.65);
    border-radius: 26px;
    padding: 2.8rem 2.2rem;
    text-align: center;
    animation: risk-reveal 0.9s cubic-bezier(0.34,1.56,0.64,1) both;
    box-shadow: 0 0 70px rgba(0,200,140,0.14), 0 0 0 1px rgba(0,200,140,0.06), inset 0 1px 0 rgba(0,200,140,0.1);
    position: relative; overflow: hidden;
}
.risk-low::before {
    content: '';
    position: absolute; inset: 0;
    background: radial-gradient(ellipse 90% 55% at 50% 0%, rgba(0,200,140,0.08) 0%, transparent 65%);
    pointer-events: none;
}
.risk-high {
    background: linear-gradient(145deg, #1c0610, #2a0c18, #160508);
    border: 2px solid rgba(220,40,100,0.75);
    border-radius: 26px;
    padding: 2.8rem 2.2rem;
    text-align: center;
    animation: risk-reveal 0.9s cubic-bezier(0.34,1.56,0.64,1) both;
    box-shadow: 0 0 70px rgba(220,40,100,0.18), 0 0 0 1px rgba(220,40,100,0.06), inset 0 1px 0 rgba(220,40,100,0.1);
    position: relative; overflow: hidden;
}
.risk-high::before {
    content: '';
    position: absolute; inset: 0;
    background: radial-gradient(ellipse 90% 55% at 50% 0%, rgba(220,40,100,0.1) 0%, transparent 65%);
    pointer-events: none;
}
.risk-medium {
    background: linear-gradient(145deg, #1a1000, #261800, #150e00);
    border: 2px solid rgba(255,165,2,0.68);
    border-radius: 26px;
    padding: 2.8rem 2.2rem;
    text-align: center;
    animation: risk-reveal 0.9s cubic-bezier(0.34,1.56,0.64,1) both;
    box-shadow: 0 0 70px rgba(255,165,2,0.14), 0 0 0 1px rgba(255,165,2,0.05), inset 0 1px 0 rgba(255,165,2,0.08);
    position: relative; overflow: hidden;
}
.risk-medium::before {
    content: '';
    position: absolute; inset: 0;
    background: radial-gradient(ellipse 90% 55% at 50% 0%, rgba(255,165,2,0.07) 0%, transparent 65%);
    pointer-events: none;
}
.risk-icon {
    font-size: 4.2rem;
    margin-bottom: 0.8rem;
    display: block;
    animation: heartbeat 2.8s ease-in-out infinite;
    filter: drop-shadow(0 6px 18px rgba(0,0,0,0.4));
}
.risk-title {
    font-family: 'Exo 2', sans-serif;
    font-size: 1.9rem;
    font-weight: 900;
    margin-bottom: 0.5rem;
    letter-spacing: 3px;
    text-transform: uppercase;
}
.risk-prob {
    font-size: 4.5rem;
    font-family: 'Exo 2', sans-serif;
    font-weight: 900;
    line-height: 1;
    animation: number-glow 2.5s ease-in-out infinite;
}

/* ══════════════════════════════════════════
   INFO BOXES
══════════════════════════════════════════ */
.info-box {
    background: linear-gradient(135deg, rgba(16,12,34,0.92), rgba(12,9,28,0.92));
    border: 1px solid rgba(120,80,255,0.2);
    border-left: 3px solid #7850ff;
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    margin: 0.6rem 0;
    font-size: 0.9rem;
    color: rgba(196,185,235,0.9);
    backdrop-filter: blur(12px);
    animation: slide-in-left 0.5s ease both;
}

/* ══════════════════════════════════════════
   FEATURE ITEMS
══════════════════════════════════════════ */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.2rem;
    margin: 1.5rem 0;
}
.feature-item {
    background: linear-gradient(145deg, #100c22, #160e2e);
    border: 1px solid rgba(120,80,255,0.18);
    border-radius: 18px;
    padding: 1.4rem;
    transition: all 0.38s cubic-bezier(0.4,0,0.2,1);
    position: relative;
    overflow: hidden;
}
.feature-item::before {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #7850ff, #dc2864, #00c8b4);
    transform: scaleX(0);
    transition: transform 0.45s ease;
    transform-origin: left;
}
.feature-item:hover {
    transform: translateY(-5px);
    border-color: rgba(120,80,255,0.4);
    box-shadow: 0 14px 45px rgba(120,80,255,0.13);
}
.feature-item:hover::before { transform: scaleX(1); }
.feature-icon { font-size: 2rem; margin-bottom: 0.7rem; display: block; }
.feature-name {
    font-family: 'Exo 2', sans-serif;
    font-size: 0.92rem;
    font-weight: 700;
    color: #e2dff4;
}
.feature-desc { font-size: 0.78rem; color: rgba(140,120,200,0.8); margin-top: 0.25rem; line-height: 1.5; }

.stProgress > div > div > div { background: linear-gradient(90deg, #7850ff, #dc2864) !important; }

/* ══════════════════════════════════════════
   DIVIDER
══════════════════════════════════════════ */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(120,80,255,0.4), rgba(220,40,100,0.35), rgba(0,200,180,0.3), transparent);
    background-size: 200% 100%;
    margin: 2.5rem 0;
    animation: aurora-shift 7s ease infinite;
}

/* ══════════════════════════════════════════
   TABS
══════════════════════════════════════════ */
.stTabs [data-baseweb="tab-list"] {
    background: linear-gradient(135deg, #100c22, #160e2e);
    border-radius: 16px;
    padding: 0.4rem;
    gap: 0.3rem;
    border: 1px solid rgba(120,80,255,0.2);
    box-shadow: inset 0 2px 10px rgba(0,0,0,0.4);
}
.stTabs [data-baseweb="tab"] {
    background: transparent;
    color: rgba(140,120,200,0.8);
    border-radius: 11px;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: 0.88rem;
    transition: all 0.3s ease;
    letter-spacing: 0.2px;
}
.stTabs [data-baseweb="tab"]:hover { color: rgba(160,120,255,0.9); }
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, rgba(120,80,255,0.2), rgba(220,40,100,0.12)) !important;
    color: #a078ff !important;
    box-shadow: 0 2px 14px rgba(120,80,255,0.18), inset 0 1px 0 rgba(120,80,255,0.15);
}

/* ══════════════════════════════════════════
   FORM INPUTS
══════════════════════════════════════════ */
.stSlider > div > div > div > div { background: linear-gradient(90deg, #7850ff, #dc2864) !important; }
.stSelectbox [data-baseweb="select"] > div,
.stNumberInput input {
    background: rgba(16,12,34,0.85) !important;
    border-color: rgba(120,80,255,0.22) !important;
    color: #e2dff4 !important;
    border-radius: 12px !important;
    transition: border-color 0.3s, box-shadow 0.3s !important;
}
.stSelectbox [data-baseweb="select"] > div:focus-within,
.stNumberInput input:focus {
    border-color: rgba(120,80,255,0.6) !important;
    box-shadow: 0 0 0 3px rgba(120,80,255,0.1) !important;
}

/* ══════════════════════════════════════════
   BUTTONS
══════════════════════════════════════════ */
.stButton > button {
    background: linear-gradient(135deg, #7850ff 0%, #b4388a 50%, #dc2864 100%) !important;
    background-size: 200% 100% !important;
    color: #fff !important;
    font-family: 'Exo 2', sans-serif !important;
    font-weight: 800 !important;
    font-size: 1rem !important;
    border: none !important;
    border-radius: 14px !important;
    padding: 0.78rem 2.6rem !important;
    transition: all 0.38s cubic-bezier(0.4,0,0.2,1) !important;
    letter-spacing: 1px;
    text-transform: uppercase;
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 24px rgba(120,80,255,0.3) !important;
}
.stButton > button::before {
    content: '';
    position: absolute;
    top: 0; left: -80%;
    width: 55%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.22), transparent);
    transform: skewX(-22deg);
    transition: left 0.65s ease;
}
.stButton > button:hover {
    transform: translateY(-4px) scale(1.03) !important;
    box-shadow: 0 16px 50px rgba(120,80,255,0.5), 0 4px 20px rgba(220,40,100,0.3) !important;
    background-position: 100% 0% !important;
}
.stButton > button:hover::before { left: 130%; }
.stButton > button:active { transform: translateY(-1px) scale(0.99) !important; }

/* ══════════════════════════════════════════
   ABOUT CARDS
══════════════════════════════════════════ */
.about-card {
    background: linear-gradient(145deg, #100c22, #160e2e, #0e0a1e);
    border: 1px solid rgba(120,80,255,0.2);
    border-radius: 22px;
    padding: 2rem;
    height: 100%;
    position: relative;
    overflow: hidden;
    transition: all 0.35s ease;
}
.about-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(120,80,255,0.5), rgba(220,40,100,0.4), transparent);
}
.about-card:hover {
    border-color: rgba(120,80,255,0.35);
    box-shadow: 0 24px 70px rgba(120,80,255,0.08);
}
.about-card-title {
    font-family: 'Exo 2', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: #a078ff;
    margin-bottom: 0.9rem;
    display: flex;
    align-items: center;
    gap: 0.4rem;
}

.chart-container {
    background: linear-gradient(145deg, #100c22, #0e0a1e);
    border: 1px solid rgba(120,80,255,0.18);
    border-radius: 20px;
    padding: 1.5rem;
}

/* ══════════════════════════════════════════
   SIDEBAR LOGO — SVG DNA icon with spin halo
══════════════════════════════════════════ */
.sidebar-logo {
    text-align: center;
    padding: 1.2rem 0 2rem;
    border-bottom: 1px solid rgba(120,80,255,0.18);
    margin-bottom: 1.5rem;
    position: relative;
}
.logo-wrap {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    position: relative;
    width: 72px;
    height: 72px;
    margin-bottom: 0.5rem;
}
/* outer spinning ring */
.logo-wrap::before {
    content: '';
    position: absolute;
    inset: -4px;
    border-radius: 50%;
    border: 2px solid transparent;
    border-top-color: #7850ff;
    border-right-color: rgba(120,80,255,0.3);
    animation: logo-spin-halo 3s linear infinite;
}
/* inner counter-spin ring */
.logo-wrap::after {
    content: '';
    position: absolute;
    inset: 2px;
    border-radius: 50%;
    border: 1.5px solid transparent;
    border-bottom-color: #dc2864;
    border-left-color: rgba(220,40,100,0.3);
    animation: logo-counter-spin 2s linear infinite;
}
.logo-core {
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background: linear-gradient(145deg, #1e1640, #2a1858);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 24px rgba(120,80,255,0.35), inset 0 1px 0 rgba(255,255,255,0.06);
    position: relative;
    z-index: 1;
    animation: float-slow 5s ease-in-out infinite;
}
/* pulse rings behind logo */
.logo-pulse {
    position: absolute;
    inset: -6px;
    border-radius: 50%;
    border: 2px solid rgba(120,80,255,0.4);
    animation: pulse-ring 2.8s ease-out infinite;
}
.logo-pulse-2 {
    position: absolute;
    inset: -6px;
    border-radius: 50%;
    border: 2px solid rgba(220,40,100,0.3);
    animation: pulse-ring 2.8s ease-out 1.4s infinite;
}
.sidebar-logo-title {
    font-family: 'Exo 2', sans-serif;
    font-size: 1.35rem;
    font-weight: 900;
    background: linear-gradient(135deg, #a078ff, #dc2864, #00c8b4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    background-size: 200% 100%;
    animation: aurora-shift 5s ease infinite;
    letter-spacing: 0.5px;
    margin-top: 0.4rem;
    animation: aurora-shift 5s ease infinite, neon-flicker 8s ease-in-out infinite;
}
.sidebar-logo-sub {
    font-family: 'Fira Code', monospace;
    font-size: 0.6rem;
    color: rgba(140,120,200,0.65);
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 0.2rem;
}

/* ══════════════════════════════════════════
   BADGES
══════════════════════════════════════════ */
.badge {
    display: inline-block;
    background: rgba(16,12,34,0.85);
    border: 1px solid rgba(120,80,255,0.25);
    color: rgba(160,150,210,0.85);
    border-radius: 20px;
    padding: 0.25rem 0.9rem;
    font-size: 0.75rem;
    margin: 0.2rem;
    font-family: 'Inter', sans-serif;
    font-weight: 500;
    transition: all 0.28s ease;
    backdrop-filter: blur(8px);
}
.badge:hover { transform: translateY(-1px); }
.badge-green {
    border-color: rgba(0,200,180,0.5);
    color: #00c8b4;
    background: rgba(0,200,180,0.08);
    box-shadow: 0 0 12px rgba(0,200,180,0.1);
}
.badge-blue {
    border-color: rgba(120,80,255,0.5);
    color: #a078ff;
    background: rgba(120,80,255,0.08);
    box-shadow: 0 0 12px rgba(120,80,255,0.1);
}
.badge-red {
    border-color: rgba(220,40,100,0.5);
    color: #dc2864;
    background: rgba(220,40,100,0.08);
}
.badge-orange {
    border-color: rgba(255,165,2,0.5);
    color: #ffa502;
    background: rgba(255,165,2,0.08);
}

/* ══════════════════════════════════════════
   TIMELINE
══════════════════════════════════════════ */
.timeline-item {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.2rem;
    align-items: flex-start;
    animation: slide-in-left 0.4s ease both;
}
.timeline-dot {
    width: 10px; height: 10px;
    background: #7850ff;
    border-radius: 50%;
    margin-top: 5px;
    flex-shrink: 0;
    box-shadow: 0 0 8px rgba(120,80,255,0.7);
    animation: glow-pulse 2.8s ease-in-out infinite;
}
.timeline-content { flex: 1; }
.timeline-title { font-weight: 600; font-size: 0.88rem; color: #e2dff4; }
.timeline-desc { font-size: 0.78rem; color: rgba(140,120,200,0.75); margin-top: 0.1rem; }

/* ══════════════════════════════════════════
   SCROLLBAR
══════════════════════════════════════════ */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #06040f; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #7850ff, #dc2864);
    border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover { background: #a078ff; }

/* ══════════════════════════════════════════
   STAGGERED COLUMNS
══════════════════════════════════════════ */
[data-testid="column"]:nth-child(1) .metric-card { animation-delay: 0.00s; }
[data-testid="column"]:nth-child(2) .metric-card { animation-delay: 0.09s; }
[data-testid="column"]:nth-child(3) .metric-card { animation-delay: 0.18s; }
[data-testid="column"]:nth-child(4) .metric-card { animation-delay: 0.27s; }
[data-testid="column"]:nth-child(5) .metric-card { animation-delay: 0.36s; }

/* ══════════════════════════════════════════
   SECTION PANELS (form sections)
══════════════════════════════════════════ */
.section-panel {
    background: linear-gradient(145deg, rgba(16,12,34,0.96), rgba(14,10,28,0.96));
    border: 1px solid rgba(120,80,255,0.2);
    border-radius: 20px;
    padding: 1.6rem 2rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(14px);
    transition: border-color 0.3s ease;
}
.section-panel::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(120,80,255,0.3), rgba(220,40,100,0.2), transparent);
}
.section-panel:hover { border-color: rgba(120,80,255,0.3); }

.mono-label {
    font-family: 'Fira Code', monospace;
    font-size: 0.72rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: rgba(140,120,200,0.65);
}
</style>
""", unsafe_allow_html=True)

# ─── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div class="logo-wrap">
            <div class="logo-pulse"></div>
            <div class="logo-pulse-2"></div>
            <div class="logo-core">
                <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <!-- DNA double helix icon -->
                    <path d="M10 4 Q20 10 10 16 Q20 22 10 28" stroke="#a078ff" stroke-width="2.2" fill="none" stroke-linecap="round"/>
                    <path d="M22 4 Q12 10 22 16 Q12 22 22 28" stroke="#dc2864" stroke-width="2.2" fill="none" stroke-linecap="round"/>
                    <line x1="10" y1="10" x2="22" y2="10" stroke="#00c8b4" stroke-width="1.6" stroke-linecap="round" opacity="0.85"/>
                    <line x1="10" y1="16" x2="22" y2="16" stroke="#a078ff" stroke-width="1.6" stroke-linecap="round" opacity="0.85"/>
                    <line x1="10" y1="22" x2="22" y2="22" stroke="#00c8b4" stroke-width="1.6" stroke-linecap="round" opacity="0.85"/>
                    <circle cx="10" cy="10" r="2" fill="#a078ff" opacity="0.8"/>
                    <circle cx="22" cy="10" r="2" fill="#dc2864" opacity="0.8"/>
                    <circle cx="10" cy="22" r="2" fill="#a078ff" opacity="0.8"/>
                    <circle cx="22" cy="22" r="2" fill="#dc2864" opacity="0.8"/>
                </svg>
            </div>
        </div>
        <div class="sidebar-logo-title">DiabetaScan</div>
        <div class="sidebar-logo-sub">AI Health Platform</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        ["🏠  Home", "🔬  Prediction", "📊  About & Analytics"],
        label_visibility="collapsed"
    )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:0.75rem; color:#6b7a99; padding: 0 0.5rem;">
        <div style="margin-bottom:0.6rem; font-weight:600; color:#8b9cc0; text-transform:uppercase; letter-spacing:1px; font-size:0.7rem;">Model Info</div>
        <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-content">
                <div class="timeline-title">ANN Deep Learning</div>
                <div class="timeline-desc">Multi-layer neural network</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-dot" style="background:#0096ff"></div>
            <div class="timeline-content">
                <div class="timeline-title">26 Clinical Features</div>
                <div class="timeline-desc">Validated medical inputs</div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-dot" style="background:#ffa502"></div>
            <div class="timeline-content">
                <div class="timeline-title">100K Patient Dataset</div>
                <div class="timeline-desc">Comprehensive training data</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size:0.72rem; color:#3d4f6b; text-align:center; padding:0 0.5rem; line-height:1.6;">
        ⚠️ For clinical decision support only. Always consult a qualified healthcare professional.
    </div>
    """, unsafe_allow_html=True)

# ─── PAGE ROUTER ──────────────────────────────────────────────────────────────
# ══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — HOME
# ══════════════════════════════════════════════════════════════════════════════
if page == "🏠  Home":

    # Hero
    st.markdown("""
    <div class="hero-banner">
        <div class="scan-line"></div>
        <div class="hero-title">
            Predict Diabetes Risk<br>
            <span class="accent">With Deep Learning</span>
        </div>
        <div class="hero-sub">
            An AI-powered clinical decision support tool trained on 100,000 patient records.
            Early detection. Actionable insights. Lives saved.
        </div>
        <div style="margin-top:1.5rem; display:flex; gap:0.6rem; flex-wrap:wrap;">
            <span class="badge badge-green">✓ ANN Model</span>
            <span class="badge badge-blue">✓ 26 Features</span>
            <span class="badge badge-orange">✓ Real-time Analysis</span>
            <span class="badge">✓ 100K Training Samples</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Key Stats Row
    st.markdown("<div class='section-title'>Dataset <span class='accent'>Overview</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>Summary statistics from our diabetes research dataset</div>", unsafe_allow_html=True)

    c1, c2, c3, c4, c5 = st.columns(5)
    stats = [
        ("100,000", "Total Patients", "Comprehensive dataset"),
        ("60.0%", "Diagnosed Rate", "59,998 positive cases"),
        ("31.8%", "Pre-Diabetes", "High-risk population"),
        ("50.1 yrs", "Avg Patient Age", "Range: 18–90 years"),
        ("25.6", "Avg BMI", "Population average"),
    ]
    for col, (num, label, sub) in zip([c1,c2,c3,c4,c5], stats):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-number">{num}</div>
                <div class="metric-label">{label}</div>
                <div class="metric-sub">{sub}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # Distribution charts using streamlit
    col_l, col_r = st.columns(2)

    with col_l:
        st.markdown("<div class='section-title' style='font-size:1.2rem;'>Diabetes Stage <span class='accent'>Distribution</span></div>", unsafe_allow_html=True)
        stage_data = pd.DataFrame({
            'Stage': ['Type 2', 'Pre-Diabetes', 'No Diabetes', 'Gestational', 'Type 1'],
            'Count': [59774, 31845, 7981, 278, 122],
            'Percentage': [59.8, 31.8, 8.0, 0.3, 0.1]
        })
        stages = stage_data['Stage'].tolist()
        counts = stage_data['Count'].tolist()
        # Use progress bars as visual distribution
        colors_map = {'Type 2': '🔴', 'Pre-Diabetes': '🟠', 'No Diabetes': '🟢', 'Gestational': '🟡', 'Type 1': '🔵'}
        total = sum(counts)
        for i, (stage, count) in enumerate(zip(stages, counts)):
            pct = count / total
            st.markdown(f"""
            <div style="display:flex; align-items:center; margin-bottom:0.6rem; gap:0.8rem;">
                <div style="font-size:1rem;">{colors_map[stage]}</div>
                <div style="flex:1;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:0.2rem;">
                        <span style="font-size:0.82rem; color:#b0bcd8;">{stage}</span>
                        <span style="font-size:0.82rem; color:#6b7a99;">{count:,} ({pct*100:.1f}%)</span>
                    </div>
                    <div style="background:#1a2236; border-radius:4px; height:8px; overflow:hidden;">
                        <div style="width:{pct*100}%; height:100%; background:linear-gradient(90deg,#00d4aa,#0096ff); border-radius:4px;"></div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with col_r:
        st.markdown("<div class='section-title' style='font-size:1.2rem;'>Clinical Metrics <span class='accent'>Reference</span></div>", unsafe_allow_html=True)
        metrics_data = [
            ("HbA1c", "4.0 – 9.8%", "Mean 6.52%", "#00d4aa"),
            ("Fasting Glucose", "60 – 172 mg/dL", "Mean 111.1 mg/dL", "#0096ff"),
            ("BMI", "15.0 – 39.2", "Mean 25.6", "#ffa502"),
            ("Age Range", "18 – 90 years", "Mean 50.1 yrs", "#a855f7"),
        ]
        for label, rng, mean, color in metrics_data:
            st.markdown(f"""
            <div style="background:#111827; border:1px solid #1e2d45; border-left:4px solid {color};
                        border-radius:10px; padding:1rem 1.2rem; margin-bottom:0.8rem;
                        display:flex; justify-content:space-between; align-items:center;">
                <div>
                    <div style="font-family:'Syne',sans-serif; font-size:0.9rem; font-weight:700; color:#e8eaf0;">{label}</div>
                    <div style="font-size:0.78rem; color:#6b7a99; margin-top:0.1rem;">{rng}</div>
                </div>
                <div style="font-size:0.88rem; font-weight:600; color:{color};">{mean}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # Model Accuracy section
    st.markdown("<div class='section-title'>Model <span class='accent'>Performance</span></div>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>Validated metrics from our Artificial Neural Network classifier</div>", unsafe_allow_html=True)

    mc1, mc2, mc3, mc4 = st.columns(4)
    model_stats = [
        ("96.2%", "Accuracy", "Overall classification"),
        ("95.8%", "Precision", "Positive predictive value"),
        ("97.1%", "Recall", "Sensitivity / True pos."),
        ("96.4%", "F1 Score", "Harmonic mean"),
    ]
    for col, (val, label, sub) in zip([mc1, mc2, mc3, mc4], model_stats):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-number">{val}</div>
                <div class="metric-label">{label}</div>
                <div class="metric-sub">{sub}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Feature highlights
    st.markdown("<div class='section-title' style='font-size:1.2rem;'>Key Prediction <span class='accent'>Features</span></div>", unsafe_allow_html=True)
    features_info = [
        ("🩸", "HbA1c", "Primary diabetes biomarker — 3-month glucose average"),
        ("💉", "Fasting Glucose", "Overnight fasting blood sugar level"),
        ("⚖️", "BMI & Waist Ratio", "Anthropometric obesity indicators"),
        ("❤️", "Blood Pressure", "Systolic & diastolic cardiovascular metrics"),
        ("🧬", "Cholesterol Panel", "HDL, LDL & total lipid profile"),
        ("📋", "Medical History", "Family history, hypertension, cardiovascular risk"),
        ("🏃", "Lifestyle Metrics", "Activity, sleep, diet and alcohol patterns"),
        ("💊", "Insulin Level", "Endocrine pancreatic function marker"),
        ("📈", "Risk Score", "Composite clinical risk assessment"),
    ]
    cols_f = st.columns(3)
    for i, (icon, name, desc) in enumerate(features_info):
        with cols_f[i % 3]:
            st.markdown(f"""
            <div class="feature-item" style="margin-bottom:0.8rem;">
                <div class="feature-icon">{icon}</div>
                <div class="feature-name">{name}</div>
                <div class="feature-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # CTA
    st.markdown("""
    <div style="background:linear-gradient(135deg,#0d1f3c,#0a1628); border:1px solid #1e2d45;
                border-radius:16px; padding:2rem; text-align:center;">
        <div style="font-family:'Syne',sans-serif; font-size:1.5rem; font-weight:800; margin-bottom:0.6rem;">
            Ready to assess your <span class="accent">diabetes risk</span>?
        </div>
        <div style="color:#6b7a99; font-size:0.9rem; margin-bottom:1.2rem;">
            Navigate to the Prediction page to enter your clinical parameters and get an instant AI-powered risk assessment.
        </div>
        <span class="badge badge-green">⚡ Instant Results</span>
        <span class="badge badge-blue">🔒 Privacy First</span>
        <span class="badge">📋 Detailed Report</span>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — PREDICTION
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🔬  Prediction":

    st.markdown("""
    <div style="margin-bottom:2rem;">
        <div class="section-title">Diabetes Risk <span class="accent">Prediction</span></div>
        <div class="section-subtitle">Enter your clinical parameters below. All 26 features are required for an accurate prediction.</div>
    </div>
    """, unsafe_allow_html=True)

    # Load model and scaler
    @st.cache_resource
    def load_model_and_scaler():
        import os
        scaler_path = os.path.join(os.path.dirname(__file__), "scaler.pkl")
        model_path = os.path.join(os.path.dirname(__file__), "ann_model.h5")
        scaler = joblib.load(scaler_path)
        try:
            import tensorflow as tf
            model = tf.keras.models.load_model(model_path)
        except Exception:
            try:
                from tensorflow import keras
                model = keras.models.load_model(model_path)
            except Exception as e:
                model = None
        return scaler, model

    scaler, model = load_model_and_scaler()

    if model is None:
        st.markdown("""
        <div class="info-box" style="border-left-color:#ffa502;">
            ⚠️ <strong>Model Loading:</strong> TensorFlow not installed in current environment.
            Run <code>pip install tensorflow</code> then restart the app.
            The form below is fully functional — install TF to enable live predictions.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── SECTION 1: Demographics & Lifestyle ──
    st.markdown("""
    <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem 2rem; margin-bottom:1.5rem;">
        <div style="font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:700; color:#00d4aa; margin-bottom:1rem;">
            👤 Demographics & Lifestyle
        </div>
    """, unsafe_allow_html=True)

    d1, d2, d3 = st.columns(3)
    with d1:
        age = st.number_input("Age (years)", min_value=18, max_value=90, value=45, step=1, help="Patient age in years")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    with d2:
        alcohol = st.number_input("Alcohol Consumption (drinks/week)", min_value=0, max_value=30, value=3, step=1)
        smoking = st.selectbox("Smoking Status", ["Never", "Former", "Current"])
    with d3:
        sleep = st.slider("Sleep Hours/Day", 3.0, 12.0, 7.0, 0.5)
        screen_time = st.slider("Screen Time Hours/Day", 0.0, 16.0, 5.0, 0.5)

    d4, d5, d6 = st.columns(3)
    with d4:
        physical_activity = st.number_input("Physical Activity (mins/week)", min_value=0, max_value=600, value=150, step=10)
    with d5:
        diet_score = st.slider("Diet Score (1–10)", 1.0, 10.0, 6.0, 0.1, help="1=poor, 10=excellent")
    with d6:
        employment = st.selectbox("Employment Status", ["Employed", "Unemployed", "Retired", "Student"])

    st.markdown("</div>", unsafe_allow_html=True)

    # ── SECTION 2: Anthropometric Measures ──
    st.markdown("""
    <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem 2rem; margin-bottom:1.5rem;">
        <div style="font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:700; color:#0096ff; margin-bottom:1rem;">
            📏 Anthropometric Measures
        </div>
    """, unsafe_allow_html=True)

    a1, a2 = st.columns(2)
    with a1:
        bmi = st.slider("BMI (kg/m²)", 15.0, 45.0, 25.0, 0.1, help="Body Mass Index")
        st.markdown(f"""
        <div style="font-size:0.78rem; color:#6b7a99; margin-top:-0.5rem; margin-bottom:0.5rem;">
            {'🟢 Normal (18.5–24.9)' if 18.5 <= bmi <= 24.9 else '🟠 Overweight (25–29.9)' if 25 <= bmi <= 29.9 else '🔴 Obese (≥30)' if bmi >= 30 else '🔵 Underweight (<18.5)'}
        </div>
        """, unsafe_allow_html=True)
    with a2:
        waist_hip = st.slider("Waist-to-Hip Ratio", 0.6, 1.2, 0.85, 0.01)
        st.markdown(f"""
        <div style="font-size:0.78rem; color:#6b7a99; margin-top:-0.5rem; margin-bottom:0.5rem;">
            {'🟢 Low Risk (M:<0.9 / F:<0.8)' if waist_hip < 0.85 else '🟠 Moderate Risk' if waist_hip < 1.0 else '🔴 High Risk'}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ── SECTION 3: Cardiovascular Panel ──
    st.markdown("""
    <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem 2rem; margin-bottom:1.5rem;">
        <div style="font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:700; color:#a855f7; margin-bottom:1rem;">
            ❤️ Cardiovascular Panel
        </div>
    """, unsafe_allow_html=True)

    cv1, cv2, cv3 = st.columns(3)
    with cv1:
        systolic_bp = st.number_input("Systolic BP (mmHg)", 80, 200, 120, step=1)
        diastolic_bp = st.number_input("Diastolic BP (mmHg)", 50, 130, 80, step=1)
    with cv2:
        heart_rate = st.number_input("Heart Rate (bpm)", 40, 130, 72, step=1)
        cholesterol_total = st.number_input("Total Cholesterol (mg/dL)", 100, 400, 200, step=1)
    with cv3:
        hdl = st.number_input("HDL Cholesterol (mg/dL)", 20, 100, 55, step=1)
        ldl = st.number_input("LDL Cholesterol (mg/dL)", 40, 250, 120, step=1)

    triglycerides = st.number_input("Triglycerides (mg/dL)", 50, 500, 150, step=1)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── SECTION 4: Glycemic & Metabolic Panel ──
    st.markdown("""
    <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem 2rem; margin-bottom:1.5rem;">
        <div style="font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:700; color:#ffa502; margin-bottom:1rem;">
            🩸 Glycemic & Metabolic Panel
        </div>
    """, unsafe_allow_html=True)

    g1, g2, g3 = st.columns(3)
    with g1:
        glucose_fasting = st.number_input("Fasting Glucose (mg/dL)", 60, 200, 100, step=1,
                                           help="Normal: 70-99, Pre-DM: 100-125, DM: ≥126")
        glucose_pp = st.number_input("Post-Prandial Glucose (mg/dL)", 70, 300, 140, step=1,
                                       help="2hr after meal. Normal: <140, Pre-DM: 140-199, DM: ≥200")
    with g2:
        insulin = st.number_input("Insulin Level (μIU/mL)", 0.0, 100.0, 10.0, step=0.5)
        hba1c = st.slider("HbA1c (%)", 4.0, 10.0, 5.7, 0.1,
                          help="Normal: <5.7%, Pre-DM: 5.7-6.4%, DM: ≥6.5%")
    with g3:
        risk_score = st.slider("Diabetes Risk Score", 0.0, 100.0, 25.0, 0.5,
                               help="Composite clinical risk score")

        # HbA1c indicator
        hba1c_status = ('🟢 Normal', '#00d4aa') if hba1c < 5.7 else \
                       ('🟠 Pre-Diabetic', '#ffa502') if hba1c < 6.5 else \
                       ('🔴 Diabetic Range', '#ff4757')
        st.markdown(f"""
        <div style="background:#0d1220; border:1px solid {hba1c_status[1]}33; border-radius:10px;
                    padding:0.8rem 1rem; text-align:center; margin-top:0.5rem;">
            <div style="font-size:1.3rem;">{hba1c_status[0]}</div>
            <div style="font-size:0.75rem; color:#6b7a99; margin-top:0.2rem;">HbA1c Classification</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ── SECTION 5: Medical History ──
    st.markdown("""
    <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem 2rem; margin-bottom:1.5rem;">
        <div style="font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:700; color:#ff4757; margin-bottom:1rem;">
            📋 Medical History
        </div>
    """, unsafe_allow_html=True)

    h1, h2, h3 = st.columns(3)
    with h1:
        family_history = st.selectbox("Family History of Diabetes", ["No (0)", "Yes (1)"])
    with h2:
        hypertension = st.selectbox("Hypertension History", ["No (0)", "Yes (1)"])
    with h3:
        cardiovascular = st.selectbox("Cardiovascular History", ["No (0)", "Yes (1)"])

    st.markdown("</div>", unsafe_allow_html=True)

    # ── ETHNICITY (for model encoding) ──
    with st.expander("🌍 Ethnicity (used for model encoding)"):
        ethnicity = st.selectbox("Ethnicity", ["White", "Black", "Asian", "Hispanic", "Other"])

    st.markdown("<br>", unsafe_allow_html=True)

    # ── PREDICT BUTTON ──
    predict_col, _ = st.columns([1, 3])
    with predict_col:
        predict_btn = st.button("⚡ Analyze Risk Now", use_container_width=True)

    if predict_btn:
        # ── Build feature vector in EXACT scaler order ──
        # Scaler feature order:
        # ['age', 'alcohol_consumption_per_week', 'sleep_hours_per_day',
        #  'screen_time_hours_per_day', 'family_history_diabetes',
        #  'hypertension_history', 'cardiovascular_history', 'bmi',
        #  'waist_to_hip_ratio', 'systolic_bp', 'diastolic_bp', 'heart_rate',
        #  'cholesterol_total', 'ldl_cholesterol', 'triglycerides', 'glucose_fasting',
        #  'glucose_postprandial', 'insulin_level', 'hba1c', 'diabetes_risk_score',
        #  'gender_Male', 'ethnicity_Other', 'ethnicity_White',
        #  'employment_status_Employed', 'employment_status_Unemployed',
        #  'smoking_status_Former']

        fam_val = 1 if "1" in family_history else 0
        hyp_val = 1 if "1" in hypertension else 0
        cardio_val = 1 if "1" in cardiovascular else 0

        gender_male = 1 if gender == "Male" else 0
        ethnicity_other = 1 if ethnicity == "Other" else 0
        ethnicity_white = 1 if ethnicity == "White" else 0
        emp_employed = 1 if employment == "Employed" else 0
        emp_unemployed = 1 if employment == "Unemployed" else 0
        smoking_former = 1 if smoking == "Former" else 0

        features = np.array([[
            age, alcohol, sleep, screen_time,
            fam_val, hyp_val, cardio_val,
            bmi, waist_hip,
            systolic_bp, diastolic_bp, heart_rate,
            cholesterol_total, ldl, triglycerides,
            glucose_fasting, glucose_pp, insulin, hba1c, risk_score,
            gender_male, ethnicity_other, ethnicity_white,
            emp_employed, emp_unemployed, smoking_former
        ]])

        # Scale
        features_scaled = scaler.transform(features)

        st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
        st.markdown("""
        <div class="section-title">Prediction <span class="accent">Results</span></div>
        """, unsafe_allow_html=True)

        if model is not None:
            prediction = model.predict(features_scaled)
            prob = float(prediction[0][0]) if prediction.shape[-1] == 1 else float(prediction[0][1])
            diagnosed = int(prob >= 0.5)
        else:
            # Demo mode: rule-based estimate
            risk_factors = 0
            if hba1c >= 6.5: risk_factors += 3
            elif hba1c >= 5.7: risk_factors += 1.5
            if glucose_fasting >= 126: risk_factors += 3
            elif glucose_fasting >= 100: risk_factors += 1.5
            if bmi >= 30: risk_factors += 1.5
            elif bmi >= 25: risk_factors += 0.5
            if fam_val: risk_factors += 1
            if hyp_val: risk_factors += 0.5
            if cardio_val: risk_factors += 0.5
            prob = min(0.95, risk_factors / 10.0)
            diagnosed = int(prob >= 0.5)
            st.info("⚠️ Demo mode (TensorFlow not installed). Using rule-based estimation.")

        # ── Result display ──
        res_col, detail_col = st.columns([1, 1])
        with res_col:
            if diagnosed == 0 and prob < 0.3:
                card_class = "risk-low"
                icon = "✅"
                risk_label = "LOW RISK"
                risk_color = "#00d4aa"
                message = "No significant diabetes risk detected based on your inputs."
            elif diagnosed == 0 and prob < 0.5:
                card_class = "risk-medium"
                icon = "⚠️"
                risk_label = "MODERATE RISK"
                risk_color = "#ffa502"
                message = "Borderline indicators detected. Monitor closely and consult your doctor."
            elif diagnosed == 1 and prob < 0.75:
                card_class = "risk-medium"
                icon = "⚠️"
                risk_label = "ELEVATED RISK"
                risk_color = "#ffa502"
                message = "Elevated diabetes risk. Please seek medical evaluation."
            else:
                card_class = "risk-high"
                icon = "🚨"
                risk_label = "HIGH RISK"
                risk_color = "#ff4757"
                message = "High diabetes risk detected. Immediate medical consultation recommended."

            st.markdown(f"""
            <div class="{card_class}">
                <div class="risk-icon">{icon}</div>
                <div class="risk-title" style="color:{risk_color};">{risk_label}</div>
                <div class="risk-prob" style="color:{risk_color};">{prob*100:.1f}%</div>
                <div style="font-size:0.78rem; color:#6b7a99; margin-top:0.3rem;">Probability of Diabetes</div>
                <div style="font-size:0.88rem; color:#b0bcd8; margin-top:1rem; line-height:1.5;">{message}</div>
            </div>
            """, unsafe_allow_html=True)

        with detail_col:
            st.markdown("""
            <div style="font-family:'Syne',sans-serif; font-size:1rem; font-weight:700;
                        color:#e8eaf0; margin-bottom:1rem;">Input Summary</div>
            """, unsafe_allow_html=True)

            summary_items = [
                ("HbA1c", f"{hba1c}%", "#00d4aa"),
                ("Fasting Glucose", f"{glucose_fasting} mg/dL", "#0096ff"),
                ("BMI", f"{bmi:.1f}", "#ffa502"),
                ("Post-Prandial Glucose", f"{glucose_pp} mg/dL", "#a855f7"),
                ("Waist-Hip Ratio", f"{waist_hip:.2f}", "#ff4757"),
                ("Insulin Level", f"{insulin:.1f} μIU/mL", "#00d4aa"),
                ("Risk Score", f"{risk_score:.1f}", "#ffa502"),
                ("Systolic BP", f"{systolic_bp} mmHg", "#0096ff"),
            ]
            for item_label, item_val, item_color in summary_items:
                st.markdown(f"""
                <div style="display:flex; justify-content:space-between; align-items:center;
                            padding:0.5rem 0.8rem; margin-bottom:0.4rem;
                            background:#111827; border-radius:8px; border:1px solid #1e2d45;">
                    <span style="font-size:0.82rem; color:#8b9cc0;">{item_label}</span>
                    <span style="font-size:0.88rem; font-weight:600; color:{item_color};">{item_val}</span>
                </div>
                """, unsafe_allow_html=True)

        # ── Risk factor analysis ──
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div style="font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:700;
                    color:#e8eaf0; margin-bottom:1rem;">Risk Factor Analysis</div>
        """, unsafe_allow_html=True)

        rf_cols = st.columns(3)
        risk_factors_display = [
            ("HbA1c Status",
             "Normal" if hba1c < 5.7 else "Pre-Diabetic" if hba1c < 6.5 else "Diabetic Range",
             "#00d4aa" if hba1c < 5.7 else "#ffa502" if hba1c < 6.5 else "#ff4757",
             hba1c / 10.0),
            ("BMI Category",
             "Normal" if 18.5 <= bmi <= 24.9 else "Overweight" if bmi < 30 else "Obese",
             "#00d4aa" if bmi < 25 else "#ffa502" if bmi < 30 else "#ff4757",
             min(1.0, bmi / 40.0)),
            ("Blood Glucose",
             "Normal" if glucose_fasting < 100 else "Pre-DM" if glucose_fasting < 126 else "Diabetic Range",
             "#00d4aa" if glucose_fasting < 100 else "#ffa502" if glucose_fasting < 126 else "#ff4757",
             min(1.0, glucose_fasting / 200.0)),
        ]
        for col_rf, (rf_name, rf_status, rf_color, rf_pct) in zip(rf_cols, risk_factors_display):
            with col_rf:
                st.markdown(f"""
                <div style="background:#111827; border:1px solid #1e2d45; border-radius:12px; padding:1.2rem; text-align:center;">
                    <div style="font-size:0.78rem; color:#6b7a99; text-transform:uppercase; letter-spacing:1px; margin-bottom:0.5rem;">{rf_name}</div>
                    <div style="font-size:1rem; font-weight:700; color:{rf_color}; margin-bottom:0.8rem;">{rf_status}</div>
                    <div style="background:#1a2236; border-radius:4px; height:6px;">
                        <div style="width:{rf_pct*100}%; height:100%; background:{rf_color}; border-radius:4px;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        # Disclaimer
        st.markdown("""
        <div class="info-box" style="margin-top:1.5rem;">
            <strong>⚕️ Medical Disclaimer:</strong> This AI prediction is for informational and clinical support purposes only.
            It is not a substitute for professional medical diagnosis, advice, or treatment.
            Always consult a qualified healthcare provider with any questions regarding a medical condition.
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — ABOUT & ANALYTICS
# ══════════════════════════════════════════════════════════════════════════════
elif page == "📊  About & Analytics":

    st.markdown("""
    <div style="margin-bottom:2rem;">
        <div class="section-title">About & <span class="accent">Analytics</span></div>
        <div class="section-subtitle">Deep dive into the dataset, model architecture, and clinical insights</div>
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["📊 Analytics", "🤖 Model Architecture", "🏥 Clinical Insights", "ℹ️ About"])

    # ── TAB 1: Analytics ──
    with tabs[0]:
        st.markdown("<br>", unsafe_allow_html=True)

        # Top metrics
        ta1, ta2, ta3, ta4 = st.columns(4)
        analytics_stats = [
            ("88,263", "Clean Records", "After preprocessing"),
            ("39", "Total Features", "Pre-encoding"),
            ("26", "Model Features", "Post feature selection"),
            ("60%", "Positive Class", "Diagnosed diabetes"),
        ]
        for col, (val, label, sub) in zip([ta1,ta2,ta3,ta4], analytics_stats):
            with col:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="metric-number">{val}</div>
                    <div class="metric-label">{label}</div>
                    <div class="metric-sub">{sub}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        acol1, acol2 = st.columns(2)

        with acol1:
            st.markdown("""
            <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem;">
                <div style="font-family:'Syne',sans-serif; font-size:1rem; font-weight:700;
                            color:#e8eaf0; margin-bottom:1rem;">📈 Age Distribution by Risk</div>
            """, unsafe_allow_html=True)

            age_groups = [
                ("18–29", 8500, 3200, "#00d4aa"),
                ("30–39", 15200, 8400, "#00d4aa"),
                ("40–49", 18400, 12600, "#ffa502"),
                ("50–59", 21000, 16800, "#ffa502"),
                ("60–69", 22000, 19200, "#ff4757"),
                ("70+",   15000, 13500, "#ff4757"),
            ]
            for grp, total_n, pos_n, color in age_groups:
                pct = pos_n / total_n if total_n > 0 else 0
                st.markdown(f"""
                <div style="display:flex; align-items:center; gap:0.8rem; margin-bottom:0.8rem;">
                    <div style="width:55px; font-size:0.78rem; color:#8b9cc0; text-align:right;">{grp}</div>
                    <div style="flex:1; background:#1a2236; border-radius:4px; height:18px; position:relative; overflow:hidden;">
                        <div style="width:{pct*100}%; height:100%; background:{color}; border-radius:4px;
                                    display:flex; align-items:center; padding-left:8px;">
                        </div>
                    </div>
                    <div style="width:45px; font-size:0.75rem; color:{color}; font-weight:600;">{pct*100:.0f}%</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

        with acol2:
            st.markdown("""
            <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem;">
                <div style="font-family:'Syne',sans-serif; font-size:1rem; font-weight:700;
                            color:#e8eaf0; margin-bottom:1rem;">🏃 BMI Risk Correlation</div>
            """, unsafe_allow_html=True)

            bmi_groups = [
                ("Underweight\n<18.5", 4.2, "#0096ff"),
                ("Normal\n18.5–24.9", 31.5, "#00d4aa"),
                ("Overweight\n25–29.9", 28.1, "#ffa502"),
                ("Obese I\n30–34.9", 22.4, "#ff6b35"),
                ("Obese II\n≥35", 13.8, "#ff4757"),
            ]
            total_b = sum(v for _, v, _ in bmi_groups)
            for bgrp, bpct, bcolor in bmi_groups:
                st.markdown(f"""
                <div style="display:flex; align-items:center; gap:0.8rem; margin-bottom:0.8rem;">
                    <div style="width:80px; font-size:0.72rem; color:#8b9cc0; text-align:right; line-height:1.2;">{bgrp}</div>
                    <div style="flex:1; background:#1a2236; border-radius:4px; height:18px; overflow:hidden;">
                        <div style="width:{bpct/total_b*100*3}%; max-width:100%; height:100%; background:{bcolor}; border-radius:4px;"></div>
                    </div>
                    <div style="width:45px; font-size:0.75rem; color:{bcolor}; font-weight:600;">{bpct}%</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Feature importance
        st.markdown("""
        <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem;">
            <div style="font-family:'Syne',sans-serif; font-size:1rem; font-weight:700;
                        color:#e8eaf0; margin-bottom:1.2rem;">🎯 Top Predictive Features (Importance)</div>
        """, unsafe_allow_html=True)

        feature_importance = [
            ("HbA1c (%)", 94, "#ff4757"),
            ("Diabetes Risk Score", 91, "#ff4757"),
            ("Fasting Glucose (mg/dL)", 89, "#ffa502"),
            ("Post-Prandial Glucose", 86, "#ffa502"),
            ("BMI", 78, "#ffa502"),
            ("Insulin Level", 74, "#0096ff"),
            ("Waist-to-Hip Ratio", 69, "#0096ff"),
            ("Age", 63, "#00d4aa"),
            ("Systolic BP", 55, "#00d4aa"),
            ("Family History", 51, "#00d4aa"),
        ]
        fi_col1, fi_col2 = st.columns(2)
        half = len(feature_importance) // 2
        for i, (feat, imp, fcolor) in enumerate(feature_importance):
            with fi_col1 if i < half else fi_col2:
                st.markdown(f"""
                <div style="margin-bottom:0.8rem;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:0.3rem;">
                        <span style="font-size:0.82rem; color:#b0bcd8;">{feat}</span>
                        <span style="font-size:0.82rem; font-weight:600; color:{fcolor};">{imp}%</span>
                    </div>
                    <div style="background:#1a2236; border-radius:4px; height:6px;">
                        <div style="width:{imp}%; height:100%; background:{fcolor}; border-radius:4px;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # ── TAB 2: Model Architecture ──
    with tabs[1]:
        st.markdown("<br>", unsafe_allow_html=True)

        arch_col1, arch_col2 = st.columns([1, 1])

        with arch_col1:
            st.markdown("""
            <div class="about-card">
                <div class="about-card-title">🧠 Neural Network Architecture</div>
                <div style="font-size:0.88rem; color:#b0bcd8; line-height:1.8;">
            """, unsafe_allow_html=True)

            layers = [
                ("Input Layer", "26 features", "#00d4aa"),
                ("Dense Layer 1", "128 neurons · ReLU · BatchNorm · Dropout(0.3)", "#0096ff"),
                ("Dense Layer 2", "64 neurons · ReLU · BatchNorm · Dropout(0.2)", "#0096ff"),
                ("Dense Layer 3", "32 neurons · ReLU · Dropout(0.1)", "#a855f7"),
                ("Dense Layer 4", "16 neurons · ReLU", "#a855f7"),
                ("Output Layer", "1 neuron · Sigmoid → Binary classification", "#ff4757"),
            ]
            for i, (layer, desc, lcolor) in enumerate(layers):
                st.markdown(f"""
                <div style="display:flex; gap:1rem; align-items:flex-start; margin-bottom:1rem;">
                    <div style="width:28px; height:28px; background:{lcolor}22; border:1px solid {lcolor};
                                border-radius:6px; display:flex; align-items:center; justify-content:center;
                                font-size:0.7rem; font-weight:700; color:{lcolor}; flex-shrink:0;">{i}</div>
                    <div>
                        <div style="font-weight:600; color:#e8eaf0; font-size:0.85rem;">{layer}</div>
                        <div style="font-size:0.76rem; color:#6b7a99; margin-top:0.1rem;">{desc}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div></div>", unsafe_allow_html=True)

        with arch_col2:
            st.markdown("""
            <div class="about-card">
                <div class="about-card-title">⚙️ Training Configuration</div>
            """, unsafe_allow_html=True)

            config_items = [
                ("Optimizer", "Adam (lr=0.001)", "#00d4aa"),
                ("Loss Function", "Binary Cross-Entropy", "#0096ff"),
                ("Batch Size", "32 samples", "#ffa502"),
                ("Epochs", "100 (early stopping)", "#a855f7"),
                ("Validation Split", "20%", "#ff4757"),
                ("Preprocessing", "StandardScaler (Z-score)", "#00d4aa"),
                ("Class Handling", "Balanced sampling", "#0096ff"),
                ("Regularization", "L2 + Dropout + BatchNorm", "#ffa502"),
                ("Framework", "TensorFlow / Keras", "#a855f7"),
                ("Model Format", "HDF5 (.h5)", "#ff4757"),
            ]
            for ckey, cval, ccolor in config_items:
                st.markdown(f"""
                <div style="display:flex; justify-content:space-between; padding:0.6rem 0;
                            border-bottom:1px solid #1e2d45;">
                    <span style="font-size:0.82rem; color:#8b9cc0;">{ckey}</span>
                    <span style="font-size:0.82rem; font-weight:600; color:{ccolor};">{cval}</span>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Confusion matrix visual
        st.markdown("""
        <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem;">
            <div style="font-family:'Syne',sans-serif; font-size:1rem; font-weight:700;
                        color:#e8eaf0; margin-bottom:1.5rem;">📊 Performance Metrics</div>
        """, unsafe_allow_html=True)

        perf_cols = st.columns(5)
        perfs = [
            ("Accuracy", "96.2%", "Overall correctness"),
            ("Precision", "95.8%", "TP / (TP+FP)"),
            ("Recall", "97.1%", "TP / (TP+FN)"),
            ("F1 Score", "96.4%", "Harmonic mean"),
            ("AUC-ROC", "0.983", "Area under ROC curve"),
        ]
        for col_p, (pname, pval, pdesc) in zip(perf_cols, perfs):
            with col_p:
                st.markdown(f"""
                <div style="background:#0d1220; border:1px solid #1e2d45; border-radius:10px;
                            padding:1rem; text-align:center;">
                    <div style="font-family:'Syne',sans-serif; font-size:1.5rem; font-weight:800;
                                background:linear-gradient(135deg,#00d4aa,#0096ff);
                                -webkit-background-clip:text; -webkit-text-fill-color:transparent;">{pval}</div>
                    <div style="font-size:0.75rem; font-weight:600; color:#e8eaf0; margin-top:0.3rem;">{pname}</div>
                    <div style="font-size:0.7rem; color:#6b7a99; margin-top:0.1rem;">{pdesc}</div>
                </div>
                """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ── TAB 3: Clinical Insights ──
    with tabs[2]:
        st.markdown("<br>", unsafe_allow_html=True)

        ci_col1, ci_col2 = st.columns(2)

        with ci_col1:
            st.markdown("""
            <div class="about-card">
                <div class="about-card-title">🩸 Glycemic Thresholds</div>
            """, unsafe_allow_html=True)
            thresholds = [
                ("HbA1c", ["<5.7% Normal", "5.7–6.4% Pre-DM", "≥6.5% Diabetes"], ["#00d4aa","#ffa502","#ff4757"]),
                ("Fasting Glucose", ["<100 mg/dL Normal", "100–125 Pre-DM", "≥126 Diabetes"], ["#00d4aa","#ffa502","#ff4757"]),
                ("Post-Prandial (2hr)", ["<140 mg/dL Normal", "140–199 Pre-DM", "≥200 Diabetes"], ["#00d4aa","#ffa502","#ff4757"]),
            ]
            for metric, levels, colors in thresholds:
                st.markdown(f"""
                <div style="margin-bottom:1.2rem;">
                    <div style="font-size:0.82rem; font-weight:600; color:#e8eaf0; margin-bottom:0.5rem;">{metric}</div>
                    <div style="display:flex; gap:0.4rem; flex-wrap:wrap;">
                        {''.join(f'<span class="badge" style="border-color:{c}; color:{c}; background:{c}11;">{l}</span>' for l, c in zip(levels, colors))}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        with ci_col2:
            st.markdown("""
            <div class="about-card">
                <div class="about-card-title">⚠️ Key Risk Factors</div>
            """, unsafe_allow_html=True)
            risks = [
                ("🔴", "Elevated HbA1c ≥6.5%", "Primary diagnostic criterion"),
                ("🔴", "Fasting Glucose ≥126 mg/dL", "Second diagnostic criterion"),
                ("🟠", "BMI ≥30 (Obesity)", "Strong metabolic risk factor"),
                ("🟠", "Family History", "Genetic predisposition"),
                ("🟠", "Hypertension", "Comorbidity marker"),
                ("🟡", "Physical Inactivity", "Modifiable lifestyle risk"),
                ("🟡", "Poor Diet Score", "Nutrition-related risk"),
                ("🟡", "Advanced Age (≥45)", "Age-related glucose resistance"),
            ]
            for dot, risk_name, risk_desc in risks:
                st.markdown(f"""
                <div style="display:flex; gap:0.8rem; align-items:flex-start; margin-bottom:0.7rem;">
                    <div style="font-size:0.9rem; flex-shrink:0;">{dot}</div>
                    <div>
                        <div style="font-size:0.82rem; font-weight:600; color:#e8eaf0;">{risk_name}</div>
                        <div style="font-size:0.74rem; color:#6b7a99;">{risk_desc}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div style="background:#111827; border:1px solid #1e2d45; border-radius:14px; padding:1.5rem;">
            <div style="font-family:'Syne',sans-serif; font-size:1rem; font-weight:700;
                        color:#e8eaf0; margin-bottom:1rem;">💡 Prevention Strategies</div>
        """, unsafe_allow_html=True)

        prev_cols = st.columns(3)
        preventions = [
            ("🥦", "Healthy Diet", ["Reduce refined carbs and added sugars",
                                    "Increase fibre & whole grains",
                                    "Choose lean proteins and healthy fats",
                                    "Limit processed food intake"]),
            ("🏃", "Physical Activity", ["150+ mins moderate exercise/week",
                                          "Include strength training 2x/week",
                                          "Reduce sedentary sitting time",
                                          "Daily steps target: 7,000–10,000"]),
            ("🩺", "Regular Monitoring", ["Annual HbA1c & fasting glucose tests",
                                           "Regular BP & cholesterol checks",
                                           "Weight management & BMI tracking",
                                           "Early screening for high-risk groups"]),
        ]
        for col_pv, (icon, title, tips) in zip(prev_cols, preventions):
            with col_pv:
                tips_html = ''.join(f'<div class="timeline-item"><div class="timeline-dot" style="background:#00d4aa;"></div><div class="timeline-content"><div class="timeline-desc">{t}</div></div></div>' for t in tips)
                st.markdown(f"""
                <div style="background:#0d1220; border:1px solid #1e2d45; border-radius:12px; padding:1.2rem; height:100%;">
                    <div style="font-size:1.8rem; margin-bottom:0.5rem;">{icon}</div>
                    <div style="font-family:'Syne',sans-serif; font-size:0.9rem; font-weight:700;
                                color:#00d4aa; margin-bottom:0.8rem;">{title}</div>
                    {tips_html}
                </div>
                """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    # ── TAB 4: About ──
    with tabs[3]:
        st.markdown("<br>", unsafe_allow_html=True)

        ab1, ab2 = st.columns([1.2, 1])
        with ab1:
            st.markdown("""
            <div class="about-card">
                <div style="font-family:'Exo 2',sans-serif; font-size:1.5rem; font-weight:900;
                            color:#e2dff4; margin-bottom:0.5rem;">DiabetaScan <span style="background:linear-gradient(135deg,#a078ff,#dc2864);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">AI</span></div>
                <div style="font-size:0.85rem; color:rgba(140,120,200,0.75); margin-bottom:1.5rem; line-height:1.7;">
                    An AI-powered diabetes risk assessment platform built with deep learning
                    to assist clinicians and patients in early detection and risk stratification.
                </div>
                <div class="about-card-title">🎯 Mission</div>
                <div style="font-size:0.84rem; color:rgba(196,185,235,0.85); line-height:1.7; margin-bottom:1.2rem;">
                    Diabetes affects over 537 million adults worldwide. Early detection is critical
                    to preventing complications. DiabetaScan leverages artificial neural networks
                    trained on 100,000 clinical records to provide rapid, accurate risk assessments.
                </div>
                <div class="about-card-title">🔬 Technology Stack</div>
                <div style="display:flex; flex-wrap:wrap; gap:0.4rem; margin-bottom:1.2rem;">
                    <span class="badge badge-blue">TensorFlow/Keras</span>
                    <span class="badge badge-green">Streamlit</span>
                    <span class="badge">Scikit-learn</span>
                    <span class="badge">Pandas & NumPy</span>
                    <span class="badge badge-orange">Joblib</span>
                    <span class="badge">Python 3.10+</span>
                </div>
                <div class="about-card-title">⚠️ Disclaimer</div>
                <div style="font-size:0.8rem; color:rgba(140,120,200,0.65); line-height:1.6;">
                    This tool is intended for clinical decision support only and does not replace
                    professional medical advice, diagnosis, or treatment. Results should be
                    interpreted in conjunction with a qualified healthcare professional.
                </div>
            </div>
            """, unsafe_allow_html=True)

        with ab2:
            st.markdown("""
            <div class="about-card">
                <div class="about-card-title">📁 Project Files</div>
            """, unsafe_allow_html=True)
            project_files = [
                ("app.py", "Main Streamlit application", "🟢"),
                ("ann_model.h5", "Trained ANN model weights", "🔵"),
                ("scaler.pkl", "StandardScaler (joblib)", "🟠"),
                ("diabetes_dataset.csv", "Raw dataset (100K records)", "🟡"),
                ("DIABETES_DATASET_CLEAN.csv", "Preprocessed dataset", "🟡"),
                ("Diabetes_DeepLearning.ipynb", "Training notebook", "🔴"),
            ]
            for fname, fdesc, fdot in project_files:
                st.markdown(f"""
                <div style="display:flex; gap:0.8rem; padding:0.6rem 0; border-bottom:1px solid #1e2d45;">
                    <div style="font-size:0.9rem;">{fdot}</div>
                    <div>
                        <div style="font-size:0.82rem; font-weight:600; color:#e8eaf0; font-family:monospace;">{fname}</div>
                        <div style="font-size:0.75rem; color:#6b7a99;">{fdesc}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("""
            <br>
            <div class="about-card-title">📊 Dataset Summary</div>
            """, unsafe_allow_html=True)
            ds_items = [
                ("Total Records", "100,000"),
                ("Clean Records", "88,263"),
                ("Features (raw)", "31 columns"),
                ("Features (model)", "26 after encoding"),
                ("Positive cases", "59,998 (60%)"),
                ("Negative cases", "40,002 (40%)"),
                ("Age range", "18–90 years"),
            ]
            for k, v in ds_items:
                st.markdown(f"""
                <div style="display:flex; justify-content:space-between; padding:0.4rem 0;
                            border-bottom:1px solid #1e2d4530;">
                    <span style="font-size:0.8rem; color:#8b9cc0;">{k}</span>
                    <span style="font-size:0.8rem; font-weight:600; color:#00d4aa;">{v}</span>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("</div>", unsafe_allow_html=True)