import unittest
from result_module import (
    calculate_total_score,
    generate_result,
    calculate_gpa
)
class TestResultModule(unittest.TestCase):
    def test_calculate_total_score(self):
        self.assertEqual(
            calculate_total_score(18, 17, 52), 87
        )
    def test_generate_result(self):
        result = generate_result(
            " John ",
            " CSC/2026/001 ",
            " SWE 306 ",
            18,
            17,
            52
        )
        self.assertEqual(result["student_name"], "John")
        self.assertEqual(
            result["registration_number"], "CSC/2026/001"
        )
        self.assertEqual(result["course_code"], "SWE 306")
        self.assertEqual(result["total"], 87)
        self.assertEqual(result["grade"], "A")
        self.assertEqual(result["grade_point"], 5)
    def test_score_above_component_maximum(self):
        with self.assertRaises(ValueError):
            calculate_total_score(21, 17, 52)
    def test_invalid_student_name(self):
        with self.assertRaises(ValueError):
            generate_result(
                " ",
                "CSC/2026/001",
                "SWE 306",
                18,
                17,
                52
            )
    def test_weighted_gpa(self):
        courses = [
            {"grade_point": 5, "credit_unit": 3},
            {"grade_point": 4, "credit_unit": 2},
            {"grade_point": 3, "credit_unit": 3}
        ]
        self.assertEqual(calculate_gpa(courses), 4.0)
    def test_empty_gpa_input(self):
        with self.assertRaises(ValueError):
            calculate_gpa([])
    def test_zero_credit_unit(self):
        with self.assertRaises(ValueError):
            calculate_gpa([
                {"grade_point": 4, "credit_unit": 0}
            ])
if __name__ == "__main__":
    unittest.main()