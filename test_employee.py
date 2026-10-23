from employee import employee_details

def test_employee_details(): 
    result = employee_details("Arundhati", "CS_101", "IT", "90000")
    
    expected = "Name: Arundhati\nEmployee ID: CS_101\nDepartment: IT\nSalary: 90000"

    assert result == expected
