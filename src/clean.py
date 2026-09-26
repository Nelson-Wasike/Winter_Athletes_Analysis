"""
clean.py - Winter Olympics athlete roster cleaning pipeline (Sochi 2014,
2,606 athletes, 83 nations, 15 sports).

Two real data-quality issues are handled here:
1. A small number of rows list two sports for one athlete in a single cell
   (e.g. "Cross-Country Skiing,Biathlon") — these are split into one row
   per sport so an athlete competing in two disciplines is correctly
   counted in both, rather than creating a fake 16th/17th "sport".
2. Weight is missing for 326 athletes (12.5%) and height for 73 (2.8%) —
   left as missing rather than filled in, since guessing a physical
   measurement would misrepresent the data as more complete than it is.
"""
import pandas as pd
from pathlib import Path

RAW_PATH = Path(__file__).resolve().parents[1] / "data" / "raw" / "sampledatawinterathletes.xlsx"
OUT_DIR = Path(__file__).resolve().parents[1] / "data" / "processed"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def load_raw() -> pd.DataFrame:
    df = pd.read_excel(RAW_PATH, sheet_name="Athletes", skiprows=2)
    df.columns = ["name", "sport", "nationality", "age", "weight_kg", "height_cm"]
    return df


def split_multi_sport_rows(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["sport"] = df["sport"].str.split(",")
    df = df.explode("sport").reset_index(drop=True)
    df["sport"] = df["sport"].str.strip()
    return df


def add_bmi(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    height_m = df["height_cm"] / 100
    df["bmi"] = (df["weight_kg"] / (height_m ** 2)).round(1)
    return df


def clean_athletes() -> pd.DataFrame:
    df = load_raw()
    df = split_multi_sport_rows(df)
    df = add_bmi(df)
    return df


def build_country_summary(df: pd.DataFrame) -> pd.DataFrame:
    # Count unique athletes per country (not sport-rows, so a two-sport
    # athlete isn't double-counted in delegation size).
    unique_athletes = df.drop_duplicates(subset=["name", "nationality"])
    summary = unique_athletes.groupby("nationality").agg(
        athlete_count=("name", "count"),
        avg_age=("age", "mean"),
    ).reset_index()
    summary["avg_age"] = summary["avg_age"].round(1)
    return summary.sort_values("athlete_count", ascending=False).reset_index(drop=True)


def build_sport_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = df.groupby("sport").agg(
        athlete_count=("name", "count"),
        avg_age=("age", "mean"),
        avg_weight_kg=("weight_kg", "mean"),
        avg_height_cm=("height_cm", "mean"),
        avg_bmi=("bmi", "mean"),
        n_nationalities=("nationality", "nunique"),
    ).reset_index()
    for col in ["avg_age", "avg_weight_kg", "avg_height_cm", "avg_bmi"]:
        summary[col] = summary[col].round(1)
    return summary.sort_values("athlete_count", ascending=False).reset_index(drop=True)


def main():
    df = clean_athletes()
    print(f"Cleaned rows (athlete-sport pairs): {df.shape[0]}")
    print(f"Unique athletes: {df['name'].nunique()}")
    df.to_csv(OUT_DIR / "athletes_clean.csv", index=False)

    country_summary = build_country_summary(df)
    country_summary.to_csv(OUT_DIR / "country_summary.csv", index=False)
    print(f"Countries: {country_summary.shape[0]}")

    sport_summary = build_sport_summary(df)
    sport_summary.to_csv(OUT_DIR / "sport_summary.csv", index=False)
    print(f"Sports: {sport_summary.shape[0]}")


if __name__ == "__main__":
    main()
