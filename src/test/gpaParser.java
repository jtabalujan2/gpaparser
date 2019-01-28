package test;

import java.util.List;
import java.util.Scanner;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;

public class gpaParser {
	
	public static void main(String args[]) throws Exception {
		
		
		System.setProperty("webdriver.chrome.driver", "C:/Users/Julian/Google Drive/Workspace/SeleniumTest/lib/chromedriver.exe");
		WebDriver driver = new ChromeDriver(); 
		
		//login to CSUN OAuth
		System.out.println("Logging in via OAuth...");
		driver.get("https://uachieve.csun.edu/selfservice/student/search.html");
		WebElement username = driver.findElement(By.id("username"));
		username.sendKeys("106502225");
		WebElement password = driver.findElement(By.id("password"));
		password.sendKeys("*Jt81112577");
		WebElement Signup_button = driver.findElement(By.name("submit"));
		Signup_button.click();
		
		
		//Accessing DPR & inputting student 
		WebElement cont = driver.findElement(By.xpath("//*[@title='Continue']"));
		cont.click();
		WebElement studno = driver.findElement(By.id("stuno"));
		
		
		//asking for student ID
		Scanner myScanner = new Scanner(System.in);
		System.out.println("Please enter student ID");
		String result = myScanner.nextLine();
		studno.sendKeys(result);
		myScanner.close();
		
		
		/*
		 * if you want to simply have a predetermined ID this is where you put it
		 studno.sendKeys(input student id here);
		 *
		 */
		
		System.out.println("Inputting StudentID...");
		WebElement submit_button = driver.findElement(By.xpath("//*[@class='btn btn-primary']"));
		submit_button.click();
		WebElement request_audit = driver.findElement(By.xpath("//*[@class='btn btn-primary']"));
		request_audit.click();
		
		
		//selecting degree of ALL COURSEWORK IN DARS
		System.out.println("Requesting audit...");
		WebElement dialog = driver.findElement(By.id("useWhatIfPrograms"));
		dialog.click();
		Select option = new Select(driver.findElement(By.name("whatIfDegreeProgram")));
		option.selectByVisibleText("ALL COURSEWORK IN DARS IN ALPHABETICAL ORDER -  -  - ALL ALPH");
		Thread.sleep(2000);
		WebElement run_audit = driver.findElement(By.xpath("//*[@title='Run Audit']"));
		run_audit.click();
		
		
		//Waiting for DPR to be generated
		System.out.println("Generating DPR...");
		WebDriverWait wait = new WebDriverWait(driver, 15); //seconds
		wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("expandAll")));
		
		
		//expanding open all sections tab to expose all classes listed
		WebElement expand_sections = driver.findElement(By.id("expandAll"));
		expand_sections.click();
		
		
		// Grab the table 
		WebElement table = driver.findElement(By.className("completedCourses")); 
		System.out.println("Classes Taken: ");

		
		// Now get all the TR elements from the table 
		List<WebElement> allRows = table.findElements(By.tagName("tr")); 
		
		// And iterate over them, getting the cells 
		for (WebElement row : allRows) { 
		    List<WebElement> courses = row.findElements(By.className("course"));
		    List<WebElement> grade = row.findElements(By.className("grade"));
		// Print the contents of each cell
		    for (WebElement cell : courses) { 
				for (WebElement row1 : grade) { 
					System.out.println(cell.getText() + " : " + row1.getText());
					}
				}
		}

		driver.quit();
	}

}
