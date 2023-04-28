package test;

import java.awt.AWTException;
import java.awt.Robot;
import java.awt.event.KeyEvent;
import java.time.Duration;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.interactions.Actions;
import JavaDeps/SeleniumProject/


import io.github.bonigarcia.wdm.WebDriverManager;

public class FirstTest {
	
	public static void main(String[] args) throws InterruptedException, AWTException {
		
		ChromeOptions options = new ChromeOptions();
		options.addArguments("--remote-allow-origins=*");
        
		//System.setProperty("webdriver.chrome.driver","./Drivers/chromedriver.exe");
		WebDriverManager.chromedriver().setup();
		WebDriver driver = new ChromeDriver(options);
    
		driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(5));
		driver.manage().timeouts().scriptTimeout(Duration.ofMinutes(2));
		driver.manage().timeouts().pageLoadTimeout(Duration.ofSeconds(10));
		
		
		//RemixIDE
		driver.get("https://remix.ethereum.org/#lang=en&optimize=false&runs=200&evmVersion=null&version=soljson-v0.8.18+commit.87f61d96.js");
		
		Actions act = new Actions(driver);
		Thread.sleep(4000);
		//add full screen command
		act.moveByOffset(1, 1).click().build().perform();
		Thread.sleep(1000);
		
		driver.findElement(By.id("uploadFile")).click();
		Thread.sleep(1000);
		
		Robot r = new Robot();
		r.keyPress(KeyEvent.VK_P);
		r.keyRelease(KeyEvent.VK_P);
		r.keyPress(KeyEvent.VK_ENTER);
		r.keyRelease(KeyEvent.VK_ENTER);
		Thread.sleep(2000);
		act.moveByOffset(150, 220).click().build().perform();
		
		//Compiling the contract
		driver.findElement(By.id("verticalIconsKindsolidity")).click();
		driver.findElement(By.id("compileAndRunBtn")).click();
		Thread.sleep(10000);
		
		
		//create loops to do this more efficiently and more neatly
		//Going to Deploy page
		driver.findElement(By.id("verticalIconsKindudapp")).click();
		//drop down for Environment
		driver.findElement(By.id("selectExEnvOptions")).click();
		r.keyPress(KeyEvent.VK_DOWN);
		r.keyRelease(KeyEvent.VK_DOWN);
		r.keyPress(KeyEvent.VK_DOWN);
		r.keyRelease(KeyEvent.VK_DOWN);
		r.keyPress(KeyEvent.VK_DOWN);
		r.keyRelease(KeyEvent.VK_DOWN);
		r.keyPress(KeyEvent.VK_ENTER);
		r.keyRelease(KeyEvent.VK_ENTER);
		//Drop down for Coin type
		driver.findElement(By.id("unit")).click();
		r.keyPress(KeyEvent.VK_DOWN);
		r.keyRelease(KeyEvent.VK_DOWN);
		r.keyPress(KeyEvent.VK_DOWN);
		r.keyRelease(KeyEvent.VK_DOWN);
		r.keyPress(KeyEvent.VK_DOWN);
		r.keyRelease(KeyEvent.VK_DOWN);
		r.keyPress(KeyEvent.VK_DOWN);
		r.keyRelease(KeyEvent.VK_DOWN);
		r.keyPress(KeyEvent.VK_ENTER);
		r.keyRelease(KeyEvent.VK_ENTER);
		
		Thread.sleep(500);
		driver.findElement(By.id("value")).sendKeys("5");
		//driver.findElement(By.className("form-control")).sendKeys("hello, world");

		
		driver.findElement(By.xpath("//*[@id=\"runTabView\"]/div/div[2]/div[3]/div[1]/div/div[1]/div[1]/input")).sendKeys("0xc0ffee254729296a45a3885639AC7E10F9d54979,10");
		Thread.sleep(1000);
		driver.findElement(By.xpath("//*[@id=\"runTabView\"]/div/div[2]/div[3]/div[1]/div/div[1]/div[1]/button")).click();
		driver.findElement(By.xpath("//*[@id=\"instance0xd9145CCE52D386f254917e481eB44e9943F39138\"]/div[1]/span")).click();

		
	}

}
//*[@id="runTabView"]/div/div[2]/div[3]/div[1]/div/div[1]/div[1]/button
//*[@id="instance0xd9145CCE52D386f254917e481eB44e9943F39138"]/div[1]/div/div[1]/span
