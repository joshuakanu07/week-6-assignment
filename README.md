 1. Project overview
This Python project implements a modular student result-processing system. It validates student details and assessment scores, calculates totals, assigns grades and grade points, and computes a credit-unit-weighted GPA.

The grading scale follows the illustrative scale in the Week 6 practical:

| Score | Grade | Grade point |

| 70–100 | A | 5 |
| 60–69 | B | 4 |
| 50–59 | C | 3 |
| 45–49 | D | 2 |
| 40–44 | E | 1 |
| 0–39 | F | 0 |

Assessment maximums are assignment = 20, test = 20 and examination = 60.

## 2. Project structure
```text
Week6_Student_Result_System/
├── main.py
├── validation.py
├── grading.py
├── result_module.py
├── test_grading.py
├── test_result_module.py
└── README.md
```

## 3. Module responsibilities
- `validation.py`: checks student identity and assessment score inputs. It raises `TypeError` for incorrect data types and `ValueError` for missing or out-of-range values.
- `grading.py`: stores the grading boundaries in one place and calculates grades and grade points.
- `result_module.py`: calculates assessment totals, generates structured result dictionaries and calculates GPA.
- `main.py`: coordinates the example workflow and displays the result.
- `test_grading.py`: tests grade boundaries, grade points and invalid scores.
- `test_result_module.py`: tests total calculation, result generation, score validation and GPA calculation.

## 4. Requirements
- Python 3.8 or later
- No third-party packages are required. The project uses Python's standard library.

Check your Python installation:
```bash
python --version
```

## 5. Running the application
Open a terminal in the project directory and run:
```bash
python main.py
```

The sample assessment total is 87, giving grade A and grade point 5. The sample GPA is 4.0.

## 6. Running automated tests
Run the complete test suite with:
```bash
python -m unittest -v
```

The test suite checks normal inputs, grade transitions, boundary values and invalid inputs. A passing test is reported as `ok`. If a test fails, inspect the assertion and traceback to identify the routine responsible.

## 7. GPA calculation
GPA is calculated as a weighted average:

`GPA = sum(grade_point × credit_unit) / sum(credit_unit)`

For the sample courses:
- 5 points × 3 units = 15
- 4 points × 2 units = 8
- 3 points × 3 units = 9

Total weighted points = 32; total credit units = 8; GPA = 32 / 8 = 4.0.

## 8. Code review and refactoring notes
The original routine in the practical has several weaknesses:
1. Single-letter function and parameter names are unclear.
2. Calculation, grading and output are combined in one routine.
3. There is no validation of input types or score ranges.
4. Its grading logic omits the D and E bands in the supplied grading scale.
5. Printing inside the calculation routine makes it harder to reuse and test.
6. There is no documented input contract or clear exception behaviour.
7. The responsibilities are not separated, making maintenance more difficult.

The refactored project separates validation, grading, result processing and presentation. Grade boundaries are centralised to avoid duplicated policy rules. Processing routines return values instead of printing them, and automated tests help confirm that the intended behaviour is preserved.

