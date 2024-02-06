import pandas as pd
import datetime



def labeler(addr:str, format_time=False,format_price=False) -> pd.DataFrame:
    
    '''
    Description
    -----------
    The fuction gives the correct names to the columns of he LOBSTER 
    Both "Message" and "OrderBook" file and any level are accepted.
    The format_time (defalult=False) if True adds a new column with time in HH:MM:SS.000000 format
    
    Arguments
    ---------
    addr: str
        The first argument takes the relative Path of message or orderbook CSV file from LOBSTER,
        it is important that the file has the original name.

    format_time: bool
        The format_time (defalult=False) if True adds a new column with time in HH:MM:SS.000000 format.

    format_price: bool
        The format_price (defalult=False) if True shows all the prices in the "normal" format.
        For example if a Bid price is $ 95.43 the LOBSTER file shows 9543000, with format_price=True
        the price becomes a numpy.float64 95.43.

        
    Return
    ------
    data_message: pd.DataFrame
        or
    data_order_book: pd.DataFrame

    Example
    -----
    >>> labeler("LOBSTER_data\AAPL_2012-06-21_34200000_37800000_message_50.csv",format_time=True)
    
    '''

    if 'message' in addr:
        data_message= pd.read_csv(addr, names=['Time','Type','Order_ID','Size','Price','Direction'])
        #['Time','Type','Order_ID','Size','Price','Direction']

        if format_time:
            time= []
            for m_sec in data_message['Time']:
                time.append(str(datetime.timedelta(seconds=m_sec)))
            data_message.insert(1,'Time_Clock',time)
        
        if format_price:
            data_message["Price"]=data_message["Price"]/10000

        return data_message

    elif 'orderbook' in addr:
        data= pd.read_csv(addr)
        row =[]

        for level in range(1, int(len(data.columns)/4) + 1):
            for a in ['Ask_Price_', 'Ask_Size_','Bid_Price_', 'Bid_Size_']:
                row.append(a+str(level))

        data_order_book= pd.read_csv(addr, names= row)

        if format_price:
            for level in range(1, int(len(data_order_book.columns)/4) + 1):
                data_order_book[[f'Ask_Price_{level}',f'Bid_Price_{level}']] = data_order_book[[f'Ask_Price_{level}',f'Bid_Price_{level}']]/10000

        return data_order_book
