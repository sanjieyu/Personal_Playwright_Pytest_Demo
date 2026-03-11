# Author:Yi Sun(Tim) 2023-8-30


@then('the stored quote in database should match the UI value')
def step_impl(context):
    # 1. Get the amount from UI
    ui_quote = context.ui_page.get_quote_amount()

    # 2. SQL Query(using the existing quote id)
    sql_query = f"SELECT total_quote FROM Quote_Table WHERE quote_id = '{context.quote_id}'"

    # 3. Execute the SQL validation
    db_result = context.db.fetch_one(sql_query)
    db_quote = db_result[0]

    # 4. Assert
    assert float(ui_quote) == float(db_quote), \
        f"Data Mismatch! UI: {ui_quote}, DB: {db_quote}"