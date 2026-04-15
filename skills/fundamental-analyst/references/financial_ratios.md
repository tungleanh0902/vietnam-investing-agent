# Financial Ratio Reference — Vietnamese Equity Analysis

## Table of Contents

1. [Profitability Ratios](#1-profitability-ratios)
2. [Growth Metrics](#2-growth-metrics)
3. [Leverage & Solvency Ratios](#3-leverage--solvency-ratios)
4. [Liquidity Ratios](#4-liquidity-ratios)
5. [Efficiency Ratios](#5-efficiency-ratios)
6. [Valuation Ratios](#6-valuation-ratios)
7. [Cash Flow Quality Metrics](#7-cash-flow-quality-metrics)
8. [Banking-Specific Ratios](#8-banking-specific-ratios)
9. [Sector-Specific Benchmarks — Vietnam](#9-sector-specific-benchmarks--vietnam)
10. [DuPont Analysis Framework](#10-dupont-analysis-framework)
11. [Red Flags Checklist](#11-red-flags-checklist)

---

## 1. Profitability Ratios

### Return on Equity (ROE)
- **Formula**: `Net Income / Average Shareholders' Equity`
- **Interpretation**: Measures how effectively management uses equity capital to generate profit.
- **Benchmarks (Vietnam)**:
  - Excellent: > 20%
  - Good: 15-20%
  - Average: 10-15%
  - Below average: < 10%
- **Sector variance**: Banks often have ROE 15-25% (leveraged model); utilities may have 8-12% (asset-heavy, regulated). Always compare within sector.
- **Warning**: High ROE driven primarily by leverage (D/E) rather than margins or asset turnover is fragile.

### Return on Assets (ROA)
- **Formula**: `Net Income / Average Total Assets`
- **Interpretation**: How efficiently the company uses all assets (debt + equity funded) to generate profit.
- **Benchmarks**: 
  - Non-banks: > 8% good, > 12% excellent
  - Banks: > 1.5% good, > 2% excellent (banks are highly leveraged by design)

### Gross Profit Margin
- **Formula**: `(Revenue - COGS) / Revenue × 100`
- **Interpretation**: Pricing power and production efficiency. Rising gross margins over multiple quarters signal either pricing power or improving input costs.
- **Benchmarks (Vietnam by sector)**:
  - Technology (FPT): 35-45%
  - Consumer staples (VNM): 40-48%
  - Retail (MWG): 20-25%
  - Steel/Materials (HPG): 10-20% (highly cyclical)
  - Chemicals (DPM): 20-35% (commodity dependent)

### Net Profit Margin
- **Formula**: `Net Income / Revenue × 100`
- **Interpretation**: Bottom-line profitability after all expenses, interest, taxes.
- **Look for**: Stability and expansion over time. Volatile margins = commodity or cyclical exposure.

### EBITDA Margin
- **Formula**: `EBITDA / Revenue × 100`
- **Interpretation**: Operating profitability before capital structure and accounting decisions. Useful for comparing companies with different depreciation policies.

---

## 2. Growth Metrics

### Revenue Growth (YoY)
- **Formula**: `(Revenue_current - Revenue_prior_year) / Revenue_prior_year × 100`
- **Key insight**: Revenue growth is the most fundamental growth metric. Everything else can be engineered (cost-cutting, asset sales, accounting), but sustainable revenue growth requires real demand.
- **What to look for**:
  - Acceleration: Q4 rev growth > Q3 rev growth > Q2 rev growth → strongest signal
  - Deceleration: Declining growth rates → potential mean-reversion, market may not have priced in yet
  - Base effects: Always check if high growth is just recovery from a low base (e.g., post-COVID)

### EPS Growth (YoY)
- **Formula**: `(EPS_current - EPS_prior_year) / EPS_prior_year × 100`
- **Warning**: EPS can grow via share buybacks or one-off items even with flat/declining revenue. Always cross-check with revenue growth.
- **Quality filter**: EPS growth should be < 2× revenue growth (unless margin expansion is structural). EPS growing 50% with flat revenue is a red flag.

### Book Value Per Share Growth
- **Formula**: `(BVPS_current - BVPS_prior_year) / BVPS_prior_year × 100`
- **Use**: Especially relevant for banks and real estate companies where book value drives valuation (P/B model).

---

## 3. Leverage & Solvency Ratios

### Debt-to-Equity (D/E)
- **Formula**: `Total Liabilities / Shareholders' Equity`
- **Benchmarks (Vietnam, non-banks)**:
  - Conservative: < 0.5
  - Moderate: 0.5-1.5
  - Aggressive: 1.5-3.0
  - Dangerous: > 3.0
- **Sector exceptions**: Real estate developers commonly run 1.5-2.5x D/E; industrial companies 0.5-1.0x. Banks are excluded (see banking ratios).

### Net Debt / EBITDA
- **Formula**: `(Total Debt - Cash & Equivalents) / EBITDA`
- **Interpretation**: How many years of EBITDA to repay net debt. A company-level leverage metric that accounts for cash position.
- **Benchmarks**:
  - Comfortable: < 2x
  - Acceptable: 2-3x
  - Elevated: 3-5x
  - Distress zone: > 5x

### Interest Coverage Ratio (ICR)
- **Formula**: `EBIT / Interest Expense`
- **Interpretation**: Can the company service its debt from operating earnings?
- **Benchmarks**:
  - Strong: > 5x
  - Adequate: 3-5x
  - Concerning: 1.5-3x
  - Distress: < 1.5x (debt service at risk)

---

## 4. Liquidity Ratios

### Current Ratio
- **Formula**: `Current Assets / Current Liabilities`
- **Benchmarks**:
  - Healthy: 1.2-2.0
  - OK: 1.0-1.2 (but watch the trend)
  - Stressed: < 1.0 (may have difficulty meeting short-term obligations)
  - Too high: > 3.0 (potentially inefficient use of capital)
- **Exclude banks** (they naturally have low current ratios due to maturity transformation).

### Quick Ratio (Acid Test)
- **Formula**: `(Current Assets - Inventory) / Current Liabilities`
- **Why it matters**: Inventory may not be easily liquidated (especially for real estate companies with unsold apartments). The quick ratio gives a more conservative liquidity picture.

---

## 5. Efficiency Ratios

### Asset Turnover
- **Formula**: `Revenue / Average Total Assets`
- **Interpretation**: Revenue generated per unit of assets. Higher = more efficient use of capital base.
- **Sector variance**: Retail (MWG) may have turnover > 2x; Real estate (VHM) may be < 0.3x. Compare within sector only.

### Inventory Turnover
- **Formula**: `COGS / Average Inventory`
- **Days Inventory Outstanding (DIO)**: `365 / Inventory Turnover`
- **What to watch**: Rising inventory days can signal demand weakness or overproduction. Especially critical for:
  - Real estate developers: Unsold inventory = cash trap
  - Retail: Obsolescence risk
  - Steel/materials: Commodity price exposure

### Receivable Turnover
- **Formula**: `Revenue / Average Accounts Receivable`
- **Days Sales Outstanding (DSO)**: `365 / Receivable Turnover`
- **Red flag**: DSO rising faster than revenue growth → customers taking longer to pay → potential credit quality issue or revenue recognition aggressiveness.

### Cash Conversion Cycle (CCC)
- **Formula**: `DIO + DSO - DPO` (Days Payable Outstanding)
- **Interpretation**: How many days it takes to convert inventory investment into cash. Shorter is better.
- A negative CCC (e.g., retail companies like MWG collect from customers before paying suppliers) is a sign of strong bargaining power.

---

## 6. Valuation Ratios

### Price-to-Earnings (P/E)
- **Trailing P/E**: `Current Price / TTM EPS`
- **Forward P/E**: `Current Price / Estimated Next-12M EPS`
- **Vietnam VN-Index historical P/E ranges**:
  - Cheap: < 10x (crisis levels, e.g., Q4 2022)
  - Fair: 12-15x (long-term average)
  - Expensive: > 17x (peak optimism)
- **Sector P/E ranges (Vietnam averages)**:
  - Banks: 8-12x
  - Real Estate: 8-15x (highly volatile)
  - Consumer/Retail: 15-25x
  - Technology (FPT): 14-20x
  - Materials: 6-10x (cyclical, use forward)
  - Utilities: 10-14x

### PEG Ratio
- **Formula**: `P/E / EPS Growth Rate (%)`
- **Interpretation**: P/E adjusted for growth. Normalizes comparison between fast-growers and slow-growers.
  - PEG < 0.8: Potentially undervalued relative to growth
  - PEG 0.8-1.2: Fairly valued
  - PEG > 1.5: Expensive even after adjusting for growth
- **Caution**: Only meaningful with positive, sustainable EPS growth. Don't compute PEG for cyclical recovery or one-off growth.

### Price-to-Book (P/B)
- **Formula**: `Current Price / Book Value Per Share`
- **When to use**: P/B is most useful for asset-heavy businesses (banks, real estate, utilities) where book value is a reasonable proxy for intrinsic value.
- **Theoretical fair P/B**: `ROE / (Cost of Equity - Growth Rate)`. A bank with 20% ROE deserves a higher P/B than one with 10% ROE.
- **Vietnam bank P/B ranges**:
  - Premium banks (VCB, TCB): 2.0-3.5x
  - Mid-tier (MBB, ACB): 1.2-2.0x
  - Weak banks (STB, SHB): 0.8-1.2x

### EV/EBITDA
- **Formula**: `(Market Cap + Total Debt - Cash) / EBITDA`
- **When to use**: Capital-intensive businesses (energy, utilities, materials, telecom) where depreciation is a major non-cash expense.
- **Advantage over P/E**: Capital-structure neutral (compares enterprise value to pre-interest earnings).
- **Vietnam benchmarks**:
  - Cheap: < 5x (may signal deep value or structural issues)
  - Fair: 6-10x
  - Expensive: > 12x

### Free Cash Flow Yield
- **Formula**: `Free Cash Flow / Market Cap × 100`
- **FCF**: `Operating Cash Flow - Capital Expenditure`
- **Interpretation**: Cash return the business generates per unit of market value. A "real" yield metric.
  - \> 8%: Deep value territory
  - 5-8%: Attractive
  - 3-5%: Fair
  - < 3%: Expensive or heavy investment phase

### Dividend Yield
- **Formula**: `Annual Dividend Per Share / Current Price × 100`
- **Vietnam context**: Vietnamese companies have inconsistent dividend policies. Some pay in cash, some in stock dividends (which dilute rather than reward shareholders). Distinguish between cash and stock dividends. Cash dividend > 3% yield is attractive by Vietnam standards.

---

## 7. Cash Flow Quality Metrics

### OCF / Net Income Ratio
- **Formula**: `Operating Cash Flow / Net Income`
- **Interpretation**: Are reported earnings backed by actual cash generation?
  - \> 1.0: Excellent — cash generation exceeds reported profit
  - 0.8-1.0: Good — normal accrual differences
  - 0.5-0.8: Caution — significant gap between paper profits and cash
  - < 0.5: Red flag — earnings may be of low quality (accrual manipulation, aggressive revenue recognition)
- **Structural exceptions**: High-growth companies investing heavily (negative working capital changes) may have temporarily low ratios.

### Capex / Revenue
- **Formula**: `Capital Expenditure / Revenue × 100`
- **Interpretation**: Investment intensity. Context-dependent:
  - High capex (>15% of revenue) in growth phase: Potentially positive (investing for future)
  - High capex with declining ROE: Negative (diminishing returns on investment)
  - Low capex (<5%): Maintenance mode — low growth but high FCF

### Free Cash Flow Conversion
- **Formula**: `FCF / Net Income`
- **Interpretation**: How much of reported earnings converts to distributable cash after reinvestment needs.
  - \> 0.7: Strong conversion — company can fund growth and return cash
  - 0.3-0.7: Moderate — significant reinvestment needs
  - < 0.3: Low — most earnings are re-invested, limited shareholder return capacity

---

## 8. Banking-Specific Ratios

Vietnamese banks require a separate analytical framework because their balance sheets are fundamentally different from non-financial companies.

### Capital Adequacy Ratio (CAR)
- **Formula**: `(Tier 1 Capital + Tier 2 Capital) / Risk-Weighted Assets`
- **Regulatory minimum**: 8% (Basel II). Banks implementing Basel III target higher.
- **Benchmarks**:
  - Strong: > 12%
  - Adequate: 9-12%
  - Tight: 8-9% (limited room for growth)
  - Non-compliant: < 8% (regulatory action)

### Non-Performing Loan (NPL) Ratio
- **Formula**: `Non-Performing Loans / Total Loans`
- **Benchmarks**:
  - Excellent: < 1%
  - Good: 1-2%
  - Concerning: 2-3%
  - Danger: > 3%
- **Vietnam caveat**: The reported NPL ratio may understate true credit risk because:
  - VAMC bonds (bad debts sold to Vietnam Asset Management Company) sit off-balance-sheet
  - Restructured/rescheduled loans may not be classified as NPL
  - Always check the "Gross NPL" including VAMC bonds and restructured loans

### Net Interest Margin (NIM)
- **Formula**: `(Interest Income - Interest Expense) / Average Earning Assets`
- **Interpretation**: The bank's "gross margin" — spread between lending and funding.
- **Vietnam benchmarks**:
  - Strong: > 4% (typically retail-focused banks: TCB, VPB, MBB)
  - Average: 3-4%
  - Low: < 3% (SOE banks with policy lending: BID, CTG)

### Provision Coverage Ratio
- **Formula**: `Loan Loss Provisions / Non-Performing Loans × 100`
- **Interpretation**: How well-reserved is the bank against potential loan losses?
  - \> 150%: Strong buffer (VCB often > 300%)
  - 80-150%: Adequate
  - < 80%: Underprovided — earnings at risk if NPLs materialize

### Cost-to-Income Ratio (CIR)
- **Formula**: `Operating Expenses / Total Operating Income × 100`
- **Interpretation**: Operational efficiency.
  - Efficient: < 40%
  - Average: 40-50%
  - Inefficient: > 50%

### CASA Ratio
- **Formula**: `Current Account + Savings Account (demand deposits) / Total Deposits × 100`
- **Interpretation**: Higher CASA = cheaper funding cost = better NIM sustainability.
  - Excellent: > 35% (TCB, MBB lead in Vietnam)
  - Good: 25-35%
  - Low: < 20% (reliant on expensive term deposits)

---

## 9. Sector-Specific Benchmarks — Vietnam

These are approximate ranges based on historical data (2020-2025). Use for relative comparison, not absolute cutoffs.

| Metric | Banks | Real Estate | Materials | Consumer | Tech | Energy | Utilities |
|--------|-------|-------------|-----------|----------|------|--------|-----------|
| **ROE** | 15-25% | 8-18% | 10-20% | 15-30% | 18-28% | 10-18% | 8-14% |
| **P/E** | 8-12x | 8-15x | 6-10x | 15-25x | 14-20x | 8-12x | 10-14x |
| **P/B** | 1.0-3.5x | 0.8-2.5x | 0.8-2.0x | 3-8x | 3-6x | 0.8-1.5x | 1.0-2.0x |
| **D/E** | N/A | 1.0-3.0x | 0.3-1.5x | 0.2-0.8x | 0.1-0.5x | 0.5-1.5x | 0.5-2.0x |
| **Gross Margin** | N/A | 25-40% | 10-20% | 30-50% | 35-45% | 15-25% | 20-35% |
| **Div Yield** | 1-3% | 0-2% | 2-5% | 2-4% | 1-2% | 3-6% | 4-8% |

---

## 10. DuPont Analysis Framework

### 10.1 Three-Factor DuPont (Quick View)

Break down ROE into three core drivers:

```
ROE = Net Margin × Asset Turnover × Equity Multiplier

where:
  Net Margin     = Net Income / Revenue          (Profitability)
  Asset Turnover = Revenue / Total Assets        (Efficiency)
  Equity Mult.   = Total Assets / Equity         (Leverage)
```

| High ROE Driven By | Implication | Sustainability |
|--------------------|-------------|---------------|
| High Net Margin | Pricing power, brand moat, cost advantage | High — sustainable competitive advantage |
| High Asset Turnover | Operating efficiency, lean model | Medium — can be competed away |
| High Equity Multiplier | Heavy leverage | Low — fragile in downturns, rate-sensitive |

---

### 10.2 Five-Factor DuPont (CFA L2 Full Decomposition)

Splits the 3-factor Net Margin into two components to reveal **exactly where** profitability is coming from or leaking:

```
ROE = Tax Burden × Interest Burden × EBIT Margin × Asset Turnover × Equity Multiplier

where:
  Tax Burden      = Net Income / EBT              = (1 - effective tax rate)
  Interest Burden = EBT / EBIT                    = 1 - (Interest/EBIT)
  EBIT Margin     = EBIT / Revenue                = Operating profitability
  Asset Turnover  = Revenue / Avg Total Assets    = Capital efficiency
  Equity Mult.    = Avg Total Assets / Avg Equity = Leverage

  → ROE = (NI/EBT) × (EBT/EBIT) × (EBIT/Rev) × (Rev/Assets) × (Assets/Equity)
  → Verify: all intermediate fractions cancel →  NI / Equity = ROE ✓
```

#### Why 5-Factor is Superior

The 3-factor model lumps Tax Burden + Interest Burden into Net Margin, making it impossible to distinguish:
- "ROE fell because operating margins compressed" (competitive pressure)
- "ROE fell because interest expense surged" (over-leveraging)
- "ROE improved because tax rate dropped" (one-off, not sustainable)

The 5-factor model separates these cleanly.

#### Five-Factor Interpretation Table

| Factor | Improving (↑) | Deteriorating (↓) | What to Look For |
|--------|--------------|-------------------|------------------|
| **Tax Burden** (NI/EBT) | Tax rate ↓ → more of EBT kept | Tax rate ↑ or deferred recognition | Check if tax benefit is recurring (permanent) or one-off |
| **Interest Burden** (EBT/EBIT) | Less interest expense → less leveraged | More debt / rising rates → burden rises | Watch debt issuance, interest rate sensitivity |
| **EBIT Margin** (EBIT/Rev) | Operating efficiency ↑, pricing power | Cost increases, competition → margin squeeze | Core operational signal — most important for structural analysis |
| **Asset Turnover** (Rev/Assets) | More revenue per unit of assets | Asset bloat, overinvestment | Improving = lean, efficient model |
| **Equity Multiplier** (Assets/Equity) | — | Rising = more leverage = fragility | High leverage sustainable only if EBIT Margin > cost of debt |

#### Vietnam Application Examples

**VNM (VietnamDairy):**
```
ROE = 0.80 × 0.96 × 16% × 1.6x × 1.3x ≈ 16-18%
  → High Tax Burden (low taxes, ↑)
  → High Interest Burden (minimal debt, ↑)
  → Strong EBIT Margin (brand moat)
  → Moderate turnover (consumer staples)
  → Low leverage (conservative balance sheet)
→ Quality: ALL drivers healthy. ROE is REAL.
```

**Overleveraged RE developer:**
```
ROE = 0.75 × 0.70 × 8% × 0.4x × 5.0x ≈ 8-10%
  → Tax Burden OK
  → Low Interest Burden (high debt cost eating EBT)
  → Low EBIT Margin (land costs / construction delays)
  → Very low turnover (slow asset monetization)
  → Very high leverage (5x!)
→ WARNING: ROE propped up ENTIRELY by leverage. One rate hike or sales slowdown = ROE collapses.
```

**Best combination**: High EBIT Margin + moderate turnover + low leverage + low interest burden = quality compounder (VNM, FPT).

**Worst combination**: Low EBIT margin + low turnover + high leverage + high interest burden = value trap (overleveraged real estate / commodities at cycle bottom).

---

## 11. Red Flags Checklist

These are warning signs that should either **disqualify** a company from your LONG list or significantly reduce conviction:

### Accounting Red Flags
- [ ] Revenue growing but OCF declining for 2+ quarters
- [ ] Large "Other Income" or one-time gains driving earnings
- [ ] Receivables growing significantly faster than revenue
- [ ] Frequent changes in accounting policies or auditor
- [ ] Related-party transactions > 10% of revenue
- [ ] Inventory write-downs in consecutive periods
- [ ] Capitalization of operating expenses (e.g., development costs)

### Governance Red Flags
- [ ] Controlling shareholder pledging shares for personal debt
- [ ] Board members selling shares while issuing bullish guidance
- [ ] Frequent capital raises (dilution) without clear ROI on raised capital
- [ ] Opaque corporate structure with multiple BVI/offshore subsidiaries
- [ ] Delayed financial statement filing (> 90 days after quarter-end)

### Financial Health Red Flags
- [ ] OCF negative for 2+ consecutive quarters
- [ ] D/E > 3x (non-banks) or CAR < 8% (banks)
- [ ] Interest coverage < 1.5x
- [ ] Current ratio < 0.8
- [ ] Declining revenue for 3+ consecutive quarters
- [ ] NPL ratio > 3% (banks) or increasing trend with insufficient provisions

### Market Red Flags
- [ ] Stock price declining while insiders are selling
- [ ] Massive foreign net selling over extended period (3+ months)
- [ ] Trading volume drying up (illiquidity risk)
- [ ] Stock has been halted or placed on warning/restriction list by exchange
