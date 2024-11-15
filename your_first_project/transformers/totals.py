import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    today = '2016-05-31'

    data['TotalAmount'] = data['Quantity'] * data['UnitPrice']

    total_sales = data['TotalAmount'].sum()
    total_quantity = data['Quantity'].sum()
    total_line_profit = data['LineProfit'].sum()

    totals_df = pd.DataFrame({
        'report_date': [today],
        'total_sales': [total_sales],
        'total_quantity': [total_quantity],
        'total_line_profit': [total_line_profit]
    })

    return totals_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
