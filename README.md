# Data validation and testing
### Background
* A common data processing function is like below
    ```python
    def process(df: pd.DataFrame) -> pd.DataFrame:
        ...
        return transformed_df
    ```
* You may want to
    * validate the schame of input and output dataframe
    * validate the logic is correct
    * unit test the data processing function

### Why we need data validation and testing
* To enhance the code quality and data quality
* To ensure the transforming and business logic is as expected

### [Pandera](https://pandera.readthedocs.io/en/stable/index.html#)
#### Pros
* Light weight
* Easy to use
* Support [synthesis data](https://pandera.readthedocs.io/en/stable/data_synthesis_strategies.html) by using [hypothesis](https://hypothesis.readthedocs.io/en/latest/)
* Support [schema inference](https://pandera.readthedocs.io/en/stable/schema_inference.html) that can quickly infer a draft schema

#### Cons
* Not support backend to store the validation results
* Not support UI the check the validation results

#### Check schema on pipeline
* [check_io](app/etl.py#11)

#### Schema inference
* [infer_schema](app/etl.py#26)

#### Example based unit testing
* [assert_frame_equal](tests/test_etp.py#11)

#### Property based unit testing
* [strategy](tests/test_etp.py#22)

### How to use this repository
1. Clone the repository.
2. If you use `virtualenv` you can run the following commands:
    ```sh
    virtualenv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    docker-compose up -d
    ```
3. Run `python -m pytest tests/`
4. Run `python -m app.etl`
