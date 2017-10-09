import java.io.*;
public class EmployeeTest {
	
	public static void main(String args[]) {
		Employee e1 = new Employee("Alice");
		Employee e2 = new Employee("Bob");

		e1.setAge(21);
		e1.setRole("Designer");
		e1.setSalary(80030.40);
		e2.setAge(23);
		e2.setRole("Engineer");
		e2.setSalary(120000.50);

		e1.printEmployee();
		e2.printEmployee();
	}
}
