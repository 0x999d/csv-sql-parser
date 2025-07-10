import subprocess
import pytest

def run_awith_args(*args):
    result = subprocess.run(
        ['python', 'src/main.py'] + list(args),
        capture_output=True,
        text=True
    )
    return result

def test_with_invalid_args():
    result = run_awith_args("--file=files/test.csv", "gejogfojfg")
    assert result.returncode != 0

def test_where():
    result = run_awith_args( "--file=files/test.csv", '--where=Age=25')
    assert result.returncode == 0 
    assert "25" in result.stdout  

def test_where_with_break_args():
    result = run_awith_args("--file=files/test.csv", "--where=A2e")
    assert result.returncode != 0 

def test_where_with_invalid_args():
    result = run_awith_args("--file=files/test.csv", "--where=A2e=0")
    assert result.returncode != 0 

def test_aggregate():
    result = run_awith_args( "--file=files/test.csv", '--aggregate=Age=min')
    assert "25" in result.stdout  
    assert result.returncode == 0 

def test_aggregate_with_fake_table():
    result = run_awith_args("--file=files/test.csv", "--aggregate=A2e")
    assert result.returncode != 0 

def test_where_with_invalid_args():
    result = run_awith_args("--file=files/test.csv", "--aggregate=ASDf=min")
    assert result.returncode != 0 

def test_where_with_aggregate():
    result = run_awith_args("--file=files/test.csv", "--aggregate=Age=avg", "--where=Age=25")
    assert result.returncode == 0 

def test_order():
    result = run_awith_args("--file=files/test.csv", "--order-by=Age=desc")
    assert result.returncode == 0

def test_order_with_invalid_args():
    result = run_awith_args("--file=files/test.csv", "--order-by=desc")
    assert result.returncode != 0

def test_order_with_where():
    result = run_awith_args("--file=files/test.csv", "--order-by=Age=asc", "--where=Age>=25")
    assert result.returncode == 0

def test_order_with_aggregate():
    result = run_awith_args("--file=files/test.csv", "--aggregate=Age=avg", "--order-by=desc")
    assert result.returncode != 0