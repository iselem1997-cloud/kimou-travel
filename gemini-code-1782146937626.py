admin_login_html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Connexion Admin | Kimou Travel</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #1e3d59;
            --secondary: #ff6e40;
            --bg-body: #eceff1;
            --white: #ffffff;
            --text-muted: #607d8b;
        }
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Cairo', sans-serif;
        }
        body {
            background-color: var(--bg-body);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .login-container {
            background-color: var(--white);
            width: 100%;
            max-width: 420px;
            padding: 40px 30px;
            border-radius: 16px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.1);
            text-align: center;
        }
        .icon-wrapper {
            font-size: 50px;
            color: var(--secondary);
            margin-bottom: 20px;
        }
        h2 {
            color: var(--primary);
            font-size: 24px;
            margin-bottom: 8px;
            font-weight: 700;
        }
        .subtitle {
            color: var(--text-muted);
            font-size: 14px;
            margin-bottom: 30px;
        }
        .form-group {
            text-align: left;
            margin-bottom: 20px;
        }
        label {
            display: block;
            font-weight: 600;
            color: #333;
            margin-bottom: 8px;
            font-size: 15px;
        }
        .input-wrapper {
            position: relative;
        }
        .input-wrapper i {
            position: absolute;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
        }
        input {
            width: 100%;
            padding: 12px 12px 12px 40px;
            border: 1px solid #cfd8dc;
            border-radius: 8px;
            font-size: 15px;
            transition: all 0.3s;
        }
        input:focus {
            border-color: var(--secondary);
            outline: none;
            box-shadow: 0 0 0 3px rgba(255, 110, 64, 0.1);
        }
        .btn-submit {
            background-color: var(--secondary);
            color: var(--white);
            border: none;
            width: 100%;
            padding: 14px;
            font-size: 16px;
            font-weight: 700;
            border-radius: 8px;
            cursor: pointer;
            margin-top: 10px;
            transition: background 0.3s;
        }
        .btn-submit:hover {
            background-color: #e2582b;
        }
        .back-link {
            display: inline-block;
            margin-top: 25px;
            color: var(--secondary);
            text-decoration: none;
            font-size: 14px;
            font-weight: 600;
            transition: color 0.3s;
        }
        .back-link:hover {
            color: var(--primary);
        }
    </style>
</head>
<body>

    <div class="login-container">
        <div class="icon-wrapper">
            <i class="fa-solid fa-user-shield"></i>
        </div>
        <h2>Connexion Admin</h2>
        <p class="subtitle">Accès strictement réservé à la direction de Kimou Travel</p>
        
        <form id="loginForm">
            <div class="form-group">
                <label>Nom d'utilisateur</label>
                <div class="input-wrapper">
                    <i class="fa-solid fa-user"></i>
                    <input type="text" id="username" placeholder="admin_kimou" required>
                </div>
            </div>
            
            <div class="form-group">
                <label>Mot de Passe</label>
                <div class="input-wrapper">
                    <i class="fa-solid fa-lock"></i>
                    <input type="password" id="password" placeholder="••••••••" required>
                </div>
            </div>
            
            <button type="submit" class="btn-submit">Se Connecter <i class="fa-solid fa-arrow-right-to-bracket"></i></button>
        </form>
        
        <a href="index.html" class="back-link"><i class="fa-solid fa-arrow-left"></i> Retourner au site public</a>
    </div>

    <script>
        document.getElementById('loginForm').addEventListener('submit', function(e) {
            e.preventDefault();
            const user = document.getElementById('username').value;
            const pass = document.getElementById('password').value;
            
            // تحقق بسيط جداً محلي (لأغراض العرض والتجربة قبل ربطه بقاعدة البيانات)
            if(user === 'admin_kimou' && pass === 'kimou2026') {
                window.location.href = 'dashboard.html';
            } else {
                alert('الرجاء التحقق من اسم المستخدم أو كلمة المرور!');
            }
        });
    </script>
</body>
</html>
"""

admin_dashboard_html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Espace Direction | Kimou Travel</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #1e3d59;
            --secondary: #ff6e40;
            --bg-dark: #112233;
            --sidebar-width: 260px;
            --white: #ffffff;
        }
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Cairo', sans-serif;
        }
        body {
            background-color: #f4f6f9;
            display: flex;
            min-height: 100vh;
        }
        
        /* القائمة الجانبية */
        .sidebar {
            width: var(--sidebar-width);
            background-color: var(--bg-dark);
            color: var(--white);
            display: flex;
            flex-direction: column;
            position: fixed;
            height: 100vh;
            left: 0;
            top: 0;
        }
        .sidebar-brand {
            padding: 24px;
            font-size: 20px;
            font-weight: 700;
            color: var(--secondary);
            border-bottom: 1px solid #1f364d;
            text-align: center;
        }
        .sidebar-menu {
            list-style: none;
            padding: 20px 0;
            flex: 1;
        }
        .sidebar-menu li a {
            display: flex;
            align-items: center;
            padding: 14px 24px;
            color: #b2c0cc;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s;
        }
        .sidebar-menu li a i {
            margin-right: 12px;
            font-size: 18px;
            width: 20px;
        }
        .sidebar-menu li a:hover, .sidebar-menu li.active a {
            background-color: #1f364d;
            color: var(--white);
            border-left: 4px solid var(--secondary);
        }
        
        /* المحتوى الرئيسي */
        .main-content {
            margin-left: var(--sidebar-width);
            flex: 1;
            padding: 40px;
        }
        .top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 40px;
            background: var(--white);
            padding: 15px 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.02);
        }
        .user-info {
            display: flex;
            align-items: center;
            gap: 10px;
            font-weight: 600;
            color: var(--primary);
        }
        .btn-logout {
            background: #e74c3c;
            color: white;
            padding: 8px 15px;
            border-radius: 6px;
            text-decoration: none;
            font-size: 14px;
            font-weight: 600;
        }

        /* حاوية الأدوات */
        .dashboard-grid {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 30px;
        }
        @media (max-width: 992px) {
            .dashboard-grid { grid-template-columns: 1fr; }
        }
        
        .card {
            background: var(--white);
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        }
        .card-title {
            font-size: 18px;
            color: var(--primary);
            margin-bottom: 25px;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 10px;
            border-bottom: 2px solid #f4f6f9;
            padding-bottom: 10px;
        }
        
        /* الاستمارات */
        .form-group {
            margin-bottom: 20px;
        }
        .form-group label {
            display: block;
            font-weight: 600;
            margin-bottom: 8px;
            color: #444;
        }
        .form-control {
            width: 100%;
            padding: 10px 12px;
            border: 1px solid #ced4da;
            border-radius: 6px;
            font-size: 14px;
        }
        .form-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
        }
        .btn-primary {
            background-color: var(--primary);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 6px;
            font-weight: 700;
            cursor: pointer;
            transition: background 0.3s;
        }
        .btn-primary:hover { background-color: #122536; }
        .btn-secondary {
            background-color: var(--secondary);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 6px;
            font-weight: 700;
            cursor: pointer;
            transition: background 0.3s;
        }
        .btn-secondary:hover { background-color: #e2582b; }
    </style>
</head>
<body>

    <!-- القائمة الجانبية -->
    <div class="sidebar">
        <div class="sidebar-brand">Kimou Travel</div>
        <ul class="sidebar-menu">
            <li class="active"><a href="#"><i class="fa-solid fa-chart-line"></i> Dashboard</a></li>
            <li><a href="#"><i class="fa-solid fa-plane-departure"></i> Circuits / Offres</a></li>
            <li><a href="#"><i class="fa-solid fa-users"></i> Réservations</a></li>
            <li><a href="#"><i class="fa-solid fa-gear"></i> Paramètres</a></li>
        </ul>
    </div>

    <!-- المحتوى الرئيسي -->
    <div class="main-content">
        <div class="top-bar">
            <div class="user-info">
                <i class="fa-solid fa-circle-user" style="font-size: 24px; color: var(--secondary)"></i>
                <span>Direction Kimou Travel</span>
            </div>
            <a href="admin.html" class="btn-logout"><i class="fa-solid fa-power-off"></i> Déconnexion</a>
        </div>

        <div class="dashboard-grid">
            <!-- تغيير كلمة المرور -->
            <div class="card">
                <div class="card-title"><i class="fa-solid fa-key"></i> Changer le mot de passe</div>
                <form>
                    <div class="form-group">
                        <label>Nouveau mot de passe</label>
                        <input type="password" class="form-control" placeholder="Entrez le nouveau mot de passe">
                    </div>
                    <button type="button" class="btn-primary" style="width: 100%;">Changer le mot de passe</button>
                </form>
            </div>

            <!-- نشر عرض جديد -->
            <div class="card">
                <div class="card-title"><i class="fa-solid fa-circle-plus"></i> Publier une Nouvelle Offre</div>
                <p style="font-size: 13px; color: #777; margin-bottom: 20px;">Ajoutez un circuit qui s'affichera instantanément sur la page Destinations.</p>
                
                <form>
                    <div class="form-group">
                        <label>Nom du Circuit / Destination *</label>
                        <input type="text" class="form-control" placeholder="Ex: Grand Sahara - Taghit" required>
                    </div>
                    
                    <div class="form-row">
                        <div class="form-group">
                            <label>Séjour de la sortie *</label>
                            <input type="text" class="form-control" placeholder="Ex: Du 15 au 22 Juin" required>
                        </div>
                        <div class="form-group">
                            <label>Tarif par Personne (DZD) *</label>
                            <input type="text" class="form-control" placeholder="Ex: 35 000 DA" required>
                        </div>
                    </div>

                    <div class="form-row">
                        <div class="form-group">
                            <label>Date de départ *</label>
                            <input type="date" class="form-control" required>
                        </div>
                        <div class="form-group">
                            <label>Date de retour *</label>
                            <input type="date" class="form-control" required>
                        </div>
                    </div>

                    <div class="form-group">
                        <label>Images du Circuit (Sélectionnez plusieurs) *</label>
                        <input type="file" class="form-control" multiple required>
                    </div>

                    <button type="submit" class="btn-secondary">Enregistrer et Publier l'offre</button>
                </form>
            </div>
        </div>
    </div>

</body>
</html>
"""

with open("admin.html", "w", encoding="utf-8") as f:
    f.write(admin_login_html)

with open("dashboard.html", "w", encoding="utf-8") as f:
    f.write(admin_dashboard_html)

print("Admin pages generated successfully.")