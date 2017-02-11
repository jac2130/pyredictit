while True:
    pyredictit_api.get_my_contracts()
    i = 0
    while i < len(pyredictit_api.my_contracts):
        pyredictit_api.monitor_price_of_contract(
        	contract=pyredictit_api.my_contracts[i],
        	monitor_type='stop_loss',
        	number_of_shares=pyredictit_api.my_contracts[i].number_of_shares - 1,
        	trigger_price=(float(pyredictit_api.my_contracts[i].avg_price) - 0.01)
                                                  )
        i += 1
        sleep(30)
