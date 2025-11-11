#!/usr/bin/env python3
"""
Data Cleaner - Clean and validate data
"""

import pandas as pd
import numpy as np
import argparse
import sys


class DataCleaner:
    """Clean and validate data"""

    def __init__(self, input_file):
        """Initialize data cleaner"""
        self.input_file = input_file
        self.df = None
        self.load_data()

    def load_data(self):
        """Load data file"""
        try:
            self.df = pd.read_csv(self.input_file)
            print(f"✅ Loaded {len(self.df)} rows")
            self.show_stats()
        except Exception as e:
            print(f"❌ Error loading file: {e}")
            sys.exit(1)

    def show_stats(self):
        """Show data statistics"""
        print("\n📊 Data Statistics:")
        print(f"Total rows: {len(self.df)}")
        print(f"Total columns: {len(self.df.columns)}")
        print(f"Duplicates: {self.df.duplicated().sum()}")
        print(f"Missing values: {self.df.isnull().sum().sum()}")

    def remove_duplicates(self):
        """Remove duplicate rows"""
        before = len(self.df)
        self.df = self.df.drop_duplicates()
        removed = before - len(self.df)
        print(f"✅ Removed {removed} duplicate rows")

    def fill_missing_values(self, method='mean'):
        """Fill missing values"""
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns

        if method == 'mean':
            self.df[numeric_cols] = self.df[numeric_cols].fillna(
                self.df[numeric_cols].mean()
            )
        elif method == 'median':
            self.df[numeric_cols] = self.df[numeric_cols].fillna(
                self.df[numeric_cols].median()
            )
        elif method == 'zero':
            self.df[numeric_cols] = self.df[numeric_cols].fillna(0)

        # Fill string columns with 'Unknown'
        string_cols = self.df.select_dtypes(include=['object']).columns
        self.df[string_cols] = self.df[string_cols].fillna('Unknown')

        print(f"✅ Filled missing values using {method} method")

    def remove_outliers(self, columns=None, threshold=3):
        """Remove outliers using z-score"""
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns

        before = len(self.df)

        for col in columns:
            z_scores = np.abs(
                (self.df[col] - self.df[col].mean()) / self.df[col].std()
            )
            self.df = self.df[z_scores < threshold]

        removed = before - len(self.df)
        print(f"✅ Removed {removed} outlier rows")

    def standardize_columns(self):
        """Standardize column names"""
        self.df.columns = [
            col.lower().strip().replace(' ', '_')
            for col in self.df.columns
        ]
        print("✅ Standardized column names")

    def save(self, output_file):
        """Save cleaned data"""
        try:
            self.df.to_csv(output_file, index=False)
            print(f"✅ Saved to {output_file}")
        except Exception as e:
            print(f"❌ Error saving: {e}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Data Cleaner')
    parser.add_argument('input', help='Input CSV file')
    parser.add_argument('--output', default='cleaned_data.csv',
                        help='Output file')
    parser.add_argument('--remove-duplicates', action='store_true',
                        help='Remove duplicate rows')
    parser.add_argument('--fill-missing', choices=['mean', 'median', 'zero'],
                        help='Fill missing values')
    parser.add_argument('--remove-outliers', action='store_true',
                        help='Remove outliers')
    parser.add_argument('--standardize', action='store_true',
                        help='Standardize column names')

    args = parser.parse_args()

    # Clean data
    cleaner = DataCleaner(args.input)

    if args.remove_duplicates:
        cleaner.remove_duplicates()

    if args.fill_missing:
        cleaner.fill_missing_values(args.fill_missing)

    if args.remove_outliers:
        cleaner.remove_outliers()

    if args.standardize:
        cleaner.standardize_columns()

    cleaner.save(args.output)
    print("\n✅ Cleaning complete!")


if __name__ == "__main__":
    main()

# Upgrade file upload - 2025-11-11 13:57:53
# Enhanced: 2025-11-11 13:57:53
"""Documentation updated"""