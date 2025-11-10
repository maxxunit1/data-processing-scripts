#!/usr/bin/env python3
"""
Batch Processor - Process multiple files in batch
"""

import pandas as pd
import argparse
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed


class BatchProcessor:
    """Process multiple files in batch mode"""

    def __init__(self, input_dir, output_dir, workers=4):
        """Initialize batch processor"""
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.workers = workers

        # Create output directory
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def process_file(self, file_path):
        """Process a single file"""
        try:
            # Read file
            if file_path.suffix == '.csv':
                df = pd.read_csv(file_path)
            elif file_path.suffix == '.json':
                df = pd.read_json(file_path)
            elif file_path.suffix in ['.xlsx', '.xls']:
                df = pd.read_excel(file_path)
            else:
                return False, f"Unsupported format: {file_path.suffix}"

            # Process data (example: remove duplicates)
            df = df.drop_duplicates()

            # Save processed file
            output_file = self.output_dir / f"processed_{file_path.name}"
            df.to_csv(output_file, index=False)

            return True, f"Processed {file_path.name}"

        except Exception as e:
            return False, f"Error processing {file_path.name}: {e}"

    def process_directory(self, pattern='*.csv', parallel=True):
        """Process all files in directory"""
        files = list(self.input_dir.glob(pattern))

        if not files:
            print(f"❌ No files found matching pattern: {pattern}")
            return

        print(f"📁 Found {len(files)} files to process")

        if parallel and len(files) > 1:
            self.process_parallel(files)
        else:
            self.process_sequential(files)

    def process_sequential(self, files):
        """Process files sequentially"""
        success_count = 0
        fail_count = 0

        for i, file_path in enumerate(files, 1):
            print(f"[{i}/{len(files)}] Processing {file_path.name}...", end=' ')

            success, message = self.process_file(file_path)

            if success:
                print("✅")
                success_count += 1
            else:
                print(f"❌ {message}")
                fail_count += 1

        self.print_summary(success_count, fail_count)

    def process_parallel(self, files):
        """Process files in parallel"""
        success_count = 0
        fail_count = 0

        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            futures = {
                executor.submit(self.process_file, f): f
                for f in files
            }

            for i, future in enumerate(as_completed(futures), 1):
                file_path = futures[future]
                print(f"[{i}/{len(files)}] {file_path.name}...", end=' ')

                try:
                    success, message = future.result()
                    if success:
                        print("✅")
                        success_count += 1
                    else:
                        print(f"❌ {message}")
                        fail_count += 1
                except Exception as e:
                    print(f"❌ Exception: {e}")
                    fail_count += 1

        self.print_summary(success_count, fail_count)

    def print_summary(self, success, fail):
        """Print processing summary"""
        print("\n" + "=" * 50)
        print("📊 BATCH PROCESSING SUMMARY")
        print("=" * 50)
        print(f"✅ Successful: {success}")
        print(f"❌ Failed: {fail}")
        print(f"📁 Output directory: {self.output_dir}")
        print("=" * 50)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Batch File Processor')
    parser.add_argument('--input-dir', required=True,
                        help='Input directory')
    parser.add_argument('--output-dir', required=True,
                        help='Output directory')
    parser.add_argument('--pattern', default='*.csv',
                        help='File pattern (default: *.csv)')
    parser.add_argument('--parallel', action='store_true',
                        help='Enable parallel processing')
    parser.add_argument('--workers', type=int, default=4,
                        help='Number of parallel workers')

    args = parser.parse_args()

    processor = BatchProcessor(
        args.input_dir,
        args.output_dir,
        args.workers
    )

    processor.process_directory(
        pattern=args.pattern,
        parallel=args.parallel
    )


if __name__ == "__main__":
    main()

# Refactor build process in file handler - 2025-10-12 03:10:13
# Improved readability
data = [
    item
    for item in collection
    if item.is_valid()
]

# Patch configuration - 2025-10-12 03:26:29
# Modified: 2025-10-12 03:26:29
CONFIG_VALUE = 'new_value'

# Build backup routine - 2025-10-19 17:43:32
# Improved: 2025-10-19 17:43:32
# Additional configuration

# Correct race condition issue - 2025-10-21 07:07:47
def handle_error(error):
    """Handle error gracefully"""
    logger.error(f'Error: {error}')
    return None

# Revise dependency - 2025-10-31 09:38:20
# Improved: 2025-10-31 09:38:20
# Additional configuration

# Adjust authentication flow - 2025-11-10 13:10:02
# Modified: 2025-11-10 13:10:02
CONFIG_VALUE = 'new_value'