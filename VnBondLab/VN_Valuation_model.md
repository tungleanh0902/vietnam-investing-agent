//@version=5
indicator("VN Valuation Model Lab v2.3a - Final UI Patch", shorttitle="VN ValModel Lab v2.3a", overlay=false, precision=2, max_labels_count=500)

//====================================================
// INPUTS
//====================================================

barsPerYear = input.int(252, "So phien moi nam", minval=100, maxval=366)

panelMode = input.string("Tom tat", "Che do hien thi", options=["Tom tat", "Mo hinh", "Chan doan", "Day du"])

showTable = input.bool(true, "Hien bang")
showPlots = input.bool(true, "Hien duong gia ngu y")
showLineLabels = input.bool(true, "Gan nhan cho duong")

epsType = input.string("EPS pha loang", "Loai EPS", options=["EPS pha loang", "EPS co ban"])

showPEModel = input.bool(true, "Hien mo hinh PE")
showPBModel = input.bool(true, "Hien mo hinh PB")
showPSModel = input.bool(true, "Hien mo hinh PS")

bandModel = input.string("Tong hop", "Vung ngu y hien thi", options=["Tong hop", "PE", "PB", "PS"])

coverageHigh = input.float(0.80, "Nguong do phu HIGH", minval=0.1, maxval=1.0, step=0.05)
coverageMed = input.float(0.50, "Nguong do phu MED", minval=0.1, maxval=1.0, step=0.05)

cvHigh = input.float(0.50, "Nguong do bien dong HIGH - CV", minval=0.05, maxval=2.0, step=0.05)
cvMed = input.float(1.00, "Nguong do bien dong MED - CV", minval=0.05, maxval=3.0, step=0.05)

driftLow = input.float(10.0, "Nguong chuyen pha LOW (%)", minval=1.0, maxval=50.0, step=1.0)
driftMed = input.float(25.0, "Nguong chuyen pha MED (%)", minval=1.0, maxval=100.0, step=1.0)

robustHigh = input.float(10.0, "Nguong do ben HIGH (%)", minval=1.0, maxval=50.0, step=1.0)
robustMed = input.float(25.0, "Nguong do ben MED (%)", minval=1.0, maxval=100.0, step=1.0)

consensusHigh = input.float(10.0, "Nguong dong thuan HIGH (%)", minval=1.0, maxval=50.0, step=1.0)
consensusMed = input.float(25.0, "Nguong dong thuan MED (%)", minval=1.0, maxval=100.0, step=1.0)

horizonHigh = input.float(10.0, "Nguong dong thuan khung HIGH (%)", minval=1.0, maxval=50.0, step=1.0)
horizonMed = input.float(25.0, "Nguong dong thuan khung MED (%)", minval=1.0, maxval=100.0, step=1.0)

rankLow = input.float(25.0, "Nguong vi tri thap", minval=1.0, maxval=49.0, step=1.0)
rankHigh = input.float(75.0, "Nguong vi tri cao", minval=51.0, maxval=99.0, step=1.0)

//====================================================
// LENGTHS
//====================================================

len1Y = barsPerYear
len3Y = barsPerYear * 3
len5Y = barsPerYear * 5

//====================================================
// HELPERS
//====================================================

safeDiv(num, den) =>
    not na(num) and not na(den) and den != 0 ? num / den : na

fmt(x) =>
    na(x) ? "N/A" : str.tostring(x, "#.##")

fmtPrice(x) =>
    na(x) ? "N/A" : str.tostring(x, "#,###.##")

fmtPct(x) =>
    na(x) ? "N/A" : str.tostring(x, "#.##") + "%"

makeLabel(_oldLabel, _x, _y, _txt, _bg) =>
    label.delete(_oldLabel)
    label.new(_x, _y, _txt, xloc=xloc.bar_index, yloc=yloc.price, style=label.style_label_left, textcolor=color.white, color=_bg, size=size.small)

validRatio(seriesValue, lengthValue) =>
    ta.sma(not na(seriesValue) ? 1.0 : 0.0, lengthValue)

cvRatio(seriesValue, avgValue, lengthValue) =>
    stdevValue = ta.stdev(seriesValue, lengthValue)
    safeDiv(stdevValue, avgValue)

pctValue(seriesValue, lengthValue, pct) =>
    ta.percentile_nearest_rank(seriesValue, lengthValue, pct)

coverageLabel(cov) =>
    na(cov) ? "N/A" : cov >= coverageHigh ? "HIGH" : cov >= coverageMed ? "MED" : "LOW"

stabilityLabel(cv) =>
    na(cv) ? "N/A" : cv <= cvHigh ? "HIGH" : cv <= cvMed ? "MED" : "LOW"

reliabilityLabel(covLabel, stabLabel, statusText) =>
    statusText != "OK" ? "N/A" : covLabel == "HIGH" and stabLabel == "HIGH" ? "HIGH" : covLabel == "LOW" or stabLabel == "LOW" ? "LOW" : "MED"

driftLabel(driftPct) =>
    absDrift = math.abs(driftPct)
    na(absDrift) ? "N/A" : absDrift <= driftLow ? "ON DINH" : absDrift <= driftMed ? "DANG DOI" : "CHUYEN PHA MANH"

driftShortLabel(driftPct) =>
    absDrift = math.abs(driftPct)
    na(absDrift) ? "N/A" : absDrift <= driftLow ? "LOW" : absDrift <= driftMed ? "MED" : "HIGH"

robustLabel(gapPct) =>
    absGap = math.abs(gapPct)
    na(absGap) ? "N/A" : absGap <= robustHigh ? "HIGH" : absGap <= robustMed ? "MED" : "LOW"

consensusLabel(dispersionPct) =>
    na(dispersionPct) ? "N/A" : dispersionPct <= consensusHigh ? "HIGH" : dispersionPct <= consensusMed ? "MED" : "LOW"

horizonLabel(dispersionPct) =>
    na(dispersionPct) ? "N/A" : dispersionPct <= horizonHigh ? "HIGH" : dispersionPct <= horizonMed ? "MED" : "LOW"

rankLabel(rankValue) =>
    na(rankValue) ? "N/A" : rankValue <= rankLow ? "THAP" : rankValue >= rankHigh ? "CAO" : "TRUNG BINH"

dataStatus(isOn, baseData, multipleNow, multipleAvg, impliedPrice) =>
    not isOn ? "OFF" : na(baseData) ? "N/A - thieu du lieu" : baseData <= 0 ? "N/A - du lieu <= 0" : na(multipleNow) ? "N/A - thieu multiple" : na(multipleAvg) ? "N/A - thieu TB" : na(impliedPrice) ? "N/A" : "OK"

suitabilityLabel(statusText, reliabilityText, driftText, robustText) =>
    statusText != "OK" ? "N/A" : reliabilityText == "LOW" or robustText == "LOW" ? "LOW" : reliabilityText == "HIGH" and driftText != "HIGH" and robustText == "HIGH" ? "HIGH" : "MED"

bandPositionLabel(priceNow, p25, p50, p75) =>
    na(priceNow) or na(p25) or na(p50) or na(p75) ? "N/A" : priceNow < p25 ? "DUOI P25" : priceNow <= p50 ? "P25-P50" : priceNow <= p75 ? "P50-P75" : "TREN P75"

bandWidthPct(p25, p75, p50) =>
    safeDiv(p75 - p25, p50) * 100

distributionLabel(widthPct) =>
    na(widthPct) ? "N/A" : widthPct <= 20 ? "HEP" : widthPct <= 50 ? "VUA" : "RONG"

skewLabel(meanVal, medianVal) =>
    gap = safeDiv(meanVal - medianVal, medianVal) * 100
    na(gap) ? "N/A" : math.abs(gap) <= robustHigh ? "CAN BANG" : gap > 0 ? "TB CAO" : "TB THAP"

score3(x) =>
    x == "HIGH" or x == "ON DINH" or x == "CAN BANG" or x == "HEP" or x == "NONE" ? 3.0 : x == "MED" or x == "DANG DOI" or x == "TRUNG BINH" or x == "TB CAO" or x == "TB THAP" or x == "VUA" ? 2.0 : x == "LOW" or x == "CHUYEN PHA MANH" or x == "RONG" or x == "THAP" or x == "CAO" ? 1.0 : 0.0

relScore(x) =>
    x == "HIGH" ? 3.0 : x == "MED" ? 2.0 : x == "LOW" ? 1.0 : 0.0

qualityFromScore(score) =>
    na(score) ? "N/A" : score >= 2.5 ? "HIGH" : score >= 1.5 ? "MED" : "LOW"

percentRankManual(x, p25, p50, p75) =>
    raw = na(x) or na(p25) or na(p50) or na(p75) ? na : x <= p25 ? 25.0 * safeDiv(x, p25) : x <= p50 ? 25.0 + 25.0 * safeDiv(x - p25, p50 - p25) : x <= p75 ? 50.0 + 25.0 * safeDiv(x - p50, p75 - p50) : 75.0 + 25.0 * safeDiv(x - p75, p75)
    na(raw) ? na : math.max(0.0, math.min(100.0, raw))

horizonDispersion(a, b, c) =>
    ok = not na(a) and not na(b) and not na(c)
    avg = ok ? (a + b + c) / 3.0 : na
    variance = ok ? (math.pow(a - avg, 2) + math.pow(b - avg, 2) + math.pow(c - avg, 2)) / 3.0 : na
    stdev = ok ? math.sqrt(variance) : na
    safeDiv(stdev, avg) * 100

//====================================================
// FINANCIAL DATA
//====================================================

epsId = epsType == "EPS pha loang" ? "EARNINGS_PER_SHARE_DILUTED" : "EARNINGS_PER_SHARE_BASIC"

epsTTM = request.financial(syminfo.tickerid, epsId, "TTM")
bvpsFQ = request.financial(syminfo.tickerid, "BOOK_VALUE_PER_SHARE", "FQ")
revenueTTM = request.financial(syminfo.tickerid, "TOTAL_REVENUE", "TTM")
sharesFQ = request.financial(syminfo.tickerid, "TOTAL_SHARES_OUTSTANDING", "FQ")

//====================================================
// PER SHARE DATA
//====================================================

revenuePerShare = sharesFQ > 0 ? safeDiv(revenueTTM, sharesFQ) : na

//====================================================
// CURRENT MULTIPLES
//====================================================

peNow = epsTTM > 0 ? safeDiv(close, epsTTM) : na
pbNow = bvpsFQ > 0 ? safeDiv(close, bvpsFQ) : na
psNow = revenuePerShare > 0 ? safeDiv(close, revenuePerShare) : na

//====================================================
// MULTIPLE AVERAGES: 1Y / 3Y / 5Y
//====================================================

peAvg1 = ta.sma(peNow, len1Y)
peAvg3 = ta.sma(peNow, len3Y)
peAvg5 = ta.sma(peNow, len5Y)

pbAvg1 = ta.sma(pbNow, len1Y)
pbAvg3 = ta.sma(pbNow, len3Y)
pbAvg5 = ta.sma(pbNow, len5Y)

psAvg1 = ta.sma(psNow, len1Y)
psAvg3 = ta.sma(psNow, len3Y)
psAvg5 = ta.sma(psNow, len5Y)

//====================================================
// IMPLIED VALUES
//====================================================

peImp1 = epsTTM > 0 and peAvg1 > 0 ? epsTTM * peAvg1 : na
peImp3 = epsTTM > 0 and peAvg3 > 0 ? epsTTM * peAvg3 : na
peImp5 = epsTTM > 0 and peAvg5 > 0 ? epsTTM * peAvg5 : na

pbImp1 = bvpsFQ > 0 and pbAvg1 > 0 ? bvpsFQ * pbAvg1 : na
pbImp3 = bvpsFQ > 0 and pbAvg3 > 0 ? bvpsFQ * pbAvg3 : na
pbImp5 = bvpsFQ > 0 and pbAvg5 > 0 ? bvpsFQ * pbAvg5 : na

psImp1 = revenuePerShare > 0 and psAvg1 > 0 ? revenuePerShare * psAvg1 : na
psImp3 = revenuePerShare > 0 and psAvg3 > 0 ? revenuePerShare * psAvg3 : na
psImp5 = revenuePerShare > 0 and psAvg5 > 0 ? revenuePerShare * psAvg5 : na

//====================================================
// HISTORICAL BAND
//====================================================

peP25 = pctValue(peNow, len5Y, 25)
peP50 = pctValue(peNow, len5Y, 50)
peP75 = pctValue(peNow, len5Y, 75)

pbP25 = pctValue(pbNow, len5Y, 25)
pbP50 = pctValue(pbNow, len5Y, 50)
pbP75 = pctValue(pbNow, len5Y, 75)

psP25 = pctValue(psNow, len5Y, 25)
psP50 = pctValue(psNow, len5Y, 50)
psP75 = pctValue(psNow, len5Y, 75)

peBand25 = epsTTM > 0 and peP25 > 0 ? epsTTM * peP25 : na
peBand50 = epsTTM > 0 and peP50 > 0 ? epsTTM * peP50 : na
peBand75 = epsTTM > 0 and peP75 > 0 ? epsTTM * peP75 : na

pbBand25 = bvpsFQ > 0 and pbP25 > 0 ? bvpsFQ * pbP25 : na
pbBand50 = bvpsFQ > 0 and pbP50 > 0 ? bvpsFQ * pbP50 : na
pbBand75 = bvpsFQ > 0 and pbP75 > 0 ? bvpsFQ * pbP75 : na

psBand25 = revenuePerShare > 0 and psP25 > 0 ? revenuePerShare * psP25 : na
psBand50 = revenuePerShare > 0 and psP50 > 0 ? revenuePerShare * psP50 : na
psBand75 = revenuePerShare > 0 and psP75 > 0 ? revenuePerShare * psP75 : na

coreBandValid = not na(peBand25) and not na(pbBand25) and not na(psBand25) and not na(peBand50) and not na(pbBand50) and not na(psBand50) and not na(peBand75) and not na(pbBand75) and not na(psBand75)

coreBand25 = coreBandValid ? (peBand25 + pbBand25 + psBand25) / 3.0 : na
coreBand50 = coreBandValid ? (peBand50 + pbBand50 + psBand50) / 3.0 : na
coreBand75 = coreBandValid ? (peBand75 + pbBand75 + psBand75) / 3.0 : na

band25 = bandModel == "Tong hop" ? coreBand25 : bandModel == "PE" ? peBand25 : bandModel == "PB" ? pbBand25 : psBand25
band50 = bandModel == "Tong hop" ? coreBand50 : bandModel == "PE" ? peBand50 : bandModel == "PB" ? pbBand50 : psBand50
band75 = bandModel == "Tong hop" ? coreBand75 : bandModel == "PE" ? peBand75 : bandModel == "PB" ? pbBand75 : psBand75

bandPos = bandPositionLabel(close, band25, band50, band75)
bandWidth = bandWidthPct(band25, band75, band50)
bandDist = distributionLabel(bandWidth)
bandNormPos = safeDiv(close - band25, band75 - band25) * 100

//====================================================
// RANK
//====================================================

peRank = percentRankManual(peNow, peP25, peP50, peP75)
pbRank = percentRankManual(pbNow, pbP25, pbP50, pbP75)
psRank = percentRankManual(psNow, psP25, psP50, psP75)

peRankLabel = rankLabel(peRank)
pbRankLabel = rankLabel(pbRank)
psRankLabel = rankLabel(psRank)

//====================================================
// DATA STATUS
//====================================================

peDataStatus = dataStatus(showPEModel, epsTTM, peNow, peAvg5, peImp5)
pbDataStatus = dataStatus(showPBModel, bvpsFQ, pbNow, pbAvg5, pbImp5)
psDataStatus = dataStatus(showPSModel, revenuePerShare, psNow, psAvg5, psImp5)

//====================================================
// RELIABILITY
//====================================================

peCoverage = validRatio(peNow, len5Y)
pbCoverage = validRatio(pbNow, len5Y)
psCoverage = validRatio(psNow, len5Y)

peCV = cvRatio(peNow, peAvg5, len5Y)
pbCV = cvRatio(pbNow, pbAvg5, len5Y)
psCV = cvRatio(psNow, psAvg5, len5Y)

peCoverageLabel = coverageLabel(peCoverage)
pbCoverageLabel = coverageLabel(pbCoverage)
psCoverageLabel = coverageLabel(psCoverage)

peStabilityLabel = stabilityLabel(peCV)
pbStabilityLabel = stabilityLabel(pbCV)
psStabilityLabel = stabilityLabel(psCV)

peReliability = reliabilityLabel(peCoverageLabel, peStabilityLabel, peDataStatus)
pbReliability = reliabilityLabel(pbCoverageLabel, pbStabilityLabel, pbDataStatus)
psReliability = reliabilityLabel(psCoverageLabel, psStabilityLabel, psDataStatus)

//====================================================
// REGIME / ROBUST / HORIZON / SUIT
//====================================================

peDrift = safeDiv(peAvg1 - peAvg5, peAvg5) * 100
pbDrift = safeDiv(pbAvg1 - pbAvg5, pbAvg5) * 100
psDrift = safeDiv(psAvg1 - psAvg5, psAvg5) * 100

peDriftLabel = driftShortLabel(peDrift)
pbDriftLabel = driftShortLabel(pbDrift)
psDriftLabel = driftShortLabel(psDrift)

peRegime = driftLabel(peDrift)
pbRegime = driftLabel(pbDrift)
psRegime = driftLabel(psDrift)

peHorizonDisp = horizonDispersion(peImp1, peImp3, peImp5)
pbHorizonDisp = horizonDispersion(pbImp1, pbImp3, pbImp5)
psHorizonDisp = horizonDispersion(psImp1, psImp3, psImp5)

peHorizon = horizonLabel(peHorizonDisp)
pbHorizon = horizonLabel(pbHorizonDisp)
psHorizon = horizonLabel(psHorizonDisp)

peRobustGap = safeDiv(peAvg5 - peP50, peP50) * 100
pbRobustGap = safeDiv(pbAvg5 - pbP50, pbP50) * 100
psRobustGap = safeDiv(psAvg5 - psP50, psP50) * 100

peRobust = robustLabel(peRobustGap)
pbRobust = robustLabel(pbRobustGap)
psRobust = robustLabel(psRobustGap)

peSkew = skewLabel(peAvg5, peP50)
pbSkew = skewLabel(pbAvg5, pbP50)
psSkew = skewLabel(psAvg5, psP50)

peSuit = suitabilityLabel(peDataStatus, peReliability, peDriftLabel, peRobust)
pbSuit = suitabilityLabel(pbDataStatus, pbReliability, pbDriftLabel, pbRobust)
psSuit = suitabilityLabel(psDataStatus, psReliability, psDriftLabel, psRobust)

//====================================================
// CONSENSUS
//====================================================

coreValid = not na(peImp5) and not na(pbImp5) and not na(psImp5)
coreAvg = coreValid ? (peImp5 + pbImp5 + psImp5) / 3.0 : na
coreMin = coreValid ? math.min(peImp5, math.min(pbImp5, psImp5)) : na
coreMax = coreValid ? math.max(peImp5, math.max(pbImp5, psImp5)) : na
coreRange = safeDiv(coreMax - coreMin, coreAvg) * 100

coreVar = coreValid ? (math.pow(peImp5 - coreAvg, 2) + math.pow(pbImp5 - coreAvg, 2) + math.pow(psImp5 - coreAvg, 2)) / 3.0 : na
coreStdev = coreValid ? math.sqrt(coreVar) : na
coreDispersion = safeDiv(coreStdev, coreAvg) * 100
coreConsensus = consensusLabel(coreDispersion)

avgReliabilityScore = (relScore(peReliability) + relScore(pbReliability) + relScore(psReliability)) / 3.0
avgSuitScore = (relScore(peSuit) + relScore(pbSuit) + relScore(psSuit)) / 3.0
avgHorizonScore = (relScore(peHorizon) + relScore(pbHorizon) + relScore(psHorizon)) / 3.0

consensusQuality = coreConsensus == "HIGH" and avgReliabilityScore >= 2.5 and avgSuitScore >= 2.5 ? "HIGH" : coreConsensus == "LOW" or avgReliabilityScore < 1.5 or avgSuitScore < 1.5 ? "LOW" : "MED"

peOutGap = coreValid ? math.abs(safeDiv(peImp5 - coreAvg, coreAvg) * 100) : na
pbOutGap = coreValid ? math.abs(safeDiv(pbImp5 - coreAvg, coreAvg) * 100) : na
psOutGap = coreValid ? math.abs(safeDiv(psImp5 - coreAvg, coreAvg) * 100) : na

maxOutGap = coreValid ? math.max(peOutGap, math.max(pbOutGap, psOutGap)) : na
modelOutlier = not coreValid ? "N/A" : maxOutGap <= consensusHigh ? "NONE" : peOutGap >= pbOutGap and peOutGap >= psOutGap ? "PE" : pbOutGap >= peOutGap and pbOutGap >= psOutGap ? "PB" : "PS"

peWeight = relScore(peReliability) + relScore(peSuit)
pbWeight = relScore(pbReliability) + relScore(pbSuit)
psWeight = relScore(psReliability) + relScore(psSuit)
weightTotal = peWeight + pbWeight + psWeight

weightedCore = weightTotal > 0 and coreValid ? (peImp5 * peWeight + pbImp5 * pbWeight + psImp5 * psWeight) / weightTotal : na

bandScore = score3(bandDist)
consScore = relScore(coreConsensus)
consQualityScore = relScore(consensusQuality)

frameworkScore = (avgReliabilityScore + avgSuitScore + avgHorizonScore + bandScore + consScore + consQualityScore) / 6.0
frameworkQuality = qualityFromScore(frameworkScore)

//====================================================
// COLORS
//====================================================

priceColor = color.new(color.white, 0)
peColor = color.new(color.blue, 0)
pbColor = color.new(color.orange, 0)
psColor = color.new(color.aqua, 0)

band25Color = color.new(color.gray, 0)
band50Color = color.new(color.yellow, 0)
band75Color = color.new(color.gray, 0)
weightedColor = color.new(color.purple, 0)

headerBg = color.rgb(25, 30, 40)
labelBg = color.rgb(35, 38, 45)
valueBg = color.rgb(18, 20, 25)
noteBg = color.rgb(45, 48, 55)
activeBg = color.rgb(35, 75, 105)
offBg = color.rgb(55, 60, 70)
naBg = color.rgb(150, 90, 20)
highBg = color.rgb(20, 110, 55)
medBg = color.rgb(120, 100, 35)
lowBg = color.rgb(145, 35, 35)

modelBg(isActive, impliedPrice) =>
    not isActive ? offBg : na(impliedPrice) ? naBg : activeBg

statusBg(statusText) =>
    statusText == "OK" ? activeBg : statusText == "OFF" ? offBg : naBg

qualityBg(labelText) =>
    labelText == "HIGH" or labelText == "ON DINH" or labelText == "CAN BANG" or labelText == "HEP" or labelText == "NONE" ? highBg : labelText == "MED" or labelText == "DANG DOI" or labelText == "TRUNG BINH" or labelText == "TB CAO" or labelText == "TB THAP" or labelText == "VUA" ? medBg : labelText == "LOW" or labelText == "CHUYEN PHA MANH" or labelText == "RONG" or labelText == "THAP" or labelText == "CAO" ? lowBg : naBg

positionBg(posText) =>
    posText == "DUOI P25" ? noteBg : posText == "P25-P50" ? activeBg : posText == "P50-P75" ? medBg : posText == "TREN P75" ? lowBg : naBg

outlierBg(outText) =>
    outText == "NONE" ? highBg : outText == "N/A" ? naBg : medBg

//====================================================
// PLOTS
//====================================================

plot(showPlots ? close : na, "Gia hien tai", color=priceColor, linewidth=2)

plot(showPlots and showPEModel ? peImp5 : na, "PE 5Y", color=peColor, linewidth=2)
plot(showPlots and showPBModel ? pbImp5 : na, "PB 5Y", color=pbColor, linewidth=2)
plot(showPlots and showPSModel ? psImp5 : na, "PS 5Y", color=psColor, linewidth=2)

plot(showPlots ? band25 : na, "Vung P25", color=band25Color, linewidth=1)
plot(showPlots ? band50 : na, "Vung P50", color=band50Color, linewidth=2)
plot(showPlots ? band75 : na, "Vung P75", color=band75Color, linewidth=1)
plot(showPlots ? weightedCore : na, "Gia ngu y co trong so", color=weightedColor, linewidth=2)

//====================================================
// LINE LABELS
//====================================================

var label priceLbl = na
var label peLbl = na
var label pbLbl = na
var label psLbl = na
var label band25Lbl = na
var label band50Lbl = na
var label band75Lbl = na
var label weightedLbl = na

if barstate.islast and showLineLabels
    priceLbl := makeLabel(priceLbl, bar_index + 2, close, "Gia hien tai: " + fmtPrice(close), color.rgb(70, 70, 70))

    if showPEModel
        peLbl := makeLabel(peLbl, bar_index + 2, peImp5, "PE 5 nam: " + fmtPrice(peImp5), peColor)

    if showPBModel
        pbLbl := makeLabel(pbLbl, bar_index + 2, pbImp5, "PB 5 nam: " + fmtPrice(pbImp5), pbColor)

    if showPSModel
        psLbl := makeLabel(psLbl, bar_index + 2, psImp5, "PS 5 nam: " + fmtPrice(psImp5), psColor)

    band25Lbl := makeLabel(band25Lbl, bar_index + 2, band25, "P25: " + fmtPrice(band25), color.rgb(90, 90, 90))
    band50Lbl := makeLabel(band50Lbl, bar_index + 2, band50, "P50: " + fmtPrice(band50) + " | " + bandPos, color.rgb(150, 130, 40))
    band75Lbl := makeLabel(band75Lbl, bar_index + 2, band75, "P75: " + fmtPrice(band75), color.rgb(90, 90, 90))
    weightedLbl := makeLabel(weightedLbl, bar_index + 2, weightedCore, "Gia ngu y co trong so: " + fmtPrice(weightedCore), color.rgb(120, 60, 150))

if barstate.islast and not showLineLabels
    label.delete(priceLbl)
    label.delete(peLbl)
    label.delete(pbLbl)
    label.delete(psLbl)
    label.delete(band25Lbl)
    label.delete(band50Lbl)
    label.delete(band75Lbl)
    label.delete(weightedLbl)

//====================================================
// TABLE
//====================================================

var table dash = table.new(position.top_right, 10, 20, border_width=1, frame_color=color.rgb(90, 90, 90), border_color=color.rgb(70, 70, 70))

cell(row, col, txt, bg, txtColor) =>
    table.cell(dash, col, row, txt, bgcolor=bg, text_color=txtColor, text_size=size.small)

if barstate.islast and showTable
    table.clear(dash, 0, 0, 9, 19)

    if panelMode == "Tom tat"
        cell(0, 0, "VN VALMODEL LAB v2.3a", headerBg, color.white)
        cell(0, 1, syminfo.ticker, headerBg, color.white)
        cell(0, 2, "BANG TOM TAT", headerBg, color.white)
        cell(0, 3, "PE/PB/PS", headerBg, color.white)
        cell(0, 4, "Khong DCF", headerBg, color.white)

        cell(1, 0, "Chi tieu", labelBg, color.white)
        cell(1, 1, "Gia tri", labelBg, color.white)
        cell(1, 2, "Dien giai", labelBg, color.white)
        cell(1, 3, "Trang thai", labelBg, color.white)
        cell(1, 4, "Ghi chu", labelBg, color.white)

        cell(2, 0, "Gia hien tai", labelBg, color.white)
        cell(2, 1, fmtPrice(close), valueBg, color.white)
        cell(2, 2, "Gia dong cua", noteBg, color.white)
        cell(2, 3, "", noteBg, color.white)
        cell(2, 4, "", noteBg, color.white)

        cell(3, 0, "Vung ngu y lich su", labelBg, color.white)
        cell(3, 1, "P25: " + fmtPrice(coreBand25), valueBg, color.white)
        cell(3, 2, "P50: " + fmtPrice(coreBand50), valueBg, color.white)
        cell(3, 3, "P75: " + fmtPrice(coreBand75), valueBg, color.white)
        cell(3, 4, "Gia ngu y PE/PB/PS", noteBg, color.white)

        cell(4, 0, "Vi tri gia trong vung", labelBg, color.white)
        cell(4, 1, bandPos, positionBg(bandPos), color.white)
        cell(4, 2, "So voi P25/P50/P75", noteBg, color.white)
        cell(4, 3, "Do rong: " + fmtPct(bandWidth), qualityBg(bandDist), color.white)
        cell(4, 4, bandDist, qualityBg(bandDist), color.white)

        cell(5, 0, "Dong thuan mo hinh", labelBg, color.white)
        cell(5, 1, coreConsensus, qualityBg(coreConsensus), color.white)
        cell(5, 2, "PE/PB/PS co gan nhau khong", noteBg, color.white)
        cell(5, 3, "Lech: " + fmtPct(coreDispersion), qualityBg(coreConsensus), color.white)
        cell(5, 4, "Avg: " + fmtPrice(coreAvg), valueBg, color.white)

        cell(6, 0, "Chat luong du lieu/mo hinh", labelBg, color.white)
        cell(6, 1, frameworkQuality, qualityBg(frameworkQuality), color.white)
        cell(6, 2, "Do sach cua khung tinh toan", noteBg, color.white)
        cell(6, 3, "Muc danh gia: " + frameworkQuality, qualityBg(frameworkQuality), color.white)
        cell(6, 4, "Khong phai chat luong co phieu", noteBg, color.white)

        cell(7, 0, "Mo hinh lech nhat", labelBg, color.white)
        cell(7, 1, modelOutlier, outlierBg(modelOutlier), color.white)
        cell(7, 2, "Xa nhat so voi TB", noteBg, color.white)
        cell(7, 3, "Gap: " + fmtPct(maxOutGap), outlierBg(modelOutlier), color.white)
        cell(7, 4, "NONE = dong thuan tot", noteBg, color.white)

        cell(8, 0, "Gia ngu y co trong so", labelBg, color.white)
        cell(8, 1, fmtPrice(weightedCore), valueBg, color.white)
        cell(8, 2, "Tong hop theo chat luong mo hinh", noteBg, color.white)
        cell(8, 3, "Khong phai gia muc tieu", noteBg, color.white)
        cell(8, 4, "", noteBg, color.white)

        cell(9, 0, "Luu y", labelBg, color.white)
        cell(9, 1, "Gia ngu y", noteBg, color.white)
        cell(9, 2, "Khong phai gia muc tieu", noteBg, color.white)
        cell(9, 3, "Khong khuyen nghi mua ban", noteBg, color.white)
        cell(9, 4, "Phu thuoc du lieu TV", noteBg, color.white)

    if panelMode == "Mo hinh"
        cell(0, 0, "VN VALMODEL LAB v2.3a", headerBg, color.white)
        cell(0, 1, syminfo.ticker, headerBg, color.white)
        cell(0, 2, "MO HINH", headerBg, color.white)
        cell(0, 3, "1/3/5 nam", headerBg, color.white)
        cell(0, 4, "PE/PB/PS", headerBg, color.white)

        cell(1, 0, "Mo hinh", labelBg, color.white)
        cell(1, 1, "1 nam", labelBg, color.white)
        cell(1, 2, "3 nam", labelBg, color.white)
        cell(1, 3, "5 nam", labelBg, color.white)
        cell(1, 4, "Trang thai", labelBg, color.white)
        cell(1, 5, "Do tin cay", labelBg, color.white)

        cell(2, 0, "PE", modelBg(showPEModel, peImp5), color.white)
        cell(2, 1, fmtPrice(peImp1), valueBg, color.white)
        cell(2, 2, fmtPrice(peImp3), valueBg, color.white)
        cell(2, 3, fmtPrice(peImp5), modelBg(showPEModel, peImp5), color.white)
        cell(2, 4, peRegime + " " + fmtPct(peDrift), qualityBg(peRegime), color.white)
        cell(2, 5, peReliability, qualityBg(peReliability), color.white)

        cell(3, 0, "PB", modelBg(showPBModel, pbImp5), color.white)
        cell(3, 1, fmtPrice(pbImp1), valueBg, color.white)
        cell(3, 2, fmtPrice(pbImp3), valueBg, color.white)
        cell(3, 3, fmtPrice(pbImp5), modelBg(showPBModel, pbImp5), color.white)
        cell(3, 4, pbRegime + " " + fmtPct(pbDrift), qualityBg(pbRegime), color.white)
        cell(3, 5, pbReliability, qualityBg(pbReliability), color.white)

        cell(4, 0, "PS", modelBg(showPSModel, psImp5), color.white)
        cell(4, 1, fmtPrice(psImp1), valueBg, color.white)
        cell(4, 2, fmtPrice(psImp3), valueBg, color.white)
        cell(4, 3, fmtPrice(psImp5), modelBg(showPSModel, psImp5), color.white)
        cell(4, 4, psRegime + " " + fmtPct(psDrift), qualityBg(psRegime), color.white)
        cell(4, 5, psReliability, qualityBg(psReliability), color.white)

        cell(5, 0, "Vung ngu y tong hop", labelBg, color.white)
        cell(5, 1, "P25: " + fmtPrice(coreBand25), valueBg, color.white)
        cell(5, 2, "P50: " + fmtPrice(coreBand50), valueBg, color.white)
        cell(5, 3, "P75: " + fmtPrice(coreBand75), valueBg, color.white)
        cell(5, 4, bandPos, positionBg(bandPos), color.white)
        cell(5, 5, "Rong: " + fmtPct(bandWidth), qualityBg(bandDist), color.white)

        cell(6, 0, "Dong thuan", labelBg, color.white)
        cell(6, 1, coreConsensus, qualityBg(coreConsensus), color.white)
        cell(6, 2, "Lech: " + fmtPct(coreDispersion), qualityBg(coreConsensus), color.white)
        cell(6, 3, "Avg: " + fmtPrice(coreAvg), valueBg, color.white)
        cell(6, 4, "Gia ngu y co trong so: " + fmtPrice(weightedCore), valueBg, color.white)
        cell(6, 5, "Outlier: " + modelOutlier, outlierBg(modelOutlier), color.white)

    if panelMode == "Chan doan"
        cell(0, 0, "VN VALMODEL LAB v2.3a", headerBg, color.white)
        cell(0, 1, syminfo.ticker, headerBg, color.white)
        cell(0, 2, "CHAN DOAN", headerBg, color.white)
        cell(0, 3, "Du lieu mo hinh", headerBg, color.white)
        cell(0, 4, frameworkQuality, qualityBg(frameworkQuality), color.white)

        cell(1, 0, "Mo hinh", labelBg, color.white)
        cell(1, 1, "Do ben", labelBg, color.white)
        cell(1, 2, "Dong thuan khung", labelBg, color.white)
        cell(1, 3, "Vi tri multiple lich su", labelBg, color.white)
        cell(1, 4, "Muc phu hop", labelBg, color.white)
        cell(1, 5, "Lech TB/Median", labelBg, color.white)

        cell(2, 0, "PE", modelBg(showPEModel, peImp5), color.white)
        cell(2, 1, peRobust + " " + fmtPct(peRobustGap), qualityBg(peRobust), color.white)
        cell(2, 2, peHorizon + " " + fmtPct(peHorizonDisp), qualityBg(peHorizon), color.white)
        cell(2, 3, fmtPct(peRank) + " " + peRankLabel, qualityBg(peRankLabel), color.white)
        cell(2, 4, peSuit, qualityBg(peSuit), color.white)
        cell(2, 5, peSkew, qualityBg(peSkew), color.white)

        cell(3, 0, "PB", modelBg(showPBModel, pbImp5), color.white)
        cell(3, 1, pbRobust + " " + fmtPct(pbRobustGap), qualityBg(pbRobust), color.white)
        cell(3, 2, pbHorizon + " " + fmtPct(pbHorizonDisp), qualityBg(pbHorizon), color.white)
        cell(3, 3, fmtPct(pbRank) + " " + pbRankLabel, qualityBg(pbRankLabel), color.white)
        cell(3, 4, pbSuit, qualityBg(pbSuit), color.white)
        cell(3, 5, pbSkew, qualityBg(pbSkew), color.white)

        cell(4, 0, "PS", modelBg(showPSModel, psImp5), color.white)
        cell(4, 1, psRobust + " " + fmtPct(psRobustGap), qualityBg(psRobust), color.white)
        cell(4, 2, psHorizon + " " + fmtPct(psHorizonDisp), qualityBg(psHorizon), color.white)
        cell(4, 3, fmtPct(psRank) + " " + psRankLabel, qualityBg(psRankLabel), color.white)
        cell(4, 4, psSuit, qualityBg(psSuit), color.white)
        cell(4, 5, psSkew, qualityBg(psSkew), color.white)

        cell(5, 0, "Chat luong du lieu/mo hinh", labelBg, color.white)
        cell(5, 1, frameworkQuality, qualityBg(frameworkQuality), color.white)
        cell(5, 2, "Rel avg: " + fmt(avgReliabilityScore), noteBg, color.white)
        cell(5, 3, "Suit avg: " + fmt(avgSuitScore), noteBg, color.white)
        cell(5, 4, "Hor avg: " + fmt(avgHorizonScore), noteBg, color.white)
        cell(5, 5, "Consensus: " + coreConsensus, qualityBg(coreConsensus), color.white)

        cell(6, 0, "Trang thai du lieu", labelBg, color.white)
        cell(6, 1, "PE: " + peDataStatus, statusBg(peDataStatus), color.white)
        cell(6, 2, "PB: " + pbDataStatus, statusBg(pbDataStatus), color.white)
        cell(6, 3, "PS: " + psDataStatus, statusBg(psDataStatus), color.white)
        cell(6, 4, "Outlier: " + modelOutlier, outlierBg(modelOutlier), color.white)
        cell(6, 5, "Gap: " + fmtPct(maxOutGap), outlierBg(modelOutlier), color.white)

    if panelMode == "Day du"
        cell(0, 0, "VN VALMODEL LAB v2.3a", headerBg, color.white)
        cell(0, 1, syminfo.ticker, headerBg, color.white)
        cell(0, 2, "DAY DU", headerBg, color.white)
        cell(0, 3, "Advanced Diagnostics", headerBg, color.white)
        cell(0, 4, "PE/PB/PS", headerBg, color.white)
        cell(0, 5, "No DCF", headerBg, color.white)
        cell(0, 6, "No PFCF", headerBg, color.white)
        cell(0, 7, "No Target", headerBg, color.white)
        cell(0, 8, "Framework", headerBg, color.white)
        cell(0, 9, frameworkQuality, qualityBg(frameworkQuality), color.white)

        cell(1, 0, "Mo hinh", labelBg, color.white)
        cell(1, 1, "1 nam", labelBg, color.white)
        cell(1, 2, "3 nam", labelBg, color.white)
        cell(1, 3, "5 nam", labelBg, color.white)
        cell(1, 4, "Trang thai", labelBg, color.white)
        cell(1, 5, "Do tin cay", labelBg, color.white)
        cell(1, 6, "Do ben", labelBg, color.white)
        cell(1, 7, "Dong thuan khung", labelBg, color.white)
        cell(1, 8, "Vi tri", labelBg, color.white)
        cell(1, 9, "Phu hop", labelBg, color.white)

        cell(2, 0, "PE", modelBg(showPEModel, peImp5), color.white)
        cell(2, 1, fmtPrice(peImp1), valueBg, color.white)
        cell(2, 2, fmtPrice(peImp3), valueBg, color.white)
        cell(2, 3, fmtPrice(peImp5), modelBg(showPEModel, peImp5), color.white)
        cell(2, 4, peRegime + " " + fmtPct(peDrift), qualityBg(peRegime), color.white)
        cell(2, 5, peReliability, qualityBg(peReliability), color.white)
        cell(2, 6, peRobust + " " + fmtPct(peRobustGap), qualityBg(peRobust), color.white)
        cell(2, 7, peHorizon + " " + fmtPct(peHorizonDisp), qualityBg(peHorizon), color.white)
        cell(2, 8, fmtPct(peRank) + " " + peRankLabel, qualityBg(peRankLabel), color.white)
        cell(2, 9, peSuit, qualityBg(peSuit), color.white)

        cell(3, 0, "PB", modelBg(showPBModel, pbImp5), color.white)
        cell(3, 1, fmtPrice(pbImp1), valueBg, color.white)
        cell(3, 2, fmtPrice(pbImp3), valueBg, color.white)
        cell(3, 3, fmtPrice(pbImp5), modelBg(showPBModel, pbImp5), color.white)
        cell(3, 4, pbRegime + " " + fmtPct(pbDrift), qualityBg(pbRegime), color.white)
        cell(3, 5, pbReliability, qualityBg(pbReliability), color.white)
        cell(3, 6, pbRobust + " " + fmtPct(pbRobustGap), qualityBg(pbRobust), color.white)
        cell(3, 7, pbHorizon + " " + fmtPct(pbHorizonDisp), qualityBg(pbHorizon), color.white)
        cell(3, 8, fmtPct(pbRank) + " " + pbRankLabel, qualityBg(pbRankLabel), color.white)
        cell(3, 9, pbSuit, qualityBg(pbSuit), color.white)

        cell(4, 0, "PS", modelBg(showPSModel, psImp5), color.white)
        cell(4, 1, fmtPrice(psImp1), valueBg, color.white)
        cell(4, 2, fmtPrice(psImp3), valueBg, color.white)
        cell(4, 3, fmtPrice(psImp5), modelBg(showPSModel, psImp5), color.white)
        cell(4, 4, psRegime + " " + fmtPct(psDrift), qualityBg(psRegime), color.white)
        cell(4, 5, psReliability, qualityBg(psReliability), color.white)
        cell(4, 6, psRobust + " " + fmtPct(psRobustGap), qualityBg(psRobust), color.white)
        cell(4, 7, psHorizon + " " + fmtPct(psHorizonDisp), qualityBg(psHorizon), color.white)
        cell(4, 8, fmtPct(psRank) + " " + psRankLabel, qualityBg(psRankLabel), color.white)
        cell(4, 9, psSuit, qualityBg(psSuit), color.white)

        cell(5, 0, "Vung ngu y " + bandModel, labelBg, color.white)
        cell(5, 1, "P25: " + fmtPrice(band25), valueBg, color.white)
        cell(5, 2, "P50: " + fmtPrice(band50), valueBg, color.white)
        cell(5, 3, "P75: " + fmtPrice(band75), valueBg, color.white)
        cell(5, 4, bandPos, positionBg(bandPos), color.white)
        cell(5, 5, "Norm: " + fmtPct(bandNormPos), positionBg(bandPos), color.white)
        cell(5, 6, "Rong: " + fmtPct(bandWidth), qualityBg(bandDist), color.white)
        cell(5, 7, bandDist, qualityBg(bandDist), color.white)
        cell(5, 8, "Core P50: " + fmtPrice(coreBand50), noteBg, color.white)
        cell(5, 9, "Core Band", noteBg, color.white)

        cell(6, 0, "Dong thuan", labelBg, color.white)
        cell(6, 1, "Avg: " + fmtPrice(coreAvg), valueBg, color.white)
        cell(6, 2, "Gia ngu y co trong so: " + fmtPrice(weightedCore), valueBg, color.white)
        cell(6, 3, "Range: " + fmtPct(coreRange), valueBg, color.white)
        cell(6, 4, "Disp: " + fmtPct(coreDispersion), qualityBg(coreConsensus), color.white)
        cell(6, 5, coreConsensus, qualityBg(coreConsensus), color.white)
        cell(6, 6, "Quality", noteBg, color.white)
        cell(6, 7, consensusQuality, qualityBg(consensusQuality), color.white)
        cell(6, 8, "Lech nhat: " + modelOutlier, outlierBg(modelOutlier), color.white)
        cell(6, 9, "Gap: " + fmtPct(maxOutGap), outlierBg(modelOutlier), color.white)

        cell(7, 0, "Luu y", labelBg, color.white)
        cell(7, 1, "Gia ngu y", noteBg, color.white)
        cell(7, 2, "Khong phai gia muc tieu", noteBg, color.white)
        cell(7, 3, "Khong khuyen nghi mua ban", noteBg, color.white)
        cell(7, 4, "Phu thuoc du lieu TV", noteBg, color.white)