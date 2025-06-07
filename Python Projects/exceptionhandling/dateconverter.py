def main():
    while True:
        date = input("Date: ").strip()

        try:
            # Format: "Month Day, Year"
            if "," in date:
                month_day, year = date.split(", ")
                month_name, day = month_day.split(" ")

                # Convert month name to number
                months = {
                    "January": 1, "February": 2, "March": 3, "April": 4,
                    "May": 5, "June": 6, "July": 7, "August": 8,
                    "September": 9, "October": 10, "November": 11, "December": 12
                }

                if month_name in months:
                    month = months[month_name]
                else:
                    continue  # Invalid month name

            # Format: "MM/DD/YYYY"
            elif "/" in date:
                month, day, year = date.split("/")

            else:
                continue  # Invalid format

            # Convert to integers
            month, day, year = int(month), int(day), int(year)

            # Basic validation
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break

        except ValueError:
            pass  # Handles incorrect conversions


if __name__ == "__main__":
    main()
