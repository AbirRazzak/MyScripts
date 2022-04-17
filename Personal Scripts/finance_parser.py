import csv
import datetime
from enum import Enum
from pathlib import Path
from pprint import pprint
from typing import TypedDict


AMEX_CSV = 'C:\\Users\\Abir\\Downloads\\activity (1).csv'
AMEX_CSV_DATE_FORMAT = '%m/%d/%Y'
CARD_MEMBER_NAME = 'ABIR RAZZAK'

PERSONAL_CAPITAL_CSV = 'C:\\Users\\Abir\\Downloads\\2021-10-01 thru 2021-10-31 transactions.csv'
PERSONAL_CAPITAL_CSV_DATE_FORMAT = '%Y-%m-%d'


OUTPUT_FILE_NAME = f'C:/Users/Abir/Downloads/{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}_transactions_filtered.csv'

class AmexTransaction(TypedDict):
    Date: str
    Description: str
    Member: str
    Account: str
    Amount: str


class PersonalCapitalTransaction(TypedDict):
    Date: str
    Account: str
    Description: str
    Category: str
    Tags: str
    Amount: str


def read_amex_csv(csv_file: str) -> list[AmexTransaction]:
    """
    Reads the AMEX CSV file and returns a list of dictionaries
    :param csv_file: file path to the AMEX CSV file
    :return: list of AmexTransaction
    """
    with open(csv_file, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        return [AmexTransaction(**row) for row in reader]


def read_personal_capital_csv(csv_file: str) -> list[PersonalCapitalTransaction]:
    """
    Reads the Personal Capital CSV file and returns a list of dictionaries
    :param csv_file: file path to the Personal Capital CSV file
    :return: list of PersonalCapitalTransaction
    """
    with open(csv_file, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        return [PersonalCapitalTransaction(**row) for row in reader]


def filter_amex_transactions_by_member(amex_transactions: list[AmexTransaction], member: str) -> list[AmexTransaction]:
    """
    Filters the AMEX transactions by member
    :param amex_transactions: list of AmexTransaction
    :param member: str
    :return: list of AmexTransaction
    """
    return [transaction for transaction in amex_transactions if transaction['Member'] == member]


def group_amex_transactions_by_date(amex_transactions: list[AmexTransaction]) -> dict[datetime.datetime, list[AmexTransaction]]:
    """
    Groups the AMEX transactions by date and returns a dictionary
    :param amex_transactions: list of AmexTransaction
    :return: dictionary of lists of AmexTransaction
    """
    return {
        datetime.datetime.strptime(date, AMEX_CSV_DATE_FORMAT): [transaction for transaction in amex_transactions if transaction['Date'] == date]
        for date in set([transaction['Date'] for transaction in amex_transactions])
    }


class SplitMethod(Enum):
    HALF = '50/50'
    NONE = '100/0'


class CSVMaker:
    def __init__(
        self, 
        personal_capital_transactions: list[PersonalCapitalTransaction],
        amex_transactions_by_date: dict[datetime.datetime, list[AmexTransaction]],
        split_method: SplitMethod
    ):
        self.personal_capital_transactions = personal_capital_transactions
        self.amex_transactions_by_date = amex_transactions_by_date
        self.split_method = split_method

    def include_personal_capital_transaction_in_output(
        self, 
        personal_capital_transaction: PersonalCapitalTransaction
    ) -> bool:
        """
        Checks if the Personal Capital transaction should be included in the output
        :param personal_capital_transaction: PersonalCapitalTransaction
        :return: bool
        """

        # ignore any transactions that are not AMEX transactions
        if personal_capital_transaction['Account'] != 'Amex Gold Cards':
            return True
        
        return self._is_personal_capital_transaction_in_amex_transactions(personal_capital_transaction)
    
    def get_csv_file_contents(self) -> str:
        """
        Returns the CSV file contents
        :return: str
        """
        csv_file_contents = 'Date,Description,Category,Amount\n'
        for personal_capital_transaction in self.personal_capital_transactions:
            if self.include_personal_capital_transaction_in_output(personal_capital_transaction):
                csv_file_contents += ','.join([
                    personal_capital_transaction['Date'],
                    personal_capital_transaction['Description'],
                    personal_capital_transaction['Category'],
                    self._split_transaction_amount(personal_capital_transaction['Amount'])
                ]) + '\n'
        return csv_file_contents

    def _is_personal_capital_transaction_in_amex_transactions(
        self,
        personal_capital_transaction: PersonalCapitalTransaction
    ) -> bool:
        """
        Checks if the Personal Capital transaction is in the AMEX transactions
        :param personal_capital_transaction: PersonalCapitalTransaction
        :return: bool
        """

        transaction_date = datetime.datetime.strptime(personal_capital_transaction['Date'],
                                                      PERSONAL_CAPITAL_CSV_DATE_FORMAT)
        transaction_amount = abs(float(personal_capital_transaction['Amount']))

        amex_transactions_on_date = self.amex_transactions_by_date.get(transaction_date, [])

        for amex_transaction_on_date in amex_transactions_on_date:
            if abs(float(amex_transaction_on_date['Amount'])) == transaction_amount:
                self.amex_transactions_by_date[transaction_date].remove(amex_transaction_on_date)
                return True

        return False

    def _split_transaction_amount(
        self,
        transaction_amount: str
    ) -> str:
        """
        Applies the split method to the transaction amount
        :param transaction_amount: str representing the transaction amount
        :return: str representing the transaction amount after the split
        """
        if self.split_method == SplitMethod.HALF:
            transaction_as_float = float(transaction_amount)
            return str(transaction_as_float / 2.0)
        
        return transaction_amount
    
    def write_csv_file(self, csv_file: str):
        with open(csv_file, 'w') as csv_file:
            csv_file.write(self.get_csv_file_contents())


if __name__ == '__main__':
    amex_transactions = read_amex_csv(AMEX_CSV)
    amex_transactions = filter_amex_transactions_by_member(amex_transactions, CARD_MEMBER_NAME)
    amex_transactions_by_date = group_amex_transactions_by_date(amex_transactions)

    personal_capital_transactions = read_personal_capital_csv(PERSONAL_CAPITAL_CSV)

    csv_maker = CSVMaker(
        personal_capital_transactions=personal_capital_transactions,
        amex_transactions_by_date=amex_transactions_by_date,
        split_method=SplitMethod.HALF
    )
    csv_maker.write_csv_file(OUTPUT_FILE_NAME)

    # Display any leftover amex transactions that were not in the personal capital data set
    pprint(csv_maker.amex_transactions_by_date)
