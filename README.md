# TDS-week-8-q8
24f2004824@ds.study.iitm.ac.in

# E-commerce Retention Analysis — 2024 (Quarterly)

**Author / Contact:** 24f2004824@ds.study.iitm.ac.in

**Repository purpose:** This PR contains the data analysis, visualizations, and a short data-story explaining the declining customer retention and recommended actions. The analysis was assisted by an LLM (Jules / ChatGPT Codex) — see `LLM_ASSISTANCE.md`.

---

## Executive summary

- **Current average customer retention rate (2024):** **72.58**.
- **Industry benchmark target:** **85.00**.
- **Observed trend:** Retention started low in Q1–Q2 (68.35, 69.02), improved in Q3–Q4 (75.00, 77.94), but still remains substantially below the 85 benchmark.
- **Primary recommended solution:** **Implement targeted retention campaigns.**

This README documents findings, business implications, and concrete recommendations to help the company reach the 85% retention target.

---

## Data & Key numbers

Quarterly retention rates (2024):
- Q1: 68.35
- Q2: 69.02
- Q3: 75.00
- Q4: 77.94

**Average (2024): 72.58**

Industry target: **85.00**

(These are the exact values used in the analysis and visualization.)

---

## Visualizations

The chart `analysis/figures/retention_trend_vs_benchmark.png` shows:
- the 2024 quarterly retention trend,
- the computed average (72.58) as a dotted line,
- the industry benchmark (85) as a dashed line.

(See the `analysis` folder for code that reproduces this chart.)

---

## Key findings

1. **Below-benchmark performance:** The 2024 average retention rate (72.58) is 12.42 percentage points below the target of 85. This is material — it represents a meaningful shortfall in customer loyalty.
2. **Improving trend late in the year:** Retention improved from 69.02 in Q2 to 77.94 in Q4 — a positive sign that recent initiatives may be working, but the magnitude is not yet sufficient.
3. **Seasonality or recent program effects:** The improvement in Q3–Q4 suggests either seasonal factors or effects from actions taken mid-year. We must test which.
4. **Opportunity vs risk:** Small incremental improvements (e.g., +2–4 pp per quarter) compound. But current pace is unlikely to reach 85 within one year without targeted work.

---

## Business implications

- **Revenue and CAC:** Lower retention increases lifetime customer acquisition cost (LTV/CAC declines). If churn remains elevated, ARPU and long-term revenue will be negatively impacted.
- **Marketing spend efficiency:** More acquisition spend is required to offset churn instead of investing to strengthen existing relationships.
- **Product & CX signals:** Declining or low retention can reflect product gaps, UX friction, pricing mismatch, or poor onboarding/post-purchase experience.
- **Strategic priority:** Improving retention is typically a higher ROI lever than marginal customer acquisition — prioritized investments here can improve profitability faster.

---

## Specific recommendations (to reach the 85 target)

**Overarching solution**: **Implement targeted retention campaigns** — a coordinated program combining segmentation, personalization, re-engagement, loyalty incentives, and product/experience fixes.

Tactical plan (30–90–180 day roadmap):

### 30-day (quick wins)
1. **Segment and measure**:
   - Create retention segments (new customers: 0–3 months, 3–12 months, 12+ months; high-frequency vs low-frequency; high vs low order value).
   - Identify segments with highest churning rates.
2. **Win-back drip**:
   - Launch a short email + SMS win-back flow for customers inactive for 30–90 days, with a personalized offer (e.g., tailored discounts, curated product picks).
3. **Critical UX fixes**:
   - Audit checkout and post-purchase flows for friction (cart abandonment, delivery delays). Fix top 1–3 friction points.

### 90-day (medium term)
4. **Personalized retention campaigns**:
   - Use behavior-driven triggers (browsing without buying, cart abandonment with prior purchases, price drop alerts).
   - Tailor offers based on segment (e.g., loyalty credits for high-LTV customers; limited-time discount for price-sensitive segments).
5. **Onboarding program**:
   - For new customers, a 4–6 step onboarding email sequence showing value, recommended products, and how to get support.
6. **Analyze product/price fit**:
   - Run cohort analysis to detect product categories with higher churn.
   - Adjust pricing or bundles where appropriate.

### 180-day (strategic)
7. **Loyalty program & retention KPI targets**:
   - Design a points-based loyalty program rewarding repeat purchases, referrals, and app engagement.
   - Set quarterly retention KPIs (e.g., +4 pp next quarter, +3 pp next quarter).
8. **A/B test and measure**:
   - Run randomized experiments on offers, messaging, and onboarding to identify what lifts retention most cost-effectively.
9. **Cross-functional ops**:
   - Put in place a retention squad (growth, product, ops, analytics) to continuously measure, iterate, and scale winning tactics.

---

## How the recommendation ties to the target (85)

- The proposed targeted campaigns focus on the highest-impact customers (high LTV, mid-term customers) and the biggest drivers of churn (onboarding, UX friction).
- Conservative modeling: if targeted campaigns lift average retention by +4 percentage points in the first 2 quarters and +3 in the next 2, we would be close to or reach 85 within a year.
- The ROI is attractive because retention improvements increase LTV without proportionally increasing CAC.

---

## Implementation considerations & dashboarding

- Track retention by cohort (by acquisition month) and by segment.
- Build a dashboard showing rolling retention, LTV, churn, and impact of campaigns.
- Measure incremental lift with holdout groups to avoid overestimating campaign effects.

---

## Reproducibility & LLM assistance

- Code to reproduce charts and numbers is in `analysis/retention_analysis.py`.
- This PR contains explicit LLM assistance. See `LLM_ASSISTANCE.md`.

---

## Contact

24f2004824@ds.study.iitm.ac.in
