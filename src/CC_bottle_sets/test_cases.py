from challenge import optim_sets

# Cases and results (dictionary):
cases_result = { # Coded
'5': 1, 
'8.8.8': 3, 
'40.40.40.50.80': 3
}

def test_result(cases_result):
    # Evaluate all cases:
    N = 0 # Initiate success counts
    for case in cases_result:
        decoded_list = [int(x) for x in case.split('.')]
        output = optim_sets(decoded_list)
        if output == cases_result[case]:
            N += 1

    # Calculate success rate:
    success_rate = N/len(cases_result) * 100
    print(f'Test results: {success_rate:.2f}% of the test cases were successful.')

test_result(cases_result)