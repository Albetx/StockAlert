import smtplib

my_email = "testserver.con@outlook.com"
password = "Dovnemalim1"



class SendEmail:

    def __init__(self, mail_addr: str,ticker_symbol: str) -> bool:
        self.mail_addr = mail_addr
        self.ticker = ticker_symbol


    def send_dramatic_change_mail(self, massage:[], change: float):
        try:
            with smtplib.SMTP("smtp-mail.outlook.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)

                test = connection.sendmail(
                    from_addr=my_email,
                    to_addrs=self.mail_addr,
                    msg=f'Subject:{self.ticker.upper()}: {round(change)}%\n\n{massage[0]}\n\n{massage[1]}\n\n{massage[2]}\n\n'.encode("utf8")
                )
                print(test)

        except smtplib.SMTPException:
            print("ERROR while sending the mail..")
            return False

        else:
            return True

