"""
clean_data.py

Functions to clean and merge CDC WONDER mortality/natality exports
with the NCHS urban-rural classification.

Usage (from a notebook):
    from src.clean_data import load_wonder_export, calculate_prmr, merge_with_rural_data
"""

import pandas as pd


def load_wonder_export(filepath: str) -> pd.DataFrame:
    """
    CDC WONDER exports are tab-delimited .txt files by default, with a
    footer of notes below the data rows. This strips the footer and
    returns a clean DataFrame.
    """
    df = pd.read_csv(filepath, sep="\t")
    # WONDER exports typically mark the start of footnotes with a row
    # where the first column starts with '---' or is blank/NaN across all columns.
    # Inspect your specific export and adjust this line if needed:
    df = df.dropna(how="all")
    return df


def calculate_prmr(deaths: int, live_births: int) -> float:
    """Pregnancy-related mortality ratio per 100,000 live births."""
    if live_births == 0:
        return None
    return (deaths / live_births) * 100_000


def merge_with_rural_data(mortality_df: pd.DataFrame, rural_df: pd.DataFrame,
                           state_col: str = "State") -> pd.DataFrame:
    """
    Merge state-level mortality data with NCHS rural-urban classification.
    rural_df should have a 'State' column and a 'percent_rural' column
    (you'll calculate this from county-level NCHS codes).
    """
    return mortality_df.merge(rural_df, on=state_col, how="left")
