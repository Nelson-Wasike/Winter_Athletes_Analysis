# Sochi 2014 Winter Olympics - Athlete Demographics, Health & Delegation Equity

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-2.x-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**A cleaning pipeline and policy-oriented analysis of 2,606 Winter Olympic athletes
- sport, nationality, age, weight, and height - including a geographic bubble map
of delegation size by country.**

## The question

Two real, policy-relevant questions this dataset can actually answer: does athlete
body composition vary meaningfully - and concerningly - by sport? And how unequal
is national participation in winter sports across the 83 competing nations?

## Headline findings

- **Ski Jumping has the lowest average BMI of any sport (19.4)**, sitting right at
  the edge of the WHO underweight threshold (18.5) as a *whole-sport average* -
  meaning a substantial share of individual ski jumpers fall below it. This matches
  well-documented sports science concerns: aerodynamic advantage from low body
  weight historically drove unhealthy weight-cutting in ski jumping, prompting the
  International Ski Federation to introduce BMI-linked equipment rules.
- **Bobsleigh sits at the opposite extreme (BMI 27.5)** - explosive power and
  sled-push strength favor greater mass, the physiological opposite of ski jumping.
- **18 of 83 nations sent exactly one athlete** to these Games, while the United
  States (214) and Canada (203) alone account for roughly 16% of the entire roster
  - a striking participation gap visible directly on the geographic map.
- **Weight data is completely missing for 100% of Figure Skating and Curling
  athletes** (245 of the dataset's 326 missing weight values) - not random
  missingness, but an apparent structural gap in how those two sports were
  recorded. No BMI conclusion is possible for either sport, and the README and
  report both say so explicitly rather than leaving a silent gap.

## What's in this repo

```
winterathletes-analysis/
├── data/
│   ├── raw/
│   │   └── sampledatawinterathletes.xlsx   # original sample dataset
│   └── processed/
│       ├── athletes_clean.csv              # 2,610 athlete-sport rows, with BMI
│       ├── country_summary.csv             # 83 nations, delegation size + avg age
│       └── sport_summary.csv               # 15 sports, averages + nationality count
├── src/
│   ├── clean.py                            # multi-sport row splitting, BMI calculation
│   └── country_coords.py                   # lat/lon centroids used for the map
├── notebooks/
│   └── winter_athletes_analysis.ipynb    # full walkthrough, including map code
├── images/                                 # 4 charts, including the geographic map
├── reports/
│   └── WinterAthletes_Policy_Report.docx   # policy-oriented written report
├── requirements.txt
└── README.md
```

## How the cleaning works

1. **Multi-sport rows are split, not discarded.** A handful of athletes are listed
   with two sports in one cell (e.g. `"Cross-Country Skiing,Biathlon"`) - each such
   row is split into one row per sport, so a dual-discipline athlete is correctly
   counted in both sports' totals instead of forming a fake combined category.
2. **BMI is calculated, not estimated**, directly from each athlete's own weight
   and height (`weight_kg / height_m²`) - left as missing wherever either input is
   missing, rather than imputed.
3. **Country-level delegation counts use unique athletes**, not sport-rows, so a
   two-sport athlete isn't counted twice toward their country's total.

## The map, without internet access or a mapping library

This environment has no internet access, so libraries like `plotly` or
`geopandas` (and the shapefiles/GeoJSON they need) aren't available. The map in
`notebooks/winter_athletes_analysis.ipynb` uses a different, genuinely common
technique instead: a **geographic bubble map**, plotting each country at its real
latitude/longitude centroid (`src/country_coords.py`) on a plain coordinate grid,
sized and colored by delegation size. No shapefile, boundary data, or external
service is required - just real coordinates and `matplotlib`.

**Data source:** Sample dataset ("Winter Athletes," Sochi 2014 roster) via Contextures.com
