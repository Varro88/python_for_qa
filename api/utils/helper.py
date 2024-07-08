import string

import datetime
from dateutil import parser
from datetime import timezone

from faker import Faker


def get_seconds_diff(updated_date_time: string) -> float:
    updated_at = parser.parse(updated_date_time).replace(tzinfo=timezone.utc)
    now = datetime.datetime.now(datetime.UTC)
    return (now - updated_at).total_seconds()


def get_random_type():
    valid_types = ["Science", "Satire", "Drama", "Adventure", "Romance"]
    return valid_types[Faker().pyint(0, len(valid_types) - 1)]
