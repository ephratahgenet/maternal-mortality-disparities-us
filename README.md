# Racial Disparities in U.S. Maternal Mortality: A Geographic Analysis

## Why this project
Black and American Indian/Alaska Native women in the U.S. die from pregnancy-related
causes at roughly 3x the rate of white women — a gap that has persisted for decades
and, according to CDC estimates, is about 66% preventable. As someone who works on
community health equity through Columbia Students for Global Health Equity & Medicine,
I wanted to dig into the *geographic* side of this disparity: does the racial gap in
maternal mortality get worse in rural areas with less access to care, or is it
consistent regardless of location?

## Research question
How does pregnancy-related mortality by race compare across U.S. states, and does
the size of the racial gap correlate with rural vs. urban access to maternal care?

## Data sources
- **CDC WONDER** — Natality and Underlying Cause of Death databases
  (https://wonder.cdc.gov/), queried for pregnancy-related mortality by
  state and race/ethnicity.
- **NCHS Urban-Rural Classification Scheme for Counties** — used to classify
  each state's counties (and aggregate to a state-level rural share) so mortality
  data can be compared against rural/urban access.

## Method
1. Query CDC WONDER for pregnancy-related deaths and live births by state and
   race/ethnicity (Black, White, at minimum) to calculate a pregnancy-related
   mortality ratio (PRMR) per 100,000 live births, by state and race.
2. Join state-level PRMR data with the NCHS rural-urban classification to get a
   "percent rural population" figure per state.
3. Calculate the racial gap (Black PRMR − White PRMR) for each state.
4. Test whether percent-rural correlates with the size of that gap
   (`scipy.stats.pearsonr` or `spearmanr`, since this is a small-N, non-normal dataset).
5. Visualize with a U.S. choropleth map of the racial gap by state, plus a
   scatterplot of rural share vs. gap size.

## Key finding
*(Fill this in once you've run the analysis — 2-3 sentences with the main number.
Put your best figure right below this section once it's generated.)*

## Repository structure
```
data/raw/            Original CDC WONDER and NCHS exports, unmodified
data/processed/       Cleaned, merged datasets used for analysis
notebooks/            Jupyter notebooks with the analysis, step by step
src/                  Reusable Python functions (cleaning, plotting)
figures/              Final saved plots (PNG/SVG)
```

## How to reproduce
```bash
git clone https://github.com/YOUR-USERNAME/maternal-mortality-disparities-us.git
cd maternal-mortality-disparities-us
pip install -r requirements.txt
jupyter notebook notebooks/01_data_cleaning.ipynb
```

## Data limitations
CDC WONDER suppresses small counts (fewer than 10 deaths) for privacy, which limits
state-level granularity for smaller states. Race/ethnicity on birth and death
certificates is self-reported by the mother or assigned by a certifier, which is a
known source of misclassification in vital statistics data.

## Author
Ephratah Genet — Columbia University, B.A. Computational Biology
[linkedin.com/in/ephratahgenet-010b45297](https://linkedin.com/in/ephratahgenet-010b45297)
