<?php
// Retrieve credentials safely from environment variables
$host = getenv('PGHOST');
$db   = getenv('PGDATABASE'); // Should be set to 'course'
$user = getenv('PGUSER');
$pass = getenv('PGPASSWORD');
$port = getenv('PGPORT') ?: '5432';

try {
    // Connect to PostgreSQL
    $dsn = "pgsql:host=$host;port=$port;dbname=$db";
    $pdo = new PDO($dsn, $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Query the newly created table using the exact column names
    $stmt = $pdo->query("SELECT id, course_name, tech_stack, duration, level FROM courses");
    
    // Output the unformatted list
    echo "<ul>\n";
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        echo "<li>{$row['id']} | {$row['course_name']} | {$row['tech_stack']} | {$row['duration']} | {$row['level']}</li>\n";
    }
    echo "</ul>\n";
    
} catch (PDOException $e) {
    // Handle connection errors gracefully
    echo "Database error: " . $e->getMessage();
}
?>
