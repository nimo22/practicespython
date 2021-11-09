from datetime import datetime
from database.data import Data

# class instance
dat = Data()
dat.disconnect()


# get today date and replace '-' by ''
def today_date():
    today = datetime.today().strftime('%Y-%m-%d').replace("-", "")
    return today


# loop throught element of the data base check they date and return  the one witha date inferior or equal to today date
def filter():
    today = today_date()
    article_id = dat.inter_command("SELECT  id,date_publication   FROM article;")
    dicto = {}
    dat_accepter = []
    for dict_name in article_id.fetchall():
        dicto.update({dict_name[1].replace('-', ""): dict_name[0]})
    for accepted in dicto.keys():
        if accepted <= today:
            dat_accepter.append(dicto[accepted])

    return dat_accepter

