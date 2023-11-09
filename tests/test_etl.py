import pandas as pd
import pandera as pa
from pandas.testing import assert_frame_equal
import hypothesis
from hypothesis import settings, Verbosity, HealthCheck

from app.etl import flatten_df, import_data
from app.schemas import source_df_schema, output_df_schema


def test_flatten_df_by_example_based_testing():
    source_df = import_data('datasets/input.csv')
    expected = pd.read_csv('datasets/output.csv', parse_dates=['hr_ts'])
    result = flatten_df(source_df)
    
    assert_frame_equal(result, expected, check_dtype=True)

    # test other business logics
    assert (result['shows'] >= result['clicks']).all() == True


@hypothesis.given(source_df_schema.strategy(size=10))
@settings(verbosity=Verbosity.verbose, suppress_health_check=[HealthCheck.filter_too_much, HealthCheck.too_slow ])
def test_flatten_df_by_property_based_testing(dataframe):
    output_df = flatten_df(dataframe)
    assert len(output_df) > 0
