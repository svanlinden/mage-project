if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    data['TotalAmount'] = data['Quantity'] * data['UnitPrice']

    top_products_df = (
    data.groupby('Description', as_index=False)
    .agg(total_quantity=('Quantity', 'sum'), total_revenue=('TotalAmount', 'sum'))
    .sort_values(by='total_quantity', ascending=False)
    .head(10)
    )

    return top_products_df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
