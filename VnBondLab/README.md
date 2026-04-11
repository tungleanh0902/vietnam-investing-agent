# VnBondLab - Bộ Công Cụ Nghiên Cứu Thị Trường Việt Nam

## 🎯 Giới thiệu

**VnBondLab** là bộ công cụ phân tích tài chính chuyên sâu cho thị trường Việt Nam, được xây dựng trên TradingView Pine Script v5/v6. Bộ công cụ gồm **5 dự án độc lập**, mỗi dự án có phiên bản gốc và phiên bản **EconAdj** (điều chỉnh tham số kinh tế cho Việt Nam):

- **01_MacroAcademic_Engine**: Phân tích vĩ mô & Risk Score
- **02_Macro_Alert_System**: Hệ thống cảnh báo vĩ mô
- **03_Indices_Research_Map**: Mapping vĩ mô → Thị trường chứng khoán
- **04_YieldCurveLab**: Nghiên cứu đường cong lợi suất trái phiếu
- **05_Bond_Transmission_Monitor**: Giám sát truyền dẫn trái phiếu từ nước ngoài

Mỗi dự án được thiết kế độc lập nhưng có thể sử dụng kết hợp để có góc nhìn đa chiều về thị trường.

---

## 📁 Tổng quan các dự án

### 📊 01_MacroAcademic_Engine
**Dashboard phân tích vĩ mô Việt Nam**

Phiên bản gốc: v2.1 | Phiên bản EconAdj: v2.2 | Tác giả: MacroAcademic

**Mục đích:** Đánh giá sức khỏe kinh tế Việt Nam qua 4 trụ cột chính:
- Lạm phát (Inflation)
- Lãi suất & Thanh khoản (Interest Rates & Liquidity)
- Tăng trưởng (GDP Growth)
- Yếu tố chi phí & ngoại lực (Cost Push & External Forces)

**Kết quả:** Risk Score (0-100%) và Bucket (B0-B4) để xác định mức độ rủi ro vĩ mô

**v2.2 EconAdj — Điều chỉnh kinh tế:**
- Trọng số Risk: Drivers 0.10→0.25, Inflation 0.40→0.30 (phản ánh nền KT mở)
- Taylor Rule: R*=2.5, PHI_Y=0.75 (ưu tiên growth kiểu NHNN)
- IDI weights: FX=0.40 > PPI=0.30 (FX truyền dẫn nhanh nhất)
- GDP trend window: 12→20 quý (giảm bias COVID)
- Credit proxy: IB momentum weight 0.5→0.8

**Sử dụng khi:**
- Bạn cần đánh giá tổng quan về sức khỏe kinh tế
- Bạn muốn timing cho asset allocation (stocks/bonds/cash)
- Bạn cần hiểu bối cảnh vĩ mô trước khi quyết định đầu tư

**File chính:**
- `MacroAcademic_Engine_v2.1_Full.pine` (Bản gốc)
- `MacroAcademic_Engine_v2.2_EconAdj.pine` (Bản điều chỉnh kinh tế)

📖 **Xem chi tiết:** [README MacroAcademic Engine](./01_MacroAcademic_Engine/)

---

### 🔔 02_Macro_Alert_System
**Hệ thống cảnh báo vĩ mô toàn diện**

Phiên bản gốc: v5.0.1 | Phiên bản EconAdj: v5.1 | Tác giả: Macro Research Team

**Mục đích:** Hệ thống cảnh báo rủi ro vĩ mô với phân tích đa trụ cột:
- Căng thẳng thanh khoản (Interbank - Policy Rate)
- Độ dốc đường cong lợi suất (VN10Y - VN02Y)
- Chênh lệch quốc tế (VN10Y - US10Y)
- Spread ngắn-dài (VN10Y - Policy Rate)

**v5.1 EconAdj — Điều chỉnh kinh tế:**
- Thêm 2 pillar mới: Credit proxy (w=1.5) + FX trực tiếp (w=1.0)
- Tổng pillars: 4 → 6 (đa chiều hơn cho risk assessment)

**3 Panel (chọn trong Settings):**

**Panel 1: "Macro — Rates & Spreads"**
- Hiển thị đường biểu đồ: VN10Y (cam), VN02Y (tím), Interbank (xanh lá), SBV Policy (đỏ), US10Y (xanh dương)
- Bảng bên trái hiển thị: giá trị lãi suất, spread, flags (HIGH/OK), chất lượng (Confidence)
- **Cách đọc:** Nếu Interbank vượt xa Policy Rate → thanh khoản căng. Nếu VN10Y < VN02Y → đường cong đảo ngược (cảnh báo)

**Panel 2: "Risk — Dashboard"**
- Đường trắng = **Risk %** (0-100, quan trọng nhất):
  - **0-20 (B0):** Rủi ro rất thấp → tăng tỷ trọng cổ phiếu
  - **20-40 (B1):** Rủi ro thấp → nghiêng về cyclical (Finance, Real Estate)
  - **40-60 (B2):** Trung tính → giữ kỷ luật, hedged
  - **60-80 (B3):** Rủi ro cao → giảm rủi ro, nghiêng defensive
  - **80-100 (B4):** Rủi ro rất cao → ưu tiên tiền mặt/trái phiếu
- 3 đường phụ phân tách nguồn rủi ro:
  - 🔴 **Layer 1 Funding** = căng thẳng thanh khoản ngắn hạn
  - 🟠 **Layer 2 Cycle** = chu kỳ đường cong lợi suất
  - 🔵 **Layer 3 External** = áp lực quốc tế + FX
- Đường bạc = **Policy Pressure** (áp lực lên SBV)
- Đường xanh lá = **Confidence** (độ tin cậy của tín hiệu)
- **Cách đọc:** Xem Risk % hiện tại → xác định Bucket → đối chiếu với Confidence. Nếu Risk > 60 nhưng Confidence < 45 → tín hiệu chưa chắc chắn

**Panel 3: "Equity — Regime & Rotation"**

Panel này gồm **4 khối bảng**, tất cả đều hiển thị dữ liệu **theo bucket hiện tại**:

**Khối 1 — Markets (6 chỉ số):**

| Cột | Ý nghĩa |
|-----|---------|
| Symbol | VNINDEX, VN30, VN100, VNALLSHARE, VNMIDCAP, VNSMALLCAP |
| AvgR20 | Lợi nhuận trung bình sau 20 ngày khi ở bucket này trong quá khứ |
| Win20% | Tỷ lệ có lãi sau 20 ngày |
| AvgDD20 | Drawdown trung bình (mức giảm tối đa) |
| N | Số mẫu lịch sử (dấu `*` = ít mẫu, cần thận trọng) |
| Bias | Chỉ VNINDEX: POS/NEG/FLAT = xu hướng lịch sử ở bucket này |

Ví dụ: Đang ở B1, VNSMALLCAP có AvgR20 = +2.1%, Win = 62%, N = 45 → "Khi risk thấp, smallcap thường tăng 2.1% trong 20 ngày, đúng 62% số lần"

**Khối 2 — VNINDEX Validation (so với baseline):**

| Cột | Ý nghĩa |
|-----|---------|
| H | Horizon: 5D (tuần), 20D (tháng), 60D (quý) |
| CondAvg | Return trung bình khi ở bucket này |
| BaseAvg | Return trung bình trung lập (mọi bucket) |
| **Excess** | = CondAvg - BaseAvg — **số quan trọng nhất!** Dương = bucket này tốt hơn bình thường |
| Stab | STABLE/MIXED/UNSTABLE = kết quả có ổn định không |

Ví dụ: Excess 20D = +0.5%, Stab = STABLE → "Ở bucket này, VNINDEX thường tốt hơn bình thường 0.5%"

**Khối 3 — Sectors Top/Bottom (xếp hạng 11 ngành):**

| Nhãn | Ý nghĩa |
|------|---------|
| T1, T2, T3 | 3 ngành **mạnh nhất** (Leader) — AvgRR20 cao nhất |
| B1, B2, B3 | 3 ngành **yếu nhất** (Lag) — AvgRR20 thấp nhất |
| AvgRR20 | Return vượt trội **so với VNINDEX** (ví dụ: +0.8% = outperform VNINDEX 0.8%) |

→ Ưu tiên mua cổ phiếu thuộc ngành T1-T3, tránh B1-B3

**Khối 4 — Transition Matrix (góc dưới trái):**

| Hàng | Ý nghĩa |
|------|---------|
| Up bucket | Xác suất rủi ro **tăng** (xấu đi) sau 20 ngày |
| Stay | Xác suất **duy trì** bucket hiện tại |
| Down bucket | Xác suất rủi ro **giảm** (tốt lên) |

Ví dụ: Stay = 65%, Down = 25%, Up = 10% → "Rủi ro nhiều khả năng giữ nguyên hoặc giảm"

**Tóm gọn workflow Panel 3:**
1. Xem **Bias** VNINDEX → POS hay NEG?
2. Xem **Excess 20D** → dương/âm? Stable hay Unstable?
3. Xem **Top 3 ngành** → ưu tiên đầu tư ngành nào?
4. Xem **Transition** → rủi ro sẽ tăng hay giảm?

**Sử dụng khi:**
- Bạn cần cảnh báo sớm rủi ro vĩ mô
- Bạn muốn so sánh hiệu suất 6 indices theo regime
- Bạn cần tìm ngành mạnh/yếu theo chu kỳ kinh tế

**File chính:**
- `Macro_Alert_System_v5.0.1 pine` (Bản gốc)
- `Macro_Alert_System_v5.1_EconAdj.pine` (Bản điều chỉnh kinh tế)

📖 **Xem chi tiết:** [README Macro Alert System](./02_Macro_Alert_System/)

---

### 📈 03_Indices_Research_Map
**Mapping vĩ mô → Hiệu suất thị trường (Script B)**

Phiên bản: v2.0 | Tác giả: Macro Research Team

**Mục đích:** Script B trong hệ thống 2 script, map Risk Score từ Script A sang hiệu suất thị trường:
- Replicate Macro Engine từ Script A
- Mapping Risk Score → Average Returns, Win Rate, Drawdown
- Phân tích chi tiết theo bucket (B0-B4)

**Kết hợp với:**
- 6 chỉ số thị trường: VNINDEX, VN30, VN100, VNALLSHARE, VNMIDCAP, VNSMALLCAP
- 11 ngành kinh tế: Finance, Industrials, IT, Real Estate, Consumer, Energy, Materials, Healthcare, Utilities, v.v.

**Sử dụng khi:**
- Bạn đã chạy Script A và có Risk Score
- Bạn muốn chọn indices/sectors phù hợp với regime hiện tại
- Bạn cần backtest chiến lược theo bucket

**File chính:**
- `Indices_Research_Map_v2.0.pine`

📖 **Xem chi tiết:** [README Indices Research Map](./03_Indices_Research_Map/)

---

### 💰 04_YieldCurveLab
**Laboratory nghiên cứu đường cong lợi suất trái phiếu**

Phiên bản gốc: v1.8.1 | Phiên bản EconAdj: v1.9 | Tác giả: VnBondLab

**Mục đích:** Phân tích sâu đường cong lợi suất Việt Nam (1Y/2Y/3Y/5Y/7Y/10Y)

**3 khối phân tích chính:**
1. **Shape & Regime:** Level, Slope, Curve, Classification (YC0-YC4)
2. **Quality & Distortion:** Đánh giá độ "khỏe" của dữ liệu (HIGHQ/MEDQ/LOWQ)
3. **Research vs VNINDEX:** Tương quan, Beta, R² giữa Stress và thị trường cổ phiếu

**v1.9 EconAdj — Điều chỉnh kinh tế:**
- Thêm Overnight-1Y spread (VNINBR - VN01Y) vào macro_stress
- Khi overnight > 1Y = money market stress → risk 100%
- Weights: level/slope 0.45→0.40, thêm short_end 0.10

**3 Panel:**
- Panel 1: Shape Dashboard (tổng quan YC)
- Panel 2: Grid (bảng lưới theo kỳ hạn)
- Panel 3: Diagnostics + Research (thống kê học thuật)

**Sử dụng khi:**
- Bạn là bond trader hoặc quan tâm đến thị trường trái phiếu
- Bạn muốn dự báo rủi ro hệ thống từ YC inversion
- Bạn cần nghiên cứu mối quan hệ bond → equity

**File chính:**
- `VN YieldCurveLab v1.8.1` (Bản gốc)
- `VN_YieldCurveLab_v1.9_EconAdj.pine` (Bản điều chỉnh kinh tế)

📖 **Xem chi tiết:** [README YieldCurveLab](./04_YieldCurveLab/)

---

### 🔗 05_Bond_Transmission_Monitor
**Giám sát truyền dẫn trái phiếu từ nước ngoài**

Phiên bản gốc: v6.0.2 | Phiên bản EconAdj: v6.1 | Tác giả: MacroAcademic Team

**Mục đích:** Phân tích tác động từ thị trường nước ngoài sang trái phiếu VN thông qua 6 kênh truyền dẫn

**6 Panel phân tích:**
- **P1**: Nhật (BOJ) → VN (Lợi suất Nhật tác động lên VN)
- **P2**: Trái phiếu toàn cầu → VN (US + DE + GB + AU + CA)
- **P3**: Đường cong toàn cầu → VN (Level + Slope)
- **P4**: Yên carry (risk-off) → VN (USDJPY + VIX + Carry trade)
- **P5**: FX & Thanh khoản → VN (USDVND + VNINBR)
- **P6**: Chuỗi truyền dẫn → VN (US2Y → USDVND → VNINBR → VN10Y)

**v6.1 EconAdj — Điều chỉnh kinh tế:**
- Regime-aware sign: tự động phát hiện decoupling VN vs Global
- Khi VN10Y giảm >20bp + Global tăng >10bp trong 60 ngày → override sign = -1
- Phản ánh đúng giai đoạn NHNN nới lỏng bất chấp Fed thắt chặt

**Tính năng:**
- Hồi quy OLS để đo lường độ truyền dẫn (R², Beta, Alpha)
- Impact Score (0-100) để đánh giá áp lực
- Decoupling Score để đo lường độ tự chủ
- Chain Strength (P6) để đo lường độ mạnh chuỗi 3 bước

**Sử dụng khi:**
- Bạn là bond trader cần hiểu tác động nước ngoài
- Bạn muốn dự báo SBV's policy từ FED/BOJ action
- Bạn cần timing giao dịch TPCP/trái phiếu
- Bạn muốn hiểu cơ chế truyền dẫn toàn cầu → VN

**File chính:**
- `Bond_Transmission_Monitor_v6.0.2pine` (Bản gốc)
- `Bond_Transmission_Monitor_v6.1_EconAdj.pine` (Bản điều chỉnh kinh tế)

📖 **Xem chi tiết:** [README Bond Transmission Monitor](./05_Bond_Transmission_Monitor/)

---

## 🔄 Mối quan hệ giữa các dự án

```
┌──────────────────────────────────────┐
│   01_MacroAcademic Engine (Script A) │
│   Kinh tế vĩ mô → Risk Score         │
│   v2.1 (gốc) | v2.2 (EconAdj)        │
└──────────────┬───────────────────────┘
               │
               ├──────────────────────────┐
               ▼                          ▼
    ┌────────────────────────┐  ┌───────────────────────────┐
    │ 02_Macro Alert System  │  │ 03_Indices Research Map   │
    │ v5.0.1 | v5.1 EconAdj  │  │ v2.0 (Script B)           │
    └────────────────────────┘  └───────────────────────────┘

    04_YieldCurveLab              05_Bond Transmission
    v1.8.1 | v1.9 EconAdj         v6.0.2 | v6.1 EconAdj
    Đường cong lợi suất           Truyền dẫn nước ngoài
```

**Cách sử dụng kết hợp:**

**Workflow 1: TỔNG QUAN VĨ MÔ + CẢNH BÁO**
1. **Bước 1:** Dùng **01_MacroAcademic Engine** để đánh giá bối cảnh vĩ mô
   - Kết quả: Risk Score B0-B4 (Ví dụ: B1 = Rủi ro thấp)
2. **Bước 2:** Dùng **02_Macro Alert System** để có cảnh báo chi tiết
   - Chọn Panel **"Risk — Dashboard"** → xem đường Risk % (trắng)
   - Xác định Bucket hiện tại (B0-B4) từ giá trị Risk %
   - Xem 3 Layer để hiểu **nguồn gốc** rủi ro (Funding? Cycle? External?)
   - Nếu B0-B1: Tăng tỷ trọng cyclical sectors (Finance, Industrials, Real Estate)
   - Nếu B3-B4: Ưu tiên defensive sectors (Utilities, Healthcare) hoặc tiền mặt
3. **Bước 3:** Chuyển sang Panel **"Equity — Regime & Rotation"**
   - Xem bảng hiệu suất: ở Bucket hiện tại, chỉ số/ngành nào có AvgReturn dương + WinRate > 55%?
   - Đối chiếu với ma trận chuyển đổi: Bucket hiện tại có xác suất cao duy trì hay chuyển sang bucket khác?

**Workflow 2: MAPPING VĨ MÔ → THỊ TRƯỜNG (dùng Module 03)**

> Module 03 là **Script B** — nó tự replicate logic Macro Engine (Script A) bên trong, nên **có thể chạy độc lập** mà không cần mở Module 01 song song.

Module 03 có **4 panel** (chọn trong Settings → "Panel"):

**Panel 1: "Macro Weather" — Tổng quan nhanh**
- Bảng nhỏ hiển thị: Risk %, Bucket hiện tại (B0-B4), mũi tên xu hướng (↑↓→)
- 4 dòng pillar: Liquidity, Curve, Intl, 10Y-Policy — mỗi dòng có Status + Score
- TAKEAWAY ở dưới cùng: kết luận + AvgR20 + Win% + DD cho VNINDEX ở bucket này
- **Cách đọc:** Nhìn TAKEAWAY trước → nếu AvgR20 dương + Win > 55% → bucket thuận lợi

**Panel 2: "Market Regime Map" — So sánh 6 chỉ số**

| Cột | Ý nghĩa |
|-----|---------|
| Index | VNINDEX, VN30, VN100, VNALLSHARE, VNMIDCAP, VNSMALLCAP |
| AvgR20 | Return trung bình 20 ngày khi ở bucket này |
| Win20% | Tỷ lệ có lãi |
| T-like | Chỉ số thống kê t — đo mức ý nghĩa: \|T\| ≥ 2.0 = HIGH, ≥ 1.0 = MED, < 1.0 = LOW |
| AvgR60 | Return 60 ngày (optional) |
| AvgDD20 | Drawdown trung bình |
| N20 | Số mẫu |

- **Cách đọc:** Tìm chỉ số có AvgR20 dương + T-like ≥ 1.0 + N đủ lớn → đó là chỉ số đáng đầu tư nhất ở bucket này
- Ví dụ: Ở B1, VNSMALLCAP AvgR20 = +1.8%, T = 2.1, Win = 65%, N = 52 → "Smallcap có lợi thế thống kê mạnh khi risk thấp"

**Panel 3: "Sector Rotation Map" — Top/Bottom ngành**
- Xếp hạng 11 ngành theo **relative return vs VNINDEX** (AvgRR20)
- 3 ngành TOP (mạnh nhất) + 3 ngành BOTTOM (yếu nhất) + ngành ở giữa
- Kèm T-like và N cho từng ngành
- **Cách đọc:** Ở của bucket hiện tại:
  - TOP 3: ngành thường outperform → ưu tiên mua cổ phiếu thuộc ngành này
  - BOTTOM 3: ngành thường underperform → tránh hoặc short

**Panel 4: "Transition Summary" — Dự báo regime tiếp theo**

| Hàng | Ý nghĩa |
|------|---------|
| Up risk | Xác suất bucket **tăng** (rủi ro xấu đi) |
| Same bucket | Xác suất **duy trì** bucket hiện tại |
| Down risk | Xác suất bucket **giảm** (rủi ro tốt lên) |

- TAKEAWAY tự động: STICKY REGIME (Stay ≥ 50%), RISK IMPROVING (Down > Up), RISK DETERIORATING (Up > Down)
- **Cách đọc:** Nếu STICKY REGIME + đang ở B1 → yên tâm giữ vị thế. Nếu RISK DETERIORATING + đang ở B2 → chuẩn bị phòng thủ

**Workflow thực tế:**
1. **Bước 1:** Mở Panel 1 → xem Bucket + TAKEAWAY
2. **Bước 2:** Mở Panel 2 → chọn chỉ số nào có AvgR + T-like tốt nhất
3. **Bước 3:** Mở Panel 3 → xác định ngành TOP (overweight) và BOTTOM (underweight)
4. **Bước 4:** Mở Panel 4 → đánh giá regime có bền vững không → quyết định sizing

**Workflow 3: PHÂN TÍCH SÂU TRÁI PHIẾU**
1. Dùng **04_YieldCurveLab** độc lập hoặc kết hợp với 01
   - Nếu YC4 + Slope inverted → Cảnh báo rủi ro chu kỳ cao
   - Nếu Stress High → Giảm đòn bẩy, tăng phòng thủ

---

## 🚀 Quick Start (Bắt đầu nhanh)

### Bạn là ai? Chọn dự án phù hợp:

#### 👤 Nhà đầu tư chứng khoán (Stock Investor)
**Bắt đầu với:** `02_Macro_Alert_System`
- Xem nhanh: Panel 1 (Macro Weather)
- Quyết định: Panel 3 (Sector Rotation)
- Sau đó dùng `03_Indices_Research_Map` để chọn chỉ số phù hợp

#### 👨‍💼 Quản lý danh mục (Portfolio Manager)
**Bắt đầu với:** `01_MacroAcademic_Engine`
- Sử dụng Risk Score để điều chỉnh asset allocation
- Kết hợp `02_Macro_Alert_System` cho cảnh báo chi tiết
- Dùng `03_Indices_Research_Map` để chọn indices/sectors

#### 📊 Bond Trader / Analyst
**Bắt đầu với:** `04_YieldCurveLab`
- Theo dõi YC regime (YC1-YC4)
- Research Panel 3 để hiểu mối quan hệ bond → equity
- Kết hợp với `01_MacroAcademic_Engine` để hiểu bối cảnh vĩ mô

#### 🎓 Researcher / Academic
**Dùng cả 4 dự án** để nghiên cứu:
- Macro-finance linkage (01 + 03)
- Regime-based investing (01 + 02 + 03)
- Sector rotation strategies (02 + 03)
- Yield curve theory (04)

---

## 📋 Cài đặt cơ bản (TradingView)

### Yêu cầu:
- **TradingView:** Tài khoản Free hoạt động đầy đủ (dữ liệu Economics truy cập được qua Pine Script)
- **Dữ liệu:** Các ticker Economics và HOSE indices (tự động load qua `request.security()`)
- **Timeframe:** Khuyến nghị D (Daily)

### Cách sử dụng:

1. **Mở chart** bất kỳ trên TradingView (khuyến nghị: VNINDEX)
2. **Add indicator:** Click "Indicators" → Search tên script
3. **Thêm nhiều instance:** Để xem nhiều panel, add cùng indicator nhiều lần
4. **Chọn panel:** Mỗi instance chọn 1 panel khác nhau (1, 2, 3...)

---

## 📊 So sánh nhanh 5 dự án

| Tiêu chí | 01_MacroAcademic Engine | 02_Macro Alert System | 03_Indices Research Map | 04_YieldCurveLab | 05_Bond Transmission |
|----------|------------------------|----------------------|------------------------|------------------|----------------------|
| **Phạm vi** | Kinh tế vĩ mô | Cảnh báo vĩ mô | Mapping vĩ mô → CK | Trái phiếu VN | Truyền dẫn nước ngoài |
| **Input chính** | CPI, GDP, Rates, FX, Oil | Macro + Indices + Sectors | Macro + 6 indices + 11 sectors | 1Y-10Y yields | Global bonds + FX |
| **Output** | Risk Score (0-100) | 4 Panel cảnh báo | AvgR, Win%, DD by bucket | Stress, Correlation | Impact Score, R² |
| **Số panel** | 7 | 4 | 1 | 3 | 6 |
| **User case** | Asset allocation | Cảnh báo rủi ro | Chọn indices/sectors | Bond trading | Bond timing |
| **Độ phức tạp** | Trung bình - Cao | Trung bình | Trung bình | Cao (Academic) | Cao (Academic) |
| **Thời gian** | Hàng tuần/tháng | Hàng ngày/tuần | Khi có Risk Score | Hàng ngày | Hàng ngày |

---

## ⚠️ Lưu ý quan trọng

### Giới hạn:
- Dữ liệu lịch sử hạn chế cho thị trường Việt Nam
- Mô hình dựa trên tương quan lịch sử, không đảm bảo kết quả tương lai
- Độ trễ trong dữ liệu vĩ mô (CPI: tháng, GDP: quý)
- Cần TradingView Premium để truy cập đầy đủ dữ liệu Economics

### Best Practices:
1. **Kết hợp nhiều phương pháp:** Không chỉ dựa vào một tín hiệu duy nhất
2. **Backtest:** Kiểm tra hiệu quả với dữ liệu lịch sử trước khi dùng real money
3. **Quản lý rủi ro:** Luôn có stop-loss, không all-in
4. **Cập nhật:** Theo dõi và điều chỉnh tham số theo thị trường

---

## 🔬 Tính năng học thuật (Academic Features)

Tất cả các dự án đều được xây dựng với các chuẩn mực học thuật:

- **Robust statistics:** Z-score có winsorization, Percentile-based (phi tham số)
- **Sample adequacy:** EffN (Effective Sample Size) để tránh ảo giác thống kê
- **Regime analysis:** Phân tích theo chế độ (YC4, B0-B4, v.v.)
- **Multiple-testing control:** Lag Stability check để tránh overfit
- **Quality gating:** Loại bỏ giai đoạn dữ liệu nhiễu (LOWQ)

---

## 📚 Tài liệu & Hướng dẫn

### Documentation:
- 📖 [01_MacroAcademic_Engine README](./01_MacroAcademic_Engine/)
- 📖 [02_Macro_Alert_System README](./02_Macro_Alert_System/)
- 📖 [03_Indices_Research_Map README](./03_Indices_Research_Map/)
- 📖 [04_YieldCurveLab README](./04_YieldCurveLab/)
- 📖 [05_Bond_Transmission_Monitor README](./05_Bond_Transmission_Monitor/)

### Tài liệu tham khảo:
- **Macro-finance linkage:** Mối quan hệ giữa biến số vĩ mô và thị trường tài sản
- **Regime-based investing:** Đầu tư theo chế độ thay vì market timing
- **Sector rotation:** Luân chuyển ngành theo chu kỳ kinh tế
- **Yield curve analysis:** Đường cong lợi suất như chỉ báo dự báo

---

## 🆘 Hỗ trợ & Đóng góp

### Xử lý sự cố thường gặp:
1. **Không hiển thị dữ liệu:** Kiểm tra ticker và quyền truy cập TradingView Premium
2. **Kết quả bất thường:** Reset statistics, kiểm tra lại tham số
3. **Hiệu suất chậm:** Tắt bớt panel hoặc giảm window length

### Đóng góp:
- Report bugs và đề xuất tính năng
- Chia sẻ backtest results
- Cộng tác nghiên cứu các mô hình mới

---

## 📝 Version History

### Main Repository:
- **2025-01-02:** Reorganize into 4 independent projects
- **2025-01-02:** Add comprehensive README and documentation
- **2025-01-02:** Add donate section with QR code
- **2025-01-02:** Add 05_Bond_Transmission_Monitor project
- **2025-04:** Thêm phiên bản EconAdj cho 4 module (điều chỉnh kinh tế VN)
- **Phiên bản hiện tại:** v4.0 (5 Projects + EconAdj)

### Sub-projects:
- **01_MacroAcademic_Engine:** v2.1 → v2.2 EconAdj (Risk weights, Taylor Rule, IDI, Credit proxy)
- **02_Macro_Alert_System:** v5.0.1 → v5.1 EconAdj (Credit + FX pillars)
- **03_Indices_Research_Map:** v2.0 (Script B)
- **04_YieldCurveLab:** v1.8.1 → v1.9 EconAdj (Overnight-1Y spread)
- **05_Bond_Transmission_Monitor:** v6.0.2 → v6.1 EconAdj (Regime-aware sign)

---

## 👥 Tác giả & Liên hệ

**Tác giả:** Macro Research Team & VnBondLab
**Nền tảng:** TradingView Pine Script v5/v6
**Thị trường:** HOSE - Việt Nam
**Ngày cập nhật:** April 2026

---

## 📜 License

*Disclaimer: Công cụ này chỉ phục vụ mục đích nghiên cứu và giáo dục, không phải là lời khuyên đầu tư. Nhà đầu tư cần tự chịu trách nhiệm với quyết định của mình.*

---

## 💖 Donate / Ủng hộ

Nếu bạn tìm thấy các công cụ này hữu ích và muốn ủng hộ dự án, tôi rất trân trọng sự đóng góp của bạn!

### 📱 Momo / QR Code

![Donate QR Code](assets/donate_qr.jpg)

**Hoặc quét mã QR:**

```
┌─────────────────────┐
│                     │
│   [QR CODE HERE]    │
│                     │
└─────────────────────┘
```

### 💳 Thông tin chuyển khoản

- **Ngân hàng:** [Tên ngân hàng]
- **Số tài khoản:** [Số tài khoản]
- **Chủ tài khoản:** [Tên chủ tài khoản]

### 🎁 Mục đích Donate

Ủng hộ của bạn sẽ được sử dụng để:
- Phí维护 và phát triển thêm tính năng mới
- Nâng cấp server và tài nguyên
- Cập nhật dữ liệu định kỳ
- Phát triển thêm các công cụ phân tích khác

### 🙏 Cảm ơn

Cảm ơn bạn đã sử dụng và ủng hộ VnBondLab! Mọi sự đóng góp dù nhỏ đều rất quý giá! 💝

---

**🎯 Bắt đầu ngay:** Chọn dự án phù hợp với nhu cầu của bạn và xem README chi tiết trong từng thư mục!

*Happy Trading & Research!* 📊🚀
