# Valuation Models Reference — CFA L2 Compliant

> **Purpose**: Deep-dive guide for intrinsic valuation (DCF, DDM, FCFF, FCFE, Residual Income), required return estimation (CAPM, WACC, Country Risk Premium), and VND currency forecasting (PPP, IRP, Fisher). These complement the relative valuation tools in `financial_ratios.md`.

## Table of Contents

1. [Required Return Estimation](#1-required-return-estimation)
   - 1.1 Vietnam Equity Risk Premium
   - 1.2 CAPM & Build-Up Method
   - 1.3 Country Risk Premium
   - 1.4 WACC
2. [Dividend Discount Model (DDM)](#2-dividend-discount-model-ddm)
3. [Free Cash Flow Models](#3-free-cash-flow-models)
   - 3.1 FCFF Model
   - 3.2 FCFE Model
   - 3.3 Terminal Value
4. [Residual Income Model (RI)](#4-residual-income-model-ri)
5. [Currency Analysis](#5-currency-analysis)
   - 5.1 Purchasing Power Parity (PPP)
   - 5.2 Interest Rate Parity (IRP)
   - 5.3 Fisher Effect
   - 5.4 VND Practical Forecast
6. [Model Selection Guide](#6-model-selection-guide)
7. [Vietnam-Specific Parameters](#7-vietnam-specific-parameters)

---

## 1. Required Return Estimation

### 1.1 Vietnam Equity Risk Premium (ERP)

**ERP** = excess return investors demand over the risk-free rate for holding equities.

| Component | Vietnam Value | Source / Notes |
|-----------|--------------|----------------|
| US Base ERP | 4.5–5.5% | Damodaran (implied ERP, annually updated) |
| Country Risk Premium (CRP) | 3.0–4.5% | See Section 1.3 |
| **Vietnam Total ERP** | **7.5–10.0%** | Use 8.5% as central estimate |

> **CFA L2 Note**: Always use an *implied* ERP (derived from current market prices) rather than a historical ERP when available. For Vietnam, historical ERP is unreliable due to short market history and structural changes.

---

### 1.2 CAPM & Build-Up Method

#### CAPM (Capital Asset Pricing Model)

```
Ke = Rf + β × (ERP + CRP)

Where:
  Ke  = Cost of Equity (required return)
  Rf  = Risk-Free Rate = VN Government 10-Year Bond yield
  β   = Beta (systematic risk vs VN-Index)
  ERP = US Equity Risk Premium (~5%)
  CRP = Country Risk Premium for Vietnam (~3.5%)
```

**Vietnam-specific parameters:**

| Parameter | Value | Notes |
|-----------|-------|-------|
| Rf (VN 10Y govt bond) | 2.8–3.5% | Check VCB/VietinBank bond markets or Bloomberg |
| Market Beta (vs VN-Index) | Varies — see beta table below | Beta = Cov(stock, VN-Index) / Var(VN-Index) |
| ERP + CRP | 8.5% (central estimate) | Range: 7.5–10% |

**Typical beta ranges (VN market):**

| Sector | Beta Range | Reasoning |
|--------|-----------|-----------|
| Banking (VCB, TCB) | 0.9–1.2 | Correlated with market, leveraged |
| Securities (SSI, VND) | 1.3–1.8 | High beta — amplify market moves |
| Real Estate (VHM) | 1.1–1.5 | Rate-sensitive, cyclical |
| Technology (FPT) | 0.7–1.0 | Quality growth, defensive |
| Energy (GAS, PLX) | 0.8–1.1 | Commodity exposure |
| Utilities (POW, REE) | 0.5–0.8 | Defensive, regulated cash flows |
| Consumer Staples (VNM) | 0.5–0.7 | Defensive, recurring demand |

#### Build-Up Method (alternative to CAPM)

```
Ke = Rf + ERP + CRP + Size Premium + Company-Specific Risk

Where:
  Size Premium  = 1–3% for small/mid-caps (0% for large-cap, e.g., VCB, FPT, VHM)
  Company Risk  = 0–3% for governance, leverage, concentration concerns
```

> **Use Build-Up when** beta estimation is unreliable (low liquidity, short history) or the company is a subsidiary with limited price history.

---

### 1.3 Country Risk Premium (CRP)

**CRP** quantifies the additional return required for investing in Vietnam vs. a mature market (e.g., US).

#### Damodaran Method (Standard)

```
CRP = Sovereign Default Spread × (σEquity / σBond)

Where:
  Sovereign Default Spread = VN sovereign CDS spread or moody's-implied spread
  σEquity / σBond = Ratio of equity market volatility to bond volatility
                  ≈ 1.5 for emerging markets
```

**Practical VN estimates:**

| CDS / Rating | Sovereign Spread | CRP (× 1.5) | When to use |
|---|---|---|---|
| BBB / stable | 1.0–1.5% | 1.5–2.25% | Favorable macro, FTSE upgrade era |
| BB+ / positive watch | 1.5–2.5% | 2.25–3.75% | **Current baseline for VN (2026)** |
| BB / negative watch | 2.5–4.0% | 3.75–6.0% | Stress period (FX crisis, fiscal deficit) |

> **CFA L2 Key**: CRP is subtracted from ERP when computing globally diversified portfolios but is ADDED when computing cost of equity for a purely domestic company. For VN-listed companies: always include CRP in Ke.

---

### 1.4 WACC (Weighted Average Cost of Capital)

```
WACC = Ke × (E/V) + Kd × (1 - t) × (D/V)

Where:
  Ke  = Cost of Equity (from CAPM/build-up)
  Kd  = Pre-tax cost of debt = weighted avg lending rate
  t   = Corporate tax rate (Vietnam = 20%; SOEs may vary)
  E   = Market value of equity
  D   = Book value of interest-bearing debt
  V   = D + E
```

**WACC computation table (example for FPT):**

```
Rf = 3.2% (VN 10Y bond)
β  = 0.85
ERP + CRP = 8.5%
Ke = 3.2% + 0.85 × 8.5% = 10.4%

Kd (pre-tax) = 9.5% (FPT's avg lending rate)
Tax rate (t) = 20%
Kd (after-tax) = 9.5% × (1 - 0.20) = 7.6%

Capital structure: 80% equity, 20% debt
WACC = 10.4% × 0.80 + 7.6% × 0.20 = 9.8%
```

> **Vietnam-specific note**: Use *market value* weights for equity (computed using current share price × shares outstanding). For debt, book value is acceptable since Vietnamese bonds rarely trade at large discounts/premiums.

---

## 2. Dividend Discount Model (DDM)

**Best for**: Dividend-paying stable companies — VNM, SAB, PNJ, utility stocks (REE, POW), mature banks paying consistent cash dividends.

### Gordon Growth Model (Single-Stage)

```
V₀ = D₁ / (Ke - g)

Where:
  V₀ = Intrinsic value today
  D₁ = Expected dividend next year = D₀ × (1 + g)
  Ke = Cost of equity
  g  = Sustainable long-term growth rate = ROE × (1 - payout ratio)
```

**Example — VNM:**
```
D₀ = VND 2,000/share  →  D₁ = 2,000 × 1.06 = 2,120
Ke = 3.2% + 0.6 × 8.5% = 8.3%
g  = ROE × (1 - payout) = 18% × (1 - 0.8) = 3.6%  →  use 6% (long-run VN nominal GDP)
V₀ = 2,120 / (8.3% - 6.0%) = 2,120 / 2.3% = VND 92,174
```

> **Constraint**: g must be < Ke for model to work. If g ≥ Ke, use multi-stage model.
> **Important**: g should not exceed Vietnam's long-run nominal GDP growth (~8-10%). Central estimate: 6-8%.

### H-Model (Two-Stage With Declining Growth)

```
V₀ = D₀ × (1+gₙ) / (Ke - gₙ)  +  D₀ × H × (gₛ - gₙ) / (Ke - gₙ)

Where:
  gₛ = Short-term high growth rate (now)
  gₙ = Long-term sustainable growth rate
  H  = Half-life of high-growth period (years)
```

**Use when**: Company is in a high-growth phase transitioning to mature — e.g., MWG, FPT, ACB with above-average early growth then stabilizing.

### Multi-Stage DDM

```
V₀ = Σ[Dₜ / (1+Ke)^t]  for t=1 to n  +  [Dₙ₊₁ / (Ke - g)] / (1+Ke)^n

Stage 1 (Years 1-3): High-growth dividends  (e.g., 15-25%)
Stage 2 (Years 4-7): Transition              (e.g., 10-15%)
Stage 3 (Year 8+):   Stable payout           (e.g., 6-8% = terminal)
```

---

## 3. Free Cash Flow Models

**Best for**:
- **FCFF**: Capital-intensive companies where capital structure may change (Energy, Real Estate, Industrials)
- **FCFE**: Companies with stable leverage; focus on cash available to equity holders (Technology, Consumer)

### 3.1 FCFF Model (Free Cash Flow to Firm)

```
FCFF = EBIT × (1 - Tax Rate) + D&A - CapEx - ΔNWC

Where:
  EBIT   = Earnings Before Interest and Taxes
  D&A    = Depreciation & Amortization (non-cash, add back)
  CapEx  = Capital Expenditure
  ΔNWC   = Change in Net Working Capital (increase = cash outflow)

Firm Value = Σ[FCFFₜ / (1+WACC)^t] + Terminal Value / (1+WACC)^n
Equity Value = Firm Value - Net Debt
Intrinsic Price = Equity Value / Shares Outstanding
```

**Practical steps for VN companies:**
```
1. Get EBIT from income statement (last 4 quarters)
2. Compute NOPAT = EBIT × (1 - 0.20)
3. Add back D&A from cash flow statement
4. Subtract CapEx from investing activities
5. Compute ΔNWC = (CA - Cash) - (CL - Short-term debt)  [current year - prior year]
6. Project FCFF for 5 years using growth estimate
7. Add terminal value using Gordon model (TV = FCFF × (1+g) / (WACC - g))
8. Discount at WACC
9. Subtract net debt → Equity Value → divide by shares
```

### 3.2 FCFE Model (Free Cash Flow to Equity)

```
FCFE = Net Income + D&A - CapEx - ΔNWC + Net Borrowing

Where:
  Net Borrowing = New debt issued - Debt repaid

Or equivalently:
FCFE = FCFF - Interest × (1 - tax) + Net Borrowing

Equity Value = Σ[FCFEₜ / (1+Ke)^t] + Terminal Value / (1+Ke)^n
```

> **For banks**: Do NOT use FCFE — use Residual Income instead. Bank "capital expenditure" and "working capital" are meaningless concepts for financial institutions.

### 3.3 Terminal Value

```
Gordon Growth Method:
  TV = FCF_n × (1+g) / (WACC - g)    [for FCFF]
  TV = FCF_n × (1+g) / (Ke - g)      [for FCFE]

Exit Multiple Method (cross-check):
  TV = EV/EBITDA_terminal × EBITDA_n  [then divide by (1+WACC)^n]
```

**Vietnam terminal growth assumptions:**

| Scenario | Terminal g | Rationale |
|----------|-----------|-----------|
| Conservative | 5.0% | Below VN nominal GDP, assumes maturation |
| Base | 6.5% | ~VN long-run nominal GDP |
| Optimistic | 8.0% | Structural growth story intact |

> **Sanity check**: Terminal value typically accounts for 60-80% of total DCF value. If Terminal Value / Total Value > 80%, your near-term forecasts are too conservative — review.

---

## 4. Residual Income Model (RI)

**Best for Vietnamese banks**: VCB, TCB, MBB, ACB, VPB, BID, CTG — where FCF is meaningless and dividends are irregular.

**Concept**: A company creates value only when it earns MORE than its cost of equity. Residual Income = "economic profit" above the equity hurdle rate.

### Core Formula

```
Intrinsic Value = Book Value + PV of All Future Residual Incomes

V₀ = BV₀ + Σ[RIₜ / (1+Ke)^t]

Where:
  RIₜ = Net Incomeₜ - (Ke × BV_{t-1})
       = (ROEₜ - Ke) × BV_{t-1}

Interpretation:
  RI > 0: Company earns MORE than cost of equity → creates value → P/B > 1
  RI = 0: Company earns EXACTLY cost of equity → fair value = book value → P/B = 1
  RI < 0: Company DESTROYS value → P/B < 1
```

### Single-Stage RI Model (Banks)

```
V₀ = BV₀ + (ROE - Ke) × BV₀ / (Ke - g)

Simplifies to:
V₀ = BV₀ × [1 + (ROE - Ke) / (Ke - g)]
   = BV₀ × [(Ke - g + ROE - Ke) / (Ke - g)]
   = BV₀ × [(ROE - g) / (Ke - g)]
```

**This is exactly the justified P/B formula:**
```
P/B = (ROE - g) / (Ke - g)

→ A bank with ROE = 20%, g = 8%, Ke = 12%:
  P/B_fair = (20% - 8%) / (12% - 8%) = 12% / 4% = 3.0x

→ A bank with ROE = 12%, g = 6%, Ke = 12%:
  P/B_fair = (12% - 6%) / (12% - 6%) = 1.0x  (barely creating value)
```

### Multi-Stage RI Model (for transition banks)

```
Phase 1 (Years 1-3): High ROE, explicit RI calculation
Phase 2 (Years 4-7): ROE fades toward Ke (premium erodes)
Phase 3 (Year 8+):   RI → 0 (ROE = Ke, P/B = 1.0)

V₀ = BV₀ + Σ[RIₜ / (1+Ke)^t]  +  TV_RI / (1+Ke)^n
```

### Vietnam Bank RI Scorecard

| Bank | ROE (2025) | Ke (est.) | g (est.) | Fair P/B | Current P/B | Assessment |
|------|-----------|-----------|---------|---------|------------|------------|
| VCB | 22% | 12.0% | 8.0% | 3.5x | 2.5-3.0x | Slightly undervalued |
| TCB | 19% | 12.5% | 8.0% | 2.5x | 1.8-2.2x | Undervalued |
| MBB | 20% | 12.5% | 8.0% | 2.9x | 1.5-1.8x | Significantly undervalued |
| ACB | 24% | 12.0% | 7.0% | 3.4x | 1.8-2.2x | Undervalued |
| BID | 14% | 11.0% | 7.0% | 1.75x | 1.0-1.2x | Fairly valued |
| CTG | 13% | 11.0% | 6.5% | 1.44x | 0.9-1.1x | Fairly valued |

> **Warning**: VN bank ROE figures may be overstated due to NPL underreporting (VAMC off-balance-sheet). Apply a 1-3% ROE haircut for banks with known NPL issues.

---

## 5. Currency Analysis

**Why it matters for stock picking**:
- Companies with USD revenue (FPT Software, VHC, ANV) benefit from weaker VND
- Companies with USD-denominated debt (real estate developers, airlines) suffer from weaker VND
- Foreign capital flows are directly influenced by expected VND direction
- SBV FX reserve adequacy determines policy room

### 5.1 Purchasing Power Parity (PPP)

**Law of One Price** extended to aggregate price levels.

#### Absolute PPP

```
S_VND/USD = P_VN / P_US

→ Long-run equilibrium exchange rate based on price level ratio
→ Overly simplistic; useful only as a 10+ year anchor
```

#### Relative PPP (More Useful)

```
% Change in VND/USD ≈ π_VN - π_US

Where:
  π_VN = Vietnam CPI inflation rate
  π_US = US CPI inflation rate

→ If VN inflation = 4.5%, US inflation = 3.0%:
  Expected VND depreciation ≈ 1.5% per year

→ Implication: Vietnam's structurally higher inflation means VND
  tends to depreciate ~1-2% annually in real terms vs USD
```

**VN-specific interpretation:**

| VN-US CPI differential | Expected VND movement | Action |
|------------------------|----------------------|--------|
| < 1% | Broadly stable | Neutral |
| 1–3% | Mild depreciation ~1-2%/yr | Monitor FX reserves |
| 3–5% | Meaningful pressure ~3-4%/yr | Watch SBV interventions |
| > 5% | Significant depreciation risk | Reduce FX-exposed liabilities |

### 5.2 Interest Rate Parity (IRP)

**Covered IRP** (with hedging):
```
F/S = (1 + r_VN) / (1 + r_US)

Where:
  F = Forward VND/USD rate
  S = Spot VND/USD rate
  r_VN = Vietnam 1-year interest rate
  r_US = US 1-year interest rate

→ If VN 1Y rate = 5%, US 1Y rate = 4%:
  F/S = 1.05 / 1.04 = 1.0096
  → Forward VND is 0.96% weaker than spot
```

**Uncovered IRP** (without hedging):
```
Expected % change in VND = r_VN - r_US

→ Investors expect VND to depreciate by exactly the interest rate differential
→ In practice: violated often (carry trade exists when not holding)
→ For VN: VND/USD tends to depreciate by LESS than the full rate differential
  because SBV manages the rate with intervention (±5% trading band)
```

**Current Signal (April 2026):**
```
VN refinancing rate: 4.50%
US Fed funds rate:   3.64% (effective)
Differential:        +86bps → VND should depreciate ~0.86%/year by IRP
DXY at 98.2 (weak dollar) → partially offsets pressure
Net assessment: VND under mild pressure despite favorable DXY
```

### 5.3 International Fisher Effect

```
(1 + r_VN) / (1 + r_US) = (1 + π_VN) / (1 + π_US)

→ Nominal interest rate differentials reflect inflation differentials
→ Implication: VN's higher inflation → higher nominal rates → VND depreciates
→ Real rates should equalize across markets (theory)
→ In practice for VN: real rates often negative → capital flight risk
```

### 5.4 VND Practical Forecast Framework

Combine all three signals plus SBV policy:

```
Step 1: PPP Signal  → VND fair value depreciation = π_VN - π_US = 4.65% - 3.0% = 1.65%/yr
Step 2: IRP Signal  → VND expected move = rate differential = 4.50% - 3.64% = +0.86%
Step 3: DXY Signal  → DXY at 98.2 (below 100) = USD weakness = USD-bull offset → BULLISH VND
Step 4: BoP Signal  → Trade deficit $3.64B Q1 = VND pressure; FDI $5.41B = VND support
                    → Net BoP: FDI disbursement > trade deficit → marginal VND support
Step 5: SBV policy  → Reference rate = 25,103; Market = 26,324-26,329 (near ceiling)
                    → SBV tolerating mild depreciation; no signs of forced intervention

Composite VND Forecast:
  Base: VND depreciates 1.5-2.5% vs USD over next 12 months (gradual, managed)
  Bull: VND flat/slightly stronger if DXY falls to 93-95 + BoP improves
  Bear: VND depreciates 4-6% if oil crisis → CPI spike → trade deficit worsens
```

**VND impact on sectors:**

| VND weakens | Winners | Losers |
|------------|---------|--------|
| USD revenue | FPT (software exports), VHC, ANV, HAG (agri-exports) | — |
| USD costs | — | GAS, PLX (oil imports), airlines, RE developers with USD debt |
| Tourism | ACV, VNA, hotels (USD-priced services in VND terms) | — |
| Neutral | Banks (matched VND book), VNM (domestic), MWG | — |

---

## 6. Model Selection Guide

| Company Type | Best Primary Model | Cross-Check |
|---|---|---|
| **Banks (VCB, TCB, MBB)** | Residual Income (RI) | Justified P/B |
| **Stable dividend payers (VNM, SAB, REE)** | DDM (Gordon or H-model) | EV/EBITDA |
| **Growth companies (FPT, MWG)** | FCFE multi-stage | Forward P/E, PEG |
| **Capital-intensive (GAS, HPG, VHM)** | FCFF | EV/EBITDA |
| **Conglomerates (VIC, MSN)** | Sum-of-the-parts (SOTP) | P/B, EV/EBITDA per division |
| **Cyclicals (DPM, DCM, NKG)** | EV/Normalized EBITDA | P/B at cycle mid-point |
| **SOEs transitioning (BID, CTG)** | RI + justified P/B | Dividend yield |

### The Cross-Check Rule

> **Always cross-check intrinsic value (DCF/DDM/RI) with relative valuation (P/E, P/B, EV/EBITDA). If they diverge significantly (>30%), explain why before taking a position.**

| Intrinsic | Relative | Interpretation |
|-----------|----------|----------------|
| Cheap | Cheap | High conviction LONG |
| Cheap | Expensive | Market applies premium you don't see → verify quality |
| Expensive | Cheap | Relative cheap but no intrinsic value → VALUE TRAP |
| Expensive | Expensive | Clear AVOID / SHORT candidate |

---

## 7. Vietnam-Specific Parameters

### Key Rate Reference Table (Updated April 2026)

| Rate | Value | Source |
|------|-------|--------|
| VN 10Y Government Bond Yield | ~3.2–3.5% | SBV, Bloomberg |
| SBV Refinancing Rate | 4.50% | SBV official |
| Average Lending Rate (commercial) | 10.5–12.0% | SBV banking stats |
| Corporate Tax Rate | 20% | Ministry of Finance |
| VN Equity Risk Premium | ~8.5% | Damodaran + CRP |
| Country Risk Premium (VN) | ~3.0–3.5% | CDS spread × 1.5 |

### Sustainable Growth Rate by Sector (Vietnam)

Computed as: `g = ROE × (1 - Payout Ratio)`

| Sector | ROE | Payout Ratio | g Sustainable |
|--------|-----|-------------|--------------|
| Banking (large) | 20–22% | 20–30% | 14–18% (too high → mean-reverts) |
| Technology (FPT) | 23–25% | 30–35% | 15–18% (reinvests heavily) |
| Consumer Staples (VNM) | 16–18% | 70–80% | 3–5% (matures) |
| Real Estate | 12–18% | 0–20% | 10–15% (lumpy) |
| Utilities | 10–13% | 50–70% | 3–7% (regulated) |
| Materials (HPG) | 12–18% | 20–40% | 8–15% (cyclical) |

> **Cap sustainable g at VN long-run nominal GDP growth (~8-9%) for terminal value computations.** Excess returns erode as competition intensifies.

### Cost of Equity Quick Reference

| Stock | Beta (est.) | Ke = 3.2% + β × 8.5% |
|-------|------------|----------------------|
| VCB | 0.95 | 11.3% |
| TCB | 1.10 | 12.6% |
| MBB | 1.10 | 12.6% |
| FPT | 0.85 | 10.4% |
| VHM | 1.20 | 13.4% |
| HPG | 1.15 | 13.0% |
| GAS | 0.90 | 10.9% |
| SSI | 1.45 | 15.5% |
| VNM | 0.60 | 8.3% |
| REE | 0.70 | 9.2% |
