from validation import validate_student, validate_score
from grading import calculate_grade, calculate_grade_point
def calculate_total_score(assignment, test, examination):
    validate_score(assignment, 20, "Assignment")
    validate_score(test, 20, "Test")
    validate_score(examination, 60, "Examination")
    return assignment + test + examination
def generate_result(name, registration_number, course_code,
                    assignment, test, examination):
    validate_student(name, registration_number)
    if not isinstance(course_code, str) or not course_code.strip():
        raise ValueError("Course code is required")
    total = calculate_total_score(
        assignment, test, examination
    )
    return {
        "student_name": name.strip(),
        "registration_number": registration_number.strip(),
        "course_code": course_code.strip(),
        "total": total,
        "grade": calculate_grade(total),
        "grade_point": calculate_grade_point(total),
    }
def calculate_gpa(course_results):
    if not course_results:
        raise ValueError("At least one course result is required")
    weighted_points = 0
    total_units = 0
    for course in course_results:
        if not isinstance(course, dict):
            raise TypeError("Each course result must be a dictionary")
        try:
            grade_point = course["grade_point"]
            credit_unit = course["credit_unit"]
        except KeyError as error:
            raise ValueError(
                f"Missing required course field: {error.args[0]}"
            ) from error
        if (
            not isinstance(grade_point, (int, float))
            or isinstance(grade_point, bool)
        ):
            raise TypeError("Grade point must be numeric")
        if not 0 <= grade_point <= 5:
            raise ValueError("Grade point must be between 0 and 5")
        if (
            not isinstance(credit_unit, (int, float))
            or isinstance(credit_unit, bool)
        ):
            raise TypeError("Credit unit must be numeric")
        if credit_unit <= 0:
            raise ValueError("Credit unit must be positive")
        weighted_points += grade_point * credit_unit
        total_units += credit_unit
    return weighted_points / total_units