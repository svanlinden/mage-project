from mage_ai.io.file import FileIO
from pandas import DataFrame

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_file(data, data_2, **kwargs) -> None:
    
    filepath = 'top_products.csv'
    FileIO().export(data, filepath)

    filepath = 'totals.csv'
    FileIO().export(data_2, filepath)
