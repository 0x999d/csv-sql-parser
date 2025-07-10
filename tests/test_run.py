import subprocess
import pytest

def run_with_args(*args):
    result = subprocess.run(
        ['python', 'src/main.py'] + list(args),
        capture_output=True,
        text=True
    )
    return result

def test_runs_with_no_args():
    result = run_with_args("--file=files/test.csv")
    assert result.returncode == 0 

def test_runs_with_empty_args():
    result = run_with_args()
    assert result.returncode != 0 