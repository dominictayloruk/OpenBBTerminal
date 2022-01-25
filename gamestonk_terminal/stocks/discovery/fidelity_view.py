""" Fidelity View """
__docformat__ = "numpy"

import os
import re
import pandas as pd

from gamestonk_terminal.helper_funcs import export_data, print_rich_table
from gamestonk_terminal import feature_flags as gtff

from gamestonk_terminal.stocks.discovery import fidelity_model
from gamestonk_terminal.rich_config import console


def buy_sell_ratio_color_red_green(val: str) -> str:
    """Add color tags to the Buys/Sells ratio cell

    Parameters
    ----------
    val : str
        Buys/Sells ratio cell

    Returns
    -------
    str
        Buys/Sells ratio cell with color tags
    """

    buy_sell_match = re.match(r"(\d+)% Buys, (\d+)% Sells", val, re.M | re.I)

    if not buy_sell_match:
        return val

    buys = int(buy_sell_match.group(1))
    sells = int(buy_sell_match.group(2))

    if buys >= sells:
        return f"[green]{buys}%[/green] Buys, {sells}% Sells"

    return f"{buys}% Buys, [red]{sells}%[/red] Sells"


def price_change_color_red_green(val: str) -> str:
    """Add color tags to the price change cell

    Parameters
    ----------
    val : str
        Price change cell

    Returns
    -------
    str
        Price change cell with color tags
    """

    val_float = float(val.split(" ")[0])
    if val_float > 0:
        return f"[green]{val}[/green]"
    return f"[red]{val}[/red]"


def orders_view(num: int, export: str):
    """Prints last N orders by Fidelity customers. [Source: Fidelity]

    Parameters
    ----------
    num: int
        Number of stocks to display
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    order_header, df_orders = fidelity_model.get_orders()

    pd.set_option("display.max_colwidth", None)

    if gtff.USE_COLOR:
        df_orders["Buy / Sell Ratio"] = df_orders["Buy / Sell Ratio"].apply(
            buy_sell_ratio_color_red_green
        )
        df_orders["Price Change"] = df_orders["Price Change"].apply(
            price_change_color_red_green
        )

    df_orders = df_orders.head(n=num).iloc[:, :-1]

    print_rich_table(
        df_orders,
        headers=[x.title() for x in df_orders.columns],
        show_index=False,
        title=f"{order_header}:",
    )
    console.print("")

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "ford",
        df_orders,
    )