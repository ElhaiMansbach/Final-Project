const { Builder, By, Key, until } = require('selenium-webdriver');

(async function SignupTests() {
  let driver = await new Builder().forBrowser('chrome').build();

  try {
    // Navigate to signup page
    await driver.get('http://localhost:3000/peoples_budget/sign_up');
    await new Promise(resolve => setTimeout(resolve, 1000));

    // Enter signup details
    await driver.findElement(By.id('fName')).sendKeys('Eli');
    await new Promise(resolve => setTimeout(resolve, 500));
    await driver.findElement(By.id('lName')).sendKeys('Levy');
    await new Promise(resolve => setTimeout(resolve, 500));
    await driver.findElement(By.id('signId')).sendKeys('315649752');
    await new Promise(resolve => setTimeout(resolve, 500));
    await driver.findElement(By.id('date')).sendKeys('03/06/2023');
    await new Promise(resolve => setTimeout(resolve, 500));
    await driver.findElement(By.id('gender')).click();
    await new Promise(resolve => setTimeout(resolve, 500));
    await driver.findElement(By.css("li[data-value='male']")).click();
    await new Promise(resolve => setTimeout(resolve, 500));
    await driver.findElement(By.id('email')).sendKeys('Eli_Levy@gmail.com');
    await new Promise(resolve => setTimeout(resolve, 500));
    await driver.findElement(By.id('signPassword')).sendKeys('Password123', Key.RETURN);
    await new Promise(resolve => setTimeout(resolve, 1000));

    // Navigate to Home page
    await driver.findElement(By.id('signBtn')).click();

    // Wait for signup to complete
    await driver.wait(until.urlIs('http://localhost:3000/peoples_budget/home'), 10000);

    // Verify successful signup
    let title = await driver.getTitle();
    if (title === 'Signup') {
      console.log('------------ Signup test failed ------------');
    } else {
      console.log('------------ Signup test passed ------------');
    }

    await new Promise(resolve => setTimeout(resolve, 1000));

  } finally {
    await driver.quit();
  }
})();