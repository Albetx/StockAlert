import smtplib

my_email = "testserver.con@outlook.com"
password = "Dovnemalim1"
DRAMATIC_CHANGE_CODE = 100
DAILY_UPDATE_CODE = 200
MONTHLY_UPDATE_CODE = 300
YEARLY_UPDATE_CODE = 400



class SendEmail:

    def __init__(self, mail_addr: str,ticker_symbol: str) -> bool:
        self.mail_addr = mail_addr
        self.ticker = ticker_symbol

    def send(self, massage:[], change: float, update_code: int):

        if update_code == DRAMATIC_CHANGE_CODE:
            massage = f'Subject:{self.ticker.upper()}: {round(change)}%\n\n{massage[0]}\n\n{massage[1]}\n\n{massage[2]}\n\n'.encode("utf8")

        elif update_code == DAILY_UPDATE_CODE:
            massage = f'Subject:Daily update - {self.ticker.upper()}: {round(change)}%\n\n{massage[0]}\n\n{massage[1]}\n\n{massage[2]}\n\n'.encode("utf8")

        elif update_code == MONTHLY_UPDATE_CODE:
            massage = f'Subject:Monthly update - {self.ticker.upper()}, Change this month: {round(change)}%\n\n' \
                      f'The most relevant news for this month:\n{massage[0]}\n\n{massage[1]}\n\n{massage[2]}\n\n'.encode("utf8")

        elif update_code == YEARLY_UPDATE_CODE:
            massage = f'Subject:Yearly update - {self.ticker.upper()}, Change this month: {round(change)}%\n\n' \
                      f'The most relevant news for this year:\n{massage[0]}\n\n{massage[1]}\n\n{massage[2]}\n\n'.encode("utf8")

        try:
            with smtplib.SMTP("smtp-mail.outlook.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)

                test = connection.sendmail(
                    from_addr=my_email,
                    to_addrs=self.mail_addr,
                    msg=massage
                )
                print(test)

        except smtplib.SMTPException:
            print("ERROR while sending the mail..")
            return False

        else:
            return True

