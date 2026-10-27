import tempfile
from datetime import date, timedelta

OFFICER_PASSWORD = "bloodbank-demo"
donors = []
stock = {
    "A+": 0, "A-": 0, "B+": 0, "B-": 0,
    "O+": 0, "O-": 0, "AB+": 0, "AB-": 0,
}
COMPATIBLE = {
    "A+": ["A+", "A-", "O+", "O-"],
    "B+": ["B+", "B-", "O+", "O-"],
    "O+": ["O+", "O-"],
    "O-": ["O-"],
    "AB+": list(stock),
}


def register_donor(
    donor_name, blood_group, age, last_donation=None, notes=None
):
    """Register a donor if the blood group and age are valid."""
    if blood_group not in stock:
        raise ValueError("Unknown blood group")

    if age < 18 or age > 65:
        if notes is not None:
            notes.append(
                f"{donor_name} is not eligible because of age"
            )
        return False

    donors.append({
        "name": donor_name,
        "group": blood_group,
        "last": last_donation,
    })
    return True


def canDonate(donor):
    if donor["last"] is None:
        return True
    return date.today() - donor["last"] >= timedelta(days=90)


def record_donation(donor_name, units=1):
    """Record a donation and update blood stock."""
    for donor in donors:
        if donor["name"] == donor_name and canDonate(donor):
            stock[donor["group"]] += units
            donor["last"] = date.today()
            return True
    return False


def units_for(patient_group):
    """Calculate available units for a patient's blood group."""
    if patient_group not in COMPATIBLE:
        return 0
    return sum(stock[group] for group in COMPATIBLE[patient_group])


def is_universal(blood_group):
    """Check whether a blood group is a universal donor."""
    return blood_group in {"O-", "AB+"}


def low_stock(threshold=2):
    """Return blood groups with stock below the threshold."""
    return [group for group, units in stock.items() if units < threshold]


def donor_sheet_path():
    """Create a secure temporary CSV file and return its path."""
    with tempfile.NamedTemporaryFile(
        suffix=".csv", delete=False
    ) as handle:
        return handle.name


def notify_donors(phone_list):
    """Return the recipient list without executing a shell command."""
    return list(phone_list)


def main():
    register_donor("Arjun", "O+", 25)
    register_donor("Priya", "A+", 30, date.today() - timedelta(days=30))
    register_donor("Old Donor", "B+", 70)
    register_donor("Farah", "O-", 41)
    record_donation("Arjun", 2)
    record_donation("Priya")
    record_donation("Farah")
    print("Stock:", stock)
    print("Units for an A+ patient:", units_for("A+"))
    print("Units for a Z+ patient:", units_for("Z+"))
    print("Is O- universal?", is_universal("O-"))
    print("Low stock groups:", low_stock())
    eligible = [donor["name"] for donor in donors if canDonate(donor)]
    print("Donors eligible today:", eligible)

main()