# Leading, Coincident & Lagging Indicators — Deep Reference Guide

## Table of Contents

1. [Why Indicator Timing Matters](#1-why-indicator-timing-matters)
2. [Leading Indicators — Forecasting the Future](#2-leading-indicators)
3. [Coincident Indicators — Confirming the Present](#3-coincident-indicators)
4. [Lagging Indicators — Confirming the Past](#4-lagging-indicators)
5. [Vietnam-Specific Adaptations](#5-vietnam-specific-adaptations)
6. [Scenario Construction Using Indicators](#6-scenario-construction)
7. [Common Pitfalls & False Signals](#7-common-pitfalls)

---

## 1. Why Indicator Timing Matters

Economic indicators don't all move at the same time. The economy is a cascade of events, and different indicators capture different stages of that cascade. The key insight is:

> **Leading indicators → predict. Coincident indicators → confirm. Lagging indicators → validate durability.**

Without this framework, you risk:
- **Acting too late** (only watching GDP, which is backward-looking)
- **False signals** (trusting a single leading indicator without confirmation)
- **Premature reversals** (switching positions before lagging indicators confirm a regime change is real)

### The Timing Cascade

```
Event:     Fed signals rate cuts
           │
           ▼ (immediate)
Leading:   S&P 500 rallies, yield curve steepens, M2 growth expectations rise
           │
           ▼ (3-6 months)
Coincident: GDP growth picks up, IIP accelerates, retail sales strengthen
           │
           ▼ (6-12 months)
Lagging:   Unemployment falls, bank lending rates drop, unit labor costs stabilize
```

### Confidence Scoring

| Configuration | Confidence | Position Sizing |
|---------------|-----------|----------------|
| Leading ↑ + Coincident ↑ + Lagging ↑ | **HIGH** | Full conviction: 80-100% of normal position |
| Leading ↑ + Coincident ↑ + Lagging still ↓ | **MEDIUM-HIGH** | Building position: 60-80% |
| Leading ↑ + Coincident flat + Lagging ↓ | **MEDIUM** | Small position: 30-50% |
| Leading ↑ + Coincident ↓ (divergence!) | **LOW** | Observe only: 0-20% |
| All flat/mixed | **TRANSITION** | Reduce sizing, raise cash to 20-30% |

---

## 2. Leading Indicators

### 2.1 S&P 500 Index

**What it is:** The market-cap weighted index of 500 largest US public companies.

**Why it's leading:** Stock markets aggregate millions of forward-looking bets. When investors in aggregate buy, they're expressing a view that future earnings will grow. The S&P 500 historically leads the US economy by **6-9 months**.

**How to read it:**

| Metric | Signal | Implication |
|--------|--------|-------------|
| 6M rolling return > +10% | Bullish | Expansion likely 6M ahead |
| 6M rolling return -5% to +10% | Neutral | No clear signal |
| 6M rolling return < -15% | Bearish | Recession risk elevated |
| New 52-week highs | Very Bullish | Broad confidence in economy |
| New 52-week lows + VIX > 30 | Very Bearish | Panic selling, flight to safety |

**Vietnam linkage:**
- S&P 500 decline → risk-off → foreign investors sell VN equities (VN-Index correlation ~0.6-0.7 weekly)
- S&P 500 new highs → risk-on → EM allocation increases → VN benefit from passive flows
- Lag: VN-Index typically reacts within 1-2 weeks of major S&P moves

**Traps to avoid:**
- Don't trade VN based on single-day S&P moves — use 6M rolling returns for directional signal
- S&P can rally while EM underperforms (USD strength scenario) — always pair with DXY

### 2.2 US Yield Curve (10Y - 2Y Treasury)

**What it is:** The difference between 10-year and 2-year US Treasury yields.

**Why it's leading:** The yield curve reflects market expectations about future growth AND Fed policy. It's the **single most reliable recession predictor** — yield curve inversions have preceded every US recession since 1955 with only one false signal (1966).

**How to read it:**

| Condition | Signal | Timing |
|-----------|--------|--------|
| Spread > +100bps and steepening | Bullish | Economy healthy, Fed accommodative |
| Spread +50 to +100bps, stable | Neutral | Normal conditions |
| Spread 0 to +50bps, flattening | Caution | Late cycle signal; slowdown possible in 12-18M |
| Spread < 0 (inverted) for 3+ months | Warning | Recession within 12-18 months (historically) |
| Curve UN-INVERTS (goes positive after inversion) | DANGER | **This is when recession typically STARTS** — the un-inversion is the real sell signal |

**Vietnam linkage:**
- US recession → Fed cuts aggressively → DXY weakens → eventually bullish VN (6-12M horizon)
- BUT initially: US recession → global risk-off → EM gets hit first → VN-Index drops 15-30%
- Best strategy: US yield curve inverts → prepare defensive allocation → wait for un-inversion → build cash → deploy into VN when Fed is cutting and DXY falling

**Critical nuance — the "un-inversion" signal:**
```
Phase 1: Curve inverts (10Y < 2Y) — WARNING signal fires
Phase 2: Inversion persists 3-12 months — market often still rallies (trap!)
Phase 3: Curve un-inverts (goes back positive) — recession is STARTING
Phase 4: Fed panic cuts → curve steepens rapidly — PEAK fear, BEGIN accumulating
```

### 2.3 US Building Permits

**What it is:** The number of new residential building permits issued per month.

**Why it's leading:** Construction has a long lead time. A permit today → construction activity 3-6 months later → materials/labor demand → GDP contribution. Permits are also highly sensitive to interest rates, making them an early indicator of rate-sensitivity in the real economy.

**How to read it:**

| Condition | Signal |
|-----------|--------|
| Permits > 1.5M annualized and rising | Bullish — housing demand strong |
| Permits 1.2M-1.5M | Neutral |
| Permits < 1.2M or declining > 10% YoY for 3+ months | Bearish — rate-sensitive slowdown |

**Vietnam linkage:**
- US building permits decline → US construction slowdown → reduced demand for VN wood, furniture, stone exports (VN is a major US furniture exporter)
- Also serves as proxy for global rate sensitivity: if construction is slowing due to high rates everywhere, VN real estate sector also at risk

### 2.4 US Initial Jobless Claims

**What it is:** The number of first-time claims for unemployment insurance, reported weekly.

**Why it's leading:** It's the **most timely** leading indicator (weekly, 5-day lag). When firms start laying off workers, it shows up in initial claims before it appears in the unemployment rate (which is lagging).

**How to read it:**

| 4-Week Moving Average | Signal | Labor Market State |
|-----------------------|--------|--------------------|
| < 220K | Very Bullish | Extremely tight labor market |
| 220K - 250K | Bullish | Healthy |
| 250K - 300K | Caution | Softening |
| 300K - 400K | Bearish | Weakening significantly |
| > 400K | Very Bearish | Labor market in recession |

**Vietnam linkage:**
- US labor weakness → US consumption decline → reduced US import demand → VN export sector hit (US is VN's largest export market)
- Rising claims + Fed holding rates = imminent pivot → position for post-pivot EM rally

### 2.5 M2 Money Supply

**What it is:** Broad measure of the money supply, including cash, checking deposits, savings deposits, money market securities, and other time deposits.

**Why it's leading:** "Money supply leads, asset prices follow." Changes in M2 result in asset price changes 6-12 months later. When central banks inject money → M2 grows → money seeks returns → flows into equities, real estate, commodities.

**How to read it:**

| M2 YoY Growth | US Impact | VN Impact |
|---------------|-----------|-----------|
| > 8% | Very Bullish — liquidity flood | VN M2 > 12% = expansion, asset inflation ahead |
| 4-8% | Bullish — ample liquidity | VN M2 8-12% = moderate, healthy |
| 0-4% | Neutral to Tight | VN M2 < 8% = tightening, equity headwind |
| < 0% (contraction) | Very Bearish — liquidity drain | Never happened in VN — would be crisis signal |

**Vietnam-specific insight:**
- When VN M2 growth **significantly exceeds** nominal GDP growth → excess liquidity → asset inflation (stocks + real estate rally)
- When VN M2 growth **falls below** nominal GDP growth → liquidity crunch → asset deflation risk
- Track via SBV monthly monetary statistics (released ~3 weeks after month-end)

### 2.6 Consumer Confidence

**What it is:** Survey-based measure of how optimistic consumers feel about the economy and their personal finances.

**Why it's leading:** Consumers make spending decisions based on how they FEEL about the future. Falling confidence → reduced discretionary spending → GDP slowdown appears 3-6 months later.

**How to read it:**

**US (Conference Board Index):**

| Level | Signal |
|-------|--------|
| > 120 | Very Optimistic — peak confidence often precedes corrections |
| 100-120 | Healthy Optimism |
| 80-100 | Cautious — consumers pulling back |
| < 80 | Pessimistic — recession-level sentiment |

**Key nuance — Present Situation vs. Expectations:**
- Present Situation sub-index = **coincident** (how people feel NOW)
- Expectations sub-index = **leading** (how people feel about the FUTURE)
- If Expectations plunge while Present Situation holds → trouble ahead
- If Expectations rise while Present Situation is weak → recovery forming

**Vietnam (Nielsen Consumer Confidence):**
- Published quarterly
- Score > 120 = among world's most optimistic consumers
- Declining trend even at high levels = retail sector warning
- Track alongside real retail sales growth for confirmation

---

## 3. Coincident Indicators

### 3.1 Real GDP

**What it is:** Total value of goods and services produced, adjusted for inflation. Published quarterly by GSO.

**Why it's coincident:** GDP measures what ALREADY happened. By the time GDP data is released (1 month lag), the quarter is already over.

**How to use it for confirmation:**
- Compare current GDP direction with what leading indicators predicted 6 months ago
- If leading indicators said "expansion" and GDP confirms → **HIGH confidence in next leading signal**
- If leading indicators said "expansion" but GDP disappoints → possible false signal or supply-side constraint

**Vietnam-specific reading:**
- QoQ acceleration matters more than YoY level (adjusts for seasonal patterns)
- GDP composition shift: Industry & Construction > Services = early/mid cycle; Services > Industry = mid/late cycle
- Compare with ICOR (Incremental Capital-Output Ratio): declining ICOR = improving investment efficiency

### 3.2 Industrial Production Index (IIP)

**What it is:** Monthly measure of output from factories, mines, and utilities.

**Why it's coincident:** IIP directly measures current manufacturing activity. It's the most granular coincident indicator with monthly frequency.

**How to use it:**

| IIP YoY Growth | Signal |
|----------------|--------|
| > 10% | Very Strong — manufacturing boom |
| 6-10% | Strong — healthy expansion |
| 3-6% | Moderate — growth but not spectacular |
| 0-3% | Weak — stagnation/slowdown |
| Negative | Contraction — recession signal |

**Cross-reference with PMI:** IIP should confirm what PMI predicted 1-2 months prior. If PMI > 52 but IIP disappoints → supply constraints or statistical noise.

### 3.3 Personal Income / Retail Sales

**What it is:** Monthly measures of consumer income and spending.

**For Vietnam, use Real Retail Sales Growth** (nominal retail growth minus CPI).

**Key issue to watch:** If nominal retail growth is high (e.g., 10.9%) but real growth is lower (e.g., 7%) → inflation is eating into purchasing power. If real retail growth < GDP growth → consumers are falling behind economic output → unsustainable growth pattern.

### 3.4 Employment / Nonfarm Payrolls

**What it is:** Monthly measure of total employment excluding agriculture.

**Vietnam adaptation:** Direct payroll data is limited. Instead, use:
1. **Formal sector employment growth** (GSO quarterly)
2. **Underemployment rate** (more sensitive than unemployment in VN)
3. **Net enterprise creation** (new enterprises minus dissolved) — a proxy for business confidence
4. **Google Trends for "tuyển dụng" and "việc làm"** — real-time labor market proxy

---

## 4. Lagging Indicators

### 4.1 Average Unemployment Duration

**What it is:** How long, on average, unemployed workers have been looking for work.

**Why it's lagging:** Duration only rises AFTER the recession has been underway for months. It tells you whether the downturn is deepening or stabilizing.

**Use case in VN:** Watch the proportion of people unemployed > 6 months. If this rises → structural unemployment (not cyclical) → recovery will be slower → don't rush into cyclical stocks.

### 4.2 Inventory-to-Sales Ratio

**What it is:** Total business inventories divided by total sales.

**Why it's lagging:** Inventories build up during late expansion (firms over-produced expecting demand), and the correction (production cuts, discounts) happens AFTER demand has already turned.

**Vietnam-specific data sources:**
- Steel/cement inventory reports (VN steel association)
- Listed company quarterly reports (inventory line item)
- Retail inventory surveys (GSO)

**Trading signal:**
- I/S ratio rising for 2+ quarters → firms will cut production → industrial slowdown confirmed → avoid materials/industrials
- I/S ratio falling rapidly → demand outstripping supply → production expansion ahead → accumulate industrial stocks

### 4.3 Bank Lending Rate (Prime Rate)

**What it is:** The actual rate banks charge their most creditworthy customers.

**Why it's lagging:** Banks adjust lending rates 1-3 months AFTER SBV changes policy rates.

**Vietnam-specific reading:**
- If SBV cuts refinancing rate but bank lending rates DON'T fall → transmission is blocked (banks hoarding margin or facing funding cost pressure)
- If lending rates fall FASTER than SBV cuts → banks competing aggressively for loan growth → credit expansion accelerating → bullish for economy but watch for credit quality issues
- The GAP between deposit rates and lending rates (NIM proxy) tells you about bank profitability trends

### 4.4 Unit Labor Cost (ULC)

**What it is:** Labor cost per unit of output = Total Labor Compensation / Total Output.

**Why it's lagging:** Wages are sticky and change slowly. ULC only rises persistently AFTER the economy has been growing long enough to create labor shortage.

**Vietnam calculation:** Average wage growth (GSO monthly) ÷ Labor productivity growth (GSO derived)

| ULC Trend | Signal |
|-----------|--------|
| ULC growth < productivity growth | Bullish — competitiveness improving, margins expanding |
| ULC growth = productivity growth | Neutral — stable |
| ULC growth > productivity growth for 3+ quarters | Bearish — cost-push inflation, margin compression |
| ULC growth > 5% sustained | Dangerous — inflationary, equity margins under pressure |

### 4.5 Commercial Loans Outstanding

**What it is:** Total outstanding loans from the banking system to businesses and individuals.

**Why it's lagging:** Credit stock changes slowly. Credit peaks → rates already biting. Credit troughs → economy already bottoming.

**Vietnam-specific reading:**
- YoY credit growth decelerating for 3+ months → tightening cycle CONFIRMED
- YoY credit growth re-accelerating for 3+ months → easing cycle has TAKEN HOLD
- Compare credit growth with SBV ceiling: if credit is well below ceiling → banks or borrowers are cautious → demand weakness (more concerning than supply constraint)

---

## 5. Vietnam-Specific Adaptations

### 5.1 Data Availability Challenges

Many indicators available weekly/monthly in the US are only available quarterly or with significant lag in Vietnam. Workarounds:

| US Indicator | VN Substitute | Frequency | Note |
|-------------|--------------|-----------|------|
| Weekly Initial Claims | GSO monthly employment data | Monthly | Less timely; supplement with Google Trends |
| Conference Board Consumer Confidence | Nielsen VN Consumer Confidence | Quarterly | Supplement with retail sales trends |
| Building Permits | HCMC/Hanoi construction data | Monthly (variable) | Incomplete coverage |
| Nonfarm Payrolls | GSO Labor Survey | Quarterly | Focus on formal sector + enterprise creation |
| ISM PMI | S&P Global Vietnam PMI | Monthly | Good quality; released 1st business day |
| FRED M2 | SBV Monetary Statistics | Monthly | ~3 week lag |

### 5.2 VN-Specific Leading Indicators Not in Textbooks

| Indicator | What It Tells You | Data Source |
|-----------|-------------------|------------|
| SBV Credit Growth Ceiling changes | Most powerful near-term liquidity signal in VN | SBV announcements |
| VN-Index foreign net buy/sell | Foreign sentiment toward VN risk assets | Exchange daily reports |
| VND interbank overnight rate | Real-time banking system liquidity | Bloomberg, SBV |
| Google Trends: "vay mua nhà" | Mortgage demand sentiment | Google Trends |
| Google Trends: "tuyển dụng" | Corporate hiring intentions | Google Trends |
| Gold premium (VN vs. global) | Domestic financial stress | Kitco vs. SJC price |
| New car sales monthly | Consumer big-ticket discretionary spending | VAMA monthly data |

### 5.3 The Vietnam Cycle vs. US Cycle

Vietnam's business cycle has some key differences from the US cycle:

1. **Shorter cycles:** VN cycles tend to be 3-5 years vs. 5-10 years in the US
2. **More policy-driven:** SBV credit ceiling and public investment dominate cycle dynamics more than organic business investment
3. **External shock sensitivity:** Vietnam's open economy (trade/GDP >190%) means global shocks transmit quickly
4. **Seasonal patterns:** H2 fiscal spending acceleration is a calendar effect, not a cycle signal
5. **FDI as cycle driver:** Large FDI commitments can independently create expansion phases in specific regions/sectors

---

## 6. Scenario Construction

### 6.1 The Scenario Framework

Every macro analysis should produce 3 scenarios:

```
SCENARIO = TRIGGER CONDITION + PROBABILITY + TRANSMISSION MECHANISM + PORTFOLIO ACTION
```

### 6.2 Trigger Identification

Use leading indicators to identify scenario triggers:

| If This Happens (Leading) | Then Expect (Coincident, 3-6M later) | Then Confirm (Lagging, 6-12M later) |
|---------------------------|--------------------------------------|-------------------------------------|
| PMI New Orders plunge < 45 | IIP decline, GDP deceleration | Credit growth slowdown, ULC falls |
| M2 growth surges > 15% | Retail sales boom, RE prices rise | Lending rates eventually rise (SBV tightens) |
| US yield curve un-inverts | US GDP contracts, S&P declines | US unemployment rises, Fed cuts |
| DXY breaks above 110 | VND depreciates > 3%, SBV intervenes | FX reserves decline, imported inflation |
| SBV raises credit ceiling significantly | Bank lending accelerates, GDP boost | NPL ratio may rise (watch with 4-6Q lag) |

### 6.3 Probability Assignment

Base probabilities on:
1. **Current trajectory** — If current trends continue, what's the most likely outcome? (Base case: 45-60%)
2. **Positive deviation** — What specific catalyst would make things better? How likely? (Bull: 15-25%)
3. **Negative shock** — What specific risk would make things worse? How likely? (Bear: 15-30%)
4. **Tail risk** — Low probability but extreme impact event? (Black swan: 2-5%)

### 6.4 Action Playbook Template

For each scenario, pre-define:

```
Scenario: [Name]
Probability: [X%]
Trigger: [Specific data point or event]
Monitoring frequency: [Weekly / Monthly / Quarterly]
Next data release to watch: [Date + source]

If triggered:
  Equity allocation: [X% → Y%]
  Sector rotation: [From X → To Y]
  Position sizing: [Full / Reduced / Exit]
  Hedging action: [None / Partial / Full]
  Cash target: [X%]
  Timeline to act: [Immediate / Within 1 week / Over 1 month]
```

---

## 7. Common Pitfalls & False Signals

### 7.1 Over-relying on Single Indicators

**Trap:** "PMI dropped below 50, sell everything!"
**Reality:** A single month's PMI can be noisy (seasonal, one-off events). Require 2+ months of consistent signal AND corroboration from at least one other leading indicator.

### 7.2 Ignoring the Cycle Phase

**Trap:** Seeing strong GDP growth and staying fully invested.
**Reality:** GDP is coincident/lagging. If GDP is strong BUT leading indicators are turning down → you're at LATE EXPANSION → the peak is near → start rotating to defensive.

### 7.3 Fighting the Fed (or SBV)

**Trap:** Being bearish when central bank is aggressively easing.
**Reality:** Monetary policy is the most powerful force. When SBV cuts rates + raises credit ceiling → the liquidity flood will lift asset prices regardless of current fundamentals. "Don't fight the central bank."

### 7.4 The Vietnam "Phantom Recovery"

**Trap:** Leading indicators turn up, but the recovery stalls.
**Reality:** In VN, this sometimes happens because SBV credit ceiling prevented credit transmission. Check that credit growth is ACTUALLY accelerating, not just that rates are lower. Supply of credit (ceiling) AND demand for credit (corporate confidence) must BOTH be present.

### 7.5 Confusing Calendar Effects with Cycle Signals

**Trap:** H2 GDP acceleration interpreted as economic recovery.
**Reality:** Vietnam's fiscal disbursement pattern creates predictable H2 acceleration. Adjust for this by comparing H2 2026 vs. H2 2025, not H2 2026 vs. H1 2026.

### 7.6 DXY Divergence from Fundamentals

**Trap:** DXY strengthening = bearish for VN, always.
**Reality:** Context matters. If DXY strengthens because US economy is booming (growth divergence) → likely net negative for VN (capital outflows). BUT if DXY strengthens because of risk-off flight to safety while US economy also weakens → Fed will cut soon → bearish short-term but bullish medium-term for VN.
