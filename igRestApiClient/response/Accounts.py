from dataclasses import dataclass
from igRestApiClient.helper.TypeConverter import List
from igRestApiClient.helper.TypeConverter import Any
from igRestApiClient.helper.TypeConverter import from_list
from igRestApiClient.helper.TypeConverter import to_class
from igRestApiClient.model.Account import Account


@dataclass
class Accounts:
    items: List[Account]

    @staticmethod
    def from_dict(obj: Any) -> 'Accounts':
        assert isinstance(obj, dict)
        accounts = from_list(Account.from_dict, obj.get("accounts"))
        return Accounts(accounts)

    def to_dict(self) -> dict:
        result: dict = {"accounts": from_list(lambda x: to_class(Account, x), self.items)}
        return result


def accounts_from_dict(s: Any) -> Accounts:
    return Accounts.from_dict(s)


def accounts_to_dict(x: Accounts) -> Any:
    return to_class(Accounts, x)
