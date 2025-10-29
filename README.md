# Data Processing Scripts

Collection of Python scripts for data processing, transformation, and analysis. Handle CSV, JSON, Excel files with ease.

## ✨ Features

- 📊 CSV data processing and transformation
- 📈 Excel file manipulation
- 🔄 JSON data conversion
- 📉 Data cleaning and validation
- 📦 Batch processing support

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/data-processing-scripts.git
cd data-processing-scripts
pip install -r requirements.txt
```

### Basic Usage

```bash
# Process CSV file
python csv_processor.py input.csv output.csv

# Clean data
python data_cleaner.py data.csv

# Convert formats
python format_converter.py data.json data.csv
```

## 📦 Scripts

### csv_processor.py
Process and transform CSV files with filtering, sorting, and aggregation.

```bash
python csv_processor.py input.csv output.csv --filter "age>25" --sort name
```

### data_cleaner.py
Clean and validate data by removing duplicates, handling missing values.

```bash
python data_cleaner.py input.csv --remove-duplicates --fill-missing
```

### format_converter.py
Convert between CSV, JSON, and Excel formats.

```bash
python format_converter.py input.csv output.json
python format_converter.py data.json data.xlsx
```

### batch_processor.py
Process multiple files in batch mode.

```bash
python batch_processor.py --input-dir ./data --output-dir ./processed
```

## 📂 Project Structure

```
data-processing-scripts/
├── README.md              # Documentation
├── requirements.txt       # Dependencies
├── csv_processor.py       # CSV processing
├── data_cleaner.py        # Data cleaning
├── format_converter.py    # Format conversion
├── batch_processor.py     # Batch processing
└── .gitignore            # Git ignore
```

## 🔧 Advanced Usage

### CSV Processing

```python
from csv_processor import CSVProcessor

processor = CSVProcessor('data.csv')
processor.filter(lambda row: row['age'] > 25)
processor.sort_by('name')
processor.save('output.csv')
```

### Data Cleaning

```python
from data_cleaner import DataCleaner

cleaner = DataCleaner('data.csv')
cleaner.remove_duplicates()
cleaner.fill_missing_values(method='mean')
cleaner.save('clean_data.csv')
```

### Format Conversion

```python
from format_converter import convert

convert('data.csv', 'data.json')
convert('data.json', 'data.xlsx')
```

## 📊 Features Details

### CSV Processor
- Filter rows by conditions
- Sort by columns
- Aggregate data (sum, mean, count)
- Column selection and renaming
- Merge multiple CSV files

### Data Cleaner
- Remove duplicate rows
- Handle missing values (fill, drop, interpolate)
- Remove outliers
- Standardize data formats
- Validate data types

### Format Converter
- CSV ↔ JSON ↔ Excel
- Preserves data types
- Handles large files
- Custom encoding support

### Batch Processor
- Process directory of files
- Parallel processing support
- Progress tracking
- Error handling and logging

## 🛠️ Configuration

Create a `config.json` file:

```json
{
  "encoding": "utf-8",
  "delimiter": ",",
  "chunk_size": 10000,
  "parallel_workers": 4
}
```

## 📈 Examples

### Example 1: Filter and Sort

```bash
python csv_processor.py sales.csv filtered_sales.csv \
  --filter "revenue>1000" \
  --sort date \
  --columns date,customer,revenue
```

### Example 2: Clean Data

```bash
python data_cleaner.py users.csv \
  --remove-duplicates \
  --fill-missing mean \
  --remove-outliers
```

### Example 3: Batch Conversion

```bash
python batch_processor.py \
  --input-dir ./raw_data \
  --output-dir ./processed \
  --format json \
  --parallel
```

## 🔍 Troubleshooting

### Memory Issues

For large files, use chunking:
```python
processor.process_chunks(chunk_size=10000)
```

### Encoding Problems

Specify encoding:
```python
processor = CSVProcessor('data.csv', encoding='latin-1')
```

### Performance

Enable parallel processing:
```bash
python batch_processor.py --parallel --workers 8
```

## 📝 Best Practices

1. **Validate input data** before processing
2. **Use chunking** for large files
3. **Enable logging** for debugging
4. **Backup data** before transformation
5. **Test on sample** before full processing

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open Pull Request

## 📄 License

MIT License - see LICENSE file

---

**Made with ❤️ for data engineers**

## Update 2025-10-23 10:15:52
# Enhanced: 2025-10-23 10:15:52
"""Documentation updated"""

## Update 2025-10-29 14:37:36
@decorator
def enhanced_function():
    """Enhanced functionality"""
    return improved_result()