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


def recordDonation(donorName, units=1):
    for donor in donors:
        if donor["name"] == donorName and canDonate(donor):
            stock[donor["group"]] += units
            donor["last"] = date.today()
            return True
    return False


def unitsFor(patientGroup):
    try:
        return sum(stock[group] for group in COMPATIBLE[patientGroup])
    except Exception:
        return 0


def isUniversal(bloodGroup):
    return bloodGroup == "O-" or bloodGroup == "AB+"


def lowStock(threshold=2):
    return [group for group, units in stock.items() if units < threshold]


def donor_sheet_path():
    """Create a secure temporary CSV file and return its path."""
    handle = tempfile.NamedTemporaryFile(
        suffix=".csv", delete=False
    )
    handle.close()
    return handle.name


def notify_donors(phone_list):
    """Return the recipient list without executing a shell command."""
    return list(phone_list)


def main():
    register_donor("Arjun", "O+", 25)
    register_donor("Priya", "A+", 30, date.today() - timedelta(days=30))
    register_donor("Old Donor", "B+", 70)
    register_donor("Farah", "O-", 41)
    recordDonation("Arjun", 2)
    recordDonation("Priya")
    recordDonation("Farah")
    print("Stock:", stock)
    print("Units for an A+ patient:", unitsFor("A+"))
    print("Units for a Z+ patient:", unitsFor("Z+"))
    print("Is O- universal?", isUniversal("O-"))
    print("Low stock groups:", lowStock())  # below 2 units
    eligible = [donor["name"] for donor in donors if canDonate(donor)]
    print("Donors eligible today:", eligible)


main()
