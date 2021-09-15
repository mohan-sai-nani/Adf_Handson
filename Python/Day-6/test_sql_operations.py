from sql_operations import DbOperations
import pytest


@pytest.mark.parametrize("input_list, response, reason",
                         "(['Mohan', 'Sai', 'Regulagaddi', '1999-11-03', 'M', 'Indian', 'Vizag',"
                         "'Andhra Pradesh', 530045, 'BE', 42000, 'ADF1234'],"
                         "'Validation Failure', 'Age is less than expected.'),"
                         "(['Mohan', 'Sai', 'Regulagaddi', '1998-11-03', 'M', 'Indian', 'Vizag',"
                         "'Andhra Pradesh', 530045, 'BE', 42000, 'ADF1234'],"
                         "'Success', 'null')"
                         )
def test_input(input_list):
    pass
