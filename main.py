from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.click('aria-label="Dismiss sign-in info."')
        bot.click('data-testid="header-currency-picker-trigger"')
        bot.select_currency("USD")
        bot.place_to_go("Colombia")
        bot.select_date("2024-10-20","2024-10-28")
        bot.seach_button()
        bot.filter(4,5)
        bot.report_result()
        bot.Print_table()
        print("closing....")
except Exception as e:
    print(f"Error {e}")