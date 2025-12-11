<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Contributing — BFMC Embedded Platform</title>
  <style>
    :root{
      --bg:#0f1724;
      --card:#0b1220;
      --muted:#94a3b8;
      --accent:#2dd4bf;
      --glass: rgba(255,255,255,0.03);
      --mono: 'SFMono-Regular', Consolas, "Liberation Mono", Menlo, monospace;
    }
    *{box-sizing:border-box}
    html,body{height:100%}
    body{
      margin:0;
      font-family:Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
      background: linear-gradient(180deg,#071029 0%, #081022 50%, #041018 100%);
      color:#e6eef6;
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
      line-height:1.5;
      padding:32px;
    }

    .container{
      max-width:980px;
      margin:0 auto;
    }

    header{
      display:flex;
      align-items:center;
      gap:16px;
      margin-bottom:20px;
    }
    .logo{
      width:72px;
      height:72px;
      background:linear-gradient(135deg,#0ea5a4,#38bdf8);
      border-radius:12px;
      display:flex;
      align-items:center;
      justify-content:center;
      font-weight:700;
      color:#042027;
      box-shadow:0 6px 20px rgba(7,18,34,0.6);
    }
    .title{
      line-height:1;
    }
    .title h1{
      margin:0;
      font-size:20px;
      letter-spacing:-0.2px;
    }
    .title p{
      margin:4px 0 0 0;
      color:var(--muted);
      font-size:13px;
    }

    main{
      background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
      border:1px solid rgba(255,255,255,0.03);
      border-radius:12px;
      padding:22px;
      box-shadow:0 12px 40px rgba(2,6,23,0.6);
    }

    h2.section{
      display:flex;
      align-items:center;
      gap:12px;
      margin-top:0;
      margin-bottom:12px;
      font-size:18px;
    }
    .lead{
      color:var(--muted);
      margin-bottom:18px;
    }

    .grid{
      display:grid;
      grid-template-columns: 1fr 320px;
      gap:18px;
    }

    .card{
      background:var(--card);
      border-radius:10px;
      padding:16px;
      border:1px solid rgba(255,255,255,0.02);
    }

    .code{
      background:linear-gradient(180deg, rgba(255,255,255,0.015), rgba(255,255,255,0.01));
      padding:12px;
      border-radius:8px;
      font-family:var(--mono);
      font-size:13px;
      color:#d6f0ef;
      overflow:auto;
      border:1px solid rgba(255,255,255,0.03);
    }

    pre{margin:0}
    .muted{color:var(--muted)}
    ul{margin:0 0 12px 20px}
    li{margin:6px 0}
    .btn{
      display:inline-block;
      background:linear-gradient(90deg,var(--accent),#7dd3fc);
      color:#002a2a;
      padding:8px 12px;
      border-radius:8px;
      font-weight:600;
      text-decoration:none;
      border: none;
      cursor:pointer;
      box-shadow:0 6px 18px rgba(11,22,30,0.5);
      font-size:13px;
    }

    aside .meta{
      font-size:13px;
      color:var(--muted);
      margin-bottom:12px;
    }

    .section-block{
      margin-bottom:14px;
    }

    table.roadmap{
      width:100%;
      border-collapse:collapse;
      font-size:13px;
    }
    table.roadmap th, table.roadmap td{
      padding:8px 10px;
      border-bottom:1px dashed rgba(255,255,255,0.03);
      text-align:left;
    }
    table.roadmap th{color:var(--muted); font-weight:600}

    footer{
      margin-top:18px;
      color:var(--muted);
      font-size:13px;
      display:flex;
      justify-content:space-between;
      align-items:center;
      gap:12px;
    }

    /* Responsive */
    @media (max-width:880px){
      .grid{grid-template-columns:1fr; }
      aside{order:2}
    }

    /* small copy feedback */
    .copied{
      display:inline-block;
      margin-left:8px;
      color:#9ff5e9;
      font-size:12px;
      opacity:0;
      transform:translateY(-2px);
      transition:all .28s ease;
    }
    .copied.show{opacity:1; transform:translateY(0)}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="logo">BF</div>
      <div class="title">
        <h1>Contributing — BFMC Embedded Platform</h1>
        <p class="muted">Guidelines, workflow & best practices for contributors</p>
      </div>
    </header>

    <main>
      <h2 class="section">🤝 Thank you for contributing!</h2>
      <p class="lead">This repository helps developers, students, and BFMC competitors set up, understand, and extend the embedded platform used in the <strong>Bosch Future Mobility Challenge</strong>. We welcome code, docs, tools, tests, ideas — all contributions help.</p>

      <div class="grid">
        <div>
          <section class="card section-block">
            <h3 style="margin-top:0">📌 Contribution Guidelines</h3>

            <h4 style="margin-bottom:8px">1️⃣ Fork the Repository</h4>
            <p class="muted">Click the <strong>Fork</strong> button in the top-right of the repository to create your working copy.</p>

            <h4 style="margin-top:14px; margin-bottom:8px">2️⃣ Clone Your Fork</h4>
            <div class="code" role="region" aria-label="clone command">
<pre><code>git clone https://github.com/&lt;your-username&gt;/Embedded_Platform.git
cd Embedded_Platform</code></pre>
            </div>

            <h4 style="margin-top:14px; margin-bottom:8px">3️⃣ Create a New Branch</h4>
            <div class="code" role="region" aria-label="branch command">
<pre><code>git checkout -b feature-name</code></pre>
            </div>
            <p class="muted">Example branch names: <em>fix-build-error</em>, <em>update-readme</em>, <em>sensor-calibration-tool</em>.</p>

            <h4 style="margin-top:14px; margin-bottom:8px">4️⃣ Make Your Changes</h4>
            <ul>
              <li>Keep code clean and commented.</li>
              <li>Follow the project's folder structure.</li>
              <li>Ensure changes do not break existing builds.</li>
              <li>Update documentation when behaviour changes.</li>
            </ul>

            <h4 style="margin-top:14px; margin-bottom:8px">5️⃣ Commit Your Work</h4>
            <div class="code" role="region" aria-label="commit example">
<pre><code>git commit -m "Added motor control flow diagram"</code></pre>
            </div>
            <p class="muted">Good commit messages: <em>Fixed PWM init in motor driver</em>, <em>Updated Mbed OS instructions for Windows</em>.</p>

            <h4 style="margin-top:14px; margin-bottom:8px">6️⃣ Push and Open a PR</h4>
            <div class="code" role="region" aria-label="push command">
<pre><code>git push origin feature-name</code></pre>
            </div>
            <p class="muted">Open a Pull Request with: what you changed, why, how you tested, and logs/screenshots if applicable.</p>
          </section>

          <section class="card section-block">
            <h3 style="margin-top:0">✔️ Coding & Documentation Standards</h3>
            <h4 style="margin-bottom:8px">Embedded Code</h4>
            <ul>
              <li>Consistent spacing (project default — use 4 spaces).</li>
              <li>Follow Mbed OS coding patterns.</li>
              <li>Keep functions small and document hardware-specific logic.</li>
            </ul>

            <h4 style="margin-top:12px; margin-bottom:8px">Markdown / Docs</h4>
            <ul>
              <li>Short lines, clear headers, and code blocks for commands.</li>
              <li>Add diagrams or screenshots where useful.</li>
            </ul>
          </section>

          <section class="card section-block">
            <h3 style="margin-top:0">🧪 Testing Your Changes</h3>
            <ul>
              <li>Make sure the project compiles successfully.</li>
              <li>Test flashing on <strong>NUCLEO-F401RE</strong> where applicable.</li>
              <li>Validate sensor/actuator behaviour after changes.</li>
              <li>Confirm nothing breaks existing functionality.</li>
            </ul>
          </section>

          <section class="card section-block">
            <h3 style="margin-top:0">🌟 Types of Contributions Welcome</h3>
            <ul>
              <li>🔧 Code — drivers, utilities, enhancements</li>
              <li>📚 Documentation — guides, README updates, diagrams</li>
              <li>🛠 Tools — flashing/monitoring/debugging scripts</li>
              <li>🧪 Testing — bug reports, test cases</li>
              <li>💡 Ideas — modules, architecture suggestions, feature requests</li>
            </ul>
          </section>

          <section class="card section-block">
            <h3 style="margin-top:0">📬 Need Help?</h3>
            <p class="muted">If you need help understanding architecture or want guidance:</p>
            <ul>
              <li>Open an <strong>Issue</strong> describing the problem or proposal.</li>
              <li>Start a <strong>Discussion</strong> for architectural / roadmap conversations.</li>
              <li>Contact the maintainer via the repo profile.</li>
            </ul>
            <p style="margin-top:8px">Every contribution — big or small — helps the BFMC community. Thank you! 🚗💡</p>
          </section>
        </div>

        <aside>
          <div class="card">
            <div class="meta">
              <strong>Repository</strong><br>
              Embedded_Platform — BFMC
            </div>

            <div style="margin-bottom:12px">
              <button class="btn" id="copyCmd">Copy Clone Command</button>
              <span id="copied" class="copied">Copied!</span>
            </div>

            <div style="margin-bottom:14px">
              <strong>Quick commands</strong>
              <div class="code" style="margin-top:8px;">
<pre><code>git clone https://github.com/&lt;your-username&gt;/Embedded_Platform.git
git checkout -b feature-name
git push origin feature-name</code></pre>
              </div>
            </div>

            <div style="margin-bottom:10px">
              <strong>Roadmap (high-level)</strong>
              <table class="roadmap" aria-label="roadmap table">
                <thead>
                  <tr><th>Phase</th><th>Feature</th><th>Status</th></tr>
                </thead>
                <tbody>
                  <tr><td>Phase 1</td><td>Embedded platform setup</td><td>✅ Done</td></tr>
                  <tr><td>Phase 2</td><td>Sensor + actuator integration</td><td>⏳ In progress</td></tr>
                  <tr><td>Phase 3</td><td>Vehicle calibration utilities</td><td>🔜 Soon</td></tr>
                </tbody>
              </table>
            </div>

            <div>
              <strong>Files to add</strong>
              <ul>
                <li>ISSUE_TEMPLATE.md</li>
                <li>PULL_REQUEST_TEMPLATE.md</li>
                <li>CODE_OF_CONDUCT.md</li>
                <li>LICENSE</li>
              </ul>
            </div>
          </div>
        </aside>
      </div>

      <footer>
        <div>Maintainer: <strong>Harshid Bhupendra Rawal</strong> — DDU Nadiad</div>
        <div class="muted">Robotics • Embedded Systems • Computer Vision</div>
      </footer>
    </main>
  </div>

  <script>
    // copy clone command
    const btn = document.getElementById('copyCmd');
    const copied = document.getElementById('copied');
    btn.addEventListener('click', () => {
      const text = 'git clone https://github.com/<your-username>/Embedded_Platform.git';
      navigator.clipboard?.writeText(text).then(()=>{
        copied.classList.add('show');
        setTimeout(()=> copied.classList.remove('show'),1600);
      }).catch(()=> {
        alert('Copy failed — please select and copy manually.');
      });
    });
  </script>
</body>
</html>
