<!-- templates/student_progress.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Student Progression</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
<header>
  <div class="header-container">
      <img src="{{ url_for('static', filename='logo.jpg.png') }}" alt="College Logo"  class="college-logo">
      <div class="college-details">
        <center>
          <h2>Department of Computer Science</h2>
          <h1>St. Joseph’s College (Autonomous)</h1>
          <p>Tiruchirappalli, Tamil Nadu – 620002</p>
        </center>
      </div>
  </div>
</header>

<nav>
    <a href="{{ url_for('student_progress') }}">📘 Student Progress</a>
    <a href="{{ url_for('placement_details') }}">💼 Placement Details</a>
</nav>

<div class="container">
    <h2 style="text-align:center;">📘 Student Progression</h2>
    <form action="/submit" method="POST" enctype="multipart/form-data">
        <label>Name:</label>
        <input type="text" name="name" required>

        <label>D.No:</label>
        <input type="text" name="dno" required>

        <label>College Name:</label>
        <input type="text" name="college" required>

        <label>Place:</label>
        <input type="text" name="place" required>

        <label>Name of the Degree:</label>
        <input type="text" name="degree" required>

        <label> Current ID Card (PDF only):</label>
        <input type="file" name="id_card" accept="application/pdf" required>

        <button type="submit">Submit</button>
    </form>
</div>
</body>
</html>