# Task 3 Summary: Statistical Validation & Data Segmentation for Risk Drivers

## Objective
This task focuses on statistically validating key hypotheses regarding risk drivers for insurance policies, forming the foundation of our new segmentation strategy. The goal is to identify significant differences in risk metrics across demographic and geographic features.

---

## Key Metrics
- **Claim Frequency:** Proportion of policies with at least one claim.
- **Claim Severity:** Average claim amount, conditional on a claim occurring.
- **Margin:** Defined as (TotalPremium - TotalClaims), representing profitability.

---

## Hypothesis Testing Results

### 1. Risk Differences Across Provinces (Claim Frequency)
- **Test:** One-way ANOVA
- **Result:** F-statistic = 13.5162, p-value < 0.001
- **Interpretation:** I reject the null hypothesis, indicating significant differences in claim frequency across provinces.

### 2. Risk Differences Between Zip Codes (Claim Frequency)
- **Test:** One-way ANOVA
- **Result:** F-statistic = 1.7212, p-value < 0.001
- **Interpretation:** I reject the null hypothesis, suggesting significant differences in claim frequency across zip codes.

### 3. Margin Differences Between Zip Codes
- **Test:** One-way ANOVA
- **Result:** F-statistic = 0.9242, p-value = 0.9419
- **Interpretation:** I fail to reject the null hypothesis, indicating no significant margin differences between zip codes.

### 4. Risk Differences Between Genders (Claim Frequency)
- **Test:** Independent t-test
- **Result:** t-statistic = -0.2055, p-value = 0.8372
- **Interpretation:** I fail to reject the null hypothesis, indicating no significant claim frequency difference between women and men.

---

## Data Segmentation Analysis

### Segmentation Feature: **TrackingDevice**

- **Group A (Control):** Policies without a tracking device (`TrackingDevice = No`)
- **Group B (Test):** Policies with a tracking device (`TrackingDevice = Yes`)

| Metric           | Group A           | Group B           | Statistical Test         | Result               |
|------------------|-------------------|-------------------|-------------------------|----------------------|
| Claim Frequency  | 0.0028            | 0.0027            | Independent t-test      | p = 0.2303 (Fail to reject H₀) |
| Claim Severity   | 21,561.64         | 26,190.91         | Independent t-test      | p = 0.0047 (Reject H₀)            |
| Margin          | -4.5763           | -0.9429           | Independent t-test      | p = 0.4863 (Fail to reject H₀)  |

### Control Checks for Confounding Variables

- **Gender Distribution** and **Vehicle Type Distribution** were compared between groups.
- No significant differences detected, supporting valid comparison.

---

## Conclusions

- Significant differences exist in claim frequency across provinces and zip codes.
- Gender does not significantly impact claim frequency.
- Margin does not significantly differ across zip codes.
- The presence of a tracking device is associated with a significantly higher claim severity but no difference in claim frequency or margin.
- Control checks confirm the comparability of groups in segmentation analysis.

---

## Next Steps

- Use these validated features and segments to design targeted risk-based pricing and marketing strategies.
- Conduct deeper multivariate analysis and predictive modeling incorporating these insights.
- Document and automate the testing pipeline for continuous validation.

---
Statistical Testing Summary

1. Impact of TrackingDevice on KPIs

    Claim Frequency (HasClaim)
    Chi-square test: p = 0.2417 → No significant association between having a tracking device and the likelihood of claim occurrence.

    Claim Severity
    T-test: p = 0.0047 → Significant difference in average claim severity between policies with and without a tracking device. Policies with a tracking device have higher average claim severity.

    Margin
    T-test: p = 0.4863 → No significant difference in profit margin between policies with or without a tracking device.

2. Impact of Gender on KPIs

    Claim Frequency (HasClaim)
    Chi-square test: p = 0.0299 → Significant association between gender and claim occurrence. Different genders show different claim frequencies.

    Claim Severity & Margin
    Skipped t-tests because Gender has more than two groups (e.g., Male, Female, Not specified). For more detailed analysis, consider grouping or selecting two categories.

Next Steps / Recommendations

    For features with more than two categories (like Gender), consider creating binary groups or use ANOVA tests instead of t-tests.

    Investigate why policies with tracking devices show higher claim severity — this could point to specific risk patterns or reporting differences.

    Extend testing to other features (e.g., VehicleType, Policy Type) to identify additional significant drivers.

## Scripts

- Hypothesis testing: `scripts/task_3_hypothesis_testing.py`
- Segmentation analysis: `scripts/task_3_segmentation_analysis.py`
- Statistical Testing Summary: `scripts/task3_Statistical_Testing.py`
---
Task 3: Hypothesis Testing and Feature Impact Analysis
🎯 Objective

Evaluate key features that may impact insurance risk metrics such as Claim Frequency, Claim Severity, and Margin. Use statistical testing to determine whether to reject the null hypotheses and interpret the implications for segmentation and strategy.
🔍 Key Hypotheses & Results
1. Risk Differences Across Provinces

    Test: ANOVA on Claim Frequency

    Result: p < 0.001 → Reject H₀

    Interpretation: Claim frequencies vary significantly between provinces, suggesting geographic segmentation could enhance risk-based pricing or risk mitigation efforts.

2. Risk Differences Between Zip Codes

    Test: ANOVA on Claim Frequency

    Result: p < 0.001 → Reject H₀

    Interpretation: Zip code plays a role in claim occurrence, reinforcing the value of micro-geographic targeting or adjusting premiums by postal zones.

3. Margin Differences Between Zip Codes

    Test: ANOVA on Margin

    Result: p = 0.94 → Fail to Reject H₀

    Interpretation: No significant profit margin difference among zip codes. This implies that while risk levels vary, the profitability remains uniform geographically.

4. Gender-Based Risk Differences

    Test: T-test on Claim Frequency

    Result: p = 0.8372 → Fail to Reject H₀

    Interpretation: No evidence of significant gender-based risk differences. Gender alone may not be a reliable basis for segmentation.

🧪 Feature-Based Statistical Testing
📌 TrackingDevice
Metric	Result	p-value	Interpretation
Claim Frequency	Chi² = 1.37	0.2417	No significant effect
Claim Severity	t = -2.83	0.0047	Significant difference → higher average severity in 'Yes' group
Margin	t = -0.69	0.4863	No significant effect

    Business Insight: Vehicles with tracking devices tend to result in higher claim severity, possibly due to high-value car owners adopting trackers. Recommend further risk profiling or incentivized premiums.

📌 Gender
Metric	Result	p-value	Interpretation
Claim Frequency	Chi² = 7.02	0.0299	Significant association
Claim Severity / Margin	—	—	Skipped due to >2 gender categories

    Business Insight: There is a weak but significant link between gender and claim frequency, although gender diversity in data is low (majority "Not specified"). Gender-based strategy is not actionable without better data quality.

💡 Strategic Implications

    Geographic Features (Province, ZipCode) are strong predictors of risk and should be used in segmentation strategies.

    Tracking Device presence correlates with claim severity, offering a potential flag for high-risk/high-value policyholders.

    Gender and ZipCode margin showed weak or no effect, and should not be prioritized without cleaner data.

📦 Recommendations

    Build Segments by Province and ZipCode for differentiated risk handling.

    Enhance Data Collection: Encourage clients to provide accurate gender data.

    Investigate High Severity Among TrackingDevice Users: Explore targeted pricing or alerts.

    Use results to inform pricing strategy and customer communications for better alignment with risk.