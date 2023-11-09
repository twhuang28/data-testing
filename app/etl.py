import pandas as pd
import duckdb
import pandera as pa
from app.schemas import source_df_schema, output_df_schema


def import_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=['hr_ts'])
    return df

@pa.check_io(source_df=source_df_schema, out=output_df_schema, lazy=True)
def flatten_df(source_df: pd.DataFrame) -> pd.DataFrame:
    sql = """
        SELECT
            hr_ts, campaign_id, creative_id,
            SUM(IF(event_id='show', count, 0))::BIGINT AS shows,
            SUM(IF(event_id='click', count, 0))::BIGINT AS clicks,
            SUM(IF(event_id='install', count, 0))::BIGINT AS installs
        FROM source_df
        GROUP BY hr_ts, campaign_id, creative_id
        ORDER BY hr_ts, campaign_id, creative_id;
    """
    output_df = duckdb.sql(sql).df()
    return output_df

def show_schema(df: pd.DataFrame):
    schema = pa.infer_schema(df)
    return schema


if __name__ == '__main__':

    df = import_data('datasets/input.csv')
    output_df = flatten_df(df)
    print('##########################')
    print(output_df.info())

    # schema inference
    schema = show_schema(df)
    print('\n')
    print('############ Schema inference #############')
    print(schema)

    print('\n')
    print('############ Schema inference to script #############')
    print(schema.to_script())

    # schema = show_schema(output_df)
    # print(schema)
    # print(schema.to_script())
