# Macro Analysis Framework — Detailed Reference

## Table of Contents

1. [Global Macro Scoring Rubric](#1-global-macro-scoring-rubric)
2. [Vietnam Domestic Scoring Rubric](#2-vietnam-domestic-scoring-rubric)
3. [SBV Policy Transmission Mechanism](#3-sbv-policy-transmission-mechanism)
4. [Macro Regime Examples (Historical)](#4-macro-regime-examples-historical)
5. [Geopolitical Risk Scoring](#5-geopolitical-risk-scoring)
6. [Financial Conditions Index Construction](#6-financial-conditions-index-construction)

---

## 1. Global Macro Scoring Rubric

Each factor is scored as **Bullish (+1)**, **Neutral (0)**, or **Bearish (-1)**.
Sum all factor scores to get a **Global Macro Score** (range: -6 to +6).

| Score Range | Interpretation |
|------------|---------------|
| +4 to +6 | Strongly Risk-On — favor cyclicals, growth, EM |
| +1 to +3 | Mildly Risk-On — balanced exposure, slight tilt to risk |
| -1 to +1 | Neutral — no clear directional bias, focus on stock-picking |
| -3 to -1 | Mildly Risk-Off — reduce exposure, raise cash, favor defensives |
| -6 to -3 | Strongly Risk-Off — capital preservation, hedge tail risks |

### Factor Details

#### 1.1 Fed Policy

| Condition | Score | Rationale |
|-----------|-------|-----------|
| Cutting rates or signaling cuts; QT ending/slowing | +1 (Bullish) | Easing financial conditions → capital flows to EM, risk assets rally |
| Holding rates; balanced rhetoric | 0 (Neutral) | Status quo; markets price in current conditions |
| Hiking rates or signaling hikes; accelerating QT | -1 (Bearish) | Tightening conditions → USD strength, EM outflows |

#### 1.2 US Dollar Index (DXY)

| Condition | Score | Rationale |
|-----------|-------|-----------|
| DXY falling (3M downtrend, below 100) | +1 | Weak USD supports EM currencies and commodity prices |
| DXY range-bound (±2% over 3M) | 0 | No directional pressure |
| DXY rising (3M uptrend, above 105) | -1 | Strong USD creates capital outflow pressure on EM |

#### 1.3 Global Risk Appetite (VIX)

| Condition | Score | Rationale |
|-----------|-------|-----------|
| VIX < 15 and falling | +1 | Extreme complacency — risk-on but watch for reversal |
| VIX 15-25 | 0 | Normal range |
| VIX > 25 or spiking > 30% in a week | -1 | Fear regime — de-risking in progress |

#### 1.4 China Economy (PMI)

| Condition | Score | Rationale |
|-----------|-------|-----------|
| Manufacturing PMI > 51, services PMI > 53 | +1 | Chinese expansion → increased Vietnam export orders |
| Manufacturing PMI 49-51 | 0 | Stagnation — no directional impact |
| Manufacturing PMI < 49 for 2+ months | -1 | Chinese contraction → reduced demand for Vietnamese exports |

#### 1.5 Geopolitical Risk

| Condition | Score | Rationale |
|-----------|-------|-----------|
| No major conflicts; trade tensions de-escalating | +1 | Stability supports investment flows |
| Localized tensions; trade friction without escalation | 0 | Market prices in known risks |
| Active conflict near SCS; major trade war escalation; sanctions on Vietnam's trading partners | -1 | Supply chain disruption, energy price shock, sentiment hit |

#### 1.6 Commodity Prices

| Condition | Score | Rationale |
|-----------|-------|-----------|
| Oil stable ($60-80); industrial metals rising; agriculture stable | +1 | Good for Vietnam (manageable input costs + export commodity demand) |
| Mixed commodity picture | 0 | Neutral |
| Oil > $100; steel collapsing; food prices spiking | -1 | Input cost pressure + inflation risk for Vietnam |

---

## 2. Vietnam Domestic Scoring Rubric

Same scoring logic: **Bullish (+1)**, **Neutral (0)**, **Bearish (-1)**.
Sum for **Vietnam Domestic Score** (range: -7 to +7).

### Factor Details

#### 2.1 SBV Policy Stance

| Condition | Score |
|-----------|-------|
| Rate cuts in last 3 months; credit growth ceiling raised; active OMO injection | +1 |
| Rates unchanged for 6+ months; credit growth on track | 0 |
| Rate hikes; credit growth ceiling lowered; tightening liquidity | -1 |

#### 2.2 GDP Growth

| Condition | Score |
|-----------|-------|
| GDP > 7% YoY or accelerating vs. prior quarter | +1 |
| GDP 5.5-7% (on target) | 0 |
| GDP < 5.5% or decelerating for 2+ quarters | -1 |

#### 2.3 CPI / Inflation

| Condition | Score |
|-----------|-------|
| Headline CPI < 3% YoY; core CPI < 2.5% | +1 |
| Headline CPI 3-4.5% | 0 |
| Headline CPI > 4.5% or rising rapidly | -1 |

#### 2.4 Credit Growth

| Condition | Score |
|-----------|-------|
| Credit growth > 12% and below SBV ceiling with room | +1 |
| Credit growth 8-12% | 0 |
| Credit growth < 8% or approaching ceiling | -1 |

#### 2.5 FDI Inflows

| Condition | Score |
|-----------|-------|
| FDI disbursement growing > 10% YoY | +1 |
| FDI flat (±5%) | 0 |
| FDI declining > 10% YoY | -1 |

#### 2.6 VND Stability

| Condition | Score |
|-----------|-------|
| VND/USD stable or appreciating; SBV reserves adequate | +1 |
| VND depreciation < 2% YTD | 0 |
| VND depreciation > 3% YTD; SBV intervening heavily | -1 |

#### 2.7 Public Investment

| Condition | Score |
|-----------|-------|
| Disbursement rate > 50% of plan by mid-year; acceleration vs. prior year | +1 |
| On pace with prior year | 0 |
| Lagging significantly behind plan and prior year | -1 |

### Composite Score Interpretation

| Vietnam Score | Global Score | Overall Assessment |
|--------------|--------------|--------------------|
| +5 to +7 | +4 to +6 | **Maximum Offensive** — Fully invested, leverage OK |
| +3 to +4 | +1 to +3 | **Overweight Equities** — Sector selection matters |
| 0 to +2 | -1 to +1 | **Neutral / Stock-Picking** — Alpha over beta |
| -2 to -1 | -3 to -1 | **Underweight Equities** — Raise cash, hedge |
| -7 to -3 | -6 to -3 | **Defensive Mode** — Cash, bonds, gold |

---

## 3. SBV Policy Transmission Mechanism

Understanding how SBV policy flows through the economy:

```
SBV Rate Decision
    │
    ├──▶ Interbank Rate ──▶ Bank Funding Cost ──▶ Lending Rates
    │                                               │
    │                                               ├──▶ Corporate Borrowing Cost → Capex, Working Capital
    │                                               └──▶ Mortgage Rates → Real Estate Demand
    │
    ├──▶ OMO Operations ──▶ System Liquidity ──▶ Money Market Rates
    │                                               │
    │                                               └──▶ Securities Margin Lending → Stock Market Liquidity
    │
    ├──▶ Credit Growth Ceiling ──▶ Bank Loan Growth Capacity
    │                                │
    │                                ├──▶ Bank Earnings (NII)
    │                                └──▶ Economy-wide Credit Availability
    │
    └──▶ FX Policy ──▶ VND/USD ──▶ Import Costs, Capital Flows
```

**Key Lags**:
- SBV rate → interbank: 1-2 weeks
- Interbank → lending rates: 1-3 months
- Lending rates → real economy: 3-6 months
- Rate change → equity market reaction: Often immediate (anticipatory), but earnings impact lags 2-4 quarters

---

## 4. Macro Regime Examples (Historical)

### Vietnam Goldilocks: H2 2024
- GDP 6.8%, CPI 3.5%, SBV cut rates by 150bps in prior year
- Credit growth recovering, FDI strong (Samsung, LG expansions)
- VN-Index rallied from 1,050 to 1,280 (+22%)
- Leading sectors: Banks (NII recovery), Real Estate (rate-sensitive recovery), FPT (tech FDI beneficiary)

### Vietnam Reflation: 2021-2022
- Post-COVID recovery, GDP rebounding from low base
- Inflation starting to creep up (food, energy)
- Steel and commodity prices surging
- Leading sectors: HPG (steel), Materials, Export-oriented manufacturers

### Global Stagflation Impact on Vietnam: 2022
- Fed hiking aggressively (0% → 5.25%)
- DXY surging above 110
- VND under pressure, SBV forced to tighten
- VN-Index fell from 1,530 to 873 (-43%)
- Worst sectors: Real Estate (NVL, PDR — leverage crisis), Securities
- Relative outperformers: Energy (Gas, PVD), Export earners (VHC)

---

## 5. Geopolitical Risk Scoring

### Risks with Direct Vietnam Impact

| Risk Category | Low (Score 0) | Moderate (Score -0.5) | High (Score -1) |
|--------------|---------------|---------------------|-----------------|
| **US-China Trade War** | Tariffs stable, no escalation | New tariff rounds announced but limited scope | Broad tariffs on Vietnamese re-exports; origin investigations |
| **South China Sea** | Diplomacy ongoing, no incidents | Military exercises, fishing disputes | Active confrontation, shipping route disruption |
| **Energy Supply** | Stable oil $60-80 range | OPEC cuts, Strait of Hormuz tensions | Oil > $100, actual supply disruption |
| **Supply Chain** | Normal operations | Lockdowns in China / key suppliers | Major disruption to Vietnam's input supply chain |
| **US-Vietnam Relations** | GSP/trade agreements advancing | Currency manipulation watchlist | Sanctions, tariffs, trade barriers |

### Geopolitical Alpha Opportunities
Sometimes geopolitical events create **asymmetric opportunities** for Vietnam:
- **US-China decoupling** → "China+1" FDI beneficiary (Vietnam captures redirected manufacturing)
- **EU Green Deal** → Demand for Vietnamese solar panel components, EV battery materials
- **Global food security concerns** → Vietnam rice export premium

---

## 6. Financial Conditions Index Construction

A simplified FCI (Financial Conditions Index) for Vietnam:

### Components and Weights

| Component | Weight | Tightening Signal | Easing Signal |
|-----------|--------|-------------------|---------------|
| SBV Refinancing Rate (vs. trailing 12M avg) | 25% | Above average | Below average |
| Interbank Overnight Rate | 20% | > 4% | < 2% |
| 10Y Government Bond Yield | 15% | Rising trend | Falling trend |
| VND/USD depreciation rate (3M) | 15% | > 2% depreciation | Stable or appreciating |
| Bank Credit Growth (annualized) | 15% | < 8% | > 14% |
| Stock Market Margin Debt (change 3M) | 10% | Declining | Rising |

### FCI Interpretation

| FCI Level | Interpretation | Market Implication |
|-----------|---------------|-------------------|
| < -1 StdDev | Very Loose | Bullish — liquidity tailwind for equities |
| -1 to 0 StdDev | Slightly Loose | Mildly Bullish — favorable conditions |
| 0 to +1 StdDev | Slightly Tight | Neutral to Bearish — headwind building |
| > +1 StdDev | Very Tight | Bearish — liquidity crunch, de-risk |

The FCI is directionally more useful than its absolute level. A rapidly tightening FCI (from -1 to +1 in one quarter) is a strong sell signal even if the absolute level is still "loose" by historical standards.
