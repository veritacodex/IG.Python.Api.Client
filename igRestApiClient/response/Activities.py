from dataclasses import dataclass
from igRestApiClient.helper.TypeConverter import List
from igRestApiClient.helper.TypeConverter import Any
from igRestApiClient.helper.TypeConverter import from_list
from igRestApiClient.helper.TypeConverter import to_class
from igRestApiClient.model.Activity import Activity


@dataclass
class Activities:
    items: List[Activity]

    @staticmethod
    def from_dict(obj: Any) -> 'Activities':
        assert isinstance(obj, dict)
        activities = from_list(Activity.from_dict, obj.get("activities"))
        return Activities(activities)

    def to_dict(self) -> dict:
        result: dict = {"activities": from_list(lambda x: to_class(Activity, x), self.items)}
        return result


def activities_from_dict(s: Any) -> Activities:
    return Activities.from_dict(s)


def activities_to_dict(x: Activities) -> Any:
    return to_class(Activities, x)
