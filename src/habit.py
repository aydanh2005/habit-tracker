from datetime import datetime


class Habit:
    """
    Represents a habit with a name, periodicity, creation date,
    and a list of completion timestamps.
    """

    def __init__(self, name: str, periodicity: str, created_at=None, completions=None):
        self.name = name
        self.periodicity = periodicity.lower()
        self.created_at = created_at if created_at else datetime.now().isoformat()
        self.completions = completions if completions else []

    def check_off(self, completed_at=None):
        """
        Add a completion timestamp to the habit.
        """
        timestamp = completed_at if completed_at else datetime.now().isoformat()
        self.completions.append(timestamp)

    def to_dict(self):
        """
        Convert the Habit object into a dictionary.
        """
        return {
            "name": self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at,
            "completions": self.completions
        }

    @classmethod
    def from_dict(cls, data):
        """
        Create a Habit object from a dictionary.
        """
        return cls(
            name=data["name"],
            periodicity=data["periodicity"],
            created_at=data["created_at"],
            completions=data["completions"]
        )

    def __str__(self):
        return f"Habit(name='{self.name}', periodicity='{self.periodicity}')"