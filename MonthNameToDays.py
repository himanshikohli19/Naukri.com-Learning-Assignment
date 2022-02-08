def get_month_days(month):
    month = month.strip().lower()
    if month == "february":
        return "28/29"
    elif month in ("april", "june", "september", "november"):
        return "30"
    elif month in ("january", "march", "may", "july", "august", "october", "december"):
        return "31"

    return ""  # for invalid month name


if __name__ == '__main__':
    print("List of Months: January, February, March, April, May, June, July, August, September, October, November, "
          "December")
    month_name = input("Enter the name of Month:\n")
    days = get_month_days(month_name)
    if days:
        print(f"{month_name} will have {days} days.")
    else:
        print(f"{month_name} is not a month.")