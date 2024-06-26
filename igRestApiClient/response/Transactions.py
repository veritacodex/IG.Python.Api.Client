from dataclasses import dataclass
from igRestApiClient.helper.TypeConverter import List
from igRestApiClient.helper.TypeConverter import Any
from igRestApiClient.helper.TypeConverter import from_list
from igRestApiClient.helper.TypeConverter import to_class
from igRestApiClient.model.Transaction import Transaction


@dataclass
class Transactions:
    items: List[Transaction]

    @staticmethod
    def from_dict(obj: Any) -> 'Transactions':
        assert isinstance(obj, dict)
        transactions = from_list(Transaction.from_dict, obj.get("transactions"))
        return Transactions(transactions)

    def to_dict(self) -> dict:
        result: dict = {"transactions": from_list(lambda x: to_class(Transaction, x), self.items)}
        return result


def transactions_from_dict(s: Any) -> Transactions:
    return Transactions.from_dict(s)


def transactions_to_dict(x: Transactions) -> Any:
    return to_class(Transactions, x)
