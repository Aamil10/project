<html>
  <head>
    <title>Palindrome Numbers</title>
  </head>
  <body>
    <h1>Palindrome Check</h1>
    <form method="POST">
      Enter the number: <input type="number" name="num1" required><br><br>
      <input type="submit" name="submit" value="Submit">
    </form>

    <?php
    if (isset($_POST['submit'])) {
      $num1 = $_POST['num1'];
      $reverse = strrev($num1);
      if ($num1 == $reverse) {
        echo "The number is a palindrome.";
      } else {
        echo "The number is not a palindrome.";
      }
    }
    ?>
  </body>
</html>
