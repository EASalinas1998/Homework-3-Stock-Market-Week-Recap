#########################
# CSCI 1380.04
# Spring 2022
# Homework 03
# Eduardo Salinas
#########################

# Creates the user defined function {display_week_summary} with arguments (stock_ticker, company_name, close_prices)
def display_week_summary(stock_ticker, company_name, close_prices):
  
  # Displays in console a message of the company's stock price summary via {display_week_summary}'s arguments.
  print(f"Stock Price Summary for {company_name} ({stock_ticker}) from Monday, April 4, 2022 to Friday, April 8, 2022") 

  # Creates a "for" loop with newly defined {current_close_price_index} to go through the indices of the argument {close_prices} except the last index
  for current_close_price_index in range(len (close_prices)-1):

    # Defines {current_close_price} as the current price index in {current_close_price_index}
    current_close_price = close_prices[current_close_price_index]

    # Defines {next_close_price} to be the next price index in {current_close_price_index}
    next_close_price = close_prices[current_close_price_index + 1]

    # Defines {change_value} as {next_close_price} minus {current_close_price}
    change_value = next_close_price - current_close_price

    # Rounds {change_value} to 2 decimal places
    change_value = round(change_value, 2)
    
    # Defines {change_percentage} as {next_close_price} divided by {current_close_price} minus 1, then times 100
    change_percentage = (next_close_price / current_close_price - 1) * 100

    # Rounds {change_percentage} to 2 decimal places
    change_percentage = round(change_percentage, 2)

    # Displays in console the current index {current_close_price_index} plus 1 to represent the day, and variables {next_close_price}, {change_value}, {change_percentage}
    print(f"Day {current_close_price_index + 1}  \t  {next_close_price}  \t  {change_value}  \t  {change_percentage}%")

  # Inserts a blank line for spacing purposes
  print()
  
# Calls the user-defined function {display_week_summary} with arguments (stock_ticker, company_name, close_prices) being replaced
display_week_summary("ADBE", "Adobe Inc.", [458.19, 468.81, 458.58, 444.33, 452.72, 445.34])

display_week_summary("NRG", "NRG Energy, Inc.", [38.4, 37.67, 37.62, 39.21, 39.04, 39.55])

display_week_summary("PM", "Philip Morris International Inc", [96.78, 96.28, 95.66, 99.02, 99.67, 100.07])