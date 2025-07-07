"""
ColumnProfile
"""
from dataclasses import dataclass
from typing import Any, Dict, Optional, List

from profile import Profile

@dataclass
class ColumnProfile(Profile):
    """
    Concrete class
    """

    def __init__(self):
        super().__init__()
        self.column_name: str  = ""
        self.column_classification: str = ""
        self.cardinality: int = 0
        self.uniqueness_ratio: float = 0.0
        self.missing_values: int = 0
        self.missing_percentage: float = 0.0
        self.is_binary: bool = False
        self.is_time_series: bool = False
        self.potential_role: List[str] = []
        self.statistics: Optional[Dict[str, Any]] = None
