from dataclasses import dataclass
from igRestApiClient.helper.TypeConverter import Any
from igRestApiClient.helper.TypeConverter import from_float
from igRestApiClient.helper.TypeConverter import to_float


@dataclass
class Balance:
    amount: float
    deposit: float
    profit_loss: float
    available: float

    @staticmethod
    def from_dict(obj: Any) -> 'Balance':
        assert isinstance(obj, dict)
        amount = from_float(obj.get("balance"))
        deposit = from_float(obj.get("deposit"))
        profit_loss = from_float(obj.get("profitLoss"))
        available = from_float(obj.get("available"))
        return Balance(amount, deposit, profit_loss, available)

    def to_dict(self) -> dict:
        result: dict = {"balance": to_float(self.amount), "deposit": to_float(self.deposit),
                        "profitLoss": to_float(self.profit_loss), "available": to_float(self.available)}
        return result
