from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.mssql import MSSQL
from os import path
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_mssql(*args, **kwargs):
    """
    Template for loading data from a MSSQL database.
    Specify your configuration settings in 'io_config.yaml'.
    Set the following in your io_config:

    Docs: https://docs.mage.ai/integrations/databases/MicrosoftSQLServer
    """

    today = '2016-05-31'

    query = f'''
    SELECT 
        i.InvoiceDate,
        i.ConfirmedDeliveryTime,
        i.InvoiceID,
        il.Description,
        il.Quantity,
        il.UnitPrice,
        il.TaxRate,
        il.TaxAmount,
        il.LineProfit,
        i.TotalDryItems,
        i.TotalChillerItems
    FROM Sales.Invoices as i
    INNER JOIN Sales.InvoiceLines as il ON i.InvoiceID = il.InvoiceID
    WHERE i.InvoiceDate >= DATEADD(day, -1, CAST('{today}' AS Date))
    '''  # Specify your SQL query here
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    with MSSQL.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        return loader.load(query)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'