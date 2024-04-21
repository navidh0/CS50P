from project import Trend
import pytest

def test_dateChecker_format():
    trend = Trend()
    start_date = "Jan 30th, 2023"
    end_date = "2024-03-19"
    assert trend.date_checker(start_date, end_date) ==  "Invalid Date Format. Please try again"
def test_dateChecker_value():
    trend = Trend()
    start_date = "2024-03-18"
    end_date = "2023-03-19"

    assert trend.date_checker(start_date, end_date) == "Minimum 30 days is required. Please try again"

def test_dateChecker_invalid():
    trend = Trend()
    start_date = "invalid date"
    end_date = "2024-03-19"
    assert trend.date_checker(start_date, end_date) == "Invalid Date Format. Please try again"
