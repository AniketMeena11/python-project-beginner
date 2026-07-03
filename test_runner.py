class TestCase:

    environment = "Stage"

    def __init__(self, test_id, name, priority):
        self.test_id = test_id
        self.name = name
        self.priority = priority
        self.status = "Pending"
    
    def run_test(self):
        self.status = "Passed" 


test_suite = [
    TestCase("T001", "Test 1", "High"),
    TestCase("T002", "Test 2", "Medium"),
    TestCase("T003", "Test 3", "Low")
]


def run_test_engine(suite):
    status_report = {"Passed": 0 , "Pending": 0}

    for test in suite:
        if test.priority == "High":
            test.run_test()
            print(f"Running High priority test:{test.test_id}")

    for test in suite:
        if test.status == "Passed":
            status_report["Passed"] = status_report["Passed"]+1 
        else:
            status_report["Pending"] = status_report["Pending"]+1 


    print(status_report["Passed"])

    print(f"Final Results : {status_report}")


run_test_engine(test_suite)