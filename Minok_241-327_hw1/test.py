import subprocess
import pytest

# Для Windows
INTERPRETER = 'python'


def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False 
    )
    return proc.stdout.strip()



test_data = {
    'python_if_else': [
        (['1'], 'Weird'),
        (['4'], 'Not Weird'),
        (['3'], 'Weird'),
        (['6'],'Weird'),
        (['22'], 'Not Weird'),
        (['101'], "1 <= N <= 100"),
        (['0'], "1 <= N <= 100"),
    ],
    'arithmetic_operators': [
        (['1', '2'], ['3', '-1', '2']),
        (['10', '5'], ['15', '5', '50']),
        (['0', '5'], ["1 <= A <= 10^10 AND 1 <= B <= 10^10"]),
        (['5', str(10**10+1)], ["1 <= A <= 10^10 AND 1 <= B <= 10^10"])
    ],
    'division':[
        (['10', '2'], ['5', '5.0']),
        (['3', '5'], ['0', '0.6']),
        (['1', '3'], ['0', pytest.approx(1/3)]),
        (['11', '3'], ['3', pytest.approx(11/3)]),
        (['0', '5'], ['0', '0.0']),
        (['10', '0'], ['undefined: division by zero is not allowed', 'undefined: division by zero is not allowed']),
    ],
    'loops':[
        (['1'], ['0']),
        (['20'], ['0', '1', '4', '9', '16', '25', '36', '49', '64', '81', '100', '121', '144', '169', '196', '225', '256', '289', '324', '361']),
        (['3'], ['0', '1', '4']),
        (['0'], ['1 <= N <= 20']),
        (['21'], ['1 <= N <= 20']),
    ],
    'print_function':[
        (['20'], '1234567891011121314151617181920'),
        (['1'], '1'),
        (['7'], '1234567'),
        (['0'], '1 <= N <= 20'),
        (['21'], '1 <= N <= 20'),
    ],
    'second_score':[
        (['5', '2 3 6 6 5'], '5'),
        (['5', '5 4 3 2 1'], '4'),
        (['5', '9 10 8 7 6'], '9'),
        (['6', '10 20 10 20 10 20'], '10'),
    ],
    'nested_list':[
        (['5', 'Harry', '37.21', 'Berry', '37.21', 'Tina', '37.2', 'Akriti', '41', 'Harsh', '39'],
     ['Berry', 'Harry']),
        (['3', 'alpha', '50.0', 'beta', '50.0', 'chi', '20.0'], ['alpha', 'beta']),
        (['2', 'First', '10.0', 'Second', '20.0'], ['Second']),
        (['3', 'A', '30.0', 'B', '20.0', 'C', '10.0'], ['B']),
        (['4', 'W', '40.0', 'X', '30.0', 'Y', '30.0', 'Z', '20.0'], ['X', 'Y']),
        (['4', 'A', '-100.0', 'B', '-50.0', 'C', '-50.0', 'D', '0.0'], ['B', 'C']),
        (['4', 'Close1', '10.001', 'Close2', '10.002', 'Close3', '10.003', 'Far', '20.0'], ['Close2']),
    ],
    'lists':[
        (['12',
      'insert 0 5',
      'insert 1 10',
      'insert 0 6',
      'print',
      'remove 6',
      'append 9',
      'append 1',
      'sort',
      'print',
      'pop',
      'reverse',
      'print'],
     ['[6, 5, 10]',
      '[1, 5, 9, 10]',
      '[9, 5, 1]']),
        (['3',
      'append 100',
      'pop',
      'print'],
     ['[]']),
        (['4',
      'append 10',
      'append 20',
      'reverse',
      'print'],
     ['[20, 10]']),
        (['5',
      'append 10',
      'append -5',
      'append 0',
      'sort',
      'print'],
     ['[-5, 0, 10]']),
        (['6',
      'append 1',
      'append 2',
      'append 3',
      'append 2',
      'remove 2',
      'print'],
     ['[1, 3, 2]']),
        (['6',
      'append 1',
      'append 3',
      'insert 1 2',
      'print',
      'insert 0 0',
      'print'],
     ['[1, 2, 3]',
      '[0, 1, 2, 3]']),
        (['6',
      'append 1',
      'insert 0 0',    
      'insert 3 3',    
      'insert 2 2',    
      'print'],
     ['[0, 1, 2, 3]']),
       (['9',
      'append 10',
      'print',
      'append 20',
      'print',
      'append 30',
      'print',
      'reverse',
      'print'],
     ['[10]',
      '[10, 20]',
      '[10, 20, 30]',
      '[30, 20, 10]']),
        (['0'],
     ['']), 
    ],
    'swap_case':[
        (['Www.MosPolytech.ru'], 'wWW.mOSpOLYTECH.RU'),
        (['Pythonist 2'], 'pYTHONIST 2'),
        (['12345'], '12345'),
        (["Don't stop!"], "dON'T STOP!"),
        (['aB!cD@eF#'], 'Ab!Cd@Ef#'),
        (['a'*10000], '0 < len(string) <= 1000'),
    ],
    'split_and_join':[
        (['this is a string'], 'this-is-a-string'),
        (['this    is    a    string'], 'this-is-a-string')
    ],
    'anagram':[
        (['listen', 'silent'], 'YES'),
        (['hello', 'world'], 'NO'),
        ([' ', ' '], 'YES'), 
        (['a', 'b'], 'NO'),
        (['a', 'A'], 'NO'),
        (['a!b@', 'b@a!'], 'YES'),
        (['a'*10000], '0 < len(string) <= 1000'),

    ],
    'metro':[
        (['3', '5 10', '1 7', '8 12', '6'], '2'), 
        (['3', '5 10', '1 7', '8 12', '5'], '2'),
        (['3', '5 10', '1 7', '8 12', '10'], '2'),
        (['1', '0 60', '0'], '1'),
        (['1', '0 60', '61'], '0'),
        (['3', '0 10', '20 30', '40 50', '15'], '0'),
        (['3', '0 100', '20 80', '40 60', '50'], '3'),
        (['4', '0 10', '20 30', '40 50', '60 70', '15'], '0'),
    ],
    'minion_game':[
        (['BANANA'], 'Стюарт 12'),
        (['A'], 'Кевин 1'), 
        (['B'], 'Стюарт 1'),
        (['AAA'], 'Кевин 6'),
        (['BCD'], 'Стюарт 6'),
        (['a'*10000], '0 < len(string) <= 1000'),
        
    ],
    'is_leap':[
        (['2016'], 'True'),
        (['2020'], 'True'),
        (['2024'], 'True'),
        (['2017'], 'False'),
        (['2018'], 'False'),
        (['2019'], 'False'),
        (['1000'], '1900 <= YEAR <= 10^5'),
        ([str(10**5+1)], '1900 <= YEAR <= 10^5'),
    ],
    'happiness':[
        (['3 2', '1 5 3', '3 1', '5 7'], '1'),
        (['1 1', '5', '5', '10'], '1'),
        (['1 1', '5', '10', '5'], '-1'),
        (['1 1', '5', '2', '3'], '0'),
        (['0 0'], '1 <= N <= 10**5 1 <= M <= 10**5'),
        (['1 1', str(10**9+1, str(10**9+1)], '1 <= EACH NUMBER <= 10**9'),
    ],
    'pirate_ship':[
        (['10 3', 'золото 5 100', 'серебро 4 60', 'медь 6 50'],
     ['золото 5.00 100.00', 'серебро 4.00 60.00', 'медь 1.00 8.33']),
        (['10 3', 'тяжелый 9 90', 'легкий 1 20', 'средний 5 60'],
     ['средний 5.00 60.00', 'тяжелый 4.00 40.00', 'легкий 1.00 20.00']),
    ],
    'matrix_mult':[
        (['2', '1 2', '3 4', '5 6', '7 8'],
     ['19 22', '43 50']),
        (['2', '1 0', '0 1', '5 6', '7 8'],
     ['5 6', '7 8']),
        (['3', '1 0 0', '0 1 0', '0 0 1', '2 0 0', '0 2 0', '0 0 2'],
     ['2 0 0', '0 2 0', '0 0 2']),
        (['2', '-1 -2', '-3 -4', '-5 -6', '-7 -8'],
     ['19 22', '43 50']),
    ],
}


def test_hello():
    assert run_script('hello.py') == 'Hello, world!'

@pytest.mark.parametrize("input_data, expected", test_data['python_if_else'])
def test_python_if_else(input_data, expected):
    assert run_script('python_if_else.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['arithmetic_operators'])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['division'])
def test_division(input_data, expected):
    res = run_script('division.py', input_data).split('\n')
    assert res[0] == expected[0]
    if isinstance(expected[1], str):
        assert res[1] == expected[1]
    else:
        assert float(res[1]) == expected[1]

@pytest.mark.parametrize("input_data, expected", test_data['loops'])
def test_loops(input_data, expected):
    assert run_script('loops.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['print_function'])
def test_print_function(input_data, expected):
    assert run_script('print_function.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['second_score'])
def test_second_score(input_data, expected):
    assert run_script('second_score.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['nested_list'])
def test_nested_list(input_data, expected):
    assert run_script('nested_list.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['lists'])
def test_lists(input_data, expected):
    assert run_script('lists.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['swap_case'])
def test_swap_case(input_data, expected):
    assert run_script('swap_case.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['split_and_join'])
def test_split_and_join(input_data, expected):
    assert run_script('split_and_join.py', input_data) == expected

def test_max_word():
    assert run_script('max_word.py') == 'сосредоточенности'

def test_price_sum():
    assert run_script('price_sum.py') == '6842.84 5891.06 6810.9'

@pytest.mark.parametrize("input_data, expected", test_data['anagram'])
def test_anagram(input_data, expected):
    assert run_script('anagram.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['metro'])
def test_metro(input_data, expected):
    assert run_script('metro.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['minion_game'])
def test_minion_game(input_data, expected):
    assert run_script('minion_game.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['is_leap'])
def test_is_leap(input_data, expected):
    assert run_script('is_leap.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['happiness'])
def test_happiness(input_data, expected):
    assert run_script('happiness.py', input_data) == expected

@pytest.mark.parametrize("input_data, expected", test_data['pirate_ship'])
def test_pirate_ship(input_data, expected):
    assert run_script('pirate_ship.py', input_data).split('\n') == expected

@pytest.mark.parametrize("input_data, expected", test_data['matrix_mult'])
def test_matrix_mult(input_data, expected):
    assert run_script('matrix_mult.py', input_data).split('\n') == expected
