"""Dashboard for COVID.

## Stock demo
https://towardsdatascience.com/how-to-build-a-data-science-web-app-in-python-61d1bed65020
From https://github.com/restartus/demo-self-driving/blob/master/app.py
Use a main and a well formed way to run things

https://towardsdatascience.com/streamlit-101-an-in-depth-introduction-fc8aad9492f2
has more ways to do selects and tables

"""
# import logging  # noqa: F401

# https://mypy.readthedocs.io/en/latest/existing_code.html
import pandas as pd  # type:ignore
import altair as alt  # type:ignore
import streamlit as st  # type:ignore
from base import Base
from main import main
from util import Log
from model import Model
import os
import logging

# https://docs.python.org/3/howto/logging-cookbook.html
# logging.basicConfig(level=logging.DEBUG
# https://www.w3resource.com/python-exercises/python-basic-exercise-46.php
# https://www.geeksforgeeks.org/python-os-path-basename-method/
name: str = os.path.basename(__file__).split(".")[0]
log_root: Log = Log(name)
log: logging.Logger = log_root.log

log.debug("test")


def dashboard():
    """Display the decision dashboard.

    Streamlit dashboard
    """
    # sample test data
    data_df = pd.DataFrame(
        [[0, 123], [12, 23]],
        index=["healthcare", "Non-healthcare"],
        columns=["N95", "Mask"],
    )
    data_df.index.name = "Level l"
    data_df.columns.name = "Resource n"
    model = main()
    # https://stackoverflow.com/questions/1398022/looping-over-all-member-variables-of-a-class-in-python
    log.debug(f"{log=}")
    log.debug(f"{vars(model)=}")
    log.debug(f"{vars(model.population)}=")
    # https://stackoverflow.com/questions/11637293/iterate-over-object-attributes-in-python
    # this gives all kinds of things that are hidden functions;
    log.debug(f"{dir(model.population)=}")
    for name, value in vars(model).items():
        log.debug(name)
        log.debug(value)
        # http://notesbyanerd.com/2017/12/26/check-in-python-if-a-value-is-instance-of-a-custom-class/
        if isinstance(value, Base):
            log.debug(f"found ${value=} is Base")

    # https://stackoverflow.com/questions/44790030/return-all-class-variable-values-from-a-python-class
    for name, value in vars(model.population).items():
        log.debug(f"{name=}")
        log.debug(f"{value=}")

    # Simple selection
    st.sidebar.markdown(
        """
        ## Pages
        Choose the page you want from here
        """
    )
    page = st.sidebar.selectbox(
        "Choose page",
        ["Exploration", "Tables", "Home", "Test Home", "Test Tables"],
    )

    stockpile_days = st.sidebar.slider("Stockpile", max_value=120, value=30)
    log.debug(f"{stockpile_days=}")

    model.resource.set_stockpile_days(model, stockpile_days)

    if page == "Home":
        homePage(model)
    elif page == "Tables":
        tables(model)
    elif page == "Exploration":
        visualize_model(model)
    elif page == "Test Tables":
        testTables(model)
    elif page == "Test Home":
        testHome(data_df)
    elif page == "Test Exploration":
        st.title("Data Exploration")
        # https://docs.streamlit.io/en/latest/api.html
        x_axis = st.selectbox("Choose x-axis", data_df.columns, index=0)
        y_axis = st.selectbox("Choose y-axis", data_df.columns, index=1)
        visualize_data(data_df, x_axis, y_axis)
        # Not that write uses Markdown


def homePage(model):
    """Home page.

    # COVID-19 Decision Dashboard
    ## Restart.us
    Use caution when interpreting these numbers
    """


# uses the literal magic in Streamlit 0.62
# note that just putting an expression automatically wraps an st.write
def testTables(model):
    """Tables.

    The full graphical display of all tables use for debugging mainly
    """
    """
    # COVID-19 Decision Tool
    ## Restart.us
    The main data table in the model for your viewing please.
    These are all Pandas Dataframes for display. For multi-dimensional data,
    there will be both a Numpy Array for the tensor and a Multi-Index for
    display.

    When you are using these, as a hint, the row and column have distinct
    variable letters so you can keep it all straight in detailed data analysis.

    ###Resource safety Stock ln.

    The supply of resource needs
    """
    model.resource.safety_stock_ln_df

    """
    # Resource Attributes  na
    Resources main attribute is their count, but will later have volume and
    footprint
    """

    model.resource.attr_na_df
    model.description["Population.attr_pd_df"]
    model.population.attr_pd_df

    """
    # Population summarized by protection levels pl
    Population main attribute is their count, but will later have things like
    how often they are out doing work and will keep track of things like social
    mobility and columns will have characteristics like age, ethnicity, gender
    as a crosstab.t"""
    model.population.level_pl_df


def tables(model):
    """Table Exploration.

    Automatically reads from model.description a markdown string
    then displays the data found in the model by traversing the entire object
    looking for Pandas DataFrames
    """
    # https://stackoverflow.com/questions/44790030/return-all-class-variable-values-from-a-python-class
    log.debug("look for all population items")
    # eventually just go through all the model classes and keep going
    # http://effbot.org/pyfaq/how-do-i-check-if-an-object-is-an-instance-of-a-given-class-or-of-a-subclass-of-it.htm

    """
    # COVID-19 Data Table Exploration

    Use this section to look through the data. This include the descriptions
    that are included with it.
    """

    # http://net-informations.com/python/iq/instance.htm
    log.debug(f"{model} is {vars(model)}")
    # replaced by iteration
    # for model_value in model:
    # for model_key, model_value in vars(model).items():
    # http://effbot.org/pyfaq/how-do-i-check-if-an-object-is-an-instance-of-a-given-class-or-of-a-subclass-of-it.htm
    # if issubclass(value, Base):
    #     if isinstance(model_value, Base):
    #         log.debug(
    #             f"object {model_key=} holds {model_value=} subclass of Base"
    #         )
    for base_key, base_value in model:
        # now using the new model iterator that does through all dataframes in a
        # Base class
        for df_name, df_value in base_value:
            # the above replaced these lines
            # for name, value in vars(model_value).items():
            # https://stackoverflow.com/questions/14808945/check-if-variable-is-dataframe
            # if not isinstance(value, pd.DataFrame):
            #     log.debug(f"{value} is not a DataFrame")
            #     continue
            # https://kite.com/python/answers/how-to-check-if-a-value-is-in-a-dictionary-in-python
            # https://www.geeksforgeeks.org/python-check-whether-given-key-already-exists-in-a-dictionary/
            # breakpoint()
            if df_name in base_value.description:
                log.debug("found description")
                st.write(base_value.description[df_name])
            else:
                st.header(df_name)
                st.write(f"No description found for {df_name=}")
            # https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html
            # https://pbpython.com/styling-pandas.html
            st.write(df_value.style.format("{0:,.2f}"))


def testHome(data_df):
    """Test drawing.

    Test for dashboard
    """
    st.write(
        """
        # COVID-19 Decision Dashboard
        ## Restart.us
        Use caution when interpreting these numbers and consult experts on use.
        Numbers are 000s except *$0s*
        """
    )

    log.debug(f"{data_df=}")
    st.write(
        """
        ### All Resource Burn Rate Table
        """
    )

    st.dataframe(data_df.head())
    st.write(
        """
        ### Select Resource for Filtered Burn Rate Table
        """
    )

    # do a multiselect to pick relevant items
    data_ms = st.multiselect(
        "Columns", data_df.columns.tolist(), default=data_df.columns.tolist()
    )
    # now render just those columns and the first 10 rows
    filtered_data_df = data_df[data_ms]
    st.dataframe(filtered_data_df.head(10))
    st.write(
        """
        ### Histogram of uses
        """
    )
    st.bar_chart(filtered_data_df)
    # It's so easy to chart with builtin types
    # And labelsa re just more markdown
    st.line_chart(data_df)


def visualize_data(df, x_axis, y_axis):
    """Visualize data.

    Charting for the dashboard
    """
    # F strings do not work with streamlit so just put variables i
    # so use st.write to get them
    """
    ## Debug
    """
    st.write(f"{x_axis=} {y_axis=}")
    df
    df.index.name
    df.index.name = "Label" if None else df.index.name
    # first rest the index to get it to be a column
    # using melt to get column form
    df_reset = df.reset_index()
    df_reset

    # you can also use breakpoint
    # breakpoint()

    # Since this was published, there are more parameters for interactive v4
    # https://towardsdatascience.com/quickly-build-and-deploy-an-application-with-streamlit-988ca08c7e83
    # https://towardsdatascience.com/interactive-election-visualisations-with-altair-85c4c3a306f9
    # https://altair-viz.github.io
    graph = (
        alt.Chart(df)
        .mark_circle(size=60)
        .encode(x=x_axis, y=y_axis, tooltip=["N95", "Mask"], color="N95")
        .interactive()
    )
    st.write(graph)


def visualize_model(model: Model):
    """Visualize Model.

    Simple visualization
    """
    """
    # Model Visualization

    Uses an existing model
    """
    for obj in model:
        pass


# you start this by detecting a magic variable
if __name__ == "__main__":
    dashboard()
