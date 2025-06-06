# Contributing

Thank you for considering contributing to this repository! We welcome additions and improvements to the resource list.

## How to add a resource

1. **Edit `resources.csv`**
   - Each entry should include the category, name, URL, and optionally a short description.
   - Keep entries alphabetically ordered within each category.
2. **Update `README.md`**
   - Add the new resource under the appropriate section using Markdown bullet points.
   - If you introduce a new category, update the Table of Contents as well.
   - Run `python scripts/csv_to_markdown.py > README.md` to regenerate the README from `resources.csv`.
3. **Run checks**
   - Run `python scripts/check_sorting.py` to verify entries are alphabetically sorted.
   - If the check reports issues, run `python scripts/sort_resources.py` to automatically sort the file.
   - Finally, run `python -m py_compile scripts/*.py` to ensure any Python scripts compile successfully.

Feel free to open an issue or pull request if you have questions.
