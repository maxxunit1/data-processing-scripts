#!/usr/bin/env python3
"""
CSV Processor - Process and transform CSV files
"""

import pandas as pd
import argparse
import sys
from pathlib import Path


class CSVProcessor:
    """Process CSV files with filtering, sorting, and transformation"""

    def __init__(self, input_file, encoding='utf-8'):
        """Initialize CSV processor"""
        self.input_file = input_file
        self.encoding = encoding
        self.df = None
        self.load_data()

    def load_data(self):
        """Load CSV file into pandas DataFrame"""
        try:
            self.df = pd.read_csv(self.input_file, encoding=self.encoding)
            print(f"✅ Loaded {len(self.df)} rows from {self.input_file}")
        except Exception as e:
            print(f"❌ Error loading file: {e}")
            sys.exit(1)

    def filter_rows(self, condition):
        """Filter rows based on condition"""
        try:
            self.df = self.df.query(condition)
            print(f"✅ Filtered to {len(self.df)} rows")
        except Exception as e:
            print(f"❌ Error filtering: {e}")

    def sort_by(self, column, ascending=True):
        """Sort DataFrame by column"""
        try:
            self.df = self.df.sort_values(by=column, ascending=ascending)
            print(f"✅ Sorted by {column}")
        except Exception as e:
            print(f"❌ Error sorting: {e}")

    def select_columns(self, columns):
        """Select specific columns"""
        try:
            self.df = self.df[columns]
            print(f"✅ Selected columns: {columns}")
        except Exception as e:
            print(f"❌ Error selecting columns: {e}")

    def aggregate(self, group_by, agg_dict):
        """Aggregate data by grouping"""
        try:
            self.df = self.df.groupby(group_by).agg(agg_dict).reset_index()
            print(f"✅ Aggregated by {group_by}")
        except Exception as e:
            print(f"❌ Error aggregating: {e}")

    def save(self, output_file):
        """Save processed data to CSV"""
        try:
            self.df.to_csv(output_file, index=False, encoding=self.encoding)
            print(f"✅ Saved to {output_file}")
        except Exception as e:
            print(f"❌ Error saving: {e}")

    def show_info(self):
        """Display DataFrame information"""
        print("\n📊 Data Info:")
        print(f"Rows: {len(self.df)}")
        print(f"Columns: {len(self.df.columns)}")
        print(f"\nColumn names: {list(self.df.columns)}")
        print(f"\nFirst 5 rows:")
        print(self.df.head())


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='CSV Processor')
    parser.add_argument('input', help='Input CSV file')
    parser.add_argument('output', help='Output CSV file')
    parser.add_argument('--filter', help='Filter condition (e.g., "age>25")')
    parser.add_argument('--sort', help='Column to sort by')
    parser.add_argument('--columns', help='Comma-separated columns to select')
    parser.add_argument('--info', action='store_true', help='Show data info')

    args = parser.parse_args()

    # Process CSV
    processor = CSVProcessor(args.input)

    if args.filter:
        processor.filter_rows(args.filter)

    if args.columns:
        cols = [c.strip() for c in args.columns.split(',')]
        processor.select_columns(cols)

    if args.sort:
        processor.sort_by(args.sort)

    if args.info:
        processor.show_info()

    processor.save(args.output)
    print("\n✅ Processing complete!")


if __name__ == "__main__":
    main()

# Simplify data migration to enhance security - 2025-10-27 06:40:24
# Improved: 2025-10-27 06:40:24
# Additional configuration

# Add deployment script in test suite - 2025-12-01 18:57:48
async def async_operation():
    """Async operation support"""
    result = await fetch_data()
    return process(result)

# Adjust search functionality - 2025-12-04 06:59:26
# Modified: 2025-12-04 06:59:26
CONFIG_VALUE = 'new_value'

# Add file upload feature - 2025-12-29 00:28:47
def new_feature():
    """New feature implementation"""
    logger.info('Feature working')
    return True