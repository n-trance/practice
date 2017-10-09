import java.io.*;
public class Employee {

	String name;
	int age;
	String role;
	double salary;

	public Employee(String name) {
		this.name = name;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public void setRole(String role) {
		this.role = role;
	}

	public void setSalary(double salary) {
		this.salary = salary;
	}

	public void printEmployee() {
		System.out.println("Name: " + name);
		System.out.println("Age: " + age);
		System.out.println("Role: " + role);
		System.out.println("Salary: " + salary);
	}
	
}
