# Maternal Mortality Disparities Across U.S. States

## Overview
This project examines racial disparities in pregnancy-related maternal mortality across U.S. states (2018-2024), and tests whether the size of the Black-White mortality gap is associated with how rural or urban a state is.

## Data Sources
- **Births**: CDC WONDER Natality data, by state of residence and mother's race (2018-2024)
- **Deaths**: CDC WONDER Underlying Cause of Death data, filtered to pregnancy-related causes (ICD-10 codes O00-O99), by state and race (2018-2024)
- **Rurality**: NCHS Urban-Rural Classification Scheme for Counties (2023 vintage), aggregated to the state level

## Methodology
- Maternal mortality rate calculated as deaths per 100,000 live births, by state and race
- States with fewer than both Black and White race categories reported (due to CDC data suppression for small counts) were excluded, leaving 32 states with complete data
- Rurality was measured two ways: (1) percentage of a state's counties classified as nonmetro/rural, and (2) percentage of a state's *population* living in rural counties (a population-weighted measure)
- Disparity was measured as both a raw gap (Black rate minus White rate) and a ratio (Black rate divided by White rate)

## Findings

### 1. The racial gap in maternal mortality is universal
In all 32 states with sufficient data, Black mothers had a higher maternal mortality rate than White mothers — with no exceptions. Gaps ranged from about 11 to 96 deaths per 100,000 births, and ratios ranged from roughly 1.6x to over 4x.

![Black vs White maternal mortality rate by state](images/black_white_mortality_by_state.png)

### 2. Rurality does not meaningfully predict the size of the gap
Correlation between rurality and the disparity gap was weak across both measures tested:

| Rurality Measure | vs. Disparity Gap | vs. Disparity Ratio |
|---|---|---|
| % of counties rural | 0.16 | 0.02 |
| % of population in rural counties | 0.27 | -0.004 |

![Rurality vs disparity gap scatterplot](images/rurality_vs_disparity_gap.png)

Both correlations fall well below the threshold typically needed to call a relationship even suggestive, especially with a sample of 32 states. States that are highly rural (e.g., Kansas, Louisiana) and highly urban (e.g., New Jersey, California) both appear across the full range of disparity sizes.

## Limitations
- **State-level rurality may be too coarse.** Disparities in access to maternal care are often more of a county- or hospital-level phenomenon (e.g., distance to the nearest obstetric unit, rural hospital closures) than something that shows up cleanly at the state level.
- **Small sample size.** Only 32 states had complete data for both races, limiting statistical power to detect a weaker relationship if one exists.
- **This tests one possible driver among several.** A null result for rurality doesn't rule out other explanations for the disparity (e.g., differences in access to quality care, bias in clinical treatment, or underlying health disparities) — it only tells us rurality specifically isn't a strong predictor of gap *size*.

## Conclusion
The Black-White gap in maternal mortality is large and consistent across nearly every U.S. state, regardless of how rural or urban that state is. This suggests the disparity is likely driven by factors that operate broadly across geography, rather than being an artifact of rural healthcare access specifically.

## Tools
Python, pandas, matplotlib