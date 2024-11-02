import math
import json
import gspread
import pandas as pd
import streamlit as st
import matplotlib as plt
from pathlib import Path
from google.oauth2.service_account import Credentials

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='Análisis BTC, BNB, ETH y ETC',
    page_icon=':coin:'
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

def get_data():
    type = "service_account"
    project_id = "analisis-440420"
    private_key_id = "f19f971baf9e63a36617f4f2bd79bfe0168741b7"
    private_key = "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCyyHyqMQMUHd2o\n09LYLqPOtRAM9guycKK42kODpZWr4JtUENE9hQx4UX1iz5kx02iHK0Dde5hxG/Jk\nCatTvlrpm/4R76tiJ4Qd0F9zgqODrYmihtpFa3vs1rZ8C2SPGN1LPbyV81akUIJw\nUkE0++BkrDGUv1XZtOLtIrtfwNmatRfZQ7/fBUWdmHVkaK/IbVdXEgZHExkO1jht\nRXc54i3czmggnhpeHOtBIyBjlc7XujJcXa1St1bLxXmR7eDDVcMjgoa0gh7rquSd\nYY9iPM7iOhWXv9DCv6LGZss3x0hFpaxdyo0J6zEDl7gcN7+KEfmG3rDKKHD+/pjQ\ngnIOelyLAgMBAAECggEAEkWfSB2ePO4Ye2q6v9F0eGnU7B4xb9lHKDFWeRvxQhHA\njkTxvaHddmaNtA2XkJoUssve40QAfn7mtQav9e0ciYeh3d9q2qtDO3DScJHHeGvC\nB1RU9odXsQr4t5DKhD18UHZM0d5+2mhIDIa7l1iuxFs87gDoG0n7b1T/ZXfmRYNU\n3u6Rp/GdcxaJiC1CUoLQ2l6DfUM28QyJpHvzWyN93ZfcNdrErFhG6mqJXXPfxhFk\nh82Uhbab/jHLuZEKvQqhHhlxsT82Q/K9cqAwk599tJqMLUvdq0YH8pQ9A62Exhgv\no3sAlnSr4Q7A7107iWpBhylfsvGam9WmHSEcjpLbYQKBgQDcVWh2idTDPi2vBzj+\nn9RzmTwuLw31UiMJ7WWGVUT/x2lTKMw7AX1n1WQDn3+O1lHdsE2mHQ8DfGHC0EAf\npFuIaR5nQNK9HD4/QaYzgPHEJbas/4HSXgMXuRtQQyioX/A1FsqcZz/ZbK6ceUnG\nhAneD3zpAuLXzoMKIvdopJNRowKBgQDPuTvPAgzCGPByLOwF3RtSYea+MGC1MZkD\nMeu4DlF3HpQGJkIkzcul3oFHud94ugsz/HlZ3njKX8GCftcY3yxx4/QRlvdU2PDp\nVp/LVnlkA/nJEaDfAl5l4OAsTR4cR/mVtqe5itkeCjxGl3UCUxeDJGjHsJh6LQhw\nh8+duIGH+QKBgBFxIWfg2VrrXSpx4+0kMelExCLTzsMQ0X1DsbnEnkWxP4E5xZEW\nORszJUu0IKDqDmkCP+NagYnBGuwVGD5pAGX4DFQYKZaW2cagJ8wD9R+V7LQdNeW1\nU4FZQfREnL9XeOh6+WcQNVm85MW2RETWxwExMK4xcEutKWpwAi3ieVcJAoGBAJn8\noCiyRVDx+fU59fHW2jU1HD+rT1WjIeIrdKmp+5xJj8QLQodUA/6/Nqk8UjyF9l4g\ncLk9Yd/sImChtMTcVG9NZBZSCqHcfKMNs0GipjSNefMjXVVUxTPTA3vz4zll5dCl\nairykkdhoRNXnccOX+S47e/yquYPUi1RkIhEScnJAoGAT8vBsKxRqPbMO0TDQqQV\nUS/q7ky81x6V4Bs4Zo9Ag51SkHvYRPPn0m4N3jEey2SFiCqmbFgWbAWIk4NxJ8bs\n0wwtNaCe9J3x9yVawg53HsCSAEyHFB7IBXp3yGWY8AMLZYGChZL/0lRHaQaeDqzn\nN7rFwlQcy24hKVey3tQQuJA=\n-----END PRIVATE KEY-----\n"
    client_email = "analisis-btc@analisis-440420.iam.gserviceaccount.com"
    client_id = "106217323922727042983"
    auth_uri = "https://accounts.google.com/o/oauth2/auth"
    token_uri = "https://oauth2.googleapis.com/token"
    auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
    client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/analisis-btc%40analisis-440420.iam.gserviceaccount.com"
    universe_domain = "googleapis.com"

    credentials_dict = json.loads("{}")
    credentials_dict['type'] = type
    credentials_dict['project_id'] = project_id
    credentials_dict['private_key_id'] = private_key_id
    credentials_dict['private_key'] = private_key
    credentials_dict['client_email'] = client_email
    credentials_dict['client_id'] = client_id
    credentials_dict['auth_uri'] = auth_uri
    credentials_dict['token_uri'] = token_uri
    credentials_dict['auth_provider_x509_cert_url'] = auth_provider_x509_cert_url
    credentials_dict['client_x509_cert_url'] = client_x509_cert_url
    credentials_dict['universe_domain'] = universe_domain

    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    creds = Credentials.from_service_account_info(credentials_dict, scopes=scope)
    client = gspread.authorize(creds)

    spreadsheet = client.open('Analisis_BTC')
    worksheet_BTC = spreadsheet.worksheet('BTC')
    worksheet_BNB = spreadsheet.worksheet('BNB')
    worksheet_ETH = spreadsheet.worksheet('ETH')
    worksheet_ETC = spreadsheet.worksheet('ETC')

    btc = worksheet_BTC.get_all_values()
    bnb = worksheet_BNB.get_all_values()
    eth = worksheet_ETH.get_all_values()
    etc = worksheet_ETC.get_all_values()

    btc_df = pd.DataFrame(columns=btc[0], data=btc[1:])
    bnb_df = pd.DataFrame(columns=bnb[0], data=bnb[1:])
    eth_df = pd.DataFrame(columns=eth[0], data=eth[1:])
    etc_df = pd.DataFrame(columns=etc[0], data=etc[1:])

    return btc_df, bnb_df, eth_df, etc_df

def format_currency(value):
    value = value.replace(",", ".")
    value = float(value)
    formatted_value = f"$ {value:,.2f}"
    formatted_value = formatted_value.replace(',', 'X').replace('.', ',').replace('X', '.')
    return formatted_value

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# :coin: Análisis BTC, BNB, ETH y ETC
'''

# Add some spacing
''
''

btc_df, bnb_df, etc_df, eth_df = get_data()

btc, bnb, eth, etc = st.tabs(['BTC', 'BNB', 'ETH', 'ETC'])

with btc:
    ''
    ''
    st.image('images/Btc.png', width=100)
    ''
    ''
    clean_btc = btc_df.copy(deep=True)
    clean_btc['Fecha'] = pd.to_datetime(clean_btc['Fecha'] + ' ' + clean_btc['Hora'], format='%d/%m/%Y %H:%M')
    clean_btc.drop('Hora', axis=1, inplace=True)
    clean_btc['Precio'] = clean_btc['Precio'].apply(lambda x: x.replace(',', '.')).astype(float)
    clean_btc.set_index('Fecha', inplace=True)
    resampled_btc = clean_btc.resample('30min', closed='right', label='right').mean()
    resampled_btc['Precio'] = resampled_btc['Precio'].astype(str).apply(format_currency)
    
    st.line_chart(resampled_btc, x_label='Fecha', y_label='Precio')
    ''
    ''
    col1, col2, col3 = st.columns(3)
    with col2:
        formatted_btc = btc_df.copy(deep=True)
        formatted_btc['Precio'] = formatted_btc['Precio'].apply(format_currency)
        st.dataframe(formatted_btc, hide_index=True)
with bnb:
    ''
    ''
    st.image('images/Bnb.png', width=100)
    ''
    ''
    clean_bnb = bnb_df.copy(deep=True)
    clean_bnb['Fecha'] = pd.to_datetime(clean_bnb['Fecha'] + ' ' + clean_bnb['Hora'], format='%d/%m/%Y %H:%M')
    clean_bnb.drop('Hora', axis=1, inplace=True)
    clean_bnb['Precio'] = clean_bnb['Precio'].apply(lambda x: x.replace(',', '.')).astype(float)
    clean_bnb.set_index('Fecha', inplace=True)
    resampled_bnb = clean_bnb.resample('30min', closed='right', label='right').mean()
    resampled_bnb['Precio'] = resampled_bnb['Precio'].astype(str).apply(format_currency)
    
    st.line_chart(resampled_bnb, x_label='Fecha', y_label='Precio')
    ''
    ''
    col1, col2, col3 = st.columns(3)
    with col2:
        formatted_bnb = bnb_df.copy(deep=True)
        formatted_bnb['Precio'] = formatted_bnb['Precio'].apply(format_currency)
        st.dataframe(formatted_bnb, hide_index=True)
with eth:
    ''
    ''
    st.image('images/Eth.png', width=100)
    ''
    ''
    clean_eth = eth_df.copy(deep=True)
    clean_eth['Fecha'] = pd.to_datetime(clean_eth['Fecha'] + ' ' + clean_eth['Hora'], format='%d/%m/%Y %H:%M')
    clean_eth.drop('Hora', axis=1, inplace=True)
    clean_eth['Precio'] = clean_eth['Precio'].apply(lambda x: x.replace(',', '.')).astype(float)
    clean_eth.set_index('Fecha', inplace=True)
    resampled_eth = clean_eth.resample('30min', closed='right', label='right').mean()
    resampled_eth['Precio'] = resampled_eth['Precio'].astype(str).apply(format_currency)
    
    st.line_chart(resampled_eth, x_label='Fecha', y_label='Precio')
    ''
    ''
    col1, col2, col3 = st.columns(3)
    with col2:
        formatted_eth = eth_df.copy(deep=True)
        formatted_eth['Precio'] = formatted_eth['Precio'].apply(format_currency)
        st.dataframe(formatted_eth, hide_index=True)
with etc:
    ''
    ''
    st.image('images/Etc.png', width=100)
    ''
    ''
    clean_etc = etc_df.copy(deep=True)
    clean_etc['Fecha'] = pd.to_datetime(clean_etc['Fecha'] + ' ' + clean_etc['Hora'], format='%d/%m/%Y %H:%M')
    clean_etc.drop('Hora', axis=1, inplace=True)
    clean_etc['Precio'] = clean_etc['Precio'].apply(lambda x: x.replace(',', '.')).astype(float)
    clean_etc.set_index('Fecha', inplace=True)
    resampled_etc = clean_etc.resample('30min', closed='right', label='right').mean()
    resampled_etc['Precio'] = resampled_etc['Precio'].astype(str).apply(format_currency)
    
    st.line_chart(resampled_etc, x_label='Fecha', y_label='Precio')
    ''
    ''
    col1, col2, col3 = st.columns(3)
    with col2:
        formatted_etc = etc_df.copy(deep=True)
        formatted_etc['Precio'] = formatted_etc['Precio'].apply(format_currency)
        st.dataframe(formatted_etc, hide_index=True)