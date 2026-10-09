from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Beba Awrew Betting</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #03111c;
    color: white;
}

header {
    text-align: center;
    padding: 30px 15px;
    background: linear-gradient(135deg, #001522, #063b32);
    border-bottom: 2px solid #00e676;
}

.logo {
    font-size: 65px;
}

header h1 {
    font-size: 34px;
    margin: 10px 0;
}

header h1 span {
    color: #00e676;
}

header p {
    color: #c8e6d4;
}

nav {
    display: flex;
    justify-content: center;
    gap: 20px;
    padding: 15px 5px;
    background: #061c29;
}

nav a {
    color: white;
    text-decoration: none;
    font-weight: bold;
}

.hero {
    text-align: center;
    padding: 45px 15px;
    background:
      radial-gradient(ellipse at bottom, #126b32, transparent 65%),
      linear-gradient(135deg, #052438, #001018);
}

.hero h2 {
    font-size: 28px;
}

button {
    border: none;
    cursor: pointer;
    background: #00d968;
    color: #001b12;
    font-size: 18px;
    font-weight: bold;
    padding: 15px 35px;
    border-radius: 30px;
    margin: 10px 5px;
}

button:hover {
    background: #63ff9b;
}

#predictions {
    display: none;
    max-width: 800px;
    margin: 20px auto;
    padding: 15px;
}

.card {
    background: #061b28;
    border: 1px solid #00e676;
    border-radius: 15px;
    padding: 15px;
    margin-bottom: 15px;
}

.card h2 {
    color: #00e676;
    text-align: center;
}

.match {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 8px;
    padding: 14px 5px;
    border-bottom: 1px solid #21404b;
    font-size: 14px;
}

.match:last-child {
    border-bottom: none;
}

.number {
    color: #00e676;
    font-weight: bold;
}

.pick {
    color: #00ff91;
    font-weight: bold;
    text-align: right;
}

.notice {
    margin-top: 20px;
    padding: 20px 12px;
    text-align: center;
    line-height: 1.9;
    border: 1px solid #00e676;
    border-radius: 12px;
    background: #032b20;
}

footer {
    text-align: center;
    padding: 25px 10px;
    color: #9cb5ac;
}

@media (max-width: 400px) {
    header h1 {
        font-size: 27px;
    }

    .match {
        font-size: 12px;
        gap: 5px;
    }

    button {
        padding: 13px 25px;
    }
}
</style>
</head>

<body>

<header>
    <div class="logo">⚽ 👑</div>
    <h1>Beba Awrew <span>BETTING</span></h1>
    <p>⚽ Football Predictions ⚽</p>
    <p>Better Tips • Higher Chances • Bigger Wins</p>
</header>

<nav>
    <a href="#home">🏠 Home</a>
    <a href="#predictions" onclick="showPredictions()">📋 Predictions</a>
</nav>

<section class="hero" id="home">
    <h2>Welcome to Beba Awrew Betting</h2>
    <p>Your football prediction platform</p>

    <button onclick="showPredictions()">
        ⚽ GET START →
    </button>

    <br>

    <button onclick="showPredictions()">
        VIEW PREDICTIONS
    </button>
</section>

<section id="predictions">

    <div class="card">
        <h2>⚽ የ ቤባ ዕለታዊ ግምቶች</h2>

        <div class="match">
            <span class="number">1.</span>
            <span>West Ham vs QPR</span>
            <span class="pick">W1</span>
        </div>

        <div class="match">
            <span class="number">2.</span>
            <span>Lens vs Lyon</span>
            <span class="pick">X 2</span>
        </div>

        <div class="match">
            <span class="number">3.</span>
            <span>Galatasaray vs Kasimpasa</span>
            <span class="pick">Corner Over 10.5</span>
        </div>

        <div class="match">
            <span class="number">4.</span>
            <span>Dortmund vs Werder Bremen</span>
            <span class="pick">Under 4.5</span>
        </div>

        <div class="match">
            <span class="number">5.</span>
            <span>Malaga vs Espanyol</span>
            <span class="pick">Yes GG</span>
        </div>

        <div class="match">
            <span class="number">6.</span>
            <span>Braga vs Sporting</span>
            <span class="pick">X2</span>
        </div>

        <div class="match">
            <span class="number">7.</span>
            <span>PSV vs Heerenveen</span>
            <span class="pick">W1 and Over 2.5</span>
        </div>

        <div class="notice">
            <strong>የ ሙከራ ስለሆነ በ 100 ብር ብቻ መድቡ</strong>
            <br>
            <strong style="color:#00e676;">#ቤባ_ሰቦና</strong>
        </div>
    </div>

    <button onclick="window.scrollTo({top:0,behavior:'smooth'})">
        ↑ BACK TO HOME
    </button>

</section>

<footer>
    © 2026 Beba Awrew Betting<br>
    Football Predictions
    <p>Predictions are not guaranteed. Bet responsibly.</p>
</footer>

<script>
function showPredictions() {
    const section = document.getElementById("predictions");
    section.style.display = "block";

    setTimeout(function() {
        section.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }, 50);
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

