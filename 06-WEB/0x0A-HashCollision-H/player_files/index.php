<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <style>
            * {
                padding: 0px;
                margin: 0px;
                overflow: hidden;   
            }
            body {
                background-image: url("beach.jpg");
                background-size: cover;
            }
            .outer {
                display: flex;
                width: 100vw;
                height: 100vh;
                align-items: center;
                justify-content: center;
            }
            .inner {
                border: 4px outset red;
                border-radius: 20%;
                padding: 50px;
                background-color: white;
            }
        </style>
        <title>Login</title>
    </head>

    <body class="outer">
        <div class="inner">
            <h1>Login</h1>
            <div class="login" style="margin: 30px 0;">
                <form action="index.php" method="get" >
                    <div class="form-group" style="margin: 15px 0;">
                        <p>Username: <input autocomplete="off" autofocus class="form-control ifb" name="username" placeholder="Username" type="text"></p>
                    </div>
                    <div class="form-group" style="margin: 15px 0;">
                        <p>Password: <input class="form-control ifb" name="password" placeholder="Password" type="password"></p>
                    </div>
                    <button type="submit" class="btn btn-danger">Log In</button>
                </form>
            </div>

            <div>
                <?php
                    if (isset($_GET['username']) && isset($_GET['password'])) {
                        if ($_GET['username'] === $_GET['password']) {
                            echo "<h2>Username and password cannot be the same!</h2>";
                        } else {
                            if (hash('sha256', $_GET['username']) === hash('sha256', $_GET['password'])) {
                                include('flag.php');
                                echo "<h2>$flag</h2>";
                            } else {
                                echo "<img src='https://media.giphy.com/media/l4pLY0zySvluEvr0c/giphy.gif'/>";
                            }
                        }
                    } else {
                        echo '<h2>Find the magical collision!</h2>';
                    }
                ?>
            </div>
        </div>
    </body>
</html>
