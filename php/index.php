
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verventech | AI Courses</title>
    <style>
        /* CSS Variables for theming */
        :root {
            --primary-color: #2563eb;
            --primary-hover: #1d4ed8;
            --dark-bg: #0f172a;
            --light-bg: #f8fafc;
            --text-main: #334155;
            --text-light: #94a3b8;
        }

        /* Basic Reset */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            color: var(--text-main);
            line-height: 1.6;
        }

        a {
            text-decoration: none;
            color: inherit;
        }

        /* Header & Navigation */
        header {
            background-color: var(--dark-bg);
            color: white;
            padding: 1rem 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: #60a5fa;
        }

        nav ul {
            list-style: none;
            display: flex;
            gap: 2rem;
        }

        nav a:hover {
            color: #60a5fa;
            transition: color 0.3s;
        }

        .btn-signin {
            border: 1px solid white;
            padding: 0.5rem 1.5rem;
            border-radius: 5px;
        }

        .btn-signin:hover {
            background-color: white;
            color: var(--dark-bg);
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(rgba(15, 23, 42, 0.9), rgba(15, 23, 42, 0.9)), url('https://images.unsplash.com/photo-1620712943543-bcc4688e7485?auto=format&fit=crop&q=80&w=1200') center/cover;
            color: white;
            text-align: center;
            padding: 6rem 20px;
        }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }

        .hero p {
            font-size: 1.2rem;
            max-width: 800px;
            margin: 0 auto 2rem;
            color: #cbd5e1;
        }

        .btn {
            display: inline-block;
            padding: 0.8rem 2rem;
            border-radius: 5px;
            font-weight: bold;
            margin: 0.5rem;
            transition: background 0.3s;
        }

        .btn-primary {
            background-color: var(--primary-color);
            color: white;
        }

        .btn-primary:hover {
            background-color: var(--primary-hover);
        }

        .btn-secondary {
            background-color: transparent;
            border: 2px solid white;
            color: white;
        }

        .btn-secondary:hover {
            background-color: white;
            color: var(--dark-bg);
        }

        /* Section Global Styles */
        section {
            padding: 4rem 5%;
        }

        .section-title {
            text-align: center;
            font-size: 2.2rem;
            margin-bottom: 3rem;
            color: var(--dark-bg);
        }

        /* Features Section */
        .features {
            background-color: var(--light-bg);
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .feature-card {
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            text-align: center;
        }

        .feature-card h3 {
            margin-bottom: 1rem;
            color: var(--primary-color);
        }

        /* Courses Table */
        .table-container {
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 1rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }

        th, td {
            padding: 1.2rem;
            text-align: left;
            border-bottom: 1px solid #e2e8f0;
        }

        th {
            background-color: var(--dark-bg);
            color: white;
        }

        tr:hover {
            background-color: #f1f5f9;
        }

        /* Testimonials */
        .testimonials {
            background-color: var(--light-bg);
        }

        .testimonial-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 2rem;
        }

        blockquote {
            background: white;
            padding: 2rem;
            border-left: 5px solid var(--primary-color);
            border-radius: 0 8px 8px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }

        .author {
            margin-top: 1rem;
            font-weight: bold;
            color: var(--primary-color);
        }

        /* CTA Section */
        .cta-section {
            text-align: center;
            background-color: #e0e7ff;
        }

        /* Footer */
        footer {
            background-color: var(--dark-bg);
            color: var(--text-light);
            text-align: center;
            padding: 2rem 5%;
        }

        .footer-links {
            margin-top: 1rem;
        }

        .footer-links a {
            margin: 0 10px;
        }

        .footer-links a:hover {
            color: white;
        }

        /* Responsive */
        @media (max-width: 768px) {
            nav ul {
                display: none; /* In a real app, you'd add a hamburger menu here */
            }
            .hero h1 {
                font-size: 2.2rem;
            }
        }
    </style>
</head>
<body>

    <!-- Navigation Header -->
    <header>
        <div class="logo">🌐 Verventech</div>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#courses">AI Course Catalog</a></li>
                <li><a href="#enterprise">Enterprise Training</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="#signin" class="btn-signin">Sign In</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <h1>🚀 Master the Future of Technology</h1>
        <p>Industry-leading Artificial Intelligence courses designed for the next generation of innovators, builders, and leaders. Go from foundational concepts to building your own Generative AI models.</p>
        <a href="#courses" class="btn btn-primary">Start Learning for Free</a>
        <a href="#courses" class="btn btn-secondary">View Full Catalog</a>
    </section>

    <!-- Why Verventech Section -->
    <section id="about">
        <h2 class="section-title">Why Learn AI with Verventech?</h2>
        <div class="features">
            <div class="feature-card">
                <h3>Industry-Expert Instructors</h3>
                <p>Learn directly from AI practitioners who have designed and deployed large-scale machine learning models at global tech giants.</p>
            </div>
            <div class="feature-card">
                <h3>Project-Based Curriculum</h3>
                <p>Stop watching and start building. Every module ends with a hands-on coding project you can showcase in your portfolio.</p>
            </div>
            <div class="feature-card">
                <h3>Career Acceleration</h3>
                <p>Access 1-on-1 mentorship, expert resume reviews, and get fast-tracked through our exclusive tech hiring network.</p>
            </div>
        </div>
    </section>

 <?php
// 1. Establish the database connection using Apache's environment variables
$host = getenv('PGHOST');
$db   = getenv('PGDATABASE');
$user = getenv('PGUSER');
$pass = getenv('PGPASSWORD');
$port = getenv('PGPORT') ?: '5432';

$stmt = null;
$db_error = null;

try {
    $dsn = "pgsql:host=$host;port=$port;dbname=$db";
    $pdo = new PDO($dsn, $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Query the database 
    $stmt = $pdo->query("SELECT course_name, level, tech_stack, duration FROM courses");
    
} catch (PDOException $e) {
    // Catch any connection errors so they don't crash the whole HTML page
    $db_error = $e->getMessage();
}
?>

<!-- 2. Your HTML Block -->
<!-- Courses Section -->
<section id="courses">
    <h2 class="section-title">🎓 Featured AI Learning Paths</h2>
    <p style="text-align: center; margin-bottom: 2rem;">Choose the track that best fits your career goals.</p>
    
    <div class="table-container">
        <?php if ($db_error): ?>
            <!-- Display database errors gracefully if they occur -->
            <p style="color: red; text-align: center;">Database error: <?php echo htmlspecialchars($db_error); ?></p>
        <?php else: ?>
            <table>
                <thead>
                    <tr>
                        <th>Course Title</th>
                        <th>Level</th>
                        <th>Core Technologies</th>
                        <th>Duration</th>
                    </tr>
                </thead>
                <tbody>
                    <?php
                    // 3. Loop through each row in the database and generate a <tr>
                    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                        echo "<tr>";
                        echo "<td><strong>" . htmlspecialchars($row['course_name']) . "</strong></td>";
                        echo "<td>" . htmlspecialchars($row['level']) . "</td>";
                        echo "<td>" . htmlspecialchars($row['tech_stack']) . "</td>";
                        echo "<td>" . htmlspecialchars($row['duration']) . "</td>";
                        echo "</tr>\n";
                    }
                    ?>
                </tbody>
            </table>
        <?php endif; ?>
    </div>
</section>

    <!-- Testimonials Section -->
    <section class="testimonials">
        <h2 class="section-title">What Our Students Say</h2>
        <div class="testimonial-grid">
            <blockquote>
                "Verventech's Generative AI track completely transformed my career. Within two months of completing the capstone project, I transitioned from a traditional software role into a Lead AI Engineer position."
                <div class="author">— Sarah J., Senior AI Engineer</div>
            </blockquote>
            <blockquote>
                "The instructors don't just teach theory; they teach you how to solve real-world problems. The hands-on labs were challenging but incredibly rewarding."
                <div class="author">— David M., Data Scientist</div>
            </blockquote>
        </div>
    </section>

    <!-- Bottom CTA Section -->
    <section class="cta-section">
        <h2>Ready to build the future?</h2>
        <p style="margin: 1rem 0 2rem;">Join over 50,000 students worldwide who are upgrading their skills with Verventech.</p>
        <a href="#enroll" class="btn btn-primary">Enroll Now</a>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2026 Verventech Inc. All rights reserved.</p>
        <div class="footer-links">
            <a href="#privacy">Privacy Policy</a> | 
            <a href="#terms">Terms of Service</a> | 
            <a href="#support">Contact Support</a>
        </div>
    </footer>

</body>
</html>
