# VnBondLab Macro Analysis Framework

This guide provides the quantitative framework for macro-financial analysis based on the VnBondLab methodologies (Modules 01–03).
Use this reference to evaluate macroeconomic conditions, classify risk regimes, and adjust portfolio risk.

> **Data Gathering**: Since no free API exists for VN bond yields or interbank rates, use **web search** to find the latest available values. Search for terms like "Vietnam interbank rate", "VN10Y yield", "lợi suất trái phiếu chính phủ Việt Nam", "lãi suất liên ngân hàng", etc. Typical sources include SBV reports, investing.com, Bloomberg, and Vietnamese financial news outlets.

---

## 1. The 4 Interest Rate Pillars

Evaluate these 4 spreads to determine the state of the interest rate environment:

| # | Pillar | Formula | Warning Condition (Flag) | Significance |
|---|--------|---------|--------------------------|--------------|
| 1 | **Liquidity Stress** | Interbank Rate − SBV Policy Rate | > 1.0% | Measures interbank liquidity tightness. Spikes indicate short-term funding stress in the banking system. |
| 2 | **Yield Curve Slope** | VN10Y Yield − VN02Y Yield | < 0% (Inverted) | Measures cycle stage. Inversion warns of cyclical slowdown or severe monetary tightening. |
| 3 | **Sovereign Spread** | VN10Y Yield − US10Y Yield | Rapidly narrowing or < 0% | Evaluates capital flight risk. A narrow or negative spread forces SBV to defend VND via higher rates. |
| 4 | **Policy Spread** | VN10Y Yield − SBV Policy Rate | < 0% | Assesses how tight monetary policy is relative to long-term market expectations. Negative = very tight. |

### Data Sources (TradingView tickers for reference)
- `ECONOMICS:VNINTR` — SBV Policy Rate (Refinancing Rate)
- `ECONOMICS:VNINBR` — Interbank Rate
- `TVC:VN10Y` — Vietnam 10-Year Government Bond Yield
- `TVC:VN02Y` — Vietnam 2-Year Government Bond Yield
- `TVC:US10Y` — US 10-Year Treasury Yield

---

## 2. The 3 Macro Risk Layers

Group the findings from the 4 pillars and other macro data into three risk layers to identify the **root source** of risk:

### Layer 1 — Funding (Short-Term Liquidity)
- **Primary driver**: Pillar 1 (Interbank − Policy Rate spread)
- **Secondary signals**: SBV OMO activity, bank system liquidity
- **High risk means**: Immediate liquidity crunch — banks are scrambling for short-term funds
- **Typical impact**: Securities margin lending tightens → stock market liquidity drops

### Layer 2 — Cycle (Yield Curve & Growth)
- **Primary driver**: Pillar 2 (VN10Y − VN02Y slope)
- **Secondary signals**: GDP growth trend, credit growth pace
- **High risk means**: Structural economic slowdown — the yield curve is pricing in recession or severe tightening
- **Typical impact**: Cyclical sectors (Real Estate, Banks, Industrials) underperform

### Layer 3 — External (Global & FX)
- **Primary driver**: Pillar 3 (VN10Y − US10Y sovereign spread)
- **Secondary signals**: DXY trend, USD/VND exchange rate, Fed policy direction
- **High risk means**: Imported inflation pressure or capital exit risk — SBV may be forced to tighten despite weak domestic conditions
- **Typical impact**: Foreign net selling accelerates, VND depreciation pressure

---

## 3. Risk Bucket System (B0–B4)

Combine the 3 risk layers with overall macro indicators (inflation, GDP) to assign an estimated **Risk Score (0–100%)** and classify into a bucket:

| Bucket | Risk Score Range | Label | Equity Strategy |
|--------|-----------------|-------|-----------------|
| **B0** | 0–20% | Very Low Risk (Ease) | Maximum Offense. Overweight stocks, maximize cyclical exposure. Favor: Banks, Real Estate, Securities. |
| **B1** | 20–40% | Low Risk (Stable) | Risk-On. Overweight cyclicals (Financials, Real Estate, Industrials). Room for leverage. |
| **B2** | 40–60% | Neutral | Balanced. Focus on stock-picking and quality. Sector selection becomes critical. |
| **B3** | 60–80% | High Risk (Tightening) | Risk-Off. Reduce equity exposure, rotate to defensives (Utilities, Healthcare, Consumer Staples). |
| **B4** | 80–100% | Severe Stress (Danger) | Capital preservation. High cash allocation. Entirely defensive positioning. Avoid leverage. |

### How to Estimate Risk Score (without the TradingView indicator)

Since the exact RiskScore requires Pine Script computation, estimate it qualitatively:

1. Count how many of the 4 pillars are flagged (Warning):
   - 0 flagged → likely B0–B1
   - 1 flagged → likely B1–B2
   - 2 flagged → likely B2–B3
   - 3–4 flagged → likely B3–B4

2. Cross-check with:
   - **Inflation state** from Section 4 (heating up → increase risk score)
   - **GDP phase** from Section 5 (slowing → increase risk score)
   - **Macro regime** from SKILL.md Section 2.3 (should be consistent)

---

## 4. Inflation Assessment (MacroAcademic Engine — Module 01)

Go beyond headline CPI. Evaluate these dimensions:

### 4.1 CPI vs Trend
- Is current CPI **accelerating above** its long-term moving average? → Signs of heating up
- Is CPI **falling below** trend? → Signs of cooling down
- Flat near trend → Stable

### 4.2 Inflation Surprise
- **Surprise = Actual CPI − Expected CPI**
- Persistent positive surprises → inflation is running hotter than markets expect → bearish for bonds, mixed for equities
- Persistent negative surprises → inflation is undershooting → potential room for SBV easing → bullish

### 4.3 IDI (Inflation Driver Index) — Cost-Push Pressure
Combines three cost-push factors:
- **PPI (Producer Price Index)**: Rising PPI → production costs increasing → future consumer price pressure
- **FX Depreciation (USD/VND)**: VND weakening → imported inflation (Vietnam imports ~$300B/year)
- **Oil Price Movement**: Rising oil → energy costs, transportation costs → broad price increases

**Interpretation**: High IDI means cost-push inflation pressure is building even if headline CPI hasn't moved yet. This is a **leading indicator**.

### 4.4 Policy Gap (Taylor Rule Approximation)
- **Formula**: `i_implied = r* + π + φπ(π − π*) + φy(GDP_gap)`
- **Policy Gap = Actual Policy Rate − Implied Rate**
- Gap > 0 → SBV is **tighter** than the formula suggests — restrictive
- Gap < 0 → SBV is **looser** than the formula suggests — accommodative
- In practice: if CPI is low and GDP is weak but policy rate is still high → large positive gap → SBV has room to cut

---

## 5. GDP Phase Classification (Module 01 — Panel 3)

Use GDP gap (GDP vs trend) to classify the economic phase:

| Phase | Condition | Implication |
|-------|-----------|-------------|
| **Expanding** | GDP strongly above trend | Pro-cyclical environment, earnings growth accelerating |
| **Stable** | GDP near trend | Neutral, focus on micro fundamentals |
| **Slowing** | GDP below trend | Counter-cyclical risk, earnings downgrades likely |

> **Note**: GDP data is **quarterly** and released with ~1 month lag. Always read GDP in conjunction with higher-frequency indicators (PMI, industrial production, credit growth).

---

## 6. Transition Matrix Logic (Module 02 — Panel 4)

The Transition Matrix tracks how the Risk Bucket changes over time and provides forward-looking context:

### How to Read
- **Stay Probability** (e.g., "B2 stays B2: 65%"): How sticky is the current regime?
- **Up Probability** (risk increases, e.g., B2 → B3): Probability of deterioration
- **Down Probability** (risk decreases, e.g., B2 → B1): Probability of improvement

### Application to Position Sizing (Phase 4 of SKILL.md)

| Transition State | Action |
|-----------------|--------|
| **Sticky** (Stay ≥ 50%) | Current regime is stable. Maintain standard position sizing based on conviction. |
| **Deteriorating** (Up > Down) | Risk is likely increasing. Reduce position sizing by 1 notch. Prepare defensive rotations. |
| **Improving** (Down > Up) | Risk is likely decreasing. Can pre-emptively increase sizing on fundamentally strong stocks. |

### Cross-Validation with Regime
- If qualitative regime says "Goldilocks" but Transition says "Deteriorating" → downgrade confidence
- If qualitative regime says "Stagflation" but Transition says "Improving" → watch for regime shift opportunity

---

## 7. Limitations & Caveats

1. **Data Latency**: VN macro data is inherently lagged (CPI: monthly ~25th; GDP: quarterly ~1 month lag; Interbank: daily but may be 1–2 days delayed in news)
2. **No Real-Time Computation**: Without TradingView, the Risk Score is an **estimate** based on qualitative assessment of the pillars
3. **Historical PCTL**: The TradingView indicators use percentile-ranking against all historical data. Agent estimates without this exact ranking should be conservative
4. **VN-Specific**: These frameworks are calibrated for Vietnam. Do not apply directly to other markets

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────┐
│  VnBondLab Quick Assessment Checklist           │
├─────────────────────────────────────────────────┤
│  1. Find: Interbank Rate, Policy Rate           │
│     → Spread = Interbank − Policy               │
│     → Flag if > 1%                              │
│                                                 │
│  2. Find: VN10Y, VN02Y                          │
│     → Slope = VN10Y − VN02Y                     │
│     → Flag if < 0 (inverted)                    │
│                                                 │
│  3. Find: VN10Y, US10Y                          │
│     → Spread = VN10Y − US10Y                    │
│     → Flag if narrowing rapidly                 │
│                                                 │
│  4. Find: VN10Y, Policy Rate                    │
│     → Spread = VN10Y − Policy                   │
│     → Flag if < 0                               │
│                                                 │
│  5. Count flags → Estimate Bucket B0-B4         │
│  6. Cross-check: CPI trend, GDP phase           │
│  7. Assess Transition: Sticky/Deteriorating/    │
│     Improving                                   │
│  8. Adjust sizing accordingly                   │
└─────────────────────────────────────────────────┘
```
